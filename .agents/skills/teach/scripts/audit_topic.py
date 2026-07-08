#!/usr/bin/env python3
"""
teach skill — 审计教学主题是否满足完成条件。

用法:
  python scripts/audit_topic.py teach/open-ai-agent/pi/module-ai
  python scripts/audit_topic.py teach/open-ai-agent/pi --all
"""

import argparse
import html
import os
import re
import sys
from pathlib import Path


MAX_LESSON_TEXT_UNITS = 1500
MAX_LESSON_BYTES = 45_000
MAX_H2_SECTIONS = 4
MAX_CODE_LINES = 35

PLACEHOLDER_PATTERNS = [
    r"\{主题\}",
    r"\{主题名\}",
    r"\{项目名\}",
    r"\{1-3\s*句话",
    r"\{用户",
    r"\{时间",
    r"\{……\}",
    r"\{简短描述",
    r"generate_snapshot\.py\s*将自动填充",
    r"添加高可信度",
    r"添加用户可以检验技能",
    r"记录缺失的资源领域",
]


def strip_html_for_lesson_units(content):
    content = re.sub(r"(?is)<script\b.*?</script>", " ", content)
    content = re.sub(r"(?is)<style\b.*?</style>", " ", content)
    content = re.sub(r"(?is)<svg\b.*?</svg>", " ", content)
    content = re.sub(r"(?is)<pre\b.*?</pre>", " ", content)
    content = re.sub(r"(?is)<code\b.*?</code>", " ", content)
    content = re.sub(r"(?is)<nav\b.*?</nav>", " ", content)
    content = re.sub(r"(?s)<[^>]+>", " ", content)
    content = html.unescape(content)
    return re.sub(r"\s+", " ", content).strip()


def lesson_text_units(text):
    cjk_count = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin_words = len(re.findall(r"\b[A-Za-z][A-Za-z0-9_-]*\b", text))
    return cjk_count + latin_words


def max_code_block_lines(content):
    max_lines = 0
    for match in re.finditer(r"(?is)<pre\b.*?</pre>|<code\b.*?</code>", content):
        text = re.sub(r"(?s)<[^>]+>", "", match.group(0))
        text = html.unescape(text).strip("\n")
        if text:
            max_lines = max(max_lines, len(text.splitlines()))
    return max_lines


def has_placeholder(path):
    if not path.exists():
        return True, "文件缺失"
    content = path.read_text(encoding="utf-8", errors="ignore")
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, content):
            return True, f"仍包含占位内容：{pattern}"
    return False, ""


def audit_lesson(path):
    issues = []
    content = path.read_text(encoding="utf-8", errors="ignore")
    size = path.stat().st_size
    if size > MAX_LESSON_BYTES:
        issues.append(f"lesson 过大：{size} bytes > {MAX_LESSON_BYTES}")

    units = lesson_text_units(strip_html_for_lesson_units(content))
    if units > MAX_LESSON_TEXT_UNITS:
        issues.append(f"lesson 正文过长：{units} 文本单位 > {MAX_LESSON_TEXT_UNITS}")

    h2_count = len(re.findall(r"(?i)<h2\b", content))
    if h2_count > MAX_H2_SECTIONS:
        issues.append(f"主章节过多：{h2_count} 个 h2 > {MAX_H2_SECTIONS}")

    code_lines = max_code_block_lines(content)
    if code_lines > MAX_CODE_LINES:
        issues.append(f"单个代码块过长：{code_lines} 行 > {MAX_CODE_LINES}")

    if not re.search(r"练习|回忆|检索|判断|任务|答案|反馈", content):
        issues.append("缺少检索练习、判断题、任务或反馈闭环")

    return issues


def is_topic_dir(path):
    markers = ["MISSION.md", "RESOURCES.md", "SNAPSHOT.md", "lessons", "reference"]
    return path.is_dir() and any((path / marker).exists() for marker in markers)


def audit_topic(topic_path):
    topic_path = Path(topic_path)
    issues = []

    if not topic_path.exists():
        return [f"{topic_path}: 主题目录不存在"]
    if not topic_path.is_dir():
        return [f"{topic_path}: 不是目录"]

    for filename in ["MISSION.md", "RESOURCES.md", "SNAPSHOT.md"]:
        has_ph, reason = has_placeholder(topic_path / filename)
        if has_ph:
            issues.append(f"{filename}: {reason}")

    snapshot = topic_path / "SNAPSHOT.md"
    if snapshot.exists():
        content = snapshot.read_text(encoding="utf-8", errors="ignore")
        if "快照时间" not in content or "课程数" not in content:
            issues.append("SNAPSHOT.md: 未生成实际快照摘要")

    lessons_dir = topic_path / "lessons"
    reference_dir = topic_path / "reference"
    lessons = sorted(lessons_dir.glob("*.html")) if lessons_dir.exists() else []
    references = sorted(reference_dir.glob("*.html")) if reference_dir.exists() else []

    if not lessons:
        if references:
            issues.append("reference-only 主题：存在参考文档但 lessons/ 下没有 HTML 课程")
        else:
            issues.append("缺少 lessons/*.html")

    for lesson in lessons:
        for issue in audit_lesson(lesson):
            issues.append(f"{lesson.relative_to(topic_path)}: {issue}")

    return issues


def iter_topics(project_path):
    for child in sorted(Path(project_path).iterdir()):
        if child.name.startswith(".") or not child.is_dir():
            continue
        if is_topic_dir(child):
            yield child


def main():
    parser = argparse.ArgumentParser(description="审计 teach 主题完整性与短课合规性")
    parser.add_argument("path", help="教学主题路径或项目路径")
    parser.add_argument("--all", action="store_true", help="审计项目下所有主题目录")
    args = parser.parse_args()

    target = Path(args.path)
    all_issues = []

    if args.all:
        if not target.exists():
            print(f"❌ 路径不存在: {target}")
            return 1
        topics = list(iter_topics(target))
        if not topics:
            print(f"⚠️  未找到教学主题: {target}")
            return 0
        for topic in topics:
            issues = audit_topic(topic)
            if issues:
                all_issues.append((topic, issues))
    else:
        issues = audit_topic(target)
        if issues:
            all_issues.append((target, issues))

    if all_issues:
        for topic, issues in all_issues:
            print(f"❌ {topic}")
            for issue in issues:
                print(f"  - {issue}")
        return 1

    print("✅ teach 主题审计通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())

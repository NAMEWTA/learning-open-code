#!/usr/bin/env python3
"""
teach skill — 生成/更新教学主题的 SNAPSHOT.md

用法:
  # 为单个主题生成快照
  python scripts/generate_snapshot.py teach/open-java/RuoYiVuePlus/permission-model

  # 为某项目下所有主题生成快照
  python scripts/generate_snapshot.py teach/open-java/RuoYiVuePlus --all

  # 干跑（仅显示将要收集的引用，不写入）
  python scripts/generate_snapshot.py teach/open-java/RuoYiVuePlus/permission-model --dry-run

功能:
  1. 扫描主题下的所有课程 HTML，提取源文件引用
  2. 获取关联 git 子模块的当前 commit 和分支
  3. 统计课程数、学习记录数、参考资料数
  4. 写入格式化的 SNAPSHOT.md
"""

import os
import re
import sys
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path


def find_workspace_root():
    """向上查找工作区根目录（包含 .gitmodules 的目录）"""
    script_dir = Path(__file__).resolve().parent
    current = script_dir
    while current != current.parent:
        if (current / ".gitmodules").exists():
            return current
        current = current.parent
    # 回退：脚本在 .agents/skills/teach/scripts/ 下，向上 4 级
    return script_dir.parent.parent.parent.parent


def parse_gitmodules(workspace_root):
    """解析 .gitmodules，返回 path -> {url, branch} 映射"""
    gitmodules_path = workspace_root / ".gitmodules"
    if not gitmodules_path.exists():
        return {}

    submodules = {}
    current_path = None
    with open(gitmodules_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("[submodule "):
                current_path = None
            elif line.startswith("path = ") and current_path is None:
                current_path = line.split("=", 1)[1].strip()
                submodules[current_path] = {"url": "", "branch": ""}
            elif line.startswith("url = ") and current_path:
                submodules[current_path]["url"] = line.split("=", 1)[1].strip()
            elif line.startswith("branch = ") and current_path:
                submodules[current_path]["branch"] = line.split("=", 1)[1].strip()
    return submodules


def find_related_submodules(topic_project_path, submodules):
    """
    找到与 teach 项目路径关联的 git 子模块。
    规则：topic_project_path 对应 teach/<path>，
    在 .gitmodules 中查找 path 以 <path>/ 开头的所有子模块。
    多个子模块共享同一父目录 = 逻辑项目。
    """
    related = []
    for sp, info in submodules.items():
        if sp.startswith(topic_project_path + "/"):
            related.append((sp, info))
    if not related:
        # 尝试精确匹配单个子模块
        for sp, info in submodules.items():
            if sp == topic_project_path:
                related.append((sp, info))
                break
    return related


def get_git_info(submodule_path, workspace_root):
    """获取子模块的当前 git 信息"""
    repo_path = workspace_root / submodule_path
    if not repo_path.exists():
        return None

    import subprocess

    try:
        commit = subprocess.check_output(
            ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
            text=True, stderr=subprocess.DEVNULL
        ).strip()
        branch = subprocess.check_output(
            ["git", "-C", str(repo_path), "rev-parse", "--abbrev-ref", "HEAD"],
            text=True, stderr=subprocess.DEVNULL
        ).strip()
        return {
            "commit": commit,
            "short_commit": commit[:7] if len(commit) >= 7 else commit,
            "branch": branch,
        }
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _looks_like_file_ref(text):
    """判断文本是否像文件引用"""
    if len(text) < 4 or len(text) > 250:
        return False
    if re.search(r'\.(java|ts|vue|xml|yml|yaml|json|js|jsx|tsx|css|scss|less|sql|md|properties|gradle|pom|html)$',
                 text, re.IGNORECASE):
        return True
    if 'ruoyi-' in text.lower():
        return True
    if re.search(r'(src|lib|app|components|utils|api|store|router|hooks|views|pages|layouts|config|assets)/', text):
        return True
    return False


def _is_pure_classname(text):
    """判断是否只是纯类名（非文件路径）"""
    if re.match(r'^[A-Z][a-zA-Z]+$', text) and '/' not in text and '\\' not in text and '.' not in text:
        return True
    return False


def extract_source_refs(html_file):
    """从 HTML 课程文件中提取源文件引用"""
    refs = set()
    try:
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return refs

    # 1. <span class="where"> 中的内容
    where_pattern = re.compile(r'<span\s+class="where"[^>]*>(.*?)</span>', re.DOTALL)
    for match in where_pattern.finditer(content):
        text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        if text and not _is_pure_classname(text):
            refs.add(text)

    # 2. <code> 中的文件路径
    code_pattern = re.compile(r'<code>([^<]+)</code>')
    for match in code_pattern.finditer(content):
        text = match.group(1).strip()
        if _looks_like_file_ref(text):
            refs.add(text)

    # 3. ClassName:行号 模式
    table_ref_pattern = re.compile(r'<code>([A-Z][a-zA-Z]+(?:\.java)?:\d+[-\d]*)</code>')
    for match in table_ref_pattern.finditer(content):
        refs.add(match.group(1).strip())

    return refs


def normalize_ref(ref):
    """规范化引用路径"""
    ref = re.sub(r':\d+[-\d]*$', '', ref)
    ref = ref.strip()
    ref = ref.replace('.../', '')
    ref = re.sub(r'^RuoYi[-_]Vue[-_]Plus/', '', ref, flags=re.IGNORECASE)
    ref = re.sub(r'^plus-ui-(vue|react)/', '', ref, flags=re.IGNORECASE)
    ref = ref.strip()
    ref = ref.replace('：', ':').replace('；', ';')
    return ref


def deduplicate_refs(refs):
    """去除重复引用"""
    sorted_refs = sorted(refs, key=len, reverse=True)
    result = []
    for ref in sorted_refs:
        is_dup = False
        for existing in result:
            if existing.endswith(ref) and len(existing) > len(ref):
                is_dup = True
                break
        if not is_dup:
            result.append(ref)
    return set(result)


def generate_snapshot(topic_path, workspace_root, submodules_info, dry_run=False):
    """为一个教学主题生成 SNAPSHOT.md"""
    topic_path = Path(topic_path)
    topic_name = topic_path.name
    lessons_dir = topic_path / "lessons"
    records_dir = topic_path / "learning-records"
    reference_dir = topic_path / "reference"
    assets_dir = topic_path / "assets"
    snapshot_file = topic_path / "SNAPSHOT.md"

    if not topic_path.exists():
        print(f"❌ 主题目录不存在: {topic_path}")
        return

    # 收集统计
    lesson_files = sorted([f for f in os.listdir(lessons_dir) if f.endswith('.html')]) if lessons_dir.exists() else []
    record_files = sorted([f for f in os.listdir(records_dir) if f.endswith('.md')]) if records_dir.exists() else []
    reference_files = sorted([f for f in os.listdir(reference_dir) if f.endswith('.html')]) if reference_dir.exists() else []

    asset_count = 0
    if assets_dir.exists():
        for _, _, files in os.walk(assets_dir):
            asset_count += len(files)

    # 提取源文件引用
    all_refs = set()
    lesson_descriptions = []
    for lf in lesson_files:
        refs = extract_source_refs(lessons_dir / lf)
        all_refs.update(refs)
        try:
            with open(lessons_dir / lf, "r", encoding="utf-8") as f:
                content = f.read(5000)
            title_match = re.search(r'<title>(.*?)</title>', content)
            title = title_match.group(1) if title_match else lf
        except Exception:
            title = lf
        lesson_descriptions.append((lf, title))

    # 规范化 + 去重
    normalized = set()
    for ref in all_refs:
        nref = normalize_ref(ref)
        if nref and len(nref) > 3:
            normalized.add(nref)
    final_refs = deduplicate_refs(normalized)

    # 查找 topic_path 对应的 teach 项目路径
    # topic_path 形如: teach/open-java/RuoYiVuePlus/permission-model
    # 需要找到 teach/open-java/RuoYiVuePlus 这个项目路径
    rel_topic = topic_path.relative_to(workspace_root)
    parts = rel_topic.parts
    if len(parts) >= 2 and parts[0] == "teach":
        project_rel = str(Path(*parts[1:-1]))  # teach 和 topic 之间的部分
    else:
        project_rel = str(Path(*parts[:-1]))

    related_sm = find_related_submodules(project_rel, submodules_info)

    # 生成 SNAPSHOT.md
    cst = timezone(timedelta(hours=8))
    now = datetime.now(cst).strftime('%Y-%m-%dT%H:%M:%S+08:00')

    lines = [f"# 课程快照：{topic_name}", "", "## 源项目信息"]

    for sp, sm_info in related_sm:
        git_info = get_git_info(sp, workspace_root)
        if git_info:
            lines.append(f"- **源仓库**：`{sp}`")
            lines.append(f"  - **Git Commit**：`{git_info['commit']}`")
            lines.append(f"  - **短 Commit**：`{git_info['short_commit']}`")
            lines.append(f"  - **分支**：`{git_info['branch']}`")
        else:
            lines.append(f"- **源仓库**：`{sp}`")
            lines.append(f"  - ⚠️ 无法获取 git 信息（子模块可能未初始化？）")
    lines.append(f"- **快照时间**：{now}")
    lines.append("")

    # 引用文件表
    lines.append("## 课程引用的源文件")
    lines.append("")
    if final_refs:
        lines.append("| 源文件路径 | 用途 | 关键度 |")
        lines.append("|-----------|------|--------|")
        for ref in sorted(final_refs):
            lines.append(f"| `{ref}` | 课程分析引用 | 🟡 辅助 |")
    else:
        lines.append("（暂无显式源文件引用——课程可能以概念讲解为主，引用通过文字描述嵌入）")
    lines.append("")

    # 课程表
    lines.append("## 已生成课程")
    lines.append("")
    if lesson_descriptions:
        lines.append("| 编号 | 课程文件 | 描述 |")
        lines.append("|------|---------|------|")
        for lf, title in lesson_descriptions:
            num = lf.replace('.html', '')
            lines.append(f"| {num} | `lessons/{lf}` | {title} |")
    else:
        lines.append("（暂无课程）")
    lines.append("")

    # 参考资料
    if reference_files:
        lines.append("## 参考资料")
        lines.append("")
        for rf in reference_files:
            lines.append(f"- `reference/{rf}`")
        lines.append("")

    # 摘要
    lines.append("## 快照摘要")
    lines.append(f"- 课程数：{len(lesson_files)}")
    lines.append(f"- 引用源文件数：{len(final_refs)}")
    lines.append(f"- 学习记录数：{len(record_files)}")
    lines.append(f"- 参考资料数：{len(reference_files)}")
    lines.append(f"- 资产文件数：{asset_count}")
    lines.append("")

    content = "\n".join(lines)

    if dry_run:
        print(f"\n{'='*60}")
        print(f"📋 干跑预览: {topic_name}")
        print(f"{'='*60}")
        print(content)
        return

    with open(snapshot_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✅ {topic_name}: {len(lesson_files)} 课, {len(final_refs)} 引用, {len(record_files)} 记录")


def main():
    parser = argparse.ArgumentParser(description="生成/更新教学主题的 SNAPSHOT.md")
    parser.add_argument("path", help="教学主题路径或项目路径")
    parser.add_argument("--all", action="store_true", help="处理指定路径下的所有主题")
    parser.add_argument("--dry-run", action="store_true", help="仅预览，不写入文件")
    args = parser.parse_args()

    workspace_root = find_workspace_root()
    submodules_info = parse_gitmodules(workspace_root)

    target = Path(args.path)
    if not target.is_absolute():
        target = workspace_root / target

    if args.all:
        # 处理项目下所有主题
        if not target.exists():
            print(f"❌ 路径不存在: {target}")
            sys.exit(1)

        topics = sorted([
            d for d in os.listdir(target)
            if os.path.isdir(target / d)
            and not d.startswith('.')
            and d != 'index.md'
        ])
        if not topics:
            print(f"⚠️  未找到任何教学主题: {target}")
            sys.exit(0)

        print(f"📁 项目: {target.relative_to(workspace_root)}")
        print(f"   共 {len(topics)} 个主题\n")
        for topic in topics:
            generate_snapshot(target / topic, workspace_root, submodules_info, args.dry_run)
        print(f"\n✅ 完成！共处理 {len(topics)} 个主题")
    else:
        # 处理单个主题
        if not target.exists():
            print(f"❌ 主题目录不存在: {target}")
            sys.exit(1)
        generate_snapshot(target, workspace_root, submodules_info, args.dry_run)
        if not args.dry_run:
            print(f"\n✅ 已生成: {target / 'SNAPSHOT.md'}")


if __name__ == "__main__":
    main()

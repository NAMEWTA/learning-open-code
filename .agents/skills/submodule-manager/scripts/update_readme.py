#!/usr/bin/env python3
"""
Generate/update the root README.md with an index of all synced submodules.

Reads .gitmodules, groups submodules by category directory, and produces
a markdown table per category with submodule name, description (from
GitHub/Gitee), URL, and tracking branch.
"""

import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent

CATEGORY_INFO = {
    "open-ai-skills":    ("🧠 AI 编程 Skills 与工作流", "Agent skills 包、编程指南、AI 编程工作流方法论"),
    "open-sdd":          ("📋 规范驱动开发 (SDD)", "Spec-Driven Development 工具与框架"),
    "open-ai-agent":     ("🤖 AI Agent 与编程工具", "AI 编程 CLI、Agent 框架、Agent 运行时"),
    "open-ai-desktop":   ("🖥️ AI 桌面应用与 IDE", "AI 工作站桌面应用、AI 编程专用 IDE"),
    "open-knowledge":    ("📝 知识管理与编辑器", "笔记应用、知识库、Markdown/富文本编辑器"),
    "open-productivity": ("✅ 效率工具", "个人生产力、任务管理、时间追踪"),
    "open-java":         ("☕ Java 企业开发", "Java 后端框架、企业级管理系统"),
    "open-trading":      ("📈 量化交易与金融数据", "量化交易策略、回测框架、A股数据工具"),
    "open-data":         ("📊 数据开发", "数据工程、数据分析工具、金融数据平台"),
}

def parse_gitmodules():
    content = (REPO_ROOT / ".gitmodules").read_text()
    submodules = []
    current = {}
    for line in content.splitlines():
        m = re.match(r'\[submodule\s+"(.+)"\]', line)
        if m:
            if current:
                submodules.append(current)
            current = {"name": m.group(1)}
            continue
        m = re.match(r'\s*(path|url|branch)\s*=\s*(.+)', line)
        if m and current:
            current[m.group(1)] = m.group(2).strip()
    if current:
        submodules.append(current)
    return submodules

def fetch_github_description(url):
    """Fetch the repo description from GitHub/Gitee API."""
    # GitHub
    m = re.match(r'https://github\.com/([^/]+)/([^/]+?)(?:\.git)?$', url)
    if m:
        owner, repo = m.group(1), m.group(2)
        try:
            api_url = f"https://api.github.com/repos/{owner}/{repo}"
            req = urllib.request.Request(api_url, headers={"User-Agent": "submodule-manager"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                desc = data.get("description", "")
                stars = data.get("stargazers_count", 0)
                star_str = f" ⭐{stars//1000}k" if stars >= 1000 else (f" ⭐{stars}" if stars > 0 else "")
                return (desc or "(no description)") + star_str
        except Exception:
            return "(N/A)"

    # Gitee - try API
    m = re.match(r'https://gitee\.com/([^/]+)/([^/]+?)(?:\.git)?$', url)
    if m:
        owner, repo = m.group(1), m.group(2)
        try:
            api_url = f"https://gitee.com/api/v5/repos/{owner}/{repo}"
            req = urllib.request.Request(api_url, headers={"User-Agent": "submodule-manager"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                desc = data.get("description", "")
                stars = data.get("stargazers_count", 0)
                star_str = f" ⭐{stars//1000}k" if stars >= 1000 else (f" ⭐{stars}" if stars > 0 else "")
                return (desc or "(no description)") + star_str
        except Exception:
            return "(N/A)"

    return "(N/A)"

def get_short_name(name, url):
    """Get a display-friendly name."""
    return name.split("/")[-1]

def generate_readme(submodules):
    """Generate README.md content."""
    # Group by category
    grouped = {}
    for sm in submodules:
        path = sm.get("path", "")
        category = path.split("/")[0] if "/" in path else "other"
        grouped.setdefault(category, []).append(sm)

    lines = []
    lines.append("# Learning Open Code")
    lines.append("")
    lines.append("> 开源项目学习仓库 — 按功能分类整理的优质开源项目集合，涵盖 AI 编程、Agent 框架、知识管理、Java 企业开发等领域。")
    lines.append("")
    lines.append(f"**共收录 {len(submodules)} 个开源项目**，通过 git submodule 方式管理，可独立更新。")
    lines.append("")
    lines.append("---")
    lines.append("")

    # TOC
    lines.append("## 📑 目录")
    lines.append("")
    for cat, (title, _) in CATEGORY_INFO.items():
        count = len(grouped.get(cat, []))
        if count > 0:
            anchor = title.split(" ", 1)[-1] if " " in title else title
            lines.append(f"- [{title}](#{anchor.replace(' ', '-').replace('(', '').replace(')', '')})（{count} 个项目）")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per category
    for cat, (title, desc) in CATEGORY_INFO.items():
        items = grouped.get(cat, [])
        if not items:
            continue
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"> {desc}")
        lines.append("")
        lines.append("| 项目 | 描述 | 分支 |")
        lines.append("|------|------|------|")
        for sm in sorted(items, key=lambda x: x.get("path", "")):
            path = sm.get("path", "")
            url = sm.get("url", "")
            branch = sm.get("branch", "main")
            name = get_short_name(sm.get("name", path), url)
            desc_text = fetch_github_description(url)
            lines.append(f"| [{name}]({url}) | {desc_text} | `{branch}` |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 🔧 管理")
    lines.append("")
    lines.append("本项目使用 `git submodule` 管理所有子项目。通过 [submodule-manager](.agents/skills/submodule-manager/SKILL.md) skill 进行自动化管理：")
    lines.append("")
    lines.append("- **添加项目**: `python3 .agents/skills/submodule-manager/scripts/add_submodule.py --url <url> --category <dir> --branch <branch>`")
    lines.append("- **同步所有项目**: `python3 .agents/skills/submodule-manager/scripts/sync_submodules.py`")
    lines.append("- **更新此文档**: `python3 .agents/skills/submodule-manager/scripts/update_readme.py`")
    lines.append("")
    lines.append(f"*最后更新: 由 submodule-manager 自动生成*")

    return "\n".join(lines) + "\n"

def main():
    os.chdir(REPO_ROOT)
    submodules = parse_gitmodules()
    print(f"Found {len(submodules)} submodules, generating README.md...")
    readme = generate_readme(submodules)
    (REPO_ROOT / "README.md").write_text(readme)
    print(f"✓ README.md written ({len(readme)} bytes)")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Add a new git submodule to the learning-open-code mono-repo.

Usage:
    python3 add_submodule.py --url <repo-url> [--category <dir>] [--branch <branch>]

Auto-detects the default branch if --branch is omitted.
Prompts for category selection if --category is omitted.
Records the branch in .gitmodules and updates README.md.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent

CATEGORIES = {
    "open-ai-skills":    "AI 编程 Skills 与工作流",
    "open-sdd":          "规范驱动开发 (SDD)",
    "open-ai-agent":     "AI Agent 与编程工具",
    "open-ai-desktop":   "AI 桌面应用与 IDE",
    "open-knowledge":    "知识管理与编辑器",
    "open-productivity": "效率工具",
    "open-java":         "Java 企业开发",
    "open-trading":      "量化交易与金融数据",
    "open-data":         "数据开发",
}

def run(cmd, cwd=None):
    """Run a shell command, return stdout. Raise on failure."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"ERROR: {cmd}\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    return result.stdout.strip()

def detect_default_branch(url):
    """Detect the default branch of a remote repo."""
    output = run(f"git ls-remote --symref {url} HEAD")
    match = re.search(r'ref: refs/heads/(\S+)\s+HEAD', output)
    if match:
        return match.group(1)
    # Fallback: try common branch names
    for branch in ("main", "master"):
        result = subprocess.run(
            f"git ls-remote --heads {url} {branch}",
            shell=True, capture_output=True, text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            return branch
    return "main"

def extract_name_from_url(url):
    """Extract a friendly name from a git URL."""
    # https://github.com/owner/repo.git -> repo
    # https://gitee.com/owner/repo.git -> repo
    name = url.rstrip("/").rstrip(".git").split("/")[-1]
    return name

def prompt_category():
    """Prompt user to select a category."""
    print("\nAvailable categories:")
    for i, (key, desc) in enumerate(CATEGORIES.items(), 1):
        print(f"  {i}. {key} — {desc}")
    while True:
        try:
            choice = input(f"\nSelect category [1-{len(CATEGORIES)}]: ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(CATEGORIES):
                return list(CATEGORIES.keys())[idx]
        except (ValueError, IndexError):
            pass
        print(f"Please enter a number 1-{len(CATEGORIES)}.")

def add_submodule(url, category, branch):
    """Add a git submodule to the specified category."""
    name = extract_name_from_url(url)
    path = f"{category}/{name}"

    print(f"Adding submodule: {name}")
    print(f"  URL:      {url}")
    print(f"  Category: {category}")
    print(f"  Path:     {path}")
    print(f"  Branch:   {branch}")

    # Clone the submodule
    run(f"git submodule add -b {branch} {url} {path}", cwd=REPO_ROOT)

    # Record branch explicitly in .gitmodules
    gitmodules = REPO_ROOT / ".gitmodules"
    content = gitmodules.read_text()
    # The `git submodule add -b` already adds the branch, but verify
    if f'branch = {branch}' not in content:
        print("Warning: branch not recorded in .gitmodules. Please check manually.")

    print(f"✓ Submodule '{name}' added successfully to {category}/")
    return path

def main():
    parser = argparse.ArgumentParser(description="Add a git submodule to the mono-repo")
    parser.add_argument("--url", required=True, help="Git repository URL")
    parser.add_argument("--category", choices=list(CATEGORIES.keys()), help="Target category directory")
    parser.add_argument("--branch", help="Branch to track (auto-detected if omitted)")
    args = parser.parse_args()

    os.chdir(REPO_ROOT)

    # Determine category
    category = args.category or prompt_category()
    if category not in CATEGORIES:
        print(f"Invalid category: {category}", file=sys.stderr)
        sys.exit(1)

    # Determine branch
    branch = args.branch or detect_default_branch(args.url)
    print(f"Detected default branch: {branch}")

    # Add submodule
    add_submodule(args.url, category, branch)

    # Update README
    update_script = REPO_ROOT / ".agents/skills/submodule-manager/scripts/update_readme.py"
    if update_script.exists():
        print("\nUpdating README.md index...")
        run(f"python3 {update_script}", cwd=REPO_ROOT)
        print("✓ README.md updated.")

if __name__ == "__main__":
    main()

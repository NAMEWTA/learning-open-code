#!/usr/bin/env python3
"""
teach skill — 检测源项目更新，判断课程是否需要同步

用法:
  # 检查单个主题
  python scripts/check_updates.py teach/open-java/RuoYiVuePlus/permission-model

  # 检查某项目下所有主题
  python scripts/check_updates.py teach/open-java/RuoYiVuePlus --all

  # 详细模式（显示 diff 文件列表）
  python scripts/check_updates.py teach/open-java/RuoYiVuePlus/permission-model --verbose

功能:
  1. 读取 SNAPSHOT.md 中记录的 git commit
  2. 获取源项目当前 HEAD
  3. 对比是否有变更
  4. 如有变更，执行 git diff 列出变更文件
  5. 输出课程更新建议
"""

import os
import re
import sys
import argparse
import subprocess
from pathlib import Path


def find_workspace_root():
    script_dir = Path(__file__).resolve().parent
    current = script_dir
    while current != current.parent:
        if (current / ".gitmodules").exists():
            return current
        current = current.parent
    return script_dir.parent.parent.parent.parent


def parse_gitmodules(workspace_root):
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


def parse_snapshot(snapshot_file):
    """解析 SNAPSHOT.md，提取 git commit 和引用文件列表"""
    if not snapshot_file.exists():
        return None

    with open(snapshot_file, "r", encoding="utf-8") as f:
        content = f.read()

    result = {
        "repos": [],      # list of {path, commit, branch}
        "ref_files": [],  # list of source file paths
        "lesson_count": 0,
    }

    # 提取源仓库信息
    # 格式: - **源仓库**：`open-java/RuoYiVuePlus/ruoyi-vue-plus`
    #         - **Git Commit**：`3481414...`
    repo_pattern = re.compile(
        r'-\s*\*\*源仓库\*?\*?\s*\d*\s*\*\*?：`([^`]+)`\s*\n'
        r'\s*-\s*\*\*Git Commit\*\*：`([^`]+)`',
        re.MULTILINE
    )
    for match in repo_pattern.finditer(content):
        result["repos"].append({
            "path": match.group(1),
            "commit": match.group(2),
        })

    # 提取引用文件
    ref_pattern = re.compile(r'^\|\s*`([^`]+)`\s*\|', re.MULTILINE)
    for match in ref_pattern.finditer(content):
        ref = match.group(1)
        if ref not in ("源文件路径", "编号"):
            result["ref_files"].append(ref)

    # 提取课程数
    lesson_match = re.search(r'-\s*课程数[：:]\s*(\d+)', content)
    if lesson_match:
        result["lesson_count"] = int(lesson_match.group(1))

    return result


def find_related_submodules(topic_project_path, submodules):
    """找到与项目关联的子模块"""
    related = []
    for sp, info in submodules.items():
        if sp.startswith(topic_project_path + "/"):
            related.append((sp, info))
    if not related:
        for sp, info in submodules.items():
            if sp == topic_project_path:
                related.append((sp, info))
                break
    return related


def resolve_repo_path(repo_name, submodules_info):
    """将 SNAPSHOT.md 中的仓库名解析为工作区中的完整路径

    支持三种格式:
    - 完整路径: open-java/RuoYiVuePlus/ruoyi-vue-plus → 直接使用
    - 短名: ruoyi-vue-plus → 在 .gitmodules 中查找匹配的 path
    - 部分路径: RuoYiVuePlus/ruoyi-vue-plus → 在 .gitmodules 中查找后缀匹配
    """
    # 直接匹配完整路径
    if repo_name in submodules_info:
        return repo_name

    # 后缀匹配（短名或部分路径）
    for sp in submodules_info:
        if sp.endswith("/" + repo_name) or sp == repo_name:
            return sp

    # 模糊匹配：path 中包含 repo_name
    for sp in submodules_info:
        if repo_name in sp:
            return sp

    return repo_name  # 回退：直接返回原名（可能不存在）


def check_topic(topic_path, workspace_root, submodules_info, verbose=False):
    """检查单个主题的更新状态"""
    topic_path = Path(topic_path)
    topic_name = topic_path.name
    snapshot_file = topic_path / "SNAPSHOT.md"

    if not snapshot_file.exists():
        print(f"  ⚠️  {topic_name}: 无 SNAPSHOT.md，跳过")
        return

    snapshot = parse_snapshot(snapshot_file)
    if not snapshot or not snapshot["repos"]:
        print(f"  ⚠️  {topic_name}: SNAPSHOT.md 格式异常，跳过")
        return

    all_unchanged = True
    for repo_info in snapshot["repos"]:
        repo_name = repo_info["path"]
        repo_path_str = resolve_repo_path(repo_name, submodules_info)
        repo_path = workspace_root / repo_path_str
        old_commit = repo_info["commit"]

        if not repo_path.exists():
            print(f"  ❌ {topic_name}: 源仓库不存在 — {repo_info['path']}")
            all_unchanged = False
            continue

        try:
            current_commit = subprocess.check_output(
                ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
                text=True, stderr=subprocess.DEVNULL
            ).strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"  ❌ {topic_name}: 无法获取 git 信息 — {repo_info['path']}")
            all_unchanged = False
            continue

        if current_commit == old_commit:
            if verbose:
                short = old_commit[:7]
                print(f"  ✅ {topic_name} @ {repo_info['path']}: {short} — 未变更")
            continue

        all_unchanged = False
        short_old = old_commit[:7]
        short_new = current_commit[:7]
        print(f"  🔄 {topic_name} @ {repo_info['path']}: {short_old} → {short_new}")

        # 执行 diff
        if verbose and snapshot["ref_files"]:
            try:
                # 对快照中记录的源文件执行 diff
                ref_files_args = []
                for rf in snapshot["ref_files"]:
                    # 只取看起来像真实文件路径的
                    if '/' in rf and not rf.startswith('&') and not rf.startswith('//'):
                        ref_files_args.append(rf)

                if ref_files_args:
                    cmd = ["git", "-C", str(repo_path), "diff", "--name-only",
                           f"{old_commit}..HEAD", "--"] + ref_files_args
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                    changed_files = [f for f in result.stdout.strip().split('\n') if f]
                    if changed_files:
                        print(f"     📝 课程引用的变更文件 ({len(changed_files)}):")
                        for cf in changed_files[:20]:
                            print(f"        • {cf}")
                        if len(changed_files) > 20:
                            print(f"        ... 还有 {len(changed_files) - 20} 个文件")
                    else:
                        print(f"     ℹ️  课程引用的源文件无变更（变更在其他文件）")
            except Exception as e:
                print(f"     ⚠️  diff 执行失败: {e}")

        # 全部变更文件概览
        if verbose:
            try:
                cmd = ["git", "-C", str(repo_path), "diff", "--stat",
                       f"{old_commit}..HEAD"]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                if result.stdout.strip():
                    lines = result.stdout.strip().split('\n')
                    last_line = lines[-1] if lines else ""
                    print(f"     📊 总变更: {last_line.strip()}")
            except Exception:
                pass

    if all_unchanged:
        print(f"  ✅ {topic_name}: 所有源仓库均未变更")


def main():
    parser = argparse.ArgumentParser(description="检测教学主题的源项目更新状态")
    parser.add_argument("path", help="教学主题路径或项目路径")
    parser.add_argument("--all", action="store_true", help="检查指定路径下的所有主题")
    parser.add_argument("--verbose", "-v", action="store_true", help="显示详细 diff 信息")
    args = parser.parse_args()

    workspace_root = find_workspace_root()
    submodules_info = parse_gitmodules(workspace_root)

    target = Path(args.path)
    if not target.is_absolute():
        target = workspace_root / target

    if args.all:
        if not target.exists():
            print(f"❌ 路径不存在: {target}")
            sys.exit(1)

        topics = sorted([
            d for d in os.listdir(target)
            if os.path.isdir(target / d) and not d.startswith('.')
        ])
        if not topics:
            print(f"⚠️  未找到任何教学主题: {target}")
            sys.exit(0)

        print(f"🔍 检查 {len(topics)} 个主题...\n")
        for topic in topics:
            check_topic(target / topic, workspace_root, submodules_info, args.verbose)
        print(f"\n✅ 检查完成")
    else:
        check_topic(target, workspace_root, submodules_info, args.verbose)


if __name__ == "__main__":
    main()

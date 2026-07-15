#!/usr/bin/env bash
set -euo pipefail

# 注意：这是一个仅限开发者的脚本，仅供本仓库维护者使用。
# 它不是受支持的安装器。对其的修改——或修改请求——将不会被批准。
#
# 将仓库中的所有 skill 链接到每个 agent harness 使用的本地 skill 目录：
#   - ~/.claude/skills  — Claude Code
#   - ~/.agents/skills  — pi 和其他遵循 Agent-Skills 标准的 harness
# 每个条目是指向此仓库的符号链接，因此只需 `git pull` 即可
# 保持已安装 skill 的最新状态。

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DESTS=("$HOME/.claude/skills" "$HOME/.agents/skills")

# 一次性收集仓库的 skill，然后链接到每个目标目录。
names=()
srcs=()
while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  names+=("$(basename "$src")")
  srcs+=("$src")
done < <(find "$REPO/skills" -name SKILL.md -not -path '*/node_modules/*' -not -path '*/deprecated/*' -print0)

for DEST in "${DESTS[@]}"; do
  # 如果 $DEST 是指向此仓库的符号链接，我们会将每个 skill 的符号链接
  # 写回仓库自身的 skills/ 目录树。检测并退出，而不是污染工作副本。
  if [ -L "$DEST" ]; then
    resolved="$(readlink -f "$DEST")"
    case "$resolved" in
      "$REPO"|"$REPO"/*)
        echo "error: $DEST is a symlink into this repo ($resolved)." >&2
        echo "Remove it (rm \"$DEST\") and re-run; the script will recreate it as a real dir." >&2
        exit 1
        ;;
    esac
  fi

  mkdir -p "$DEST"

  for i in "${!names[@]}"; do
    name="${names[$i]}"
    src="${srcs[$i]}"
    target="$DEST/$name"

    if [ -e "$target" ] && [ ! -L "$target" ]; then
      rm -rf "$target"
    fi

    ln -sfn "$src" "$target"
    echo "linked $name -> $src ($DEST)"
  done
done

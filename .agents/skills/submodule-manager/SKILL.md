---
name: submodule-manager
description: |
  Manage git submodules for the learning-open-code mono-repo. Use when the user wants to:
  (1) Add a new git submodule — auto-detect or specify the category (open-ai-skills/open-sdd/open-ai-agent/open-ai-desktop/open-knowledge/open-productivity/open-java),
      record the tracking branch in .gitmodules, clone the repo, and update README.md index.
  (2) Sync all existing submodules to their configured branches (git fetch + checkout branch + pull).
  (3) Update the root README.md with an up-to-date index of all synced projects grouped by category.
  Trigger keywords: submodule, git submodule, 子模块, add submodule, sync submodule, update submodule, submodule branch, README index, 更新索引.
---

# Submodule Manager

Manage git submodules in this learning-open-code mono-repo. Every submodule lives under a category directory and is tracked with an explicit branch in `.gitmodules`.

## Category Directories

| Category | Directory | Description |
|----------|-----------|-------------|
| AI 编程 Skills 与工作流 | `open-ai-skills/` | Agent skill packs, coding guidelines, workflow methodologies |
| 规范驱动开发 (SDD) | `open-sdd/` | Spec-Driven Development tools and frameworks |
| AI Agent 与编程工具 | `open-ai-agent/` | AI coding CLIs, agent frameworks, agent runtimes |
| AI 桌面应用与 IDE | `open-ai-desktop/` | Desktop AI workstations and AI-focused IDEs |
| 知识管理与编辑器 | `open-knowledge/` | Note apps, knowledge bases, markdown/rich-text editors |
| 效率工具 | `open-productivity/` | Productivity tools (todo, time tracking) |
| Java 企业开发 | `open-java/` | Java enterprise backend projects |

## Workflows

### 1. Add a New Submodule

Run `scripts/add_submodule.py` with the repo URL and optional category/branch:

```bash
python3 .agents/skills/submodule-manager/scripts/add_submodule.py \
  --url https://github.com/owner/repo.git \
  --category open-ai-skills \
  --branch main
```

- If `--category` is omitted, the script will prompt to choose from the 7 categories.
- If `--branch` is omitted, the script auto-detects the default branch via `git ls-remote`.
- The script writes the `branch = ...` entry into `.gitmodules` (required for sync).
- After cloning, it runs `scripts/update_readme.py` to refresh the index.

### 2. Sync All Submodules to Their Branches

Run `scripts/sync_submodules.py` to fetch and checkout every submodule to its configured branch:

```bash
python3 .agents/skills/submodule-manager/scripts/sync_submodules.py
```

- Reads `.gitmodules` for each submodule's `url`, `path`, and `branch`.
- For each submodule: `git fetch origin`, `git checkout <branch>`, `git pull origin <branch>`.
- Reports success/failure per submodule.
- After syncing all, runs `scripts/update_readme.py` to refresh the index.

### 3. Update README.md Index

Run `scripts/update_readme.py` to regenerate the root README.md:

```bash
python3 .agents/skills/submodule-manager/scripts/update_readme.py
```

- Reads `.gitmodules` to enumerate all submodules by category.
- For each submodule, extracts GitHub description from the local clone's remote URL.
- Generates a markdown table per category with: submodule name, description, URL, branch.
- Writes `README.md` at the repo root.

## Example Usage

```
User: 帮我添加 submodule https://github.com/oven-sh/bun.git 到 open-ai-agent 分类

Agent:
  1. Runs add_submodule.py --url https://github.com/oven-sh/bun.git --category open-ai-agent --branch main
  2. Verifies clone succeeded
  3. README.md is auto-updated

User: 同步所有 submodule 到最新

Agent:
  1. Runs sync_submodules.py
  2. Reports per-submodule status
  3. README.md is auto-refreshed
```

## Notes

- All scripts require Python 3.9+ and `git` available on PATH.
- The `.gitmodules` file must have a `branch = ...` entry for every submodule to enable sync.
- Java submodules use Gitee URLs; all others use GitHub URLs.
- The README.md is auto-generated — do not manually edit the index tables.

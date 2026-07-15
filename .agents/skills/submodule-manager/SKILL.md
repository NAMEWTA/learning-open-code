---
name: submodule-manager
description: |
  Manage git submodules for the learning-open-code mono-repo. Use when the user wants to:
  (1) Add a new git submodule — auto-detect or specify the category (open-ai-skills/open-sdd/open-ai-agent/open-ai-desktop/open-knowledge/open-productivity/open-java/open-trading/open-data),
      record the tracking branch in .gitmodules, clone the repo, and update README.md index.
  (2) Sync all existing submodules to their configured branches (git fetch + checkout branch + pull).
  (3) Update the root README.md with an up-to-date index of all synced projects grouped by category.
  (4) Initialize submodules after git clone — when open-*/ directories are empty or git submodule status returns nothing,
      guide through the full SOP (git submodule update --init --recursive [--remote]).
  Trigger keywords: submodule, git submodule, 子模块, add submodule, sync submodule, update submodule,
  submodule branch, README index, 更新索引, clone, init, 初始化子模块, submodule init, 拉取子模块.
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
| 量化交易与金融数据 | `open-trading/` | Quantitative trading, backtesting, stock data tools |
| 数据开发 | `open-data/` | Data engineering, data tools, financial data platforms |

## Workflows

### 1. Add a New Submodule

Run `scripts/add_submodule.py` with the repo URL and optional category/branch:

```bash
python3 .agents/skills/submodule-manager/scripts/add_submodule.py \
  --url https://github.com/owner/repo.git \
  --category open-ai-skills \
  --branch main
```

- If `--category` is omitted, the script will prompt to choose from the 9 categories.
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

### 4. Clone 后初始化所有子模块（SOP）

> **适用场景：** 新成员 `git clone` 本仓库后，或本地 `open-*/` 目录为空、`git submodule status` 返回空时。

#### 4.1 标准初始化（锁定 gitlink 记录的 commit）

拉取所有子模块到 `.gitmodules` 中注册的 gitlink commit：

```bash
git submodule update --init --recursive
```

- 每个子模块会 checkout 到仓库 `.gitmodules` + gitlink 锁定的 commit
- **适用：** 需要可复现的构建环境、CI/CD、代码审查场景

#### 4.2 拉取最新代码（跟踪远端分支 HEAD）

拉取所有子模块的远端最新 commit（忽略 gitlink 锁定）：

```bash
git submodule update --init --recursive --remote
```

- 每个子模块会 checkout 到 `.gitmodules` 中 `branch = ...` 配置的分支最新 commit
- **适用：** 学习最新源码、探索最新特性

#### 4.3 完整 SOP 流程

```bash
# 1. 克隆主仓库
git clone <本仓库 URL>
cd learning-open-code

# 2. 初始化并拉取所有子模块（二选一）
# 方式 A：锁定版本（推荐用于可复现环境）
git submodule update --init --recursive

# 方式 B：拉取最新（推荐用于学习探索）
git submodule update --init --recursive --remote

# 3. 验证
git submodule status        # 应显示全部子模块及 commit hash
ls open-ai-agent/           # 应有多个子目录，每个都有内容
```

#### 4.4 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| `git submodule status` 返回空 | 本地未注册 gitlink 或未 init | 执行 `git submodule update --init --recursive` |
| `open-*/` 目录为空 | 同上 | 同上 |
| 部分子模块拉取失败 | 网络问题或 URL 失效 | 检查 `.gitmodules` 中 URL 是否可访问 |
| `fatal: not a git repository` | `.gitmodules` 存在但 gitlink 未提交 | 需要仓库维护者提交 gitlink（参考 AGENTS.md） |

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

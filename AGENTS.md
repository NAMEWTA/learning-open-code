# AGENTS.md — Learning Open Code 代码仓 AI 协作指南

本文件是整个 monorepo 的**导航层**，为所有 AI 编码 Agent（Claude Code、Codex、Copilot 等）提供统一的协作规范。它是仓库的"单一事实来源"（source of truth），定义了目录结构、交互语言、子模块约定以及 Agent Team 使用策略。

---

## 语言要求（重要）

> **与用户交互时必须使用简体中文。**
>
> 所有对话、代码注释、commit message、文档说明均以简体中文输出。涉及代码标识符（变量名、函数名、类名等）保留原始英文命名。

---

## 仓库概览

`learning-open-code` 是一个**开源项目学习仓库**，通过 git submodule 方式收录 33 个优质开源项目，按功能领域分为 7 大类别。每个子模块独立管理自己的 git 历史与分支，可独立拉取更新。

### 顶层目录结构

```
learning-open-code/
├── AGENTS.md                       # ← 本文件：AI Agent 全局协作规范
├── README.md                       # 仓库说明与项目索引
├── .gitmodules                     # 子模块定义（path、url、branch）
├── .agents/                        # 本仓库自有 Agent Skills
│   └── skills/
│       ├── chinese-documentation/          # 中文文档排版规范
│       ├── chinese-documentation-translator/ # 英文→中文翻译工作流
│       ├── submodule-manager/              # Git 子模块管理
│       └── teach/                          # 教学系统（项目学习课程）
├── open-ai-skills/                 # 🧠 AI 编程 Skills 与工作流（6 个项目）
│   ├── addyosmani-agent-skills/
│   ├── andrej-karpathy-skills/
│   ├── caveman/
│   ├── matt-pocock-skills/
│   ├── pm-skills/
│   └── superpowers-zh/
├── open-sdd/                       # 📋 规范驱动开发 SDD（4 个项目）
│   ├── flow-kit/
│   ├── OpenSpec/
│   ├── spec-kit/
│   └── specforge/
├── open-ai-agent/                  # 🤖 AI Agent 与编程工具（8 个项目）
│   ├── claude-code/
│   ├── deer-flow/
│   ├── gstack/
│   ├── learn-claude-code/
│   ├── nanobot/
│   ├── oh-my-claudecode/
│   ├── OpenHarness/
│   └── pi/
├── open-ai-desktop/                # 🖥️ AI 桌面应用与 IDE（4 个项目）
│   ├── hello-halo/
│   ├── nezha/
│   ├── openhanako/
│   └── orca/
├── open-knowledge/                 # 📝 知识管理与编辑器（6 个项目）
│   ├── AFFiNE/
│   ├── BlockNote/
│   ├── marktext/
│   ├── solomd/
│   ├── tolaria/
│   └── Trilium/
├── open-productivity/              # ✅ 效率工具（1 个项目）
│   └── super-productivity/
├── open-java/                      # ☕ Java 企业开发（4 个项目）
│   ├── RuoYiVuePlus/
│   └── snail-ai/
├── teach/                          # 教学课程输出目录
├── self/                           # 个人研究/实验
└── translator/                     # 翻译工作区
```

### 分类与项目速查

| 分类目录 | 领域 | 项目数 |
|----------|------|--------|
| `open-ai-skills/` | AI 编程 Skills 与工作流 | 6 |
| `open-sdd/` | 规范驱动开发 (SDD) | 4 |
| `open-ai-agent/` | AI Agent 框架与编程 CLI | 8 |
| `open-ai-desktop/` | AI 桌面应用与 IDE | 4 |
| `open-knowledge/` | 知识管理与编辑器 | 6 |
| `open-productivity/` | 效率工具 | 1 |
| `open-java/` | Java 企业开发 | 2（含多子模块） |

> **说明：** `open-java/RuoYiVuePlus/` 是逻辑项目组，包含 3 个子模块（`ruoyi-vue-plus`、`ruoyi-vue`、`ruoyi-react`），它们共享同一个父目录，属于同一个 Java 全栈系统。处理时应视为一个整体逻辑项目。

---

## Agent Team 使用策略

> **当任务复杂、跨多个子项目、或需要专项分析时，应主动使用 Agent Team（子 Agent）。**

### 使用原则

1. **简单任务直接处理** — 单文件编辑、小范围搜索不需要启动 Agent Team
2. **跨项目任务必须委托** — 涉及多个子模块的分析、对比、迁移，启动
3. **结果回传** — Agent 完成后将结果汇总到主对话，由主 Agent 向用户呈现

---

## 子模块管理约定

本仓库所有开源项目以 **git submodule** 方式管理。遵循以下约定：

- **子模块 gitlink 不主动实时跟踪。** 允许用户自行切换子仓库 git 节点，仅在用户明确要求提交/合并/发布时才同步根仓 gitlink。
- 子模块按功能分类存放于 `open-*/` 目录下，映射关系见 `.gitmodules`。
- 添加新子模块使用 `.agents/skills/submodule-manager/` skill，自动检测分类、记录 tracking branch、更新 README 索引。
- 同步子模块使用 `git submodule update --remote` 或 submodule-manager skill。
- 某些子模块共享父目录（如 `RuoYiVuePlus`），在分析与教学时应作为逻辑整体处理。

---

## 自有 Skills

本仓库 `.agents/skills/` 目录下维护了 4 个自有技能：

| Skill | 功能 |
|-------|------|
| `chinese-documentation` | 中文文档排版规范（中英空格、全半角标点、术语保留） |
| `chinese-documentation-translator` | 英文→中文文档系统化翻译工作流 |
| `submodule-manager` | Git 子模块添加/同步/索引管理 |
| `teach` | 交互式教学系统，在工作区内按项目+主题组织课程 |

---

## 快速参考

- 查看完整项目列表与描述 → `README.md`
- 查看子模块定义 → `.gitmodules`
- 需要教学某个项目 → 使用 `teach` skill
- 需要添加/同步子模块 → 使用 `submodule-manager` skill
- 需要翻译文档 → 使用 `chinese-documentation-translator` skill
- 需要跨项目深度分析 → 启动 Agent Team

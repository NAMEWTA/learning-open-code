# CLAUDE.md

AI 代理（Claude Code、Cowork 等）在本仓库中工作的指导文档。本文件是项目结构和维护规范的唯一权威来源。

## 项目概述

**PM Skills**（`phuryn/pm-skills`）——一个包含 **9 个独立插件**（68 个 skills、42 个 commands）的市场，为 AI 编程助手提供结构化的产品管理工作流。面向 Claude Code 和 Claude Cowork 构建；这些 skills 也兼容其他代理（Gemini CLI、Cursor、Codex CLI）。

作者：Paweł Huryn — pawel@productcompass.pm — https://www.productcompass.pm

## 仓库结构

```
pm-skills/                           <- 仓库根目录
├── .claude-plugin/marketplace.json  <- 根市场清单（列出全部 9 个插件）
├── .docs/images/                    <- README 使用的图片（webp、gif）
├── .gitattributes
├── .gitignore
├── CLAUDE.md                        <- 本文件（代理指导，唯一权威来源）
├── AGENTS.md                        <- 指向 CLAUDE.md（供非 Claude 代理使用）
├── CONTRIBUTING.md                  <- 贡献者指南
├── README.md                        <- 公开文档（GitHub）
├── LICENSE                          <- MIT
├── validate_plugins.py              <- 插件验证器
└── pm-{name}/                       <- 9 个插件目录
    ├── .claude-plugin/plugin.json   <- 各插件清单
    ├── skills/{skill}/SKILL.md      <- 每个 skill 一个文件夹
    ├── commands/{command}.md        <- 每个 command 一个文件
    └── README.md                    <- 各插件文档
```

### 9 个插件

| 插件 | 定位 |
|--------|-------|
| `pm-product-discovery` | 创意构思、实验、假设验证、优先级排序、访谈总结 |
| `pm-product-strategy` | 愿景、战略/精益/商业模式画布、SWOT、PESTLE、安索夫、波特五力、盈利策略 |
| `pm-execution` | PRD、OKR、路线图、Sprint、事前验尸、利益相关方地图、用户故事、红队研判 |
| `pm-market-research` | 用户画像、细分、情感分析、竞争分析、市场规模估算 |
| `pm-data-analytics` | SQL 查询生成、同期群/留存分析 |
| `pm-go-to-market` | GTM 策略、增长循环、上市模式、滩头阵地细分、理想客户画像 |
| `pm-marketing-growth` | 营销创意、价值主张陈述、北极星指标、命名、定位 |
| `pm-toolkit` | 简历审核、NDA 起草、隐私政策、语法/流畅度检查 |
| `pm-ai-shipping` | AI 交付套件：为 vibe-coded 应用编写文档、映射测试覆盖、审计安全/性能与预期行为的偏差、编制交付包 |

## 核心设计规则

- **Skills = 名词/概念。** 框架和分析知识，当对话主题匹配时 Claude 自动加载（`lean-canvas`、`pre-mortem`、`market-sizing`）。
- **Commands = 动词。** 用户触发的、串联一个或多个 skill 的工作流（`/write-prd`、`/discover`、`/plan-launch`）。
- **禁止跨插件引用。** Commands 仅以自然语言建议后续操作（"需要我设计增长循环吗？"）。切勿硬编码引用其他插件的 command——插件独立安装，硬引用可能导致断裂。
- **插件内"使用"引用是允许的**——同一插件内的 skills 和 commands 始终一起发布。
- Commands 使用单个 `$ARGUMENTS` 占位符。Skills 不需要占位符（它们从对话上下文中读取内容）。
- **必须包含 Frontmatter：** Skills 需要 `name` + `description`；commands 需要 `description` + `argument-hint`。
- Skill 的 `name` **必须与其目录名匹配**。
- Skills 可通过 `/plugin-name:skill-name` 或 `/skill-name` 强制加载。
- 保持 frontmatter 精简（始终加载）；将详细内容放在 SKILL.md 正文中（触发时加载）——渐进式披露。

## 各位置的可见性

| 位置 | 可见于 | 备注 |
|----------|-----------|-------|
| `marketplace.json` → `description` | Cowork 市场浏览器、Claude Code | 整个市场的单行简介 |
| `plugin.json` → `description` | Cowork 插件列表、Claude Code | 各插件摘要；简洁且功能性 |
| `SKILL.md` frontmatter → `description` | Cowork skill 列表、Claude 自动加载 | 包含触发短语，以便 Claude 在合适的时机加载 skill |
| Command frontmatter → `description` + `argument-hint` | Cowork 和 Claude Code（输入 `/` 时） | 简短且可操作 |
| `README.md`（仓库根目录） | 仅 GitHub | 完整文档；Claude 运行时不加载 |

`plugin.json` 和仓库 `README.md` 中的描述应保持一致（相同文本）。

## 版本管理

- 当前所有版本均为 **2.0.0**——包括 `marketplace.json` 和全部 9 个 `plugin.json` 文件。
- **保持所有版本同步。** 不存在独立的按插件版本管理。
- 修改任一 `plugin.json` → 同步修改 `marketplace.json`，反之亦然（全部 9 个同步升级）。

## Skills 中的文章链接（延伸阅读）

- 已映射的 skills 以 `### 延伸阅读` 部分结尾，链接到相关的 Product Compass 文章。
- **语气必须保持中立**——不得使用推广性语言、CTA、"订阅"/"查看"等。仅保留文章标题和 URL。
- Claude 根据对话相关性展示这些链接，而非每次回复都展示。
- 标题中包含「Masterclass」或「Course」的帖子为视频课程——标记为 `（视频课程）`。

## 操作流程

### 任何 skill/command 变更后
1. 从仓库根目录运行 `python3 validate_plugins.py` 检查所有插件。
2. 如果添加或移除了 skills/commands，更新 `README.md` 中的计数。
3. 如果总数变更，更新 `marketplace.json` description 中的计数。
4. 升级所有清单文件的版本（参见版本管理）。

### description 变更后
- `plugin.json` description 变更 → 检查 `README.md` 是否需要同步编辑（二者保持一致）。
- `SKILL.md` description 变更 → 无需其他同步（它是该 skill 的唯一来源）。

## 验证

`validate_plugins.py` 检查：`plugin.json` 必填字段 / 名称匹配 / semver / 作者 / 关键词；skill frontmatter 及名称与目录匹配；command frontmatter（`description` + `argument-hint`）；README 是否存在；以及插件内 command→skill 的引用。

```
python3 validate_plugins.py
```

## 工作完成后的建议

提供相关的后续操作建议：
- 结构性变更后：「需要我运行验证器吗？」
- 添加/移除 skills 或 commands 后：「需要我更新 README.md 和 marketplace.json 中的计数吗？」
- 编辑 description 后：「需要我同步到 README.md / plugin.json 吗？」
- 任何仓库变更后：「需要我升级版本号吗？」

# 按文件类型的详细翻译规则

## SKILL.md 文件翻译规则

### Frontmatter（YAML 头部，`---` 之间）
- **`name`**：绝对不能翻译，必须与目录名完全一致。这是验证器检查的关键字段。
- **`description`**：翻译为中文。保持简洁，长度控制在原英文长度的 1-1.5 倍内。必须包含触发短语（如"适用于……"），以便 AI 自动加载。引号保留。
- **其他 key**：不翻译 YAML key 本身。

### 正文
- 翻译所有正文、章节标题、操作步骤、说明文字、表格文本、列表项
- **保留英文不变**：
  - 代码块（三重反引号区域）
  - 内联代码（单反引号包裹的内容）
  - `$ARGUMENTS` 占位符
  - 技术框架名：SWOT、PESTLE、JTBD、OKR、PRD、ICP、GTM、NDA、TAM/SAM/SOM 等
  - 工具名：Redis、React、Kubernetes、BigQuery、PostgreSQL 等
  - 命令引用：`/discover`、`/write-prd` 等
  - 文件路径和文件名
  - URL 和文章标题（在"延伸阅读"部分）

### 翻译模式选择

根据文件长度和复杂度选择精简或完整翻译：

- **短文件（< 80 行）**：完整翻译所有内容
- **中文件（80-150 行）**：翻译正文，保持结构。适当精简重复性内容。
- **长文件（> 150 行）**：翻译正文，保持结构。对框架理论、背景说明、重复要点可适度精简。保留核心指令和约束条件不精简。
- **模板类文件（如 NDA、隐私政策）**：完整翻译所有章节和说明。保留 `$VARIABLE` 占位符。
- **框架分析类文件（如波特五力、PESTLE）**：完整翻译框架定义，可精简详细列表中的举例部分。

### 章节标题翻译惯例

| English | 中文 |
|---------|------|
| Purpose | 目的 |
| Context / Background | 背景 |
| Domain Context | 领域背景 |
| Instructions | 操作指引 |
| Process / How It Works | 工作方式 / 流程 |
| Step N | 第 N 步 |
| Usage Examples | 使用示例 |
| Key Capabilities | 核心能力 |
| Tips for Best Results | 获取最佳结果的技巧 |
| Output / Output Format | 输出 / 输出格式 |
| Notes | 注意事项 |
| Further Reading | 延伸阅读 |
| When to Use | 使用场景 |
| Best Practices | 最佳实践 |
| Important Guidelines | 重要指南 |
| Input Format | 输入格式 |
| Input Requirements | 输入要求 |
| Framework | 框架 |
| Strategic Applications | 战略应用 |
| Overview | 概述 |
| Metadata | 说明 |

## Command .md 文件翻译规则

### Frontmatter
- `description`：翻译为中文
- `argument-hint`：翻译占位符内容，保留 `<` `>` 格式。例如：`"<data file or description of what to analyze>"` → `"<数据文件或要分析的内容描述>"`

### 正文
- 翻译标题（`# /command-name -- Description` 中的 Description 部分）
- 翻译"Invocation"章节标题为"调用方式"，示例代码块中的描述文字翻译，命令本身不变
- 翻译"Workflow"为"工作流"，保留各步骤结构
- `**skill-name** skill` 交叉引用：`skill-name` 保持英文（这是验证器检查的标识符），skill 可译为"技能"
- 翻译"Notes"为"注意事项"
- 保留 `/command-name`、`$ARGUMENTS` 不变

## README.md 文件翻译规则

### 插件 README.md
- 翻译标题下的描述行（必须与对应 `plugin.json` 的 `description` 完全一致）
- 翻译 Skills 和 Commands 列表中的**描述文字**（`--` 后面的部分）
- Skill/command 名称（在反引号中）保持英文
- 保留 Author 和 License 部分的作者名、URL、许可证名称

### 根 README.md
- 翻译所有正文、章节标题、表格内容
- 保留：Badge URL、图片语法和 alt 文本、代码块（所有 CLI 命令）、插件/skill/command 名称、URL 和链接
- `<details>` 展开块：翻译 `<summary>` 中的描述，skill/command 名称保持英文
- 安装说明中的 bash/powershell 代码块完全不动
- "About" 部分：翻译背景文字，保留书目引用格式，书名和作者名不变
- 保持与阶段 1 中 JSON 描述字段的同步

## JSON 文件翻译规则

### marketplace.json
- 翻译 `description` 字段（顶级和每个插件条目）
- 绝对不翻译：`$schema`、`name`、`owner`（所有字段）、`plugins[].name`、`plugins[].source`、`plugins[].category`、`version`
- 插件 `description` 必须与对应 `plugin.json` 的 `description` 完全一致

### plugin.json
- 翻译 `description` 字段
- 绝对不翻译：`name`、`version`、`author`（所有子字段）、`keywords`、`homepage`、`license`
- 描述必须与 `marketplace.json` 中对应条目一致，也必须与 README 描述行一致

## Python 脚本翻译规则

- 翻译模块级 docstring
- 翻译函数/类 docstring
- 翻译章节分隔注释（如 `# --- Configuration ---`）
- 翻译行内注释
- **代码逻辑绝对不变**
- 输出字符串通常保持英文（可能被自动化解析）
- 验证器的错误/警告消息保持英文

## 配置文件翻译规则

### .gitignore
- 翻译注释行

### .gitattributes
- 翻译注释行

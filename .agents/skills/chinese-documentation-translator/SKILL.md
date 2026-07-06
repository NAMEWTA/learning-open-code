---
name: chinese-documentation-translator
description: "将英文技术文档仓库（插件市场、SKILL.md、command.md、README、JSON 清单、Python 验证脚本、纯 Markdown 技能集合等）全面翻译为中文的系统化流程。严格遵循中文文档排版规范（中英空格、全半角标点、术语保留、自然中文表达）。支持状态追踪和增量翻译——源文件更新后仅翻译变更部分。适用于包含 frontmatter 的 markdown 文件、插件清单、命令定义、技能集合。触发词：翻译成中文、中文本地化、translate to Chinese、中文文档、documentation translation、更新翻译、增量翻译。"
---

# 中文技术文档翻译系统化流程（SOP）

## 概述

将英文技术文档仓库全面翻译为中文的端到端流程。基于 `chinese-documentation` 技能的排版规范，覆盖项目级文档、SKILL.md、Command .md、README、JSON 配置、Python 脚本注释等所有文件类型。核心原则：*排版服务于阅读体验，规范服务于一致性，功能完整性不可妥协。*

### 新增：翻译状态追踪

此技能现在包含一个 **JSON 状态文件**（`translation-state.json`），用于：
- 记录每个文件的翻译状态和源文件 hash，支持检测源文件更新
- 支持**增量翻译**——源文件更新时，仅重新翻译变更的文件
- 让用户清楚知道当前翻译版本对应源文件的哪个版本
- 自动计算翻译进度，避免遗漏文件

状态文件格式见：[references/translation-state.schema.json](references/translation-state.schema.json)
示例文件见：[references/translation-state.example.json](references/translation-state.example.json)

## 项目类型自动检测

翻译流程取决于源目录的结构。先探索目录，然后匹配：

| 结构特征 | 项目类型 | 适用流程 |
|---------|---------|---------|
| 存在 `plugin.json` + `marketplace.json` + `validate_plugins.py` | `plugin-marketplace` | 完整 6 阶段 SOP |
| 存在多个 `*/SKILL.md` + `*/README.md`，无 JSON 配置 | `skill-collection` | 阶段 1-4（跳过 JSON/Python 阶段） |
| 单个 `SKILL.md` + 辅助文件 | `single-skill` | 简化流程（阶段 1-2） |
| 通用 Markdown 文档 | `generic-docs` | 阶段 1 + 人工判断 |

### 流程适配规则

- **`plugin-marketplace`**：执行全部 6 个阶段，每阶段后运行 `python3 validate_plugins.py`
- **`skill-collection`**：执行阶段 0→1→2→3→6，跳过 JSON/Python 阶段，用人工抽查替代
- **`single-skill`**：执行阶段 0→2，确认 frontmatter 约束
- **`generic-docs`**：执行阶段 0→1，其余按需

## 翻译总流程（7 个阶段）

### 阶段 0：初始化状态追踪（新增，必做）

**目的**：创建翻译状态文件，捕获源文件版本，为后续增量翻译打基础。

**步骤：**

1. **探索目录结构**——列出所有文件，按类型分类（SKILL.md、README.md、辅助 .md、JSON、Python 等）
2. **检测项目类型**——根据上表匹配流程
3. **采集源版本**：
   ```bash
   git -C <源目录> rev-parse HEAD 2>/dev/null  # 获取 commit hash
   git -C <源目录> rev-parse --abbrev-ref HEAD 2>/dev/null  # 获取分支名
   ```
   如果源是子模块（只读副本），记录 `"_note": "源为子模块只读副本"`，后续再补充。

4. **检查是否有旧状态文件**——如果存在 `<项目名>-translation-state.json`：
   - 读取旧状态，对比新旧文件列表
   - 对于源 hash 已变更的文件，标记为 `needs-update`
   - 对于新增文件，标记为 `pending`
   - 保持已完成文件的 `completed` 状态

5. **创建/更新状态文件**——命名为 `<项目名>-translation-state.json`，放在翻译目标目录下（如 `self/matt-pocock-skills/matt-pocock-skills-translation-state.json`），内容遵循 [references/translation-state.schema.json](references/translation-state.schema.json)。所有文件初始状态为 `pending`（增量模式则按上一步设置）。

6. **确认项目类型和翻译范围**——向用户展示检测结果，确认后开始翻译。

**完成标准**：状态文件存在，`summary.total_files` 准确，`source_version.git_commit` 已填充（或已记录无法获取的原因）。

### 阶段 1：基础文档（低风险，快速验证）

**文件类型：** 根目录级文档（CLAUDE.md、AGENTS.md、CONTRIBUTING.md）、分类目录 README.md、JSON 描述字段、配置文件注释

**规则：**
- 翻译所有正文和章节标题
- 保留代码块、命令引用（`/command-name`）、文件路径、URL 不变
- 保留 YAML frontmatter 的 key 和 `name` value；仅翻译 `description` value
- JSON 文件仅翻译 `description` 字符串；`name`、`version`、`author` 等字段以及所有关键词保持英文
- `marketplace.json` 和 `plugin.json` 中的 `description` 必须与对应 README 保持一致（相同文本）
- `.gitignore`、`.gitattributes` 仅翻译注释部分

**推荐工具**：`multi_replace_string_in_file` 一次处理多个文件，减少往返。

**状态更新**：每翻译完一个文件，立即在状态文件中将该文件标记为 `completed`，记录 `translated_at` 时间戳。

**完成后：**
- `plugin-marketplace` 类型：运行 `python3 validate_plugins.py` 确认全部通过
- 其他类型：人工快速浏览确认无误
- 更新状态文件 `phases[1].status = "completed"`

### 阶段 2：SKILL.md 文件（核心内容，按分类逐个翻译）

**文件类型：** `skills/*/SKILL.md`（每个 skill 一个文件）

**翻译顺序**：按分类从小到大处理，同一分类内按文件长度排序（短文件先翻译，建立节奏）。

**翻译规则详见** [references/translation-rules.md](references/translation-rules.md)

**关键约束：**
- **Frontmatter `name`：绝对不能翻译。** 必须与目录名完全一致。
- **Frontmatter `description`：翻译为中文**，保持简洁，长度控制在原英文长度的 1-1.5 倍内。需包含触发短语以便 AI 自动加载（"适用于用户想要……、提及……的场景"）。
- **代码块、`$ARGUMENTS`、命令引用**：保持英文不变。
- **`**skill-name** skill` 引用**：`skill-name` 保持英文，"skill" 可译为"技能"。
- **内联代码（单反引号）**：保持英文不变。
- **模板块**（`<prd-template>`、`<issue-template>` 等 XML 标签包裹的内容）：翻译描述性文本，保留结构标签。模板标题翻译，占位符说明翻译。
- **对话示例**（`> **Dev:**` 格式）：翻译角色标签和对话内容。
- **技巧提示部分**：适当精简，保留核心要点。参考原文件密度决定详略。

**推荐工具**：`multi_replace_string_in_file` 一次处理 2-5 个短文件或 1-2 个长文件。长文件（>150 行）可以分两次替换（先 frontmatter + 开头，再剩余部分）。

**状态更新**：每完成一个分类，批量更新状态文件中的对应条目。

### 阶段 3：辅助参考文件（按分类批量处理）

**文件类型：** 除 SKILL.md 和 README.md 外的其他 .md 文件（如 `GLOSSARY.md`、`ADR-FORMAT.md`、`LOGIC.md`、`DEEPENING.md`、格式模板、HTML 模板等）

**推荐方式**：使用子代理（`Explore` subagent）并行处理。将辅助文件分成 2-3 批，每批用一个子代理处理。子代理提示词中必须包含完整翻译规则。

**子代理提示词模板**：
```
You are a Chinese documentation translator. Translate these auxiliary .md files from English to Chinese.
RULES:
- Translate all body text, section headings, descriptions
- Keep ALL code blocks, HTML templates, bash commands UNCHANGED
- Keep file paths, URLs, skill names in backticks UNCHANGED
- Add spaces between Chinese and English text
- Use Chinese full-width punctuation; English half-width in code contexts
```

**HTML 模板文件**（如 `HTML-REPORT.md`）：翻译注释和说明文字，HTML 代码和 `<style>`/`<script>` 块完全不动。

**完成标准**：子代理返回成功后，抽查 1-2 个文件确认规则遵守情况。

### 阶段 4：Command .md 文件（如存在）

**文件类型：** `commands/*.md`

**翻译规则：**
- Frontmatter `description` 和 `argument-hint` 均需翻译
- `argument-hint` 中的占位符（如 `<data file or description>`）保持格式，翻译内容
- `**skill-name** skill` 模式：skill 名称保持英文
- `/command-name` 和 `$ARGUMENTS` 保持英文
- 示例代码块保持英文

### 阶段 5：根 README.md（如存在）

**文件类型：** 仓库根目录 README.md（通常是最大的单文件）

**规则：**
- 翻译所有正文、章节标题、表格内容、示例说明
- 保持与阶段 1 中 JSON 描述字段的一致性
- 保留：Badge URL、图片引用、代码块（所有 CLI 命令）、插件/skill/command 名称、URL 和链接、书籍标题和作者名
- `<details>` 展开部分：翻译标题和描述，skill 名称在反引号中保持英文

### 阶段 6：Python 脚本注释 / Shell 脚本注释（如存在）

**Python 脚本规则：**
- 翻译模块 docstring、函数 docstring、章节分隔注释、行内注释
- 代码逻辑绝对不变
- 输出字符串通常保持不变（可能被自动化解析）
- 错误消息保持英文（便于搜索引擎和工具解析）

**Shell 脚本规则：**
- 仅翻译注释行（`#` 开头的行）
- 代码逻辑绝对不变

### 阶段 7：质量保障 + 状态收尾

**自动化验证（`plugin-marketplace` 类型）：**
```bash
python3 validate_plugins.py
```
确认：全部插件 PASS、无 ERROR。

**人工抽查（抽查 10% 文件，最少 3 个）：**
- 中英文之间有空格
- 中文与数字之间有空格
- 中文语境使用全角标点（，。、：；「」？！）
- 英文/代码部分使用半角标点
- 没有被动语态（避免"被"字）
- 没有欧化长句（一逗到底 → 拆成短句）
- 代码块未被修改
- Frontmatter `name` 值未被修改

**术语一致性检查：**
- 对照术语表（见 [references/terminology.md](references/terminology.md)）统一检查
- 前后一致的术语翻译（如 product discovery 统一译为"产品探索"而非混用）

**状态文件收尾：**
- 更新 `updated_at` 为当前时间
- 更新 `summary` 统计数据（遍历 files 数组重新计数）
- 记录 `validation` 结果
- 将所有 `completed` 文件的 `source_hash` 计算并填充（便于后续增量检测）：
  ```bash
  shasum -a 256 <文件路径>
  ```

## 增量翻译工作流

当源文件更新后，无需重新翻译整个项目：

1. **读取旧状态文件**——加载 `<项目名>-translation-state.json`
2. **对比检测**——遍历 `files` 数组，对每个文件：
   ```bash
   # 计算当前源文件 hash
   shasum -a 256 <文件路径>
   ```
   与 `source_hash` 对比。不一致 → 标记为 `needs-update`。
3. **检测新增/删除文件**——对比目录实际文件列表与状态文件中的列表
   - 新增文件 → 追加并标记 `pending`
   - 已删除文件 → 标记为 `skipped`，添加 `translator_notes: "源文件已删除"`
4. **更新源版本**——采集新的 `git_commit`，更新 `source_version`
5. **仅翻译变更文件**——对 `needs-update` 和新增 `pending` 文件执行阶段 1-6 的对应流程
6. **更新状态**——完成后更新 `source_hash`、`translated_at`、`status`

## 核心翻译原则

详见 [references/translation-rules.md](references/translation-rules.md)。快速参考：

1. **空格**：中英之间、中文与数字之间加空格（°C、% 除外）。链接前后加空格。
2. **标点**：中文用全角，英文/代码用半角。
3. **术语**：专有名词保留英文（API、Redis、OKR）；首次出现标注中英对照。不过度翻译。
4. **自然中文**：避"被"字、拆长句、用列表/表格。
5. **代码不动**：命令、代码、`$ARGUMENTS`、URL 保持原样。
6. **Frontmatter**：key 不翻译；`name` value 绝对不改；`description` value 翻译为中文。

## 不翻译清单

- `LICENSE` — 法律文件保留英文
- `$ARGUMENTS` 占位符
- `/command-name` 引用
- `**skill-name**` 交叉引用中的 skill 名
- 书籍标题、URL、作者名
- YAML frontmatter 的 `name` key 和 value
- `plugin.json` 的 `name`、`version`、`author` 字段
- `marketplace.json` 的 `$schema`、`plugins[].name`、`plugins[].source`、`plugins[].category`
- 代码块和 CLI 命令中的所有内容
- Python 代码逻辑和输出字符串
- HTML/CSS/JavaScript 代码（在模板文件中）
- 图片文件（.webp、.png、.gif）

## 执行注意事项

- **分批次执行**：不要一次性修改所有文件。按阶段、按分类逐个进行，便于定位问题。
- **每批后更新状态**：翻译完一个分类的文件后，立即更新状态文件中的对应条目，避免丢失进度。
- **长文件分两次**：超过 150 行的 SKILL.md，先翻译 frontmatter + 前半部分，再翻译后半部分。
- **前后一致**：`marketplace.json` 描述 = `plugin.json` 描述 = README 描述行。每次修改后必须确认三者同步。
- **保持功能性**：插件必须在翻译后仍能正常安装和使用。skills 的触发描述变为中文后，AI 仍应能正确匹配。
- **机翻味自查**：读一遍翻译后的句子，问自己"正常人会这样说中文吗？"如果读起来像翻译，就需要调整。
- **子代理用于辅助文件**：辅助参考文件（格式模板、词汇表等）可以用子代理并行处理，但 SKILL.md 和 README.md 必须由主代理处理以保证质量。
- **状态文件是活的**：每次翻译会话开始和结束时都要更新状态文件。它是增量翻译的基础。

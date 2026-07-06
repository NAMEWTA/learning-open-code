# 超出范围知识库

仓库中的 `.out-of-scope/` 目录存储被拒绝的功能请求的持久记录。它有两个目的：

1. **机构记忆**——为什么某个功能被拒绝，以便在 issue 关闭后推理不会丢失
2. **去重**——当新的 issue 与之前的拒绝匹配时，skill 可以呈现之前的决策，而不是重新争论

## 目录结构

```
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

每个**概念**一个文件，而非每个 issue 一个文件。请求同一事物的多个 issues 归入一个文件下。

## 文件格式

文件应以轻松、可读的风格编写——更像一份简短的设计文档，而非数据库条目。使用段落、代码示例和示例使推理清晰，对第一次遇到它的人有用。

```markdown
# Dark Mode

This project does not support dark mode or user-facing theming.

## Why this is out of scope

The rendering pipeline assumes a single color palette defined in
`ThemeConfig`. Supporting multiple themes would require:

- A theme context provider wrapping the entire component tree
- Per-component theme-aware style resolution
- A persistence layer for user theme preferences

This is a significant architectural change that doesn't align with the
project's focus on content authoring. Theming is a concern for downstream
consumers who embed or redistribute the output.

```ts
// The current ThemeConfig interface is not designed for runtime switching:
interface ThemeConfig {
  colors: ColorPalette; // single palette, resolved at build time
  fonts: FontStack;
}
```

## Prior requests

- #42 — "Add dark mode support"
- #87 — "Night theme for accessibility"
- #134 — "Dark theme option"
```

### 命名文件

为概念使用简短、描述性的 kebab-case 名称：`dark-mode.md`、`plugin-system.md`、`graphql-api.md`。名称应足够可识别，使浏览目录的人无需打开文件就能理解被拒绝的内容。

### 编写原因

原因应有实质内容——不是"我们不想要这个"，而是为什么。好的原因引用：

- 项目范围或理念（"本项目专注于 X；主题化是下游关注点"）
- 技术约束（"支持此功能需要 Y，这与我们的 Z 架构冲突"）
- 战略决策（"我们选择使用 A 而非 B，因为……"）

原因应具有持久性。避免引用临时情况（"我们现在太忙了"）——那些不是真正的拒绝，而是推迟。

## 何时检查 `.out-of-scope/`

在分类期间（步骤 1：收集上下文），读取 `.out-of-scope/` 中的所有文件。评估新 issue 时：

- 检查请求是否与现有的超出范围概念匹配
- 匹配基于概念相似性，而非关键词——"night theme" 匹配 `dark-mode.md`
- 如果匹配，向维护者呈现："这与 `.out-of-scope/dark-mode.md` 类似——我们之前因为这个原因拒绝了：[原因]。你仍然持相同看法吗？"

维护者可以：

- **确认**——新 issue 被添加到现有文件的"Prior requests"列表中，然后关闭
- **重新考虑**——超出范围文件被删除或更新，issue 进入正常分类流程
- **不同意**——issues 相关但不同，继续正常分类

## 何时写入 `.out-of-scope/`

仅当一个**增强请求**（而非 bug）被*拒绝*为 `wontfix` 时。这适用于增强 PR，与 issues 完全相同——被拒绝的 PR 记录在此，以便相同的请求不会以新代码的形式再次出现。

**不要**在因**已经实现**而关闭为 `wontfix` 时写入此处。那是已构建的功能，而非被拒绝的功能；记录它会用错误的拒绝毒化去重检查。相反，关闭评论应指向该功能已存在的位置。

流程：

1. 维护者决定某个功能请求超出范围
2. 检查是否已存在匹配的 `.out-of-scope/` 文件
3. 如果存在：将新 issue 追加到"Prior requests"列表
4. 如果不存在：创建新文件，包含概念名称、决定、原因和第一个先前请求
5. 在 issue 上发布评论，解释决定并提及 `.out-of-scope/` 文件
6. 使用 `wontfix` 标签关闭 issue

## 更新或删除超出范围文件

如果维护者改变了对之前被拒绝的概念的看法：

- 删除 `.out-of-scope/` 文件
- Skill 不需要重新打开旧 issues——它们是历史记录
- 触发重新考虑的新 issue 进入正常分类流程

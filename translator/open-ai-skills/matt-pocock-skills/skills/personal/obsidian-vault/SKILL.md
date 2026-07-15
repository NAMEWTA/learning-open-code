---
name: obsidian-vault
description: "使用 wikilinks 和索引笔记在 Obsidian 仓库中搜索、创建和管理笔记。当用户想要在 Obsidian 中查找、创建或组织笔记时使用。"
---

# Obsidian Vault

## 仓库位置

`/mnt/d/Obsidian Vault/AI Research/`

在根级别基本扁平化。

## 命名约定

- **索引笔记**：聚合相关主题（例如 `Ralph Wiggum Index.md`、`Skills Index.md`、`RAG Index.md`）
- 所有笔记名称使用**标题大小写**
- 不使用文件夹组织——改用链接和索引笔记

## 链接

- 使用 Obsidian `[[wikilinks]]` 语法：`[[笔记标题]]`
- 笔记在底部链接到依赖项/相关笔记
- 索引笔记只是 `[[wikilinks]]` 的列表

## 工作流程

### 搜索笔记

```bash
# 按文件名搜索
find "/mnt/d/Obsidian Vault/AI Research/" -name "*.md" | grep -i "keyword"

# 按内容搜索
grep -rl "keyword" "/mnt/d/Obsidian Vault/AI Research/" --include="*.md"
```

或直接在仓库路径上使用 Grep/Glob 工具。

### 创建新笔记

1. 文件名使用**标题大小写**
2. 将内容写为一个学习单元（遵循仓库规则）
3. 在底部添加指向相关笔记的 `[[wikilinks]]`
4. 如果是编号序列的一部分，使用层级编号方案

### 查找相关笔记

在整个仓库中搜索 `[[笔记标题]]` 来查找反向链接：

```bash
grep -rl "\\[\\[笔记标题\\]\\]" "/mnt/d/Obsidian Vault/AI Research/"
```

### 查找索引笔记

```bash
find "/mnt/d/Obsidian Vault/AI Research/" -name "*Index*"
```

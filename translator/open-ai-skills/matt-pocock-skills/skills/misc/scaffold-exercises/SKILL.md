---
name: scaffold-exercises
description: "创建包含章节、问题、解答和讲解的练习目录结构，并通过 lint 检查。当用户想要搭建练习脚手架、创建练习桩代码、或设置新的课程章节时使用。"
---

# 搭建练习脚手架

创建能通过 `pnpm ai-hero-cli internal lint` 的练习目录结构，然后用 `git commit` 提交。

## 目录命名

- **章节**：`XX-section-name/` 放在 `exercises/` 内部（例如 `01-retrieval-skill-building`）
- **练习**：`XX.YY-exercise-name/` 放在章节内部（例如 `01.03-retrieval-with-bm25`）
- 章节编号 = `XX`，练习编号 = `XX.YY`
- 命名使用 dash-case（小写，连字符）

## 练习变体

每个练习至少需要以下子文件夹之一：

- `problem/` - 学生工作区，含 TODO
- `solution/` - 参考实现
- `explainer/` - 概念性材料，无 TODO

当搭建桩代码时，默认使用 `explainer/`，除非计划另有说明。

## 必需文件

每个子文件夹（`problem/`、`solution/`、`explainer/`）需要一个 `readme.md`，要求：

- **不为空**（必须有真实内容，哪怕只有一行标题也行）
- 没有断链

当搭建桩代码时，创建一个带有标题和描述的最小 readme：

```md
# 练习标题

此处写描述
```

如果子文件夹有代码，还需要一个 `main.ts`（>1 行）。但对于桩代码，仅 readme 的练习也可以。

## 工作流程

1. **解析计划** - 提取章节名称、练习名称和变体类型
2. **创建目录** - 对每个路径执行 `mkdir -p`
3. **创建桩 readme** - 每个变体文件夹一个 `readme.md`，带标题
4. **运行 lint** - `pnpm ai-hero-cli internal lint` 进行验证
5. **修复任何错误** - 迭代直到 lint 通过

## Lint 规则摘要

Linter（`pnpm ai-hero-cli internal lint`）检查：

- 每个练习有子文件夹（`problem/`、`solution/`、`explainer/`）
- 至少存在 `problem/`、`explainer/` 或 `explainer.1/` 中的一个
- 主子文件夹中存在 `readme.md` 且不为空
- 没有 `.gitkeep` 文件
- 没有 `speaker-notes.md` 文件
- readme 中没有断链
- readme 中没有 `pnpm run exercise` 命令
- 每个子文件夹需要 `main.ts`，除非是仅 readme 的

## 移动/重命名练习

当重新编号或移动练习时：

1. 使用 `git mv`（而非 `mv`）重命名目录——保留 git 历史
2. 更新数字前缀以保持顺序
3. 移动后重新运行 lint

示例：

```bash
git mv exercises/01-retrieval/01.03-embeddings exercises/01-retrieval/01.04-embeddings
```

## 示例：根据计划搭建桩代码

给定如下计划：

```
Section 05: Memory Skill Building
- 05.01 Introduction to Memory
- 05.02 Short-term Memory (explainer + problem + solution)
- 05.03 Long-term Memory
```

创建：

```bash
mkdir -p exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer
mkdir -p exercises/05-memory-skill-building/05.02-short-term-memory/{explainer,problem,solution}
mkdir -p exercises/05-memory-skill-building/05.03-long-term-memory/explainer
```

然后创建 readme 桩代码：

```
exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer/readme.md -> "# Introduction to Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/explainer/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/problem/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/solution/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.03-long-term-memory/explainer/readme.md -> "# Long-term Memory"
```

# 标准任务单与全局上下文包

> 本文件是 **GCP 模板与字段填充规则的唯一来源**。goal-loop.md、teach-review.md 均引用此处，不另行维护副本。

## 目录

- [全局上下文包（GCP）模板](#全局上下文包gcp模板)
- [标准任务单模板](#标准任务单模板)
- [Subagent 执行流程](#subagent-执行流程)
- [不同层级的任务单差异](#不同层级的任务单差异)

每次从 Goal 队列取出一个目标后，主 Agent 按以下两步组装 subagent prompt：

1. **先生成全局上下文包（GCP）**——提供项目全局信息、进度状态、已生成内容的目录快照
2. **再填充标准任务单**——描述当前 goal 的具体要求

二者拼接后作为 subagent 的完整 prompt 派发。**一个 subagent prompt = GCP + 任务单，一个 subagent 只处理一个 goal。**

## 全局上下文包（GCP）模板

**每次派发 subagent 必须前置此模板。** GCP 让 subagent 在无前置记忆的情况下也能了解项目全局、自主探查已生成内容。

```
═══════════════════════════════════════
全局上下文包 (GCP) — 由 teach-goal 编排器自动生成
═══════════════════════════════════════

【项目标识】
PROJECT_NAME: {项目名称}
PROJECT_ROOT: {目标仓库绝对路径}

【teach/<project>/ 当前目录树】
{list_dir teach/<project>/ 的完整输出}
↑ 你可以使用 list_dir、read_file 等工具自主探查以上目录中的任何文件

【整体进度】
已完成: {done_count} / {total_count} goals（{percentage}%）
最近完成的 5 个 goal:
  1. {goal_id} — {title} → {output_path}
  2. ...
  3. ...
  4. ...
  5. ...

【当前 Goal 的依赖状态】
{depends_on 中每个依赖 goal 的完成状态}:
  - {dep_goal_id}: ✅ done → {dep_output_path}（可交叉引用）
  - {dep_goal_id}: ⏳ pending（尚未完成，但当前 goal 不依赖其结果）

【锚点参考】
L0 项目总览: teach/<project>/00-overview/reference/00-overview.html

【关联文档路径】
{以下路径如不存在则标注"尚未生成"}
父模块总览 (L1): {parent_output_path}
同级垂直切片 (L2): {sibling_slice_paths}
同级 API 参考 (L3): {sibling_api_paths}
关联深度剖析 (L4): {related_deepdive_paths}

═══════════════════════════════════════
以下是本次任务单 — 你的唯一执行目标
═══════════════════════════════════════
```

### GCP 字段填充规则

| 字段 | 填充规则 |
|------|---------|
| PROJECT_NAME | 从用户输入或仓库名推断 |
| PROJECT_ROOT | 目标仓库的绝对路径 |
| 目录树 | 使用 `list_dir` 工具获取 `teach/<project>/` 的完整输出，**不要裁剪**。subagent 据此可自主探查 |
| 整体进度 | 从 `_progress.json` 统计 status=done 的数量 |
| 最近完成 | 从 `_progress.json` 按 `completed_at` 倒序取前 5 个 status=done 的 goal |
| 依赖状态 | 遍历当前 goal 的 `depends_on`，查 `_progress.json` 中各依赖 goal 的 status 和 output_path |
| 锚点参考 | 固定路径，L0 总览始终在此位置 |
| 关联文档 | 从 `_progress.json` 筛选同 `parent` 的其他 goal 的 output_path，按 level 分类列出。尚未生成的标注"尚未生成" |

## 标准任务单模板

```
【教学生成任务单】
goal_id: {id}
层级: L0 / L1 / L2(垂直切片) / L3 / L4
标题: {title}
所属模块: {parent}
前置知识回顾: {对已完成的依赖 goal 的 2-3 句话概括，避免重复讲解。引用上方 GCP 中依赖状态所列的文档路径}
涉及源码:
  - {文件路径}:{起始行}-{结束行}   # 一句话说明这段代码的作用
  - ...
是否为垂直切片: {是/否}；若是，列出涉及的层级顺序（如：路由 → 中间件 → Service → DAO → 数据库）
目标读者水平: {TARGET_AUDIENCE}
输出语言: {OUTPUT_LANGUAGE}
输出路径: {output_path}
---
请严格依据 teach SKILL 的教学规范（章节结构、深度要求、HTML 课程格式、参考文档格式等），
基于以上信息生成完整教学内容，不要自行简化或另起一套格式。

完成后请回报：
1. 产出文件路径
2. 产出摘要（2-3 句话）
3. 新发现的、尚未覆盖的模块/函数/依赖（如有）
```

## 字段说明

| 字段 | 说明 | 示例 |
|------|------|------|
| `goal_id` | Goal 唯一标识 | `L2-auth-login-flow` |
| `层级` | L0 / L1 / L2(垂直切片) / L3 / L4 | `L2(垂直切片)` |
| `标题` | 中文简短标题 | `用户登录鉴权全链路` |
| `所属模块` | 父 goal 的 id，L0 填 `-` | `L1-auth-module` |
| `前置知识回顾` | 2-3 句概括已完成的依赖 goal 讲了什么 | `L1-auth-module 已讲解认证模块的三层架构(Controller→Service→DAO)及 JWT 配置` |
| `涉及源码` | 每行一个文件路径 + 行号范围 + 一句话说明 | `src/middleware/authGuard.ts:30-58 # JWT 验证与刷新逻辑` |
| `是否为垂直切片` | 是/否 | `是；层级顺序：路由 → 中间件 → Service → DAO → 数据库` |
| `目标读者水平` | 学习者背景描述 | `具备一定编程基础、希望从0到1精通该项目架构与实现细节的开发者` |
| `输出语言` | 教学文档输出语言 | `中文` |
| `输出路径` | 产出文件在工作区中的相对路径 | `teach/open-java/RuoYiVuePlus/slice-auth-login-flow/lessons/auth-login-flow.html` |

## Subagent 执行流程

> **重要：本节描述的是 subagent 拿到 GCP + 任务单后的执行流程。主 Agent 不直接执行这些步骤。**

teach-goal 负责"喂料"（决定讲什么、给什么代码上下文、按什么顺序讲），教学内容的**具体写法完全交给 teach SKILL 决定**。这个决策由 subagent 执行。

subagent 拿到 GCP + 任务单后，执行以下步骤：

1. **理解上下文**：阅读 GCP 了解项目全局、已有产出、依赖关系；阅读任务单了解当前 goal 的具体要求
2. **读取源码**：根据任务单中的 `涉及源码` 列表读取相关源文件，必要时使用 `list_dir`、`grep_search` 等工具自主探查更多上下文
3. **调用 teach SKILL**：将任务单内容和源码上下文传递给 teach SKILL，明确告知本次为批量生成模式、MISSION.md 使用自动生成的默认使命（不交互等待用户输入）
4. **写入产出**：teach SKILL 按自己的规范生成 HTML 课程或参考文档，subagent 将其写入指定的 `output_path`
5. **回报结果**：返回以下信息给主 Agent：
   - 是否成功生成产出文件（含完整路径）
   - 产出文件的摘要（2-3 句话）
   - 本次分析中新发现的、尚未覆盖的模块/函数/依赖（供主 Agent 生成新 goal）

> **重要：** teach subagent **不负责自我审查**。产出文件的质量审查由独立的 `teach-review` subagent 执行（见 [agent/teach-review.md](../agent/teach-review.md)）。主 Agent 在收到回报后会立即派发 teach-review。如果审查发现 Critical 问题，主 Agent 会将修复任务反馈给本 subagent。

### Subagent 回报格式

```
【Subagent 回报】
goal_id: {id}
status: success / failed
output_path: {产出文件完整路径}
summary: {2-3 句话摘要}
new_discoveries:
  - {新发现的模块/函数/依赖的简短描述}
  - ...
errors: {如失败，简述原因}
```

> **回报后的流程：** 主 Agent 收到此回报后 → 派发 teach-review subagent 审查产出 → 根据审查结论决定 goal 状态。如有 Critical 问题，可能要求本 subagent 修复后重新提交（最多 2 轮修复-审查循环）。

## 不同层级的任务单差异

### L0 项目总览

输出到独立 teach 主题 `teach/<project>/00-overview/`。产出文件：`reference/00-overview.html`，内容为全项目宏观视角的参考文档。

### L1 模块总览

输出到独立 teach 主题 `teach/<project>/module-<slug>/`。产出文件：`reference/<slug>-overview.html`，重点讲模块职责、接口、分层，不需要深入到每个函数。

### L2 垂直切片

输出到独立 teach 主题 `teach/<project>/slice-<slug>/`。产出文件：`lessons/<slug>.html`，按课程格式生成，包含完整调用链路 + 至少一条异常路径。

### L3 微观 API

输出到其父 L1 模块的 teach 主题 `teach/<project>/module-<slug>/`（与 L1 同目录）。产出文件：`reference/<slug>-api.html`。注意：L3 不创建新的 teach 主题目录，而是复用 L1 已创建的 `module-<slug>/` 目录。

### L4 深度剖析

输出到独立 teach 主题 `teach/<project>/deep-dive-<slug>/`。产出文件：`lessons/<slug>.html`，按课程格式生成，重点讲设计决策、算法拆解、性能权衡。

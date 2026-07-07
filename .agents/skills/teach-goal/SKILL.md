---
name: teach-goal
description: 对开源项目进行穷尽式教学文档生成——从宏观架构到微观实现的五层分级讲解，使用 Goal Loop 算法自主驱动完整代码覆盖。调用 teach 原子 SKILL 生成 HTML 课程与参考文档。触发条件：用户要求"完整学习某个项目"、"生成项目架构文档"、"从入口到落地讲清楚每个功能"、"代码考古"、"源码分析"、或指定一个项目目录/仓库要求全面教学。
---

# 角色与使命

你是一名资深代码考古 / 技术教学工程师。你的任务是：对目标开源项目进行**穷尽式**教学文档生成——从项目整体架构（宏观）一路下钻到每个函数/边界条件的实现细节（微观），用**垂直切片**方式把"一个功能从入口到落地"的完整链路讲清楚。整个过程由 **Goal Loop** 算法**完全自主**驱动，不等待用户逐步确认，循环直到覆盖率校验全部通过。

## 与 teach SKILL 的职责边界

| | teach-goal（本 SKILL） | teach（原子 SKILL） |
|---|---|---|
| **角色** | 规划层——决定讲什么、按什么顺序讲、喂什么代码上下文 | 执行层——决定怎么写、什么格式、怎么排版 |
| **产出** | Goal 清单、进度台账、00-index.md 总导航 | HTML 课程（lessons/）、HTML 参考文档（reference/） |
| **驱动方式** | Goal Loop 自主循环 | 按任务单逐次调用 |

**重要**：本 SKILL 不重新定义教学文风/格式——这些由 teach SKILL 的规范决定。本 SKILL 只负责"喂料"与进度管理。

## Agent Team 硬约束

本 SKILL 依赖 Agent Team 并行加速。主 Agent（teach-goal）是编排器，subagent 是执行器。三条不可违背的约束：

1. **一个 subagent 只处理一个 goal**，绝不合并多个 goal 到一个 subagent。
2. **主 Agent 不直接调用 teach SKILL、不直接读源码写文档**——只负责组装任务单、创建主题目录、派发、收集结果、更新台账。
3. **每次派发 subagent 必须前置全局上下文包（GCP）**，模板见 [references/task-order.md](references/task-order.md)。

调度模型（角色分工、并行/串行判断、异常重试、审查状态机）全部定义在 [references/goal-loop.md](references/goal-loop.md)。

## 核心工作流

### 1. 确认目标与初始化

- 从用户输入获取目标仓库路径和项目名称；未明确指定时从工作区上下文推断，仅在无法推断时询问。
- 按 teach SKILL 的子模块分组规则确定 `<project>`，创建项目级目录 `teach/<project>/`。
- 用 teach SKILL 的 `scripts/init_topic.sh <project> 00-overview` 创建 L0 主题工作区。后续每个新主题目录同样由**主 Agent 在派发前**用此脚本创建。

### 2. 生成 L0 总览

扫描仓库结构（顶层目录、README、关键配置文件、技术栈），派发 subagent 生成 L0 项目总览到 `teach/<project>/00-overview/reference/00-overview.html`。L0 是所有后续 goal 的锚点，必须最先完成并通过审查。内容标准见 [references/five-levels.md](references/five-levels.md)。

### 3. 构建 Goal Backlog

从 L0 产出中提取：

- 每个顶层目录/子系统 → L1 goal（主题目录 `module-<slug>`）
- README/路由表/CLI/UI 入口中识别的核心功能 → L2 goal（主题目录 `slice-<slug>`）

写入 `_progress.json`，向用户展示初始清单作为**进度通报**（不等待确认，立即进入循环）。

### 4. 运行 Goal Loop

**这是本 SKILL 的核心引擎**，完整算法与数据结构见 [references/goal-loop.md](references/goal-loop.md)。概要：

1. 按优先级（L0 → L1 → L2 → L3 → L4，同层广度优先）取出依赖已满足的 goal，每批最多 4 个 subagent 并行
2. 为每个 goal 组装 GCP + 标准任务单（格式见 [references/task-order.md](references/task-order.md)），派发 subagent
3. 收集回报 → 按采样策略派发 teach-review 审查（审查员定义见 [agent/teach-review.md](agent/teach-review.md)）→ 依审查结论更新 goal 状态
4. 从回报中提取新发现的模块/函数/依赖，生成新 goal 入队
5. 更新进度台账，输出本轮简报
6. 循环直到 goal_queue 清空且覆盖率校验通过

### 5. 覆盖率校验

每轮循环结束前执行自检；goal_queue 清空后执行终检，对"全部源码文件 vs 已讲解文件"做差集扫描，缺口生成补充 goal 继续循环。清单见 [references/coverage-checklist.md](references/coverage-checklist.md)。

### 6. 收尾

Definition of Done 全部达成后执行：

1. 为每个主题目录运行 teach SKILL 的 `scripts/generate_snapshot.py <project-path> --all`，生成/更新 SNAPSHOT.md
2. 补全 `teach/<project>/index.md` 中所有主题的名称与描述（init_topic.sh 只写占位符）
3. 生成 `00-index.md` Wiki 总导航（格式见 [references/output-structure.md](references/output-structure.md)）
4. 输出完成报告（模板见 [references/coverage-checklist.md](references/coverage-checklist.md)），blocked goal 单独列出

## 输出结构

**每个 L0 / L1(含L3) / L2 / L4 各自为一个独立的 teach 主题目录**，严格遵循 teach SKILL 的工作区规范。进度台账和总导航放在项目级目录下。

```
teach/<project>/
├── index.md                      # teach SKILL 项目索引
├── _progress.json                # 机器可读进度台账
├── _progress.md                  # 人类可读进度看板
├── 00-index.md                   # Wiki 总导航
├── 00-overview/                  # L0 — 项目总览
├── module-<slug>/                # L1 + L3 — 模块（总览 + 微观 API）
├── slice-<slug>/                 # L2 — 垂直切片
└── deep-dive-<slug>/             # L4 — 深度剖析
```

**目录前缀规则（强制）**：`00-` = L0、`module-` = L1+L3、`slice-` = L2、`deep-dive-` = L4。

| 层级 | teach 主题目录 | 产出文件 |
|------|---------------|---------|
| L0 项目总览 | `00-overview/` | `reference/00-overview.html` |
| L1 模块总览 | `module-<slug>/` | `reference/<slug>-overview.html` |
| L2 垂直切片 | `slice-<slug>/` | `lessons/<slug>.html` |
| L3 微观 API | `module-<slug>/`（与 L1 同目录） | `reference/<slug>-api.html` |
| L4 深度剖析 | `deep-dive-<slug>/` | `lessons/<slug>.html` |

完整说明见 [references/output-structure.md](references/output-structure.md)。

## 参考指南

以下文件包含详细方法论，按需读取：

| 文件 | 内容 | 何时读取 |
|------|------|---------|
| [goal-loop.md](references/goal-loop.md) | Goal Loop 算法、调度模型、goal 状态机、异常处理 | 运行循环、管理进度台账时 |
| [task-order.md](references/task-order.md) | GCP 模板（唯一来源）+ 标准任务单 + subagent 执行流程 | 每次派发 subagent 前 |
| [five-levels.md](references/five-levels.md) | L0-L4 五层体系与各层产出标准 | 确定某层 goal 的产出标准时 |
| [vertical-slice.md](references/vertical-slice.md) | 垂直切片设计指南 | 选取和设计 L2 goal 时 |
| [output-structure.md](references/output-structure.md) | 输出目录结构、00-index.md 格式 | 创建工作区目录、生成总导航时 |
| [coverage-checklist.md](references/coverage-checklist.md) | 每轮自检 + DoD 终检 + 完成报告模板 | 每轮循环结束和最终验收时 |
| [agent/teach-review.md](agent/teach-review.md) | 审查员 subagent 提示模板与审查策略 | 每次派发审查时 |

## 执行原则

- **完全自主**：批次之间自动无缝衔接，不等待用户确认；仅在源码无法访问或需人工决策（如 blocked goal 处置）时中止。MISSION.md 使用自动生成的默认使命（如"深度理解 {PROJECT_NAME} 的完整架构与实现细节"），不阻塞循环
- **不可跳过**：不允许因代码"太琐碎"而完全跳过，只允许降低详略程度
- **进度可见**：每轮完成后输出简报——完成了什么、新发现了什么、当前总体进度百分比
- **测试佐证**：引用测试用例作为功能预期行为与边界情况的佐证
- **质量闸门**：审查不通过的 goal 不得标记为 done；Critical 问题必须修复（最多 2 轮修复-审查循环，仍失败则 blocked 留待人工）

# Mission: 读懂 RuoYi-Vue-Plus 工作流模块（ruoyi-workflow + Warm-Flow）

## Why
学习者要能在脑中完整重建 RuoYi-Vue-Plus 这套系统「一张审批单从发起到办结」的全链路：后端 `ruoyi-workflow` 模块如何封装国产工作流引擎 **Warm-Flow 1.8.8**，如何用**事件驱动**把流程引擎与业务模块（如请假 TestLeave）解耦，前端两套 UI（Vue/React）如何对接发起、待办、审批、流程设计器。达到能给同事讲清楚、能照着 TestLeave 把自己的业务接入工作流、能看懂面试题的程度。重点是**读懂设计与调用链**，不是改引擎源码。

## Success looks like
- 能用一张图 + 一段话讲清「请假申请」从前端提交到后端发起流程、生成任务、审批办结、回写业务状态的完整链路，并说出每一环的关键类/文件。
- 能解释 `ruoyi-workflow` 如何集成 Warm-Flow：`warm-flow.enabled` 开关 + `@ConditionalOnEnable`、引擎注入的 `TaskService/InsService/DefService` 等核心服务、flow_definition/flow_instance/flow_task/flow_his_task 四张引擎表各自的角色。
- 能讲清 `startWorkFlow` 发起流程的全过程：businessId 去重、流程变量装配（initiator/businessId/autoPass）、`insService.start()`、首任务生成，以及 `WorkflowService` API 如何让任意业务模块一行代码发起流程。
- 能讲清 `completeTask` 办理任务的核心：`FlowParams` 的装配、`taskService.skip()`、`SkipType`(PASS/REJECT) 与 `BusinessStatusEnum`/`TaskStatusEnum` 两套状态的关系，以及驳回 `backProcess`、终止、作废的差异。
- 能说清四种运行时任务操作（委派/转办/加签/减签）走 `taskOperation` 的统一分发，以及办理人是怎么按 用户/角色/部门/岗位/SpEL 五种 `TaskAssigneeEnum` 通过 storageId 前缀解析的。
- 能讲清**事件驱动解耦**的设计：`WorkflowGlobalListener`（引擎全局监听器）→ `FlowProcessEventHandler` 发 Spring 事件 → 业务模块用 `@EventListener` 接收（TestLeave 回写状态），以及节点扩展（按钮权限/抄送/SpEL 动态办理人）如何挂在节点上。
- 能讲清前端（Vue 的 Element Plus + Pinia，React 的 Ant Design）如何封装 workflow API、渲染待办列表、用 `submitVerify` 审批组件收集意见/抄送/下一步办理人调 `completeTask`、用 iframe 嵌入 Warm-Flow 流程设计器，并能对比两套实现的异同。

## Constraints
- 学习者是全栈背景，后端 Java + 前端 Vue/React 都要覆盖，以后端引擎集成与调用链为主、前端对接为辅。
- 目标是「读懂 + 能照着接入」而非「改引擎」——课程以追踪真实代码调用链、解释设计动机为主，练习以「读代码答问题 / 复述链路 / 对比设计」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与类名/行号。
- 交互语言：简体中文。

## Out of scope
- Warm-Flow 引擎内部源码实现（如 `taskService.skip()` 内部的节点流转算法）——仅讲它对外的契约与本模块如何调用。
- 流程设计器（warm-flow-ui 前端插件）的内部实现——仅讲本项目如何 iframe 嵌入与传参。
- 多租户、数据权限在工作流上的完整实现细节——仅在交叉处点到为止。
- 会签/票签/网关分支的引擎级数学语义细节——讲到节点类型与 nodeRatio 即可。

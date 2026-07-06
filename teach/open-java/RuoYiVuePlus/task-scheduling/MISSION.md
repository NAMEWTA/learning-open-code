# Mission: 全面读懂 RuoYi-Vue-Plus 的 ruoyi-job 任务调度模块

## Why
学习者要能完整理解 `ruoyi-job` 模块如何使用 **SnailJob** 框架实现分布式任务调度，掌握 6 种任务模式的原理与适用场景（注解任务 / 类任务 / 广播任务 / 静态分片 / Map / MapReduce + DAG 工作流），并能在自己的业务中根据场景正确选择任务类型。重点在「读懂每种模式的设计动机与数据流」，不要求从零搭建 SnailJob 服务端。讲解全部基于本仓库真实代码（已逐文件核对）。

## Success looks like
- 能说清 ruoyi-job 模块的整体定位、与 `ruoyi-common-job` 的分工、Maven 依赖结构，以及 SnailJob 在 `application-dev.yml` 中的配置项含义。
- 能解释 `SnailJobConfig` 自动装配原理：`@EnableSnailJob` + `@EnableScheduling` + `SnailLogbackAppender` 远程日志挂载，以及 `snail-job.enabled` 开关的作用。
- 能区分 3 种基础任务执行方式：`@JobExecutor` 注解式（`TestAnnoJobExecutor`）、`extends AbstractJobExecutor` 继承式（`TestClassJobExecutor`）、以及广播任务（`TestBroadcastJob`），并说出每种方式的注册机制与适用场景。
- 能讲清静态分片（`TestStaticShardingJob`）的原理：服务端通过 `jobArgs.getJobParams()` 下发分片参数，执行器按参数范围处理数据。
- 能讲清 Map 任务（`TestMapJobAnnotation`）的完整链路：根 Map 拆分数据 → `MapHandler.doMap()` 动态分配 → 子 Map 并行执行，以及「只分片不汇总」的语义。
- 能讲清 MapReduce 任务（`TestMapReduceAnnotation1`）在 Map 基础上增加了 `@ReduceExecutor` 汇总阶段，以及 reduce 如何收集所有 map 结果做最终聚合。
- 能讲清 DAG 工作流的原理：通过 `JobArgs.wfContext`（工作流上下文）在 `WechatBillTask` → `AlipayBillTask` → `SummaryBillTask` 三个节点间传递 `BillDTO` 数据，以及 `appendContext` / `getWfContext` 的用法。
- 能说清 `SnailJobLog.LOCAL` vs `SnailJobLog.REMOTE` 的区别，以及 `SnailLogbackAppender` 如何将日志上报到 SnailJob 服务端。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解以追踪真实代码 + 解释设计动机为主。
- 目标是「读懂并能正确选用任务模式」而非「能运维 SnailJob 服务端」——练习以「读代码答问题 / 选型判断 / 复述链路」为主。
- SnailJob 服务端（管理后台）的部署与运维不在本课程范围——仅在理解客户端配置时交叉引用。
- 全部讲解基于仓库真实代码，引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- SnailJob 服务端（`snail-job-server`）的部署、数据库初始化、集群运维。
- SnailJob 管理后台的使用操作（创建任务、配置触发规则、查看日志等 UI 操作）。
- 其他模块中如何使用 ruoyi-job 的任务（本模块主要是 demo 示例）。
- Spring Task（`@Scheduled`）的原生定时任务机制——仅在 `@EnableScheduling` 处交叉提到。
- SnailJob 的重试模块（snail-job-client-retry）——本模块只涉及 job 调度。

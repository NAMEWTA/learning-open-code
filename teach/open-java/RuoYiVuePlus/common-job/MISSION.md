# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-job 定时任务模块

## Why
学习者要能彻底读懂 `ruoyi-common-job` 这个公共模块：它本身只有一个 Java 类，是对开源分布式任务调度框架 **SnailJob** 的一层「客户端接入适配」。理解它，等于理解 RuoYi-Vue-Plus 如何把一个第三方分布式调度框架「收编」进自己的技术栈——用 Spring Boot 自动配置实现「依赖即生效」，用 `@ConditionalOnProperty` 实现开关控制，用事件监听机制挂载远程日志 Appender。达到能给同事讲清「这个模块为什么只有一个类却能支撑所有分布式定时任务」「SnailJob 客户端是怎么和 Server 服务端协同工作的」「从编写一个任务到服务端调度执行，链路怎么走通」，并能在此基础上自己编写新的定时任务、排查调度失败问题的程度。重点是**读懂设计动机与真实调用链**，不是从零学习 SnailJob 全部功能。

## Success looks like
- 能用一句话说清 `ruoyi-common-job` 与 SnailJob 的关系，并说出模块仅有的一个类 `SnailJobConfig` 承担什么职责。
- 能解释 `SnailJobConfig` 上四个注解各自的作用：`@AutoConfiguration`（自动装载）、`@ConditionalOnProperty`（开关控制）、`@EnableScheduling`（启用 Spring 调度）、`@EnableSnailJob`（启用 SnailJob 客户端）。
- 能讲清 `onStarting` 方法如何通过监听 `SnailClientStartingEvent` 事件，在 SnailJob 客户端启动时将 `SnailLogbackAppender` 挂载到 Logback 根 Logger 上，实现任务日志回传服务端。
- 能解释 `snail-job` 配置段各字段的含义：`enabled`、`group`、`token`、`server.host/port`、`namespace`、`port`（客户端端口漂移机制），以及它们如何决定客户端能否成功接入调度服务端。
- 能完整追踪「编写任务 → 服务端创建任务 → 调度触发 → 任务执行 → 日志回传」这条真实链路：`@JobExecutor` 标记任务类 → SnailJob 服务端控制台创建任务 → 客户端接收调度指令 → 执行 `jobExecute()` → `SnailJobLog.REMOTE` 回传日志到服务端。
- 能对照示例代码（`TestAnnoJobExecutor`、`TestBroadcastJob`、`TestStaticShardingJob`、`TestMapJobAnnotation`、`TestMapReduceAnnotation1`、`AlipayBillTask` 等）讲清 SnailJob 支持的任务类型：普通任务、广播任务、静态分片、Map 任务、MapReduce 任务、DAG 工作流任务。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会联系 SnailJob 服务端管理控制台（Web UI）说明任务创建与管理的操作流程。
- 目标是「读懂」而非「能改造框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路」为主。
- 全部讲解基于仓库真实代码与 SnailJob 客户端 starter 源码，引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- SnailJob 服务端（`ruoyi-snailjob-server`）的内部实现细节——只讲客户端如何连接，不讲服务端如何存储任务、分发调度。
- `ruoyi-job` 业务模块中所有示例任务的具体业务逻辑（如支付宝账单、微信账单的对账算法）——只讲任务结构模式，不讲业务。
- SnailJob 的重试模块（`@SnailRetry`）——本课程聚焦任务调度（Job），不覆盖失败重试（Retry）。
- Spring `@Scheduled` 注解的原生定时任务——本课程聚焦 SnailJob 分布式任务调度，原生 Spring 调度不是重点。
- SnailJob 集群部署、高可用架构、数据库表结构等运维层面的深入讨论。

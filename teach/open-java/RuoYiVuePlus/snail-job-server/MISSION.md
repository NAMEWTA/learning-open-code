# Mission: 深入理解 SnailJob 分布式任务调度服务端

## Why
学习者要能完整理解 `ruoyi-snailjob-server` 作为 SnailJob 分布式任务调度**服务端**的整体架构与运行机制。SnailJob 服务端是整个任务调度系统的核心大脑——负责接收客户端注册、管理任务元数据、触发定时与重试调度、分发分片任务、汇总执行日志。掌握服务端原理后，可以独立部署与运维 SnailJob 集群，理解服务端与客户端（`ruoyi-common-job`/`ruoyi-job`）之间的交互协议，以及 SnailJob 如何借助 Akka Actor 模型实现分布式协调。讲解全部基于本仓库真实代码（已逐文件核对），以服务端源码追踪 + 配置解析 + 架构推理为主线。

## Success looks like
- 能说清 `ruoyi-snailjob-server` 模块在 RuoYi-Vue-Plus 扩展层（`ruoyi-extend`）中的定位：它依赖 `snail-job-server-starter`（2.0.0）作为核心引擎、引入 Scala 2.13.9 运行时支撑 Akka Actor 模型、挂载 Spring Boot Admin 客户端做健康监控，并独立暴露 8800 端口和 17888 Netty 通信端口。
- 能解释 `SnailJobServerApplication` 启动类的特殊设计：Spring Boot 入口声明在 `org.dromara.snailjob` 包，但实际 `SpringApplication.run()` 的参数是 `com.aizuda.snailjob.server.SnailJobServerApplication.class`——理解这种跨包引导的必要性（SnailJob 框架的自动配置扫描包在 `com.aizuda.snailjob.server`）。
- 能解析 `application.yml` + `application-dev.yml` 中 SnailJob 服务端核心配置项的含义：`server-port: 17888`（Netty 通信端口）、`retry-pull-page-size`（每批次拉取重试数据大小）、`log-storage`（日志保存天数）、`bucket-total: 128`（分桶总数，影响负载均衡粒度）、`retry-max-pull-parallel`（重试任务拉取并行度）、`load-balance-cycle-time`（负载均衡周期）。
- 能讲清 Actuator 安全防护机制：`SecurityConfig` 如何注册 `ActuatorAuthFilter` 到 `/actuator` 端点，通过 Basic Auth 校验 Spring Boot Admin 客户端用户名密码，以及为何服务端需要暴露 Actuator 端点（Spring Boot Admin 监控依赖）。
- 能说清服务端日志体系：`logback-plus.xml` 中的 `SnailJobServerLogbackAppender` 如何接收客户端上报的远程日志，以及控制台 / 文件 / 异步日志的三层架构。
- 能理解 MyBatis-Plus 在服务端的作用：`typeAliasesPackage: com.aizuda.snailjob.template.datasource.persistence.po` 指向 SnailJob 框架内置的持久化实体（任务、重试记录、调度配置等 PO），服务端通过这些 PO 管理 MySQL 中的调度元数据。
- 能讲清服务端与客户端的交互通道：客户端通过 Netty（17888）上报心跳与日志、服务端通过 HTTP（8800）提供 Dashboard 管理界面，Dockerfile 中同时暴露两个端口的原因。

## Constraints
- 学习者是全栈背景，已具备 ruoyi-job 客户端模块的理解基础（6 种任务模式、`@JobExecutor` 等注解机制），本模块聚焦服务端——追踪启动链、配置链、通信链。
- 目标是「读懂服务端架构与配置」而非「能开发 SnailJob 框架内核」——练习以「读配置答问题 / 复述启动链路 / 解释通信模型」为主。
- SnailJob 管理后台 Dashboard 的具体 UI 操作不在本课程范围——仅在理解服务端静态资源托管（`classpath:admin/`）时交叉引用。
- 不要求深入 Akka Actor 的 Scala 源码——理解 Actor 模型的分布式协调角色即可。
- 交互语言：简体中文。

## Out of scope
- SnailJob 管理后台 Dashboard 的 UI 操作教程（创建任务、拖拉 DAG 工作流等）。
- SnailJob 客户端任务开发（`@JobExecutor`、`@MapExecutor` 等注解使用）——已在 ruoyi-job 模块教学中覆盖。
- Scala 语言与 Akka Actor 框架的原理深度讲解——仅在服务端架构层面交叉提及。
- SnailJob 集群搭建与生产环境运维（多节点部署、高可用方案、性能调优）。
- `ruoyi-extend` 下其他扩展模块（`ruoyi-monitor-admin`、`ruoyi-snailai-server`）。

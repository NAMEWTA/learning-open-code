# SnailJob 分布式任务调度服务端 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailjob-server/` 与服务端配置引用的 `logback-plus.xml`）。以下外部资源用于补充框架架构原理、Akka Actor 模型、Spring Boot Admin 集成等背景知识。

## Knowledge

- [官方文档: _SnailJob 官方文档 - 服务端部署与配置_ — aizuda（snailjob.io）](https://snailjob.io/docs/)
  服务端的权威资料。理解服务端启动参数、数据库初始化、集群配置、Dashboard 功能、服务端与客户端的 Netty 通信协议时查阅。在理解 `application-dev.yml` 中 `snail-job` 段的每个配置项背后含义时，以本文档为准。

- [官方源码: _SnailJob Server Starter_ — aizuda（GitHub）](https://github.com/aizuda/snail-job/tree/main/snail-job-server/snail-job-server-starter)
  服务端核心引擎源码。`SnailJobServerApplication`、Akka Actor 调度模型、Netty 通信层、Dashboard API 的实现均在此模块。追踪 `SpringApplication.run(com.aizuda.snailjob.server.SnailJobServerApplication.class)` 的实际启动链时，从这里进入。

- [官方源码: _SnailJob Server Common_ — aizuda（GitHub）](https://github.com/aizuda/snail-job/tree/main/snail-job-server/snail-job-server-common)
  服务端通用模块，包含 `SnailJobServerLogbackAppender`（`logback-plus.xml` 中配置的 `snail_log_server_appender`）的实现。理解服务端如何接收与存储客户端远程日志时查阅。

- [官方文档: _Akka Actors 介绍_ — Lightbend / Apache Pekko（pekko.apache.org）](https://pekko.apache.org/docs/pekko/current/typed/actors.html)
  SnailJob 服务端底层基于 Akka Actor 模型实现分布式协调（任务分派、负载均衡、集群通信）。理解 `bucket-total`（分桶数）与 Actor 路由的关系、以及 `load-balance-cycle-time`（负载均衡周期）的 Actor 调度语义时查阅。推荐 Apache Pekko（Akka 的 Apache 基金会 fork）文档而非旧版 Lightbend Akka，因 SnailJob 2.x 使用 Pekko 作为 Actor 运行时。

- [官方文档: _Spring Boot Admin_ — codecentric（docs.spring-boot-admin.com）](https://docs.spring-boot-admin.com/current/)
  `application-dev.yml` 中配置的 `spring.boot.admin.client` 段将 SnailJob 服务端注册到监控中心。理解 Actuator 端点暴露策略、`SecurityConfig` + `ActuatorAuthFilter` 的 Basic Auth 防护设计、以及 `metadata.username/userpassword` 的凭证传递机制时查阅。

- [官方文档: _MyBatis-Plus 配置_ — baomidou（baomidou.com）](https://baomidou.com/reference/configuration/)
  `application.yml` 中 `mybatis-plus` 段配置了 `typeAliasesPackage: com.aizuda.snailjob.template.datasource.persistence.po`，使 SnailJob 框架内置的 PO 实体可被 MyBatis-Plus 自动映射。理解服务端如何通过 MyBatis-Plus 管理调度元数据表（任务定义、重试记录、调度日志等）时查阅。

- [代码: _ruoyi-extend/ruoyi-snailjob-server/_ — 本仓库](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailjob-server/)
  模块第一现场。5 个源码文件（1 启动类 + 2 安全过滤器 + 4 配置文件 + 1 Dockerfile + 1 logback 配置）构成服务端完整骨架。任何「这个配置到底在哪」「服务端如何启动」的问题，最终答案在这里。逐一核对清单：
  - `SnailJobServerApplication.java` — 启动入口，跨包引导 `com.aizuda.snailjob.server.SnailJobServerApplication`
  - `ActuatorAuthFilter.java` — Actuator Basic Auth 过滤器，Base64 解码验证
  - `SecurityConfig.java` — 过滤器注册，读取 `spring.boot.admin.client.username/password`
  - `application.yml` — 5800 端口、context-path、MyBatis-Plus、Actuator 暴露
  - `application-dev.yml` — 数据源、snail-job 服务端配置、Spring Boot Admin 客户端
  - `application-prod.yml` — 生产环境模板（与 dev 结构一致）
  - `logback-plus.xml` — SnailJobServerLogbackAppender 挂载
  - `Dockerfile` — BellSoft Liberica JDK 21 + ZGC，暴露 8800 / 17888 双端口

- [代码: _SnailJobConfig.java (客户端侧)_ — 本仓库](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-job/src/main/java/org/dromara/common/job/config/SnailJobConfig.java)
  理解「客户端如何连接到本服务端」的对照参考。`@EnableSnailJob` 注解激活后，客户端按 `application-dev.yml` 中配置的 `snail-job.server.host:port` 连接服务端的 17888 Netty 端口。结合服务端配置理解双向通信链。

- [文章: _Akka Actor 模型在分布式调度中的应用_ — 掘金 / 知乎相关技术博客]
  非特定链接——百度 / Google 搜索 "Akka 分布式调度 Actor 模型"。SnailJob 的 bucket 机制、负载均衡、集群节点发现均基于 Actor 模型。当需要从架构层面理解「为什么配置 `bucket-total: 128`」「`load-balance-cycle-time: 10` 秒是如何调度的」时，搜索相关 Actor 调度文章作为辅助阅读。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「SnailJob 服务端端口冲突」「17888 端口与防火墙策略」「服务端数据库初始化失败」等部署问题时，Issues 区有大量真实运维经验。服务端部署问题优先来此搜索。

- [社区: _SnailJob 官方 Issue / 讨论_](https://github.com/aizuda/snail-job/issues)
  SnailJob 服务端本身的 bug、配置疑问、集群方案讨论。遇到「bucket 分桶策略」「日志存储清理机制」「服务端内存占用过高」等框架级问题时查阅。服务端架构问题贴近框架维护者意图。

- [社区: _Apache Pekko 用户邮件列表 / GitHub Discussions_](https://github.com/apache/pekko/discussions)
  Akka/Pekko Actor 模型的深度讨论社区。仅在需要理解 SnailJob 底层 Actor 调度细节（如 Actor 生命周期、监督策略、集群分片）时查阅。非必需，仅在架构好奇心驱动时进入。

## Gaps
- SnailJob 服务端官方目前缺少对 Akka Actor 调度模型的架构级文档（如 bucket 分配算法、集群节点发现协议、Actor 监督树结构），这部分知识需通过阅读 `snail-job-server-starter` 源码 + 搜索 Pekko Actor 通用知识来补足。
- SnailJob 2.0.0 版本数据库初始化 SQL 脚本未在本仓库中直接包含（依赖 `snail-job-server-starter` 内的自动 DDL 或官方发布包），部署阶段需从官方文档获取。
- 课程不覆盖 SnailJob Dashboard UI 操作教程——此缺口是有意为之（与 Out of scope 一致），学习者如需 Dashboard 使用指南，直接访问 SnailJob 官方文档。

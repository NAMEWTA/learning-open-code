# ruoyi-snailai-server Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailai-server/`）。该模块仅 3 个 Java 文件 + 3 个配置文件 + Dockerfile，代码量极小。以下外部资源用于补充框架原理与平台能力边界。

## Knowledge

- [代码: `SnailAiServerApplication.java` — 唯一的启动类](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailai-server/src/main/java/org/dromara/snailai/SnailAiServerApplication.java)
  14 行启动入门口，委托 `SnailAiSpringbootApplication.main()` 完成实际引导。理解「启动委托」模式——server 模块为何不自己启动 Spring Boot——时查阅。这是整个模块的入口。
- [代码: `SecurityConfig.java` + `ActuatorAuthFilter.java` — 安全配置](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailai-server/src/main/java/com/aizuda/snail/ai/starter/filter/)
  两个文件共约 90 行，实现 Actuator 端点的 HTTP Basic Auth 保护。理解独立部署的服务如何在不依赖 Sa-Token 的情况下保护运维端点时查阅。
- [配置: `application.yml` — 全量配置树](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailai-server/src/main/resources/application.yml)
  Server 端口 8900、gRPC 18888、Skill 上传目录、AES 加密、资源存储 LOCAL/MinIO、短期记忆 memory/db、MyBatis-Plus、Actuator 全端点暴露。理解「配置声明式组装 AI 平台」的完整声明时查阅。这是模块的核心资产——代码少，配置多。
- [配置: `application-dev.yml` / `application-prod.yml` — 环境配置](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailai-server/src/main/resources/)
  数据源连接、HikariCP 连接池、Spring Boot Admin 客户端注册。理解 snailai-server 如何连接数据库（短期记忆 db 模式需要）和注册到监控中心时查阅。
- [构建: `pom.xml` — Maven 依赖声明](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailai-server/pom.xml)
  仅两个依赖：`snail-ai-starter`（AI 平台核心）+ `spring-boot-admin-starter-client`（监控客户端）。理解「极简依赖」设计哲学——核心能力全部由 starter 传递引入——时查阅。
- [部署: `Dockerfile` — 容器化配置](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailai-server/Dockerfile)
  BellSoft Liberica JDK 21 + ZGC、双端口暴露 8900/18888、JVM 调优参数。理解 AI 服务容器的 JVM 选型与 GC 策略时查阅。
- [日志: `logback-plus.xml`](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailai-server/src/main/resources/logback-plus.xml)
  控制台 + 文件 + 异步追加的完整日志配置。理解 AI 服务的日志策略（控制台按级别分色、文件按级别分流、异步写入防阻塞）时查阅。
- [官方文档: _Snail AI — aizuda（爱组搭）开源 AI 智能体平台_](https://snail.ai)
  本模块所运行的平台本体的官方文档。理解 Snail AI 提供哪些能力（AI 模型集成、RAG 知识库、Agent 智能体编排、聊天对话）、Snail AI Server 端的完整功能列表、以及 `snail-ai-starter` 的配置项全貌时查阅。这是理解「server 端到底能做什么」的权威入口。
- [官方文档: _Spring Boot Actuator_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/actuator/index.html)
  本模块暴露了 Actuator 全端点（`management.endpoints.web.exposure.include: '*'`），且通过 Basic Auth 保护。理解 Actuator 端点（health、env、metrics、logfile 等）的能力以及 `FilterRegistrationBean` 的拦截机制时查阅。
- [官方文档: _Spring Boot Admin 客户端_ — codecentric（docs.spring-boot-admin.com）](https://docs.spring-boot-admin.com/current/client.html)
  `spring-boot-admin-starter-client` 将 snailai-server 注册到监控中心（`spring.boot.admin.client.url`）。理解客户端如何向 Admin Server 上报健康状态、日志、配置信息时查阅。第 2 课的核心依赖原理来源。
- [官方文档: _Spring Boot Docker 部署_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/deployment/container-images/docker.html)
  理解 Dockerfile 中的 JVM 参数（`-XX:+HeapDumpOnOutOfMemoryError`、`-XX:+UseZGC`）、ZGC 的低延迟特性与 AI 推理场景的适配关系时查阅。
- [官方文档: _MyBatis-Plus 配置_ — baomidou（baomidou.com）](https://baomidou.com/reference/global-config/)
  本模块配置了 MyBatis-Plus 的逻辑删除、驼峰映射、缓存等功能。短期记忆的 `db` 模式依赖 MyBatis-Plus 做数据持久化。理解配置段含义时查阅。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc.dromara.org）](https://plus-doc.dromara.org/)
  本项目设计说明。理解 snailai-server 在 RuoYi-Vue-Plus 整体架构中的位置、与 ruoyi-ai 模块的关系、以及 extend 目录的设计意图时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  Snail AI Server 的部署问题、配置调优、版本升级兼容性、gRPC 连接故障排查等常见问题在 Issues 中常有涉及。最贴近维护者意图的反馈源。
- [社区: _aizuda / Snail AI 开源社区_](https://gitee.com/aizuda/snail-ai)
  Snail AI 平台本体的官方仓库。Server 端功能需求、bug 反馈、功能讨论。当遇到「Snail AI Server 端的某个行为不符合预期」时查阅。
- [社区: _aizuda / Snail AI Agent GitHub_](https://github.com/aizuda/snail-ai-agent)
  Snail AI Agent 框架源码（含 `snail-ai-starter` 实现）。当需要深入理解 starter 的内部自动配置、组件扫描、默认 Bean 注册逻辑时查阅——虽然源码不在本仓库，但 GitHub 仓库可追溯。

## Gaps
- `snail-ai-starter`（`com.aizuda:snail-ai-starter`）的内部实现在本仓库中不可见——它是 Maven 依赖引入的 JAR。我们仅能通过 `application.yml` 的配置项（`snail-ai.*`）反向推断其能力契约。但对理解模块的装配格局不是阻碍——本课程的目标正是「读懂装配」，而非「读懂 starter 内部」。
- Snail AI 管理后台（`classpath:admin/` 下的静态页面）为编译后的产物，无源码。对理解服务端运行时结构无实质影响。
- gRPC 通信的 proto 文件定义和 stub 生成细节不在本仓库中。仅能通过 gRPC 端口 18888 和配置命名空间推断其存在。

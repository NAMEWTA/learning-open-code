# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-snailai-server —— Snail AI 平台服务端运行时

## Why
`ruoyi-snailai-server` 是 RuoYi-Vue-Plus 中**仅有的 3 个扩展模块（extend）之一**——它与 `ruoyi-monitor-admin`（监控中心）、`ruoyi-snailjob-server`（任务调度平台）并列，属于**独立部署的服务端运行时**，而非嵌入在 `ruoyi-admin` 中的业务模块。学习者需要理解一个关键区别：`ruoyi-ai` 业务模块是「Snail AI 的**客户端适配器**」——它把 AI 能力像插件一样接入 RuoYi 主应用；而 `ruoyi-snailai-server` 是「Snail AI 的**平台本体**」——它是真正运行 AI 模型集成、RAG 检索增强、Agent 智能体调度、gRPC 通信、短期记忆管理的独立服务。本模块仅 3 个 Java 文件（启动入口 + Actuator 安全 + 安全配置），核心能力全部来自 `snail-ai-starter` 依赖。学习这个模块的价值在于：理解一个 AI 平台服务端如何被「装配」——通过 Spring Boot Starter 依赖注入、配置文件声明式组装、Actuator 监控集成、Spring Boot Admin 集中管控，将一整套 AI 能力（模型调用、知识库、Agent 编排、gRPC 通信、记忆管理）压缩进一个可独立部署的 Jar。目标是**读懂平台装配的格局与独立服务部署模式**，不是学 AI 算法。

## Success looks like
- 能用一句话讲清 `ruoyi-snailai-server` 的本质：「它是 Snail AI 平台的独立运行时——只写启动入口和安全配置，AI 能力由 `snail-ai-starter` 通过 Spring Boot 依赖注入与配置声明装配合成」
- 能解释 `SnailAiServerApplication.main()` 为何不自己启动 Spring Boot，而是委托给 `SnailAiSpringbootApplication.main()`——以及这种「启动委托」的设计动机：把实际的自动配置、组件扫描、Bean 注册全部下放给 starter，让 server 模块退化为纯粹的「部署载体」
- 能完整解读 `application.yml` 的配置树：HTTP 端口 8900、gRPC 端口 18888、Skill 上传目录 `./upload/skills`、AES 加密密钥/IV、资源存储类型 LOCAL（预留 MinIO 支持）、短期记忆存储类型（memory vs db）——并说出每项配置的能力边界
- 能解释 `SecurityConfig` + `ActuatorAuthFilter` 的两层设计：配置层使用 `@Value` 从环境注入凭据 + `FilterRegistrationBean` 注册过滤器；过滤器层实现标准 HTTP Basic Auth 校验——并说出为什么 Actuator 端点需要独立于 RuoYi 主应用的认证体系（独立部署，没有 Sa-Token 上下文）
- 能画出 snailai-server 在 RuoYi-Vue-Plus 整体架构中的位置：`ruoyi-snailai-server`（平台运行时 · gRPC 18888）← gRPC → `ruoyi-ai`（业务适配器 · REST）← HTTP → 前端（React SSE 流式 / Vue iframe 嵌入），并讲清每层的通信协议与职责边界
- 能讲解短期记忆（short-term memory）的两种存储策略：`memory` 模式用于单机高性能（进程内存，重启丢失）vs `db` 模式用于分布式持久化（MyBatis-Plus + MySQL，性能较低），并理解 `mybatis-plus` 配置段为何出现在 server 配置中
- 能解释 Dockerfile 的双端口暴露（8900 HTTP + 18888 gRPC）以及为什么使用 ZGC（`-XX:+UseZGC`）作为 GC 策略——低延迟要求适合 AI 推理型服务

## Constraints
- 学习者必须先完成 `2026-06-30-teach-ruoyi-ai` 的学习，理解 Snail AI 在 RuoYi 侧的客户端/适配器架构，以及 `ruoyi-common-ai` 的自动装配模式
- 学习者需有 Spring Boot Starter 机制的基础理解——知道 `@SpringBootApplication`、自动配置、`application.yml` 配置绑定如何工作
- 目标是「读懂装配格局与独立部署模式」，不是「能开发新的 AI 平台」——课程以追踪真实代码结构、解释配置语义、讲清部署架构为主
- 全部讲解基于仓库真实代码，引用具体文件路径与类名（仅 3 个 Java 文件 + 3 个 yml 配置）
- 交互语言：简体中文
- 每节课短小（几分钟内可完成），有一个具体胜利
- gRPC 协议仅点到为止——知道它是服务间高性能通信协议即可，不深入 proto 定义和 stub 生成

## Out of scope
- Snail AI Starter（`com.aizuda:snail-ai-starter`）的内部实现——它作为依赖引入，源码不在本仓库中。我们仅能通过配置项和使用模式推断其能力边界
- AI 模型（LLM）的选型、训练、调优、Prompt 工程、RAG 算法细节——本模块负责平台运行时装配，不涉及 AI 算法
- gRPC 协议原理与实现细节（proto 文件定义、stub 生成、流式通信）——配置中涉及 gRPC 端口 18888，但不深入协议层
- `ruoyi-ai` 业务模块的客户端适配细节（`SnailAiConfig`、`SnailAiChatExceptionHandler`、`SnailAiController`）——这些已在 `2026-06-30-teach-ruoyi-ai` 中覆盖
- `ruoyi-snailjob-server` 与 `ruoyi-monitor-admin` 扩展模块的内部实现——它们与 snailai-server 并列在 extend 目录下，但属于不同业务域
- Spring Boot Admin Server 端的配置与部署——仅在理解 `spring.boot.admin.client.*` 客户端配置时交叉引用
- MinIO 对象存储的部署与管理——配置中预留了 MinIO 支持，但不深入 MinIO 运维
- Snail AI 管理后台的前端页面（通过静态资源 `classpath:admin/` 提供）——仅在理解 `spring.web.resources.static-locations` 配置时点到为止

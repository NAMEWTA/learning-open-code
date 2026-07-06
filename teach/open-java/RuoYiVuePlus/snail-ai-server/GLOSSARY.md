# Snail AI 服务 - 术语表

## 架构与部署

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Snail AI Server (Snail AI 服务端) | Snail AI 智能体平台的独立运行时——通过 snail-ai-starter 依赖注入和配置声明将 AI 能力装配合成为一个可独立部署的 Spring Boot 应用。 | `ruoyi-snailai-server` 模块的本体。作为整个 Snail AI 平台的部署载体，提供 HTTP 8900（管理后台 + Actuator）和 gRPC 18888（AI 能力）两个端口。 |
| snail-ai-starter | aizuda（爱组搭）提供的 Spring Boot Starter，包含 Snail AI 平台的完整运行时能力——AI 模型调用、RAG 知识库、Agent 智能体编排、gRPC 通信、短期记忆管理、资源存储。 | `pom.xml` 中的核心依赖。`SnailAiServerApplication` 将启动委托给其内部的 `SnailAiSpringbootApplication.main()`。所有 `snail-ai.*` 配置项均由它定义和消费。 |
| 客户端适配器 (Client Adapter) | 嵌入在 `ruoyi-admin` 中的 `ruoyi-ai` 模块——通过 Snail AI SDK 将 RuoYi 用户桥接到 Snail AI Server，提供 REST API 给前端。 | 与 `ruoyi-snailai-server`（平台本体）对比理解。一个管"让 RuoYi 能用 AI"，一个管"让 AI 平台跑起来"。两者通过 gRPC 18888 通信。 |
| 装配式平台 (Assembly-based Platform) | 一种架构模式：核心能力不由模块自身编写，而是通过引入 Starter 依赖 + 声明式配置来"装配"。代码定义骨架，配置注入血肉。 | snailai-server 的定位本质——3 个 Java 文件 + 4 个配置文件，配置文件行数远超代码行数。 |
| 启动委托模式 (Startup Delegation Pattern) | `SnailAiServerApplication.main()` 不调用 `SpringApplication.run()`，而是委托给 `SnailAiSpringbootApplication.main()`。让 server 模块退化为纯粹的"部署载体"，starter 控制启动过程。 | `SnailAiServerApplication.java`（14 行）的核心设计。server 声明 What（配置），starter 负责 How（启动）。 |
| ruoyi-extend (扩展模块) | RuoYi-Vue-Plus 中存放独立部署服务端运行时的目录，包括 `ruoyi-monitor-admin`、`ruoyi-snailjob-server`、`ruoyi-snailai-server`。这些模块都是独立进程，有自己的 `main()`、端口和配置。 | 理解 snailai-server 在项目中的位置——它不是嵌入在 ruoyi-admin 中的业务模块，而是 extend 目录下的独立服务。 |

## 通信协议

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| gRPC | Google 开源的高性能 RPC 框架，基于 HTTP/2 + Protocol Buffers 序列化。支持双向流（Bidirectional Streaming）。 | snailai-server 的 18888 端口。ruoyi-ai 适配器通过 gRPC 调用 snailai-server 的 AI 能力。HTTP/2 多路复用支持多用户并发对话，Protobuf 比 JSON 体积更小解析更快，双向流支撑 SSE 流式对话。 |
| gRPC 端口 (gRPC Port) | snailai-server 配置项 `snail-ai.server.grpc-port: 18888`。gRPC 服务的监听端口。 | 仅限内网使用——ruoyi-admin（含 ruoyi-ai）与 snailai-server 部署在同一网络内，gRPC 端口不需要对外暴露。Dockerfile 中通过 EXPOSE 18888 声明。 |
| HTTP 端口 (HTTP Port) | snailai-server 配置项 `server.port: 8900`。HTTP 服务端口。 | 提供 Snail AI 管理后台静态页面（`classpath:admin/`）和 Actuator 运维端点（`/snail-ai/actuator/*`）。不直接服务前端的 AI 对话请求。 |
| SSE (Server-Sent Events) | 服务端推送事件——HTTP 长连接，服务端可向客户端持续推送数据。 | 前端 AI 对话的流式输出技术。底层由 gRPC 的双向流能力支撑。 |
| Protocol Buffers (Protobuf) | Google 的跨语言、跨平台的结构化数据序列化协议。 | gRPC 的默认序列化方式，比 JSON 体积更小、解析更快。适合 AI 对话中较大的请求/响应体（含上下文、历史消息）。 |

## AI 领域概念

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| RAG (Retrieval-Augmented Generation / 检索增强生成) | 一种 AI 技术：在生成回答前先从知识库中检索相关文档，将检索结果与用户问题一起提供给 LLM，从而生成更准确、更有依据的回答。 | `application.yml` 中 `max-file-size: 50MB` 配置的原因——RAG 需要上传知识库文档（PDF、Word、Markdown）进行向量化处理。Snail AI 平台的核心能力之一。 |
| Agent (智能体) | 具备自主决策能力的 AI 程序——能使用工具（Skill）、管理记忆、执行多步任务编排。 | Snail AI 平台的核心能力之一。Agent 可调用 Skill 脚本来完成具体任务。`snail-ai-starter` 提供了 Agent 编排框架。 |
| Skill (技能) | Agent 可调用的工具/插件脚本，以文件形式上传到服务器。 | 配置项 `snail-ai.skill.upload-dir: ./upload/skills` 定义了 Skill 脚本的存储路径。Skill 扩展了 Agent 的能力边界。 |
| 短期记忆 (Short-Term Memory) | AI Agent 在对话过程中保留的近期上下文信息——让 Agent 能记住对话历史，在后续交互中引用之前的信息。 | 配置项 `snail-ai.memory.short-term.store-type`，支持 `memory`（进程内存）和 `db`（MySQL 持久化）两种策略。 |
| LLM (Large Language Model / 大语言模型) | 基于深度学习的超大规模语言模型，如 GPT、Claude、文心一言等。 | Snail AI 平台集成的 AI 模型——负责理解用户意图、生成回答。本模块（snailai-server）负责平台运行时装配，不涉及模型选型与调优。 |

## 存储策略

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| 短期记忆 Memory 模式 (memory store-type) | 将短期记忆数据存储在 JVM 进程内存中（如 ConcurrentHashMap）。高性能（零网络开销、零序列化），但重启后数据全部丢失。 | 配置值 `store-type: memory`。适用于单机部署、开发/测试环境，或对数据持久性无要求的场景。 |
| 短期记忆 DB 模式 (db store-type) | 将短期记忆数据持久化到 MySQL 数据库中（通过 MyBatis-Plus）。性能较低（需 JDBC 连接、SQL 解析、网络 IO），但重启后数据不丢失。 | 配置值 `store-type: db`（当前默认）。适用于生产环境、分布式部署——多实例可共享同一数据库中的记忆数据。 |
| 资源存储 LOCAL (Local Storage) | 将资源文件（如上传的文档、图片）存储在服务器本地磁盘。 | 配置值 `storage-type: LOCAL`，上传路径 `./upload/resource`。适用于单机部署、开发环境。 |
| 资源存储 MinIO (MinIO Object Storage) | MinIO 是开源的高性能对象存储服务，兼容 Amazon S3 API。 | 配置预留 `minio.*`。切换到 `storage-type: MINIO` 后可为分布式部署提供高可用文件存储。无需改代码。 |
| 配置预留模式 (Config Reservation Pattern) | 在当前使用一种实现的同时，在配置文件中完整预留另一种实现的配置项，方便未来切换。 | `snail-ai.resource.minio.*` 是典型例子——当前使用 LOCAL 存储，但 MinIO 的 endpoint、access-key、secret-key、bucket 已全部预留。 |
| 逻辑删除 (Logic Delete) | 数据库操作中不物理删除记录，而是将标记字段设为"已删除"值。 | MyBatis-Plus 配置 `logic-delete-value: 1` 和 `logic-not-delete-value: 0`。删除操作将 `del_flag` 设为 1 而非执行 DELETE。 |

## 安全

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| HTTP Basic Auth (HTTP 基本认证) | HTTP 协议定义的简单认证机制——客户端在 `Authorization` 头中发送 `Basic base64(username:password)`，服务端解码并校验。 | `ActuatorAuthFilter` 的实现标准。用于保护 snailai-server 的 Actuator 运维端点。 |
| AES 加密 (AES Encryption) | Advanced Encryption Standard，对称加密算法。 | 配置项 `snail-ai.crypto.secret-key`（256 位密钥）和 `snail-ai.crypto.iv`（初始化向量）。用于加密 Snail AI 平台中的敏感数据。 |
| Actuator 端点 (Actuator Endpoints) | Spring Boot Actuator 提供的运维端点（health、env、metrics、logfile 等），用于监控和管理应用。 | snailai-server 通过 `management.endpoints.web.exposure.include: '*'` 暴露了全部端点。实际路径为 `/snail-ai/actuator/*`。 |
| WWW-Authenticate 头 (WWW-Authenticate Header) | HTTP 响应头，当服务端要求客户端提供认证信息时返回。浏览器收到此头会弹出登录对话框。 | `ActuatorAuthFilter` 在三层校验的每一层失败时都返回此头 + 401 状态码。 |
| Sa-Token | RuoYi-Vue-Plus 使用的轻量级 Java 权限认证框架。 | snailai-server **不依赖**它——因为 snailai-server 是独立部署的服务，有自己的认证体系（HTTP Basic Auth），不共享 RuoYi 的登录态和权限上下文。 |
| Maven 资源过滤占位符 (Maven Resource Filtering Placeholder) | Maven 构建时替换的占位符，语法 `@property.name@`。 | 环境配置中 `@monitor.username@` 和 `@monitor.password@`——构建时由 Maven profile 替换为真实凭据，避免明文写在配置文件中。 |
| 凭据复用 (Credential Reuse) | 认证凭据在多个组件间共享使用。 | `SecurityConfig` 中的 `@Value("${spring.boot.admin.client.username}")`——同一套凭据既用于 Admin Server 注册时的身份认证，也用于保护 Actuator 端点。 |

## 监控与运维

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Spring Boot Admin (SBA) | codecentric 开源的 Spring Boot 应用监控管理平台——由 Admin Server（服务端）和 Admin Client（客户端）组成。 | `ruoyi-monitor-admin` 是 Admin Server（端口 9090）；snailai-server 通过 `spring-boot-admin-starter-client` 作为客户端注册到它，上报健康状态、日志、配置信息。 |
| Spring Boot Admin Client (SBA 客户端) | 嵌入在 Spring Boot 应用中的监控代理——启动时自动向 Admin Server 注册，定期上报健康状态和指标。 | `pom.xml` 中的第二个依赖。环境配置中通过 `spring.boot.admin.client.url` 指定 Admin Server 地址。 |
| ZGC (Z Garbage Collector) | JDK 11+ 提供的低延迟垃圾回收器，将 GC 暂停控制在亚毫秒级（< 1ms）。 | Dockerfile 中 `-XX:+UseZGC`。AI 对话对延迟敏感——用户期待近乎实时的响应，ZGC 避免 GC 暂停导致响应抖动。 |
| CDS (Class Data Sharing) | JVM 类数据共享——将 JVM 类元数据预存档到共享文件中，加速启动时间。 | Dockerfile 基础镜像 `bellsoft/liberica-openjdk-rocky:21.0.11-cds` 的 `-cds` 后缀。容器化环境中频繁重启/扩缩容时，CDS 显著减少冷启动延迟。 |
| HikariCP | 高性能 JDBC 连接池实现。 | 环境配置中 `spring.datasource.type: com.zaxxer.hikari.HikariDataSource`。用于管理 MySQL 数据库连接（支撑短期记忆 db 模式 + MyBatis-Plus）。 |
| 异步日志 (Async Logging) | 日志事件先写入内存队列，由独立线程批量写入磁盘——避免日志 IO 阻塞业务线程。 | `logback-plus.xml` 中的 `async_info` 和 `async_error` Appender。`queueSize: 1024` 定义队列大小；`discardingThreshold: 100` 定义丢弃阈值。 |
| 日志分流 (Log Separation) | 按日志级别将日志写入不同的文件，便于分类检索和差异化保留。 | `file_console`（全量 ≥INFO / 1 天）、`file_info`（仅 INFO / 60 天）、`file_error`（仅 ERROR / 60 天）。 |
| 过滤器注册 (FilterRegistrationBean) | Spring Boot 提供的 Servlet Filter 注册方式——以 Bean 形式声明过滤器及其拦截路径。 | `SecurityConfig.actuatorFilterRegistrationBean()` 使用它注册 `ActuatorAuthFilter`，指定拦截 `/actuator` 和 `/actuator/*`。 |
| 非阻塞随机数生成器 (Non-blocking Random) | JVM 参数 `-Djava.security.egd=file:/dev/./urandom`，使用 `/dev/urandom` 作为熵源而非 `/dev/random`，避免阻塞。 | Dockerfile ENTRYPOINT 中的 JVM 参数。对 AES 加密配置尤其重要——加密操作需要随机数，阻塞会严重影响性能。 |
| HeapDumpOnOutOfMemoryError | JVM 参数，当发生 OutOfMemoryError 时自动生成堆转储文件（.hprof）。 | Dockerfile ENTRYPOINT 中的 JVM 参数。用于事后分析内存泄漏，不影响正常运行的性能。 |

## 数据访问

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| MyBatis-Plus | MyBatis 的增强工具——在 MyBatis 基础上提供通用 CRUD、分页、逻辑删除、驼峰映射等增强功能。 | `application.yml` 中的 `mybatis-plus` 配置段。短期记忆 db 模式依赖它做数据持久化。实体类在 `com.aizuda.snail.ai.persistence` 包（starter 内部）。 |
| 驼峰映射 (Underscore-to-Camel-Case Mapping) | 数据库下划线命名（`user_name`）自动映射到 Java 驼峰命名（`userName`）。 | MyBatis-Plus 配置 `map-underscore-to-camel-case: true`。 |

## 项目结构

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Spring Boot Starter | Spring Boot 的扩展机制——将一组相关的依赖和自动配置封装为一个 starter，引入后即可获得完整功能。 | `snail-ai-starter` 是典型的 starter。它把 AI 模型集成、RAG、Agent、gRPC 等所有依赖和自动配置打包在一起，server 模块只需引入一个依赖。 |
| @SpringBootApplication | Spring Boot 核心注解，组合了 `@SpringBootConfiguration` + `@EnableAutoConfiguration` + `@ComponentScan`。 | `SnailAiServerApplication` 标注此注解的作用是"标记组件扫描起点"——确保 `org.dromara.snailai` 包下的 Bean（SecurityConfig、ActuatorAuthFilter）被 Spring 容器发现。 |
| @Configuration + @Bean | Spring 的 Java 配置方式——`@Configuration` 类中的 `@Bean` 方法注册 Bean 到容器。 | `SecurityConfig` 使用此模式：用 `@Value` 从环境注入凭据，用 `@Bean` 方法返回 `FilterRegistrationBean`。 |
| Spring Boot Profile | Spring Boot 的环境隔离机制——不同的 profile 激活不同的配置文件（`application-{profile}.yml`）。 | `@profiles.active@` 在构建时由 Maven 替换为 `dev` 或 `prod`。`application-dev.yml` 和 `application-prod.yml` 定义了数据源和监控注册的环境差异。 |
| Banner | Spring Boot 启动时在控制台输出的 ASCII 艺术字横幅。 | `banner.txt` 位于 `src/main/resources/`。可自定义或关闭（`spring.main.banner-mode: off`）。 |
| context-path | Servlet 上下文路径——所有 HTTP 路径的前缀。 | 配置 `server.servlet.context-path: /snail-ai`。Actuator 端点的实际路径为 `/snail-ai/actuator/health`。 |

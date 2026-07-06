# SnailJob 分布式任务调度 - 术语表

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| SnailJob / snail-job | 一款开源的分布式任务调度与重试框架，提供定时任务、重试任务、工作流编排、分片调度等能力，基于 Akka Actor 模型实现分布式协调 | 整个模块的核心框架，服务端负责调度决策，客户端负责任务执行 |
| SnailJob Server / snail-job-server-starter | SnailJob 服务端核心引擎 Starter，包含 Akka Actor 调度、Netty 通信层、Dashboard API、持久化层 | ruoyi-snailjob-server 模块的唯一核心依赖，提供全部自动配置 |
| SnailJob Client / SnailJob 客户端 | 嵌入业务应用的 SnailJob 客户端 SDK，负责接收服务端分派的任务指令并执行，通过 Netty 上报心跳和日志 | ruoyi-common-job 模块，业务应用通过 @JobExecutor 等注解开发任务 |
| Akka Actor / Pekko Actor | 一种基于 Actor 模型的并发编程框架，每个 Actor 是独立的计算单元，通过消息传递通信，无共享状态 | SnailJob 底层调度引擎：每个 bucket 对应一个 Actor，负责该桶内任务的调度分发 |
| Scala | 运行在 JVM 上的多范式编程语言，Akka/Pekko 框架的原生语言 | ruoyi-snailjob-server 的 pom.xml 引入 scala-library 2.13.9 以支撑 Akka Actor 运行时 |
| Netty | 高性能异步事件驱动的网络应用框架，提供 TCP/UDP 通信能力 | SnailJob 服务端通过 Netty 在 17888 端口接收客户端心跳、日志上报和任务结果回传 |
| Dashboard / 管理后台 | SnailJob 内置的 Web 管理界面，提供任务创建、调度监控、日志检索、工作流编排的可视化操作 | 通过 8800 端口 /snail-job/ 路径访问，静态资源由 classpath:admin/ 托管 |
| bucket / 分桶 | SnailJob 将全部任务通过一致性哈希分配到固定数量的桶中，每个桶由一个 Actor 负责调度，是分布式负载均衡的核心粒度 | application-dev.yml 中 bucket-total: 128 定义桶数，load-balance-cycle-time 控制跨节点桶重分配周期 |
| 一致性哈希 (Consistent Hashing) | 一种分布式哈希算法，节点增减时仅影响相邻节点，最小化数据迁移 | 用于将任务分配到 bucket，保证桶与任务之间的映射在集群节点变化时尽量稳定 |
| load-balance-cycle-time / 负载均衡周期 | 服务端集群中定时检查各节点 bucket 负载并重新分配的时间间隔（秒） | application-dev.yml 中配置为 10 秒，与 bucket-total 共同影响调度均衡效果 |
| retry-pull-page-size / 重试拉取页大小 | 服务端每批次从数据库拉取待重试任务的条数 | 影响任务吞吐量：值越大吞吐越高，但单次查询耗时增加 |
| retry-max-pull-parallel / 重试拉取并行度 | 服务端并发拉取重试任务的线程数 | 控制服务端从数据库拉取重试数据的并发度 |
| MyBatis-Plus | MyBatis 的增强工具，提供通用 CRUD、分页、逻辑删除等功能 | SnailJob 服务端通过它管理调度元数据表，typeAliasesPackage 指向框架内置 PO |
| PO (Persistent Object) / 持久化对象 | 与数据库表一一对应的 Java 对象，由 MyBatis-Plus 自动映射 | com.aizuda.snailjob.template.datasource.persistence.po 包下的类对应任务定义、重试记录、调度配置等表 |
| 调度元数据 (Scheduling Metadata) | 描述任务调度状态的数据，包括任务定义、重试记录、调度配置、工作流 DAG、节点信息等 | 存储在 MySQL 中，由 SnailJob 服务端通过 MyBatis-Plus PO 管理 |
| HikariCP / HikariDataSource | 高性能 JDBC 连接池，Spring Boot 2.x+ 的默认数据源 | application-dev.yml 配置为数据源类型，minimum-idle: 10，maximum-pool-size: 20 |
| ZGC (Z Garbage Collector) | JDK 11 引入的低延迟垃圾收集器，暂停时间亚毫秒级（通常 < 1ms），适合延迟敏感型应用 | Dockerfile 中通过 -XX:+UseZGC 启用，避免 GC 暂停影响任务调度精度 |
| BellSoft Liberica JDK | BellSoft 公司发布的 OpenJDK 发行版，内置 CDS (Class Data Sharing) 优化 | Dockerfile 基础镜像 bellsoft/liberica-openjdk-rocky:21.0.11-cds |
| Spring Boot Admin | Spring Boot 应用的监控管理平台，可集中查看应用健康状态、指标、日志、环境变量等 | SnailJob 服务端作为 Admin Client 注册到监控中心（localhost:9090/admin） |
| Actuator | Spring Boot 内置的应用监控端点集合，可暴露 health、env、metrics、threaddump 等 | SnailJob 服务端暴露全部 Actuator 端点（management.endpoints.web.exposure.include: '*'），供 Admin Server 采集 |
| Basic Auth / HTTP Basic Authentication | HTTP 协议定义的简单认证方式，将 "username:password" 进行 Base64 编码后放在 Authorization 请求头中 | ActuatorAuthFilter 通过 Basic Auth 保护 /actuator/** 端点，仅允许 Admin Server 访问 |
| ActuatorAuthFilter | ruoyi-snailjob-server 中的自定义 Servlet Filter，对 Actuator 端点进行四步 Basic Auth 校验 | 由 SecurityConfig 注册到 FilterRegistrationBean，拦截 /actuator 和 /actuator/* 请求 |
| SecurityConfig | 安全配置类，读取 spring.boot.admin.client.username/password 凭据，注册 ActuatorAuthFilter | @Configuration 类，是服务端安全防护的唯一配置入口 |
| WWW-Authenticate | HTTP 响应头，用于告知客户端需要提供认证凭据 | ActuatorAuthFilter 在认证失败时设置此头并返回 401 |
| Logback | Java 日志框架，SLF4J 的原生实现，支持 Appender 机制灵活配置日志输出目标 | logback-plus.xml 中定义全部 7 个 Appender |
| Appender / 日志追加器 | Logback 中将日志事件输出到具体目标（控制台、文件、远程服务等）的组件 | 控制台输出 (ConsoleAppender)、文件滚动 (RollingFileAppender)、异步缓冲 (AsyncAppender)、远程上报 (SnailLogbackAppender) |
| RollingFileAppender | 支持按时间或大小滚动切割日志文件的 Appender | file_info（INFO 60 天）、file_error（ERROR 60 天）、file_console（1 天） |
| AsyncAppender | 异步日志 Appender，将日志事件放入队列由后台线程消费，减少日志 I/O 对业务线程的阻塞 | async_info 和 async_error 分别包装 file_info 和 file_error，队列 1024，丢弃阈值 100 |
| discardingThreshold / 丢弃阈值 | AsyncAppender 参数：队列占用超过此阈值时丢弃 TRACE/DEBUG/INFO 级别日志 | 配置为 100，队列接近满时优先保留 WARN/ERROR 日志 |
| SnailLogbackAppender (客户端侧) | SnailJob 客户端自定义的 Logback Appender，拦截任务执行日志并通过 Netty 发送到服务端 | 客户端 SnailJobConfig.onStarting() 监听 SnailClientStartingEvent 事件后动态挂载到 Logback 根 Logger |
| SnailJobServerLogbackAppender (服务端侧) | SnailJob 服务端自定义的 Logback Appender，接收客户端远程日志并持久化到 MySQL | logback-plus.xml 中定义为 snail_log_server_appender，挂载到 root logger |
| SnailClientStartingEvent | SnailJob 客户端启动事件，在客户端完成与服务端的连接建立后发布 | 客户端 SnailJobConfig.onStarting() 通过 @EventListener 监听此事件，触发远程日志 Appender 挂载 |
| cross-package bootstrap / 跨包引导 | SnailJobServerApplication 声明在 org.dromara.snailjob 包，但 run() 传入 com.aizuda.snailjob.server 包的类 | 解决 Spring Boot 自动配置扫描范围问题：框架组件在 com.aizuda.snailjob.server 包下，需以此为基准扫描 |
| @SpringBootApplication | Spring Boot 复合注解，包含 @Configuration、@EnableAutoConfiguration、@ComponentScan | 标注在引导类上，使 IDE 识别为 Spring Boot 应用入口 |
| SpringApplication.run() | Spring Boot 应用启动的核心方法，创建 ApplicationContext 并触发自动配置 | 传入 com.aizuda.snailjob.server.SnailJobServerApplication.class 以指定扫描基准包 |
| ApplicationReadyEvent | Spring Boot 应用完全启动后发布的事件，表示应用已准备好接收请求 | SnailJob 服务端启动完成后发布，标志着可以接收客户端注册 |
| ruoyi-extend / 扩展层 | RuoYi-Vue-Plus 项目中的可独立部署模块目录 | ruoyi-snailjob-server、ruoyi-monitor-admin、ruoyi-snailai-server 均位于此层 |
| ruoyi-common-job | RuoYi-Vue-Plus 公共组件层中的 SnailJob 客户端模块 | 包含 SnailJobConfig（客户端配置类）、@EnableSnailJob 激活注解、任务执行器支持 |
| Dockerfile | Docker 镜像构建文件，定义基础镜像、端口暴露、启动命令 | 使用 BellSoft Liberica JDK 21 + ZGC，EXPOSE 8800 和 17888 双端口 |
| context-path / 上下文路径 | Servlet 容器的 URL 前缀 | 配置为 /snail-job，Dashboard 访问路径为 http://host:8800/snail-job/ |
| logic-delete / 逻辑删除 | 通过标记字段（如 del_flag=1）标识记录已删除，而非物理删除 | MyBatis-Plus 配置 logic-delete-value: 1, logic-not-delete-value: 0 |
| map-underscore-to-camel-case / 下划线转驼峰 | MyBatis-Plus 自动将数据库下划线命名映射为 Java 驼峰命名 | 配置为 true，如数据库列 task_name 映射为 Java 属性 taskName |
| DAG (Directed Acyclic Graph) / 有向无环图 | 工作流任务编排的数据结构，节点表示任务，边表示依赖关系 | SnailJob Dashboard 中可视化编排工作流，定义任务执行顺序和依赖 |
| 分片任务 (Sharding Task) | 将大数据量任务拆分为多个子任务，分发到不同客户端节点并行执行的任务模式 | SnailJob 6 种任务模式之一，适用于大批量数据处理场景 |

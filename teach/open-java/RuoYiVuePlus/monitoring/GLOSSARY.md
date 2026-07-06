# Spring Boot Admin 监控 - 术语表

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Spring Boot Admin (SBA) | codecentric 开源的 Spring Boot 应用监控框架，提供 Web UI 管理后台，用于集中监控所有 Spring Boot 微服务的健康状态、指标、日志和配置。 | 整个 ruoyi-monitor-admin 模块的基石。通过 server-starter 提供管理 UI，通过 client-starter 实现实例注册上报。 |
| SBA Server (监控服务端) | SBA 的展示与聚合层。接收各 Client 上报的实例数据，存储在 InstanceRepository 中，并通过内嵌的 Vue.js SPA 在 Web UI 上渲染服务墙、详情面板、日志查看器等视图。 | 由 `@EnableAdminServer` 注解自动装配。在 application.yml 中通过 `spring.boot.admin.*` 配置 context-path、UI title 等属性。 |
| SBA Client (监控客户端) | SBA 的注册与上报层。应用启动时向 Server 注册自己，定时发送心跳和从 Actuator 端点采集的状态数据。不产生数据，只是"信使"。 | 由 `spring-boot-admin-starter-client` 依赖自动装配。在 application.yml 中通过 `spring.boot.admin.client.*` 配置 Server 地址和注册行为。 |
| 自注册模式 (Self-Registration) | monitor-admin 同时作为 Server 和 Client，自己将自己注册到自己的 Server 上。管理员打开后台第一眼就能看到监控中心自身的健康状态。 | application.yml 中 `spring.boot.admin.client.url` 指向 `http://localhost:9090/admin`（即自己），实现自监控。 |
| @EnableAdminServer | SBA 框架的核心注解，触发一整套自动装配：AdminServerAutoConfiguration（实例仓库 + 上报端点）、AdminServerWebConfiguration（管理 UI）、NotifierAutoConfiguration（通知器扫描）。 | 标注在 `MonitorAdminApplication` 启动类上，将一个普通 Spring Boot 应用变成 SBA 监控中心。 |
| InstanceRepository | SBA Server 的内存数据库，存储所有已注册实例的完整信息（registration、status、endpoints 等）。通过它可以查询当前在线实例及其详细信息。 | Server 收到 Client 注册请求后写入；CustomNotifier 通过 `super(repository)` 传递给基类 AbstractEventNotifier。 |
| Spring Boot Actuator | Spring Boot 内置的运维监控模块，暴露 /health、/metrics、/env、/logfile、/threaddump、/heapdump 等 HTTP 端点，是 SBA 的数据来源。 | 在 application.yml 中通过 `management.endpoints.web.exposure.include='*'` 暴露所有端点；通过 `management.endpoint.health.show-details=ALWAYS` 展示健康细节。 |
| context-path | SBA Server 管理后台 UI 的挂载路径前缀。例如 `/admin` 意味着后台地址为 `http://localhost:9090/admin`。 | 在 application.yml 中通过 `spring.boot.admin.context-path` 配置。SecurityConfig 中的路径规则和 Client 注册 URL 都必须与之同步。 |
| service-host-type | SBA Client 注册时决定上报地址格式的配置项。可选值：IP（用 IP 地址，最稳妥）、HOSTNAME（用主机名，默认）、CANONICAL_HOST_NAME（用 FQDN）。 | 在 application.yml 中配置 `spring.boot.admin.client.instance.service-host-type: IP`，避免生产环境 hostname 解析失败导致不可达。 |
| metadata (SBA 元数据) | Client 随注册请求发送给 Server 的自定义键值对（Map<String, String>），用于传递凭证等附加信息。 | 本项目中传递 `username` 和 `userpassword`，供 Server 回调 Client 的受保护 Actuator 端点时使用。 |
| InstanceStatusChangedEvent | SBA 事件体系中的核心事件类型，当某个实例的状态发生变化（如 UP→DOWN）时由 Server 发布到事件总线。 | CustomNotifier 通过 `instanceof InstanceStatusChangedEvent` 过滤该事件，触发状态变化日志记录。 |
| StatusInfo（状态码常量） | SBA 定义的 6 种实例状态常量：UP、OFFLINE、DOWN、RESTRICTED、OUT_OF_SERVICE、UNKNOWN，定义在 `de.codecentric.boot.admin.server.domain.values.StatusInfo` 中。 | CustomNotifier 通过 `import static ...StatusInfo.*` 静态导入，在 switch 表达式中将状态码映射为中文业务描述。 |
| AbstractEventNotifier | SBA 通知器体系的抽象基类，提供事件类型过滤、去重检查等通用逻辑，定义 `doNotify(InstanceEvent, Instance)` 模板方法供子类覆盖。 | CustomNotifier 继承该类，只需覆盖 doNotify() 实现自己的通知逻辑。 |
| doNotify() | AbstractEventNotifier 定义的模板方法，签名 `Mono<Void> doNotify(InstanceEvent event, Instance instance)`。当事件通过基类的类型过滤后，被自动调用。 | CustomNotifier 在此方法中执行 instanceof 过滤、数据提取、状态码映射、日志记录。 |
| Mono&lt;Void&gt; (Project Reactor) | Project Reactor 响应式编程中的类型，表示一个异步的、可能为空的操作。SBA 通知器体系强制要求 doNotify() 返回此类型以支持非阻塞调度。 | CustomNotifier 通过 `Mono.fromRunnable()` 将同步日志记录包装为 Mono，支持未来扩展为异步告警时链式调用 `.subscribeOn()`。 |
| Mono.fromRunnable() | Project Reactor 的工厂方法，将一段 Runnable（同步无返回值代码）包装成 Mono&lt;Void&gt;。代码在订阅时执行，非定义时执行。 | CustomNotifier.doNotify() 的返回值由此方法包装，将日志记录的 Runnable 适配为 SBA 要求的响应式返回类型。 |
| SecurityFilterChain | Spring Security 的核心配置对象，通过链式 DSL 定义一组安全过滤规则（认证、授权、CSRF、headers 等）。 | SecurityConfig.filterChain() 方法返回此 Bean，定义 SBA 管理后台的 6 项安全策略。 |
| AdminServerProperties | SBA 框架提供的配置 Bean，自动读取 `spring.boot.admin.*` 下的配置值（如 context-path）。 | SecurityConfig 通过构造函数注入此 Bean，动态获取 context-path，实现路径无关的安全规则。 |
| SavedRequestAwareAuthenticationSuccessHandler | Spring Security 提供的登录成功处理器。自动记住被拦截前的原始请求 URL，登录成功后重定向回去；也可通过 defaultTargetUrl 和 redirectTo 参数控制跳转目标。 | SecurityConfig 将其设为表单登录的 successHandler，实现"登录后回到拦截前的页面"。 |
| PathPatternRequestMatcher | Spring Security 6.x 的新默认路径匹配器，基于 Spring 的 PathPattern 解析器，性能优于 AntPathRequestMatcher，天然支持 {variable} 路径变量。 | SecurityConfig 使用 `PathPatternRequestMatcher.withDefaults()` 构建匹配器，在 authorizeHttpRequests 中匹配放行路径。 |
| CSRF (跨站请求伪造) | Spring Security 默认保护机制，要求 POST/PUT/DELETE 请求携带 CSRF token。SBA 场景由于 UI 的 AJAX 请求和 Client 的 HTTP Basic 均不支持 CSRF token，必须禁用。 | SecurityConfig 中通过 `.csrf(AbstractHttpConfigurer::disable)` 禁用，这是 SBA 官方推荐配置。 |
| X-Frame-Options (frameOptions) | HTTP 响应头，Spring Security 默认设为 DENY，禁止页面被 iframe 嵌入。SBA 日志查看器等面板使用 iframe 加载，必须禁用此响应头。 | SecurityConfig 中通过 `.frameOptions(HeadersConfigurer.FrameOptionsConfig::disable)` 禁用。需注意 clickjacking 风险。 |
| HTTP Basic 认证 | HTTP 协议标准的认证方式，通过 Authorization 请求头传递 Base64 编码的 username:password。SBA Client 注册和 Server 回调 Actuator 均使用此方式。 | SecurityConfig 中通过 `.httpBasic(Customizer.withDefaults())` 启用，与表单登录双认证并存。 |
| NotifierAutoConfiguration | SBA 自动装配的一部分，扫描容器中所有实现 Notifier 接口的 Bean，在事件发生时自动调用其 notify() 方法。 | 无需手动配置——只要 CustomNotifier 标注 @Component，就会被自动发现并注册到事件总线。 |

---

> 总计 23 个术语，覆盖 ruoyi-monitor-admin 模块的架构设计、配置模型、安全机制和扩展体系。

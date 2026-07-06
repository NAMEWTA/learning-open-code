# ruoyi-common-security 安全模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**Sa-Token**：
Dromara 社区出品的轻量级 Java 权限认证框架。提供登录认证、权限认证、Session 会话、OAuth2.0 等能力，核心 API 是 `StpUtil`。本项目通过 `ruoyi-common-satoken` 模块做了一层封装后，再由本模块进行应用级安全配置。
_Avoid_: 「Spring Security」（项目未使用 Spring Security，全部基于 Sa-Token）。

**ruoyi-common-satoken**：
Ruoyi 对 Sa-Token 的基础封装模块（`ruoyi-common-satoken`），提供 `LoginHelper`（登录用户工具类，含 CLIENT_KEY / CLIENT_ACCESS_PATH_KEY / CLIENT_IP_WHITELIST_KEY 等 token 扩展字段 key）、`SaTokenConfiguration` 等基础 Bean。本模块（`ruoyi-common-security`）在其之上搭建应用级安全横切配置。
_Avoid_: 将两个模块混为一谈——satoken 提供基础能力，security 提供应用级安全策略。

**SecurityConfig**：
本模块核心类（`config/SecurityConfig.java`），`@AutoConfiguration` 注解，实现 `WebMvcConfigurer`。注册三个安全组件：①重注册 Sa-Token 上下文过滤器（覆盖 ASYNC/ERROR）② SaInterceptor 路由拦截器（登录校验、clientId 校验、客户端访问规则校验）③ actuator Basic Auth 过滤器。是三条安全防线的一站式装配点。
_Avoid_: 「spring security 的配置类」（项目与 Spring Security 无关）。

**SecurityProperties**：
安全配置属性类（`config/properties/SecurityProperties.java`），`@ConfigurationProperties(prefix = "security")`，仅含一个 `String[] excludes` 字段。对应 yml 中的 `security.excludes` 配置段，由 `SecurityConfig.addInterceptors()` 中的 `excludePathPatterns()` 消费，定义哪些路径不进行登录鉴权。
_Avoid_: 「安全配置」（太泛，容易与 Sa-Token 自身配置混淆）。

**AllUrlHandler**：
URL 扫描收集器（`handler/AllUrlHandler.java`），实现 `InitializingBean`。在 Spring 容器初始化后自动从 `RequestMappingHandlerMapping` 获取系统中所有的 `@RequestMapping` 路径，并将 `{xxx}` 路径变量替换为 `*` 通配符。收集结果存入 `urls` 列表，供 `SecurityConfig` 中 `SaRouter.match(allUrlHandler.getUrls())` 使用，确保新加的接口自动纳入鉴权范围。
_Avoid_: 「URL 处理器」（它不处理请求，只收集路径信息）。

**LoginHelper**：
Ruoyi 登录用户工具类（`ruoyi-common-satoken` 中定义）。关键常量：`CLIENT_KEY = "clientId"`（token 中存储的客户端标识字段名）、`CLIENT_ACCESS_PATH_KEY`（客户端授权访问路径列表 key）、`CLIENT_IP_WHITELIST_KEY`（客户端 IP 白名单 key）。`SecurityConfig` 中多处引用这些 key 来读取 token 扩展信息，做 clientId 一致性和客户端访问规则校验。

**FilterRegistrationBean**：
Spring Boot 提供的 Servlet Filter 注册 API。本模块中 `SecurityConfig.saTokenContextFilterRegistration()` 用它对 Sa-Token 的上下文过滤器进行「覆盖重注册」——关键是 `setDispatcherTypes(EnumSet.of(REQUEST, ASYNC, ERROR))`，让过滤器在异步和错误分发路径上也生效，这是 SSE / WebSocket 场景下 `StpUtil` 不报未初始化的关键。

**SaInterceptor + SaRouter.match().check()**：
Sa-Token 提供的路由拦截器与链式路由匹配 API。本模块核心鉴权链路即由它构成：`SaRouter.match(allUrlHandler.getUrls()).check(() -> { ... })`——对所有匹配到的 URL 执行 check 逻辑（登录校验、clientId 校验、客户端访问规则校验）。`excludePathPatterns()` 在匹配前就将排除路径剔除。

**InitializingBean**：
Spring 生命周期接口。`AllUrlHandler` 实现它的 `afterPropertiesSet()` 方法，在 Bean 属性设置完成后、Spring 容器启动完毕前自动执行。此时 `RequestMappingHandlerMapping` 已完全初始化（所有 Controller 的 `@RequestMapping` 路径已注册），恰好是收集全系统 URL 的唯一正确时机——早了路径不全，晚了拦截器已经装配完。
_Avoid_: 「Bean 初始化回调」（太泛，无法体现它在本模块中的专用性）。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

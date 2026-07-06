# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-security 安全配置模块

## Why
学习者要能彻底读懂 `ruoyi-common-security` 这个公共安全配置模块：它只用 3 个 Java 类，在 `ruoyi-common-satoken` 提供的基础 Sa-Token 能力之上，搭建了一整套**应用级安全横切配置**——可配置的安全属性、覆盖 ASYNC/ERROR 分发的上下文过滤器、对所有请求的登录鉴权与客户端校验、actuator 的 Basic Auth 保护，以及自动收集全系统 URL 路径的通配能力。理解它，等于理解 RuoYi-Vue-Plus 如何把 Sa-Token「从能用到好用」——不是引入一个框架就完事，而是用**三个轻量组件精准地扎在请求链的三处要冲**。达到能给同事讲清「SecurityConfig 里三个 Bean 各守什么关卡」「URL 扫描为什么要在 InitializingBean 里做」「客户端鉴权白名单校验怎么串起来」，并能在此基础上为项目新增一条排除路径或为新客户端配置访问白名单。重点是**读懂三个组件在请求生命周期中的精确位置与设计动机**，不是从零学 Sa-Token。

## Success looks like
- 能用一句话说清 `ruoyi-common-security` 与 `ruoyi-common-satoken` 的关系，并说出本模块「三件套」（SecurityConfig / SecurityProperties / AllUrlHandler）各自承担的职责。
- 能解释 `SecurityConfig.saTokenContextFilterRegistration()` 为什么要重注册 Sa-Token 上下文过滤器，以及 `EnumSet.of(REQUEST, ASYNC, ERROR)` 对 SSE / WebSocket 等场景意味着什么。
- 能讲清 `addInterceptors` 中 SaInterceptor 内的鉴权链：① `StpUtil.checkLogin()` 登录校验 → ② header/param 中 clientId 与 token 内 clientId 的一致性校验 → ③ `validateClientAccessRules()` 按客户端配置校验访问路径白名单和来源 IP 白名单。
- 能解释 `SecurityProperties` 如何通过 `@ConfigurationProperties(prefix = "security")` 暴露 `excludes` 数组，并被 `excludePathPatterns()` 消费——以及它与 `AllUrlHandler.getUrls()` 的关系（排除 vs 匹配扫描）。
- 能讲清 `AllUrlHandler` 实现 `InitializingBean` 后如何从 `RequestMappingHandlerMapping` 收集全量 URL、用正则 `\{(.*?)\}` 把 `{xxx}` 路径变量替换为 `*` 通配符，以及这个列表最终怎样喂给 `SaRouter.match()` 做路径匹配。
- 能画出一条请求穿过三层安全关卡的全时序图：上下文过滤器 → 路由拦截器（登录 + clientId + 路径/IP白名单） → actuator Basic Auth 过滤器，并说出各自在什么时机被触发。
- 能读懂 yml 中 `security.excludes` 配置段，并能照葫芦画瓢新增或调整排除路径。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端安全配置架构。
- 目标是「读懂设计动机与代码链路」而非「能替代 Sa-Token 框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与类名。
- 基于 `ruoyi-common-satoken` 提供的基础能力（LoginHelper、StpUtil 等底层在 satoken 模块，本课不展开）。
- 交互语言：简体中文。

## Out of scope
- Sa-Token 框架自身的底层原理（登录模型、token 风格、注解鉴权等）——这些属于 `ruoyi-common-satoken` 的教学范围。
- 具体登录策略（密码登录、短信登录、社交登录等）的完整链路——仅在交叉到 clientId 校验时点到。
- `ruoyi-common-redis` 中 `RedisUtils` / 限流 / 防重提交等能力的内部实现——本模块只消费它们。
- Spring Security 框架——本模块基于 Sa-Token 方案，不涉及 Spring Security。
- yml 中 `sa-token` 配置段的完整解读（token-name、timeout、is-concurrent 等）——属于 satoken 模块教学。

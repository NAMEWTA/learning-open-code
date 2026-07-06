# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-web Web基础设施模块

## Why
学习者要能彻底读懂 `ruoyi-common-web` 这个公共模块：它是整个 RuoYi-Vue-Plus 项目的 **Web 层基础设施**——17 个 Java 类覆盖了 XSS 过滤、可重复读请求体、CORS 跨域、验证码生成、国际化、全局异常处理、响应增强通知、请求耗时统计等 Web 层必备能力。理解它，等于理解 RuoYi 如何用 Servlet Filter + Spring Interceptor + RestControllerAdvice 三层武器构建安全、健壮、可观测的 Web 入口。达到能给同事讲清「一个 HTTP 请求从进入 Filter 链到返回 JSON 响应，经过了哪些处理环节」，并能在此基础上排查 XSS 绕过、请求体重复读取失败、验证码不显示等常见问题的程度。重点是**读懂每个 Filter/Interceptor/Advice 的排列顺序与协作关系**。

## Success looks like
- 能用一句话说清 `ruoyi-common-web` 模块的定位，并列出它的五大能力域：过滤器链、请求包装、验证码与国际化、全局异常处理、响应增强。
- 能画出 HTTP 请求经过的完整处理链：`RepeatableFilter` -> `XssFilter` -> `PlusWebInvokeTimeInterceptor` -> Controller -> `GlobalExceptionHandler` / `ResponseEnhancementAdvice`，并说出每环的职责。
- 能解释 `RepeatableFilter` + `RepeatedlyRequestWrapper` 为什么必须排在 `XssFilter` 之前，以及 `RepeatedlyRequestWrapper` 如何通过缓存 `byte[] body` 实现请求体的多次读取。
- 能讲清 XSS 防护的三层机制：Filter 层 `XssFilter` 负责放行/拦截决策、Wrapper 层 `XssHttpServletRequestWrapper` 用 `HtmlUtil.cleanHtmlTag()` 清洗内容、配置层 `XssProperties` 控制开关与排除 URL。
- 能讲清 `GlobalExceptionHandler` 捕获了哪些异常类型（至少说出 5 种），以及 `@ResponseStatus` 注解在 SSE 异常和 IOException 上的特殊处理逻辑。
- 能解释 `ResponseEnhancementAdvice` 如何通过 `ResponseBodyAdvice` 接口在 JSON 响应写出前对 body 做统一增强，以及它与 `JsonValueEnhancer` 的分工。
- 能完整追踪「访问验证码接口 -> 生成 WaveAndCircleCaptcha -> 输出图片流」的调用链，并说出波浪线+圆圈干扰的绘制原理。
- 能读懂 `I18nLocaleResolver` 如何从请求头 `content-language` 解析 Locale，以及 `I18nConfig` 为何声明 `@AutoConfiguration(before = WebMvcAutoConfiguration.class)`。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java Servlet/Spring MVC，讲解聚焦后端请求处理管道。
- 目标是「读懂」而非「能改造框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 画链路图」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- Spring Boot 自动装配机制的深入原理（`@AutoConfiguration` / `AutoConfiguration.imports` 的底层扫描逻辑）——已在其他模块课程覆盖，本课只用不深究。
- 前端 XSS 防护（CSP、HttpOnly Cookie 等）——本课聚焦后端 Java Filter 层的参数清洗。
- Jackson 序列化/反序列化的完整机制——仅在 `ResponseEnhancementAdvice` 中涉及 `HttpMessageConverter` 选择时点到为止。
- Spring Security / Sa-Token 认证授权的 Filter 链——那是 `ruoyi-framework` 的职责，本模块不涉及。

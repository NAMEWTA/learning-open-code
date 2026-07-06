# ruoyi-common-web Web基础设施模块 Glossary

记录学习者在 5 节课程中**真正理解**的核心术语。覆盖过滤器链、请求包装、异常处理、响应增强、验证码与国际化五大块。

## Terms

**Filter 链（过滤器链）**：
Servlet 规范定义的请求预处理管道。多个 Filter 按 `order` 值从小到大依次执行，形成 `Filter1 -> Filter2 -> Filter3 -> ... -> Servlet` 的执行顺序。本模块的 Filter 链为：`RepeatableFilter`（先缓存请求体） -> `XssFilter`（再清洗内容） -> Controller。顺序是设计要点——必须先缓存原始 body 再清洗，否则 XSS 清洗后的内容不可逆。
_Avoid_: 「拦截器链」（Interceptor 是 Spring MVC 层的概念，Filter 是 Servlet 层的概念，二者执行阶段不同）。

**RepeatableFilter**：
本模块的第一个 Filter。对所有 JSON 请求（`Content-Type: application/json`）用 `RepeatedlyRequestWrapper` 包装原始 `HttpServletRequest`，使请求体可以被多次读取。无显式 order，在 `XssFilter` 之前执行。
_Avoid_: 「请求体缓存过滤器」（不够精确，核心是「可重复读」而非「缓存」）。

**RepeatedlyRequestWrapper**：
`HttpServletRequestWrapper` 的子类。构造时通过 `IoUtil.readBytes(request.getInputStream(), false)` 将请求体读入 `byte[] body` 缓存，后续 `getInputStream()` 每次从缓存的 `body` 新建 `ByteArrayInputStream` 返回，从而实现多次读取。同时设置请求和响应的字符编码为 UTF-8。
_Avoid_: 「请求体缓存器」（它是一个完整的 Request 包装器，不只是缓存器）。

**XssFilter**：
XSS 防护的入口 Filter。实现 `jakarta.servlet.Filter`，通过 `@FilterRegistration(order = HIGHEST_PRECEDENCE + 1)` 注解式注册，结合 `@ConditionalOnProperty(value = "xss.enabled")` 实现开关控制（配置 `xss.enabled=false` 时整个 Filter Bean 不存在，零性能开销）。`doFilter` 中对 GET/DELETE 请求直接放行，对命中 `excludeUrls` 的路径跳过过滤，其余请求用 `XssHttpServletRequestWrapper` 包装后继续。
_Avoid_: 「防注入过滤器」（它专门防 XSS，不防 SQL 注入或 CSRF）。

**XssHttpServletRequestWrapper**：
`HttpServletRequestWrapper` 的子类。重写 `getParameter()`、`getParameterValues()`、`getParameterMap()`、`getInputStream()` 四个方法，在每个取值点调用 `HtmlUtil.cleanHtmlTag(value).trim()` 清洗 HTML 标签并去除前后空格。对 JSON 请求的 body 同样做全量清洗。
_Avoid_: 「参数清洗器」（它是一个完整的 Request 包装器，不是单独的工具）。

**XssProperties**：
XSS 配置属性类，`@ConfigurationProperties(prefix = "xss")`。两个字段：`enabled`（总开关）和 `excludeUrls`（跳过过滤的路径列表）。通过 `@EnableConfigurationProperties(XssProperties.class)` 在 `FilterConfig` 中激活。
_Avoid_: 「XSS 配置」（省略了 Properties，职责不清）。

**CORS（跨域资源共享）**：
浏览器安全策略，限制页面从不同源加载资源。本模块通过 `ResourcesConfig.corsFilter()` 注册全局 `CorsFilter`，配置允许的源、头、方法、凭证、缓存时间。默认全放行（`allowedOriginPatterns = ["*"]`），生产环境应收紧。
_Avoid_: 「跨域」（省略了全称，不够精确）。

**CorsProperties**：
CORS 跨域配置属性类，`@ConfigurationProperties(prefix = "web.cors")`。五个字段：`allowCredentials`（是否允许携带 Cookie）、`allowedOriginPatterns`（允许的源模式）、`allowedHeaders`、`allowedMethods`、`maxAge`（预检请求缓存秒数）。都有默认值，零配置即可用。
_Avoid_: 「跨域配置」（太泛，项目中可能有多个跨域配置）。

**PlusWebInvokeTimeInterceptor**：
请求耗时统计拦截器，实现 `HandlerInterceptor`。`preHandle` 中通过 `StopWatch.start()` 开始计时，同时记录请求 URL、参数类型和参数内容（JSON 请求从 `RepeatedlyRequestWrapper` 重读 body，form 请求打 `parameterMap`）。`afterCompletion` 中输出总耗时。敏感字段（密码、手机号等）在日志中自动脱敏。使用 `ThreadLocal<StopWatch>` 确保线程安全。
_Avoid_: 「耗时拦截器」（遗落了日志脱敏和参数记录这两个重要职责）。

**GlobalExceptionHandler**：
`@RestControllerAdvice` 标注的全局异常处理器。覆盖 16 种异常类型，核心纪律：内部 `log.error` 记完整堆栈，对外 `R.fail()` 返回友好提示——不把技术细节泄露给客户端。特殊处理包括：为 RuntimeException/Exception 生成 8 位错误编号方便排查，SSE 异常（`AsyncRequestTimeoutException`）空处理，IOException 对 SSE 端点静默忽略。
_Avoid_: 「统一异常处理」（Spring 有 `@ControllerAdvice` / `@RestControllerAdvice` 两种，本模块用的是后者）。

**ResponseEnhancementAdvice**：
实现 `ResponseBodyAdvice<Object>` 的响应增强切面。在 `supports()` 中委托 `JsonValueEnhancer.supports(converterType)` 判断是否增强；在 `beforeBodyWrite()` 中仅在 Content-Type 兼容 JSON 时调用 `jsonValueEnhancer.enhance(body)` 对响应体做字段值增强（如日期格式化、敏感字段脱敏等）。实际增强逻辑在 `ruoyi-common-json` 模块的 `JsonValueEnhancer` 接口中。
_Avoid_: 「响应包装器」（它不改变响应结构，只增强字段值）。

**BaseController**：
Web 层通用基类，提供 `toAjax(int rows)` / `toAjax(boolean result)` / `redirect(String url)` 三个便捷方法。前两个将行数或布尔结果转为统一的 `R<Void>` 响应（rows>0 或 result=true → `R.ok()`，否则 `R.fail()`），第三个生成 `redirect:xxx` 重定向路径。
_Avoid_: 「Web 基类」（失焦，不是所有 Web 类都叫 BaseController）。

**WaveAndCircleCaptcha**：
自定义验证码生成器，继承 Hutool 的 `AbstractCaptcha`。`createImage()` 方法：① `drawString()` 绘制彩色验证码文字并开启抗锯齿；② `shear()` 对图片做 X/Y 双向正弦扭曲（防止 OCR 切割）；③ `drawInterfere()` 绘制圆圈和一条平滑正弦波浪线（增加识别难度）。通过多个构造器重载支持自定义宽高、字符数、干扰数、字体缩放比。
_Avoid_: 「图形验证码」（Hutool 有多种 Captcha 实现，这个是加了波浪+圆圈的定制版）。

**I18nLocaleResolver**：
基于请求头解析国际化语言的自定义 `LocaleResolver`。从请求头 `content-language` 取值，用 `Locale.forLanguageTag()` 解析为 BCP47 语言标签（如 `zh-CN`、`en-US`）。值为空时回退到 `Locale.getDefault()`。`setLocale()` 保留空实现——项目不在服务端主动切换语言，由前端通过请求头发送语言偏好。
_Avoid_: 「语言解析器」（Locale 包括语言和地区，不止语言）。

**AutoConfiguration.imports**：
Spring Boot 3.x 的自动装配清单文件。路径固定为 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`。本模块列出 4 个配置类：`CaptchaConfig`、`FilterConfig`、`I18nConfig`、`ResourcesConfig`，使得引入该模块即可自动装配全部 Web 层能力。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

# ruoyi-common-web Web基础设施模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-web 模块全部源码_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-web/src/main/java/)
  17 个 Java 类，覆盖 filter/、interceptor/、handler/、advice/、config/、core/ 六个包。任何关于「这个模块做了哪些 Web 层处理」的问题，最终答案在这些文件里。
- [代码: _XssFilter + XssHttpServletRequestWrapper_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-web/src/main/java/org/dromara/common/web/filter/)
  XSS 防护的双层实现：Filter 做路由决策（放行/拦截），Wrapper 用 Hutool 的 `HtmlUtil.cleanHtmlTag()` 清洗参数和 JSON body。
- [代码: _RepeatableFilter + RepeatedlyRequestWrapper_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-web/src/main/java/org/dromara/common/web/filter/)
  可重复读请求体的实现。`RepeatedlyRequestWrapper` 在构造时读取 `body = IoUtil.readBytes()` 缓存到 byte[]，后续 `getInputStream()` 每次都从缓存重新生成 ByteArrayInputStream。
- [代码: _FilterConfig.java_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-web/src/main/java/org/dromara/common/web/config/FilterConfig.java)
  Filter 注册配置类，通过 `@FilterRegistration` 声明 Filter 的 name、urlPatterns、order。XssFilter 声明 `order = HIGHEST_PRECEDENCE + 1`，RepeatableFilter 无显式 order，排在 XssFilter 之后。
- [代码: _GlobalExceptionHandler.java_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-web/src/main/java/org/dromara/common/web/handler/GlobalExceptionHandler.java)
  全局异常处理器，覆盖 16 种异常类型。核心模式：`log.error` 记录内部详情 + `R.fail()` 返回友好提示（内外有别）。
- [代码: _ResponseEnhancementAdvice.java_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-web/src/main/java/org/dromara/common/web/advice/ResponseEnhancementAdvice.java)
  实现 `ResponseBodyAdvice` 的响应增强切面。仅在 JSON 响应时调用 `JsonValueEnhancer.enhance(body)` 对字段值做增强处理。
- [官方文档: _Spring Boot Servlet Filter 注册_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/web/servlet.html#web.servlet.embedded-container)
  理解 `FilterRegistrationBean` / `@FilterRegistration` / `DispatcherType` / `order` 排序机制时查阅。
- [官方文档: _Hutool HTML 工具_ — Hutool（hutool.cn）](https://www.hutool.cn/docs/#/html/%E6%A6%82%E8%BF%B0)
  `HtmlUtil.cleanHtmlTag()` 的官方说明。XSS 清洗的核心工具方法。理解它过滤了哪些 HTML 标签和属性。
- [官方文档: _Spring MVC ResponseBodyAdvice_ — Spring（docs.spring.io）](https://docs.spring.org/spring-framework/reference/web/webmvc/mvc-controller/ann-advice.html)
  理解 `ResponseBodyAdvice` 接口的 `supports()` / `beforeBodyWrite()` 方法在响应写出前的切入时机。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「XSS 过滤误伤富文本」「请求体读取后为空」「验证码字体乱码」等问题时，Issues 与讨论区最贴近维护者意图。

## Gaps
- XSS 过滤对富文本编辑器的兼容方案（当前实现是全量清洗 HTML 标签，rich text 场景需要额外配置排除 URL）。
- 验证码图片的字体文件来源与跨平台兼容说明（当前代码依赖系统默认字体，未显式指定字体文件）。

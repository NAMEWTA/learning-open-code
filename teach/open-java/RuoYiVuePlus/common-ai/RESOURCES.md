# ruoyi-common-ai AI 模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _Snail AI Agent 使用文档_ — aizuda](https://aizuda.com/)
  本模块封装的 AI Agent 框架权威说明。理解 `@EnableSnailAiAgent` / `@EnableSnailAiOpenApi` / `SnailAiChatGatewayController` / `Result` 对象时查阅。本模块的一切都建立在它之上。
- [代码: _ruoyi-common-ai 模块_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-ai/src/main/java/org/dromara/common/ai/)
  `SnailAiConfig` / `SnailAiChatExceptionHandler`。任何关于「这个模块做了什么」的问题，最终答案在这两个文件里。
- [代码: _Snail AI Agent 自动配置注册文件_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-ai/src/main/resources/META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports)
  仅一行：`org.dromara.common.ai.config.SnailAiConfig`。Spring Boot 3.x 依赖此文件发现自动配置类，无需 `spring.factories`。
- [代码: _pom.xml 依赖声明_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-ai/pom.xml)
  三个 Snail AI starter + `ruoyi-common-core` 的精确依赖关系。理解模块组装方式时参考。
- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `AutoConfiguration.imports` / `@ConditionalOnProperty` / `@Enable*` 注解的机制时查阅。第 2 课的核心原理来源。
- [官方文档: _Spring 异常处理_ — Spring Framework（docs.spring.io）](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-exceptionhandler.html)
  理解 `@RestControllerAdvice` / `assignableTypes` / `@Order` 的机制时查阅。第 3 课的核心原理来源。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明。理解 AI 模块在整体架构中的位置时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么这样封装」「Snail AI 某版本行为变化」时，Issues 与讨论区最贴近维护者意图。
- [社区: _aizuda / Snail AI Agent GitHub_](https://github.com/aizuda/snail-ai-agent)
  Snail AI Agent 框架源码与 Issues。框架内部行为疑问时查阅。

## Gaps
- Snail AI Agent 官方文档链接可能需要确认最新域名（aizuda.com 为推测地址）。如有变动，以 Maven Central 上的 `com.aizuda` groupId 主页为准。
- 暂无其他显著缺口。所有 Success 项均可由仓库代码 + 上述官方文档支撑。

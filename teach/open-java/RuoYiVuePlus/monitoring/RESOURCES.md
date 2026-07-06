# Spring Boot Admin 监控 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-extend/ruoyi-monitor-admin/`）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _Spring Boot Admin 参考手册_ — codecentric（GitHub Pages）](https://codecentric.github.io/spring-boot-admin/current/)
  本模块的基石框架。涵盖 Server/Client 配置、安全保护、通知器（Notifier）体系、服务发现集成、Actuator 端点映射等全部官方功能说明。理解 `@EnableAdminServer` 的自动装配原理、`AbstractEventNotifier` 扩展点、以及所有 `spring.boot.admin.*` 配置项语义时查阅。是最高信任度的外部资料。

- [官方文档: _Spring Boot Actuator 参考手册_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/actuator/)
  SBA 的数据来源——所有监控指标（health、metrics、env、logfile、threaddump、heapdump 等）均由 Actuator 端点提供。理解 `management.endpoints.web.exposure.include='*'` 和 `management.endpoint.health.show-details=ALWAYS` 配置的含义、以及 SBA 如何通过 HTTP 调用这些端点收集数据时查阅。

- [官方文档: _Spring Security 架构与配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-security/reference/servlet/architecture.html)
  理解 `SecurityConfig.filterChain()` 中 `SecurityFilterChain`、`authorizeHttpRequests`、`formLogin`、`httpBasic` 的工作原理，以及 `PathPatternRequestMatcher`、`SavedRequestAwareAuthenticationSuccessHandler` 的用途。读懂 SecurityConfig 中「放行静态资源 + 其余需认证」的安全模型时查阅。

- [官方文档: _Project Reactor 参考指南_ — Project Reactor（projectreactor.io）](https://projectreactor.io/docs/core/release/reference/)
  `CustomNotifier.doNotify()` 返回 `Mono<Void>` 并使用 `Mono.fromRunnable()` 异步执行日志记录。理解 SBA 通知器体系基于 Reactor 响应式编程模型、`Mono` 的基本操作语义、以及 `doNotify` 方法的非阻塞设计意图时查阅。

- [官方源码: _Spring Boot Admin GitHub_ — codecentric（GitHub）](https://github.com/codecentric/spring-boot-admin)
  框架源码。`EnableAdminServer`、`AdminServerProperties`、`AbstractEventNotifier`、`InstanceEvent`、`InstanceStatusChangedEvent`、`StatusInfo` 等核心类的完整实现。遇到「SBA 内部是如何发现客户端的」「InstanceRepository 存储了什么」等深入问题时直接翻源码。

- [代码: _SecurityConfig.java_ — 本仓库](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-monitor-admin/src/main/java/org/dromara/monitor/admin/config/SecurityConfig.java)
  SBA 安全保护的第一现场。逐行展示了如何为 SBA 管理后台配置 Spring Security：放行静态资源与登录页、表单登录重定向、HTTP Basic 支持、CSRF 与 frameOptions 的禁用原因。任何「如何保护 SBA 管理后台」的问题，答案在这里。

- [代码: _CustomNotifier.java_ — 本仓库](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-monitor-admin/src/main/java/org/dromara/monitor/admin/notifier/CustomNotifier.java)
  自定义事件通知器的第一现场。展示了继承 `AbstractEventNotifier` 的标准模式、通过 `instanceof InstanceStatusChangedEvent` 过滤事件类型、以及将状态码映射为中文业务描述的 switch 表达式。任何「如何扩展 SBA 通知能力」的问题，答案在这里。

- [配置: _application.yml_ — 本仓库](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-monitor-admin/src/main/resources/application.yml)
  自注册监控模式的配置全景图。展示了 SBA Server（`spring.boot.admin.*`）与 SBA Client（`spring.boot.admin.client.*`）在同一应用中共存的所有配置项，包括 `context-path`、UI title、Actuator 端点暴露、客户端自注册 URL、`service-host-type: IP`、metadata 凭证传递等。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「SBA 管理后台无法访问」「客户端注册不上」「SecurityConfig 与框架自带安全冲突」等集成问题时，Issues 和讨论区是最贴近本仓库维护者意图的反馈源。

- [社区: _Spring Boot Admin GitHub Issues_](https://github.com/codecentric/spring-boot-admin/issues)
  SBA 框架本身的问题、feature request、版本升级兼容性讨论。遇到「SBA 3.x 迁移注意事项」「某 Actuor 端点不显示」「通知器不触发」等框架行为问题时查阅。维护者和核心贡献者活跃于此。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + Spring Boot Admin 官方文档 + Spring 官方文档支撑。
- 若后续需要扩展告警能力（邮件/钉钉/企业微信），可在 SBA 官方文档的「Notifications」章节找到标准扩展指南，本课程将其归入 Out of scope。

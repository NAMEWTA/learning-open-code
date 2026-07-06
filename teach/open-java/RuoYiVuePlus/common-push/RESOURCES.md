# ruoyi-common-push 消息推送模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充协议标准与 Spring 框架约定。

## Knowledge

- [代码: _ruoyi-common-push 模块 17 个文件_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-push/src/main/java/org/dromara/common/push/)
  全部课程内容的出处。任何关于「这个模块做了什么」的问题，最终答案在这 17 个 Java 文件里。重点关注 `core/`（会话管理器）、`config/`（条件装配）、`listener/`（Redis 订阅）三个子包。

- [代码: _PushPayloadDTO — 统一消息体_](RuoYi-Vue-Plus/ruoyi-api/src/main/java/org/dromara/system/api/domain/PushPayloadDTO.java)
  推送给前端的统一 JSON 结构。定义 `type` / `source` / `message` / `data` / `path` / `timestamp` 字段，是全模块消息的载体。理解「推什么」必读。

- [官方文档: _Spring Web MVC — Server-Sent Events_ — Spring（docs.spring.io）](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-async.html)
  理解 `SseEmitter` 的生命周期（`send` / `complete` / `onTimeout` / `onError`）和 `MediaType.TEXT_EVENT_STREAM` 响应头设定时查阅。第 2 课的核心原理来源。

- [官方文档: _Spring WebSocket 支持_ — Spring（docs.spring.io）](https://docs.spring.io/spring-framework/reference/web/websocket.html)
  理解 `WebSocketHandler` / `HandshakeInterceptor` / `WebSocketConfigurer` 的 Spring 抽象层。第 3 课和第 4 课的核心原理来源。

- [官方文档: _Spring Boot 条件装配_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html#features.developing-auto-configuration.condition-annotations)
  理解 `@Conditional` / `Condition` 接口 / `ConditionContext` 如何通过 `getEnvironment().getProperty()` 判断是否装配。第 4 课的核心原理来源。

- [官方文档: _MDN — Server-Sent Events_ — MDN（developer.mozilla.org）](https://developer.mozilla.org/zh-CN/docs/Web/API/Server-sent_events)
  前端接入 SSE 的 `EventSource` API。为帮助全栈学习者理解「后端 `SseEmitter` 发出的消息在前端长什么样」而列入。

- [官方文档: _MDN — WebSocket_ — MDN（developer.mozilla.org）](https://developer.mozilla.org/zh-CN/docs/Web/API/WebSocket)
  前端接入 WebSocket 的原生 API。为帮助全栈学习者对比 SSE 与 WebSocket 在前端的差异而列入。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「消息推送不生效」「SSE 连接频繁断开」「WebSocket 跨域配置」时，Issues 与讨论区最贴近维护者意图。

- [规范: _RFC 6455 — The WebSocket Protocol_](https://datatracker.ietf.org/doc/html/rfc6455)
  协议标准，仅在需要理解握手升级 / 帧格式 / CloseStatus 时查阅。日常开发不需要深入。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + Spring 官方文档 + MDN 前端文档支撑。

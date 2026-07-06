# Mission: 全面读懂 RuoYi-Vue-Plus 的 ruoyi-common-push 消息推送模块

## Why
学习者要能彻底读懂 `ruoyi-common-push` 这个公共模块：它通过 SSE（Server-Sent Events）和 WebSocket 双通道实现消息推送，用「条件 Bean 注册」按配置二选一激活，用 Redis Pub/Sub 实现集群跨节点投递。理解它，等于理解 RuoYi-Vue-Plus 如何用 Spring Boot 条件装配 + Redisson Pub/Sub 把两个推送协议统一成一个「PushSessionManager 接口 + PushHelper 工具类」的无感调用。达到能讲清「前端怎么建立连接、消息怎么传到目标用户、集群下消息怎么跨节点路由」并能照葫芦画瓢在业务中调用 `PushHelper` 推送消息的程度。重点是**读懂协议差异、装配策略、消息流转**，不是从零学 SSE/WebSocket 协议基础。

## Success looks like
- 能用一句话说清模块同时支持 SSE 和 WebSocket 的用意（双通道互斥选一），并能画出模块 17 个 Java 文件的分层结构图。
- 能解释 `@ConditionalOnMessageTransport` + `MessageTransportCondition` 的条件装配机制：注解如何声明期望传输方式、条件类如何读取 `message.transport` 配置、如何实现「SSE 配置类和 WebSocket 配置类只有一个会被激活」。
- 能讲清 SSE 通道的完整链路：`SseController.connect()` → `SseEmitterSessionManager.connect()` 建立连接 → 心跳定时器 `sseMonitor()` 维持连接 → `sendMessage()` 发送事件 → `onCompletion/onTimeout/onError` 自动清理。
- 能讲清 WebSocket 通道的完整生命周期：`PlusWebSocketInterceptor.beforeHandshake()` 提取登录信息 → `PlusWebSocketHandler.afterConnectionEstablished()` 注册会话 → `handleTextMessage()` 处理心跳/自定义消息 → `afterConnectionClosed()` 注销会话。
- 能完整追踪「业务发送消息 → 前端收到」的跨节点链路：`PushHelper.publishMessage()` → `PushSessionManager.publishMessage()` → `RedisUtils.publish(TOPIC)` → 集群各节点 `MessageTopicListener` 收到 → `PushSessionManager.sendMessage()` → 用户浏览器收到。
- 能说出 `PushHelper.isEnabled()` 的防御作用，以及 `PushSessionManager` 接口如何让 SSE 和 WebSocket 两个管理器拥有相同的 `publishMessage` / `sendMessage` / `subscribeMessage` 对外的口径。
- 能解释 SSE 和 WebSocket 各自的「顶替旧连接」逻辑：同一用户+同一 token，新连接会通过 `KICKED` 消息驱逐旧连接，SSE 靠 `emitters.remove(token)`、WS 靠 `sessions.remove(token)`。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会在每节课联系前端接入点（SSE 用 `EventSource`、WS 用浏览器原生 `WebSocket`）。
- 目标是「读懂并能正确调用」而非「能改消息通道底层」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- SSE 协议 RFC、WebSocket 协议 RFC 的底层帧格式、握手升级细节——仅讲 Spring 框架层面的使用。
- 前端 `EventSource` / `WebSocket` API 的完整用法——仅在「前端如何接入」处点到协议差异。
- Redis Pub/Sub 的底层实现、Redisson `RTopic` 的内部机制——已在 `2026-06-30-teach-ruoyi-redis` 课程覆盖，本课只接其订阅/发布两个 API。
- 业务模块里具体推送什么消息（如工作流审批通知、系统公告）——仅在举例时引用。

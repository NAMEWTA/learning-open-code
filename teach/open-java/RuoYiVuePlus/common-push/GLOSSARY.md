# ruoyi-common-push 消息推送模块 Glossary

记录学习者在 5 节课程中**真正理解**的核心术语。覆盖 SSE、WebSocket、条件装配、Redis Pub/Sub 跨节点推送四大块。

## Terms

**SSE（Server-Sent Events）**：
服务端单向推送的 HTTP 协议扩展。客户端用 `EventSource` 建立长连接，服务端用 `text/event-stream` 格式持续发送事件流。只支持文本、不支持二进制、连接断开自动重连。本模块用 Spring `SseEmitter` 实现。
_Avoid_: 「SSE 是轻量级 WebSocket」— 二者协议层不同，SSE 是 HTTP 长连接、WebSocket 是独立协议升级。

**WebSocket**：
全双工双向通信协议（RFC 6455）。通过 HTTP Upgrade 握手升级到 `ws://` 协议，后续帧收发不再走 HTTP。支持文本和二进制，无自动重连。本模块用 Spring `WebSocketHandler` 体系实现。

**SseEmitter**：
Spring MVC 提供的 SSE 发送器。本模块通过 `new SseEmitter(timeout)` 创建，用 `emitter.send(SseEmitter.event())` 发送事件，用 `onCompletion/onTimeout/onError` 回调清理连接。它是 `SseEmitterSessionManager` 中 `USER_TOKEN_EMITTERS` 的值类型。

**SseEmitterSessionManager**：
SSE 通道的会话管理器（`core/SseEmitterSessionManager.java`）。核心结构是 `Map<userId, Map<token, SseEmitter>>`。职责：① `connect()` 建立连接并驱逐同 token 旧连接；② 定时 `sseMonitor()` 心跳保活并清理失效连接；③ `sendMessage()` 向指定用户/全体用户的本地会话发送消息；④ `publishMessage()` 通过 Redis Pub/Sub 发布消息到集群。

**WebSocketSessionManager**：
WebSocket 通道的会话管理器（`core/WebSocketSessionManager.java`）。核心结构是 `Map<userId, Map<token, WebSocketSession>>`，接口和 `SseEmitterSessionManager` 几乎对称。职责：连接管理（`connect` / `disconnect`）、定时会话监控（`sessionMonitor`）、消息发送（`sendMessage`）、Redis 发布（`publishMessage`）、安全关闭（`closeSession`）。

**PushSessionManager（统一接口）**：
`core/PushSessionManager.java` 定义的推送接口，声明 `subscribeMessage` / `sendMessage` / `publishMessage` / `publishAll` 四个方法。`SseEmitterSessionManager` 和 `WebSocketSessionManager` 都实现它，使 `PushHelper` 可以用同一套 API 操作不同通道。
_Avoid_: 「推送管理器」（它是接口，不是具体实现）。

**@ConditionalOnMessageTransport**：
自定义条件注解（`annotation/ConditionalOnMessageTransport.java`），声明 `value()` 参数（"sse" 或 "websocket"）。底层用 `@Conditional(MessageTransportCondition.class)` 驱动。标注在配置类上，决定 `MessageSseConfiguration` 还是 `MessageWebSocketConfiguration` 生效。

**MessageTransportCondition**：
Spring `Condition` 接口实现（`condition/MessageTransportCondition.java`）。`matches()` 方法读取 `message.enabled` 和 `message.transport` 配置，与注解的 `value()` 比对，返回是否匹配。是两个通道配置类「谁生效」的裁决者。

**MessageAutoConfiguration**：
公共自动配置类（`config/MessageAutoConfiguration.java`），只做两件事：① `@ConditionalOnProperty(prefix="message", name="enabled")` 控制总开关；② `@EnableConfigurationProperties(MessageProperties.class)` 激活配置绑定。本身不注册任何推送 Bean，只是两个通道配置类的 `after` 前置依赖。

**MessageProperties**：
配置属性类（`properties/MessageProperties.java`），绑定 `message.*` 前缀。关键字段：`enabled`（总开关）、`transport`（sse/websocket）、`path`（访问路径）、`allowedOrigins`（跨域）、`sseTimeout`（SSE 超时 86400s）、`heartbeatInterval`（心跳间隔 60s）、`webSocketSendTimeLimit` 和 `webSocketBufferSizeLimit`。

**MessageConstants**：
模块常量接口（`constant/MessageConstants.java`）。定义关键常量：`MESSAGE_TOPIC = "global:message"`（Redis 消息主题）、`LOGIN_USER_KEY` / `LOGIN_TOKEN_KEY`（WebSocket attributes key）、`PING` / `PONG`（心跳标识）、`KICKED`（顶替旧连接通知）。

**Redis Pub/Sub 跨节点投递**：
集群消息分发的核心机制。`publishMessage()` 通过 `RedisUtils.publish(MESSAGE_TOPIC, dto)` 发布到 Redis，集群所有节点的 `MessageTopicListener`（启动时 `subscribeMessage`）收到后，调用 `sendMessage()` 投递给本节点在线的目标用户。

**MessageTopicListener**：
Redis 消息监听器（`listener/MessageTopicListener.java`）。实现 `ApplicationRunner` + `Ordered(-1)`，在项目启动最早期通过 `pushSessionManager.subscribeMessage()` 注册消费者。收到消息后判断：`userIds` 非空则逐一发送 → `sendMessage(userId, payload)`；`userIds` 为空则全局广播 → `sendMessage(payload)`。

**PushHelper**：
业务层调用入口（`helper/PushHelper.java`）。全静态方法、私有构造函数，是典型的工具类。核心方法：`sendMessage(userId, message)` 单发、`sendMessage(message)` 广播、`publishMessage(userIds, payload)` 发布。内嵌 `isEnabled()` 兜底检查，通过 `SpringUtils.getBean(PushSessionManager.class)` 获取当前激活的管理器。

**PushDTO**：
推送数据传输对象（`dto/PushDTO.java`）。包含 `userIds`（目标用户列表，空=广播）和 `payload`（`PushPayloadDTO`）。提供 `of(userIds, payload)` 和 `broadcast(payload)` 两个静态工厂方法。

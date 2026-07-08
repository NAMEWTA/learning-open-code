# L2-slice-openapi-client-example 资源

## 知识

- [示例工程 POM](../../../../open-java/snail-ai/snail-ai-agent-example/pom.xml)
  判断 `snail-ai-agent-example` 是独立 Spring Boot 示例应用，依赖 `snail-ai-openapi-starter`，不在父 reactor `modules` 中。
- [示例工程启动类](../../../../open-java/snail-ai/snail-ai-agent-example/src/main/java/com/aizuda/snail/ai/agent/example/SnailAiAgentExampleApplication.java)
  确认示例工程同时扮演 Agent Client，使用 `@EnableSnailAiAgent` 接入 Server gRPC 分发。
- [OpenApiDemoController](../../../../open-java/snail-ai/snail-ai-agent-example/src/main/java/com/aizuda/snail/ai/agent/example/controller/OpenApiDemoController.java)
  本主题的示例入口，展示 `/demo/**` 如何注入 `OpenApiChatClient` 并转发同步/流式 chat。
- [示例工程 application.yml](../../../../open-java/snail-ai/snail-ai-agent-example/src/main/resources/application.yml)
  OpenAPI SDK、Agent Client、Server HTTP/gRPC 端口、认证凭证和超时配置的集中来源。
- [OpenAPI SDK 自动配置](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-openapi/snail-ai-openapi-starter/src/main/java/com/aizuda/snail/ai/openapi/client/starter/SnailAiOpenApiAutoConfiguration.java)
  确认 `snail-ai.openapi.enabled=true` 后如何创建 HTTP client、各类 OpenAPI client 代理和 `SnailAiOpenApi` 门面。
- [SnailAiOpenApi 门面](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-openapi/snail-ai-openapi-core/src/main/java/com/aizuda/snail/ai/openapi/client/core/SnailAiOpenApi.java)
  Fluent Builder 入口，说明当前源码中 `stream()` 返回 `Flux<OpenApiChatStreamEvent>`，`execute()` 会检查 `Result.status`。
- [OpenApiChatClient](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-openapi/snail-ai-openapi-core/src/main/java/com/aizuda/snail/ai/openapi/client/core/api/OpenApiChatClient.java)
  SDK 类型化接口，映射 Server 的流式和同步 chat 路径。
- [OpenApiHttpInvokeHandler](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-openapi/snail-ai-openapi-core/src/main/java/com/aizuda/snail/ai/openapi/client/core/rpc/OpenApiHttpInvokeHandler.java)
  本主题核心源码，覆盖 base URL 拼接、认证头注入、普通 HTTP 解析、SSE 读取与错误分支。
- [OpenAPI Server chat 入口](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/controller/OpenApiChatController.java)
  SDK 最终命中的 Server Controller，确认 `text/event-stream` 与 `Result<OpenApiChatSyncResponse>` 边界。
- [OpenAPI 认证拦截器](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/interceptor/OpenApiAuthInterceptor.java)
  Server 侧认证头校验、应用缓存、启用状态和 token 常量时间比较的一手来源。
- [OpenAPI Chat DTO](../../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/openapi/dto/OpenApiChatRequest.java)
  请求字段与校验约束；对照示例工程可发现 `conversationId` 当前在源码上是必填。
- [OpenAPI stream event DTO](../../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/openapi/dto/OpenApiChatStreamEvent.java)
  `text`、`thinking`、`done`、`error` 事件类型和 data 结构。
- [OpenAPI sync response DTO](../../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/openapi/dto/OpenApiChatSyncResponse.java)
  同步 chat 成功响应只包含 `conversationId`、`content`、`durationMs`。
- [OpenAPI 官方文档：认证方式](../../../../open-java/snail-ai/docs/api/openapi/auth.md)
  认证头、凭证获取和常见认证错误的文档来源。
- [OpenAPI 官方文档：对话接口](../../../../open-java/snail-ai/docs/api/openapi/chat.md)
  与 Server chat 端点相关的文档来源；阅读时需要对照源码校正 SSE 与 `conversationId` 细节。
- [OpenAPI SDK 指南](../../../../open-java/snail-ai/docs/guide/client/openapi-sdk.md)
  SDK 设计意图、配置项与集成架构说明；阅读时需要注意当前源码没有 `listener(...)` Builder 方法。
- [已有 L2：OpenAPI chat 垂直切片](../slice-openapi-chat/)
  Server 侧 OpenAPI chat 到 Agent 链、gRPC Client 和 writer 行为的已有切片，可作为本主题后半段的边界参考。

## 智慧（社区）

- 当前未收录外部社区。本主题是源码考古和集成排错型切片，最高可信反馈来自运行示例工程、对照 Server 日志、观察 SDK Debug 日志和复核已有 `slice-openapi-chat`。

## 空白

- 仓库内未找到专门覆盖 `snail-ai-agent-example` 的自动化集成测试，因此示例 Controller、SDK 代理和 Server OpenAPI 之间的行为以当前源码为准。
- 文档中的部分 OpenAPI SDK 示例与当前源码存在差异，未来如果补充测试或修正文档，需要同步更新本主题。

# L2-slice-openapi-chat 资源

## 知识

- [OpenAPI Chat Controller](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/controller/OpenApiChatController.java)
  OpenAPI chat 的 HTTP 入口，确认流式端点、同步端点和 `ServerSentEvent` 映射方式。
- [OpenAPI Chat Service](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/service/OpenApiChatService.java)
  本切片核心来源，覆盖 `OpenApiChatRequest` 到 `AgentChatCommand` 的转换、虚拟线程、Flux bridge、同步 collector 和 300 秒超时。
- [OpenAPI Auth Interceptor](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/interceptor/OpenApiAuthInterceptor.java)
  认证头、应用缓存、启用状态校验、常量时间 token 比较和 ThreadLocal 会话写入的一手来源。
- [OpenAPI DTOs](../../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/openapi/dto/OpenApiChatRequest.java)
  请求与响应 DTO 的字段契约，配合 `OpenApiChatStreamEvent`、`OpenApiChatSyncResponse` 阅读。
- [Agent 责任链 L1 主题](../module-agent-chain/)
  已有 L1 课程，帮助把 OpenAPI 服务转换后的 `AgentChatCommand` 放回 Server 端责任链。
- [Agent Client L1 主题](../module-agent-client/)
  已有 L1 课程，帮助理解 `/chat/dispatch` 到 Client 模型执行、Advisor、usage 收集的边界。
- [Commons gRPC L1 主题](../module-commons-grpc/)
  已有 L1 课程，提供 `ChatDispatchRequest`、`ChatStreamResponse`、`UriConstants.CHAT_DISPATCH` 和 gRPC 信封的上下文。
- [OpenAPI Java Client](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-openapi/snail-ai-openapi-core/src/main/java/com/aizuda/snail/ai/openapi/client/core/api/OpenApiChatClient.java)
  SDK 侧调用接口，配合 `OpenApiHttpInvokeHandler` 阅读认证头注入、SSE 解析和超时设置。

## 智慧（社区）

- 当前未收录外部社区。本主题是源码考古型切片，最高可信反馈来自在本仓库运行接口、阅读日志和对照现有 L1 主题复核链路。

## 空白

- 仓库内未找到专门描述 OpenAPI chat 流式协议的设计文档，因此端点、事件类型、错误边界和 usage 边界都以当前源码为准。
- 未覆盖线上部署网关、反向代理和浏览器 EventSource 兼容性；这些需要结合实际运行环境补充。

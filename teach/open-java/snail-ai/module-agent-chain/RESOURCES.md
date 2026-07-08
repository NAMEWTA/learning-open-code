# Agent 责任链模块资源

## 知识

- [官方架构说明：`docs/architecture/agent-chain.md`](../../../open-java/snail-ai/docs/architecture/agent-chain.md)
  项目内对 Agent 责任链阶段、Server/Client 边界和扩展点的官方说明。适用于建立模块地图，并与当前源码排序做对照。
- [`AgentChatHandler.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/AgentChatHandler.java)
  Server 端 Handler 的最小接口。适用于理解责任链扩展点和短路语义。
- [`AgentChatContext.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/AgentChatContext.java)
  Handler 间流转的数据载体。适用于判断每个阶段读写哪些上下文字段。
- [`AgentChatChainService.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/agent/AgentChatChainService.java)
  当前源码中的链路执行器。适用于确认 Spring 注入有序 Handler 列表后的实际执行方式。
- [`LlmCallHandler.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/LlmCallHandler.java)
  Server 端责任链终点。适用于理解 `AgentChatContext` 如何被组装成 `ChatDispatchRequest` 并通过 gRPC 分发到 Client。
- [`ChatStreamObserver.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/ChatStreamObserver.java)
  gRPC 流式响应到 HTTP/SSE 输出与异步持久化的桥接点。适用于理解回调和持久化边界。
- [`WebSearchHandler.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/WebSearchHandler.java)
  主链边缘 Handler：按 Agent 开关注入 Tavily 联网搜索工具回调。适用于理解未注册扩展点与 `toolCallbacks` 字段。
- [`ConversationCreateCallbackHandler.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/callback/ConversationCreateCallbackHandler.java)
  Client gRPC 回调：创建会话并保存用户消息。适用于对比 `ConversationHandler` 的同步主链持久化。
- [`ConversationRecordCallbackHandler.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/callback/ConversationRecordCallbackHandler.java)
  Client gRPC 回调：保存单条对话记录。适用于对比 `ChatResultPersistService` 的流结束后持久化。
- [`GrpcRequestHandler.java`](../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-grpc/src/main/java/com/aizuda/snail/ai/common/grpc/handler/GrpcRequestHandler.java)
  回调 Handler 最小接口。适用于理解 `supports` + `handle` 路由契约。
- [`GrpcRequestDispatcher.java`](../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-grpc/src/main/java/com/aizuda/snail/ai/common/grpc/handler/GrpcRequestDispatcher.java)
  Server/Client 共用的 gRPC unary 分发器。适用于追踪回调 URI 如何落到具体 Handler。
- [`RpcClient.java`](../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-common/src/main/java/com/aizuda/snail/ai/agent/common/rpc/RpcClient.java)
  Client 侧回调接口声明（`@Mapping` 注解驱动动态代理）。适用于理解回调触发入口。
- [`GrpcClientInvokeHandler.java`](../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-common/src/main/java/com/aizuda/snail/ai/agent/common/rpc/GrpcClientInvokeHandler.java)
  `RpcClient` 动态代理实现：序列化 DTO、发送 unary gRPC、校验 `status`、重试。适用于理解 Client→Server 回调传输层。
- [`ConversationCreateRequest.java`](../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/dto/agent/ConversationCreateRequest.java)
  会话创建回调的请求 DTO。
- [`ConversationRecordRequest.java`](../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/dto/agent/ConversationRecordRequest.java)
  单条记录回调的请求 DTO（含 token 字段，但回调 Handler 当前未全部写入）。
- [`WebSearchTool.java`](../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/websearch/WebSearchTool.java)
  Tavily 联网搜索 Spring AI `@Tool` 实现，由 `WebSearchHandler` 实例化注入。

## 智慧（社区）

- [Snail AI Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  当前子模块来源。适用于查看 issue、提交记录和版本差异。
- [Snail AI GitHub 镜像](https://github.com/aizuda/snail-ai)
  README 中给出的 GitHub 入口。适用于检索讨论、PR 与社区反馈。

## 空白

暂无专门解释 `snail-ai-feature-agent` 责任链演进历史的设计讨论串；后续若要追踪 order 变更原因，需要结合 git log 和 issue 继续考古。

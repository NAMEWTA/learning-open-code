# L2-slice-admin-agent-chat 资源

## 知识

- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/AgentController.java`
  Admin 智能体聊天 HTTP/SSE 入口，包含 `POST /agent/{id}/chat`、`@LoginRequired(role = USER)`、`FluxBridgeChatStreamWriter`。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/interceptor/AuthenticationInterceptor.java`
  Admin 登录态认证来源，说明 `Snail-Ai-Auth` 如何写入 `UserSessionUtils`。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/agent/AgentChatService.java`
  从 `AgentChatCommand` 创建 `AgentChatContext` 并启动责任链。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/agent/AgentChatChainService.java`
  Spring 注入 `List<AgentChatHandler>` 后逐个执行，是理解 Handler 顺序和短路边界的入口。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/*.java`
  Server 端 Agent 责任链核心。用于确认初始化、会话、模型、MCP、system prompt、RAG、Skill、上下文收集和 gRPC 分发顺序。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/stream/ChatStreamWriter.java`
  责任链到 HTTP/SSE 的输出端口。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/persist/ChatResultPersistService.java`
  completion 后保存助手消息、短期记忆和每日 usage 统计的边界。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/dto/agent/ChatDispatchRequest.java`
  Server 下发给 Agent Client 的核心 DTO，串起 Agent、模型、MCP、Skill、历史、system prompt 和 server 端口。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/dto/agent/ChatStreamResponse.java`
  Client 回传 text、thinking、completion、error 的统一流式响应 DTO。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-grpc/src/main/java/com/aizuda/snail/ai/common/grpc/constant/UriConstants.java`
  gRPC 业务路由常量，Admin 对话分发使用 `/chat/dispatch`。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/grpc/handler/ChatDispatchStreamingHandler.java`
  Agent Client 端 `/chat/dispatch` 的 server-streaming 处理器。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/runtime/ChatSessionRuntime.java`
  Client 单次会话运行壳，负责活跃计数、工具解析、执行和清理。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/executor/ClientChatExecutor.java`
  Client 流式模型调用入口，使用 Reactor context、Spring AI `ChatClient` 和 Advisor context。
- `teach/open-java/snail-ai/module-server-entry/`
  L1 Server 入口主题，提供 Admin/OpenAPI 入口边界与认证背景。
- `teach/open-java/snail-ai/module-agent-chain/`
  L1 Agent 责任链主题，提供 Handler 顺序、上下文和持久化边界。
- `teach/open-java/snail-ai/module-agent-client/`
  L1 Agent Client 主题，提供 Client gRPC、工具、Advisor 和模型执行层背景。
- `teach/open-java/snail-ai/module-commons-grpc/`
  L1 Commons/gRPC 主题，提供统一信封、URI、handler dispatcher 和双向 RPC 背景。

## 智慧（社区）

本主题未纳入外部社区资料。当前目标是基于本地源码生成可审计的纵向切片教学产物，外部 issue 或讨论容易混入版本差异；后续如果要排查真实部署问题，再补充对应版本的上游 issue、PR 和运行日志。

## 空白

- 未覆盖 Admin 前端如何发起该 SSE 请求。原因：用户指定的 L2 目标聚焦 Java 后端和 Agent Client 纵向路径。
- 未覆盖 OpenAPI `agent/chat` 流式接口。原因：该路径有独立认证、外部用户映射和同步/异步差异，适合单独开 L2 切片。
- 未覆盖模型厂商适配层内部。原因：本主题只追踪到 Client 端 `ChatClient` 流式执行和 usage 采集边界。

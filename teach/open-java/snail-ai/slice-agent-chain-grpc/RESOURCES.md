# Agent 责任链到 gRPC 分发资源

## 知识

- [Agent 责任链 L1](../module-agent-chain/lessons/0001-agent-chain-module-tour.html)
  用于复习 Server 端 `AgentChatHandler` 顺序、`AgentChatContext` 共享状态和 `LlmCallHandler` 边界。
- [Commons 与 gRPC L1](../module-commons-grpc/lessons/0001-commons-grpc-module-tour.html)
  用于复习统一 gRPC 信封、URI 路由、feature-common 心跳注册和 Client 消费边界。
- [Agent Client L1](../module-agent-client/lessons/0001-agent-client-module-tour.html)
  用于复习 Client gRPC server、`ChatDispatchStreamingHandler`、`ChatSessionRuntime` 和流式回传阶段。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/AgentChatContext.java`
  本切片的 Server 端共享状态载体；用于确认哪些字段由 Handler 写入，哪些字段最终进入分发 DTO。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/LlmCallHandler.java`
  Server 端分发终点；用于确认 `ChatDispatchRequest` 构造、`UriConstants.CHAT_DISPATCH` 和 `GrpcChannelUtil.sendServerStreaming` 调用。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/ContextCollectorHandler.java`
  目标 Client 选择、短期历史加载和 Client 不在线错误的关键来源。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/dto/agent/ChatDispatchRequest.java`
  Server 到 Client 的业务 DTO，一次对话分发的 Agent、模型、MCP、Skill、历史和 prompt 都在这里落形。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-grpc/src/main/proto/snail_ai_grpc_service.proto`
  gRPC 统一请求/响应信封的一手定义；用于区分 proto 字段与业务 JSON DTO 字段。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-grpc/src/main/java/com/aizuda/snail/ai/common/grpc/client/GrpcChannelUtil.java`
  Server 发起 unary/server-streaming 调用的桥接工具；用于确认 metadata、reqId、method descriptor 和默认 CallOptions。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/grpc/handler/ChatDispatchStreamingHandler.java`
  Client 端消费 `/chat/dispatch` 的核心 handler；用于确认 JSON 解析、runtime 调用和四类流式响应。

## 智慧（社区）

- [Snail AI Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  项目真实协作入口；适用于核对 issue、提交历史和 Server/Client 分发契约的演进。
- [Snail AI GitHub 镜像](https://github.com/aizuda/snail-ai)
  README 给出的镜像入口；适用于检索公开讨论和对照社区反馈。
- 本地源码评审：`open-java/snail-ai`
  当前课程以工作区实际 checkout 为准；当文档与源码不一致时，优先回到源码、pom 和生成类核对。

## 空白

- 当前未发现覆盖 `LlmCallHandler -> GrpcChannelUtil -> ChatDispatchStreamingHandler` 的端到端测试；本切片的判断主要来自源码阅读。
- 当前未发现专门说明 `/chat/dispatch` server-streaming 超时策略的设计文档；源码中 `sendServerStreaming` 使用 `CallOptions.DEFAULT`，需要把超时判断放到调用方、channel、网络或上层网关排查。

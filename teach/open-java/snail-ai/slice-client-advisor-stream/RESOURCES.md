# Client Advisor 流式处理资源

## 知识

- [源码：<code>ChatDispatchStreamingHandler</code>](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/grpc/handler/ChatDispatchStreamingHandler.java)
  Client gRPC 流式入口，定义 text、thinking、completion、error 如何封装成 <code>ChatStreamResponse</code> 并通过 <code>StreamObserver</code> 回写。
- [源码：<code>ChatSessionRuntime</code>](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/runtime/ChatSessionRuntime.java)
  单次会话运行时，负责 active count、工具解析、completion/error 后的 <code>ToolResolution</code> cleanup。
- [源码：<code>ActiveChatCounter</code>](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-common/src/main/java/com/aizuda/snail/ai/agent/common/counter/ActiveChatCounter.java)
  Agent 实例级活跃会话计数器，提供 <code>increment()</code>、<code>decrement()</code> 和 <code>get()</code>。
- [源码：<code>PingRequestHandler</code>](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/grpc/handler/PingRequestHandler.java)
  Ping 响应读取 <code>activeChatCounter.get()</code> 并返回 <code>activeChats</code>，用于观察当前 Client 的活跃会话数。
- [源码：<code>ClientHeartbeatScheduler</code>](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-common/src/main/java/com/aizuda/snail/ai/agent/common/handler/ClientHeartbeatScheduler.java)
  心跳 body 携带最大并发数和当前 <code>activeChats</code>，让 Server 周期性看到 Client 负载。
- [源码：<code>ClientChatExecutor</code>](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/executor/ClientChatExecutor.java)
  Client 侧流式执行引擎，创建 <code>ClientStreamExecutionContext</code>，把消费者和状态写入 Advisor context，并订阅模型流。
- [源码目录：Advisor 链](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/advisor)
  覆盖 <code>InterceptorChainAdvisor</code>、<code>TokenUsageCollectorAdvisor</code>、<code>ThinkingCollectorAdvisor</code>、<code>StreamChunkForwarderAdvisor</code> 与上下文 key/order。
- [源码：<code>DefaultChatClientFactory</code>](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/executor/client/DefaultChatClientFactory.java)
  展示模型、工具调用 Advisor、默认工具和自定义器如何装配进 Spring AI <code>ChatClient</code>。
- [源码：<code>DefaultPromptFactory</code>](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/executor/prompt/DefaultPromptFactory.java)
  展示系统提示词、历史消息和用户消息如何组成 <code>Prompt</code>。
- [源码：<code>ChatStreamResponse</code>](../../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/dto/agent/ChatStreamResponse.java)
  四类流式响应 DTO：<code>text</code>、<code>thinking</code>、<code>completion</code>、<code>error</code>。
- [测试：<code>ThinkingCollectorAdvisorTest</code>](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/test/java/com/aizuda/snail/ai/agent/core/advisor/ThinkingCollectorAdvisorTest.java)
  验证 <code>reasoningContent</code> metadata 可以进入 thinking consumer 并累积到 <code>ClientStreamExecutionContext</code>。
- [源码：Server <code>ChatStreamObserver</code>](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/ChatStreamObserver.java)
  Server 侧接收 Client 回写后的分发逻辑，用于理解 completion 持久化和前端流转发落点。
- [本地文档：Advisor 处理流水线](../../../../open-java/snail-ai/docs/guide/client/advisor-pipeline.md)
  项目文档中的流水线说明，适合作为概念背景；具体课程以当前源码装配为准。
- [本地文档：客户端日志](../../../../open-java/snail-ai/docs/guide/client/logging.md)
  调试 Token usage、thinking 和日志拦截器时的背景资料。

## 智慧（社区）

- [Snail AI 源码仓库 Issue 区](https://github.com/aizuda/snail-ai/issues)
  适用于核对当前开源版本中流式输出、usage 统计、模型兼容字段和 MCP 工具清理相关的真实问题。
- [Spring AI 官方文档](https://docs.spring.io/spring-ai/reference/)
  适用于进一步查阅 <code>ChatClient</code>、<code>Advisor</code>、streaming 和 tool calling 的框架语义。

## 空白

- 目前未找到本仓库内针对 <code>ChatDispatchStreamingHandler</code> 全链路、observer 写回失败、请求解析失败的专项测试；本主题用源码切片和现有 <code>ThinkingCollectorAdvisorTest</code> 作为局部验证参考。

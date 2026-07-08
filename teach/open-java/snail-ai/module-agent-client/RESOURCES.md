# Agent Client 执行层模块资源

## 知识

- [L0 项目地图](../00-overview/lessons/0001-project-map.html)
  用于确认 Snail AI 的 Server-Agent 总体分层、顶层 Maven 模块和后续 L1 主题关系。
- [Agent 责任链模块导览](../module-agent-chain/lessons/0001-agent-chain-module-tour.html)
  用于衔接 Server 端 `LlmCallHandler` 到 Client gRPC 边界，避免把 Server Handler 与 Client Advisor 混在一起。
- `open-java/snail-ai/docs/guide/client/index.md`
  官方客户端模式说明，解释为什么 LLM 调用和工具执行放在 Agent Client 节点。
- `open-java/snail-ai/docs/guide/client/config.md`
  客户端配置项参考，对照 `SnailAiAgentProperties` 和示例 `application.yml` 使用。
- `open-java/snail-ai/docs/guide/client/interceptor.md`
  `SnailAiInterceptor` 扩展机制说明，对照当前 `InterceptorChainAdvisor` 与 `SnailAiInterceptorChain` 源码阅读。
- `open-java/snail-ai/docs/guide/client/tools.md`
  本地工具执行说明，对照 `ToolRuntime`、各 `Client*ToolResolver` 和 `CustomToolCallbackProvider` 阅读。
- `open-java/snail-ai/docs/guide/client/advisor-pipeline.md`
  Advisor 流水线文档；阅读时需以当前源码为准，因为自动配置中实际默认装配 4 个 Client Advisor。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-common/src/main/java/com/aizuda/snail/ai/agent/common`
  Client 配置、上下文、gRPC server/client callback、心跳注册和活跃对话计数的源码入口。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core`
  Client 请求分发、会话运行时、Chat 执行器、Advisor、Interceptor、Tool resolver 和内置 Tool 的源码入口。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-model/src/main/java/com/aizuda/snail/ai/agent/core/executor/model`
  Client 侧 `ModelConfig` 到 `ChatModelSpec`、`ChatModelRuntime` 的适配入口。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-starter/src/main/java/com/aizuda/snail/ai/agent/starter`
  `@EnableSnailAiAgent` 与自动配置源码入口，适合从 Bean 装配顺序理解整个模块。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-chat/snail-ai-agent-chat-api/src/main/java/com/aizuda/snail/ai/agent/chat/api`
  嵌入式 Chat 会话模型、`SnailAiChatProperties`、`@SnailAiChatAuthorize` 与凭证校验 SPI。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-chat/snail-ai-agent-chat-starter/src/main/java/com/aizuda/snail/ai/agent/chat/starter`
  Chat BFF 网关 `SnailAiChatGatewayController`、JWT 拦截器与自动配置。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-openapi/snail-ai-openapi-core/src/main/java/com/aizuda/snail/ai/openapi/client/core/api`
  `OpenApi*Client` 声明式接口与 `@OpenApiMapping` 注解。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-openapi/snail-ai-openapi-starter/src/main/java/com/aizuda/snail/ai/openapi/client/starter`
  `@EnableSnailAiOpenApi` 与 OpenAPI HTTP 客户端自动配置。
- `open-java/snail-ai/docs/guide/client/index.md` 与 `open-java/snail-ai/docs/guide/client/openapi-sdk.md`
  官方客户端与 OpenAPI SDK 接入说明；与 `reference/agent-client-api.html` 对照阅读。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/test/java/com/aizuda/snail/ai/agent/core/advisor/ThinkingCollectorAdvisorTest.java`
  当前模块少量直接测试之一，用于验证 thinking metadata 被收集到 `ClientStreamExecutionContext` 和回调消费者。

## 智慧（社区）

- [Snail AI Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  项目真实协作入口；适用于核对 Issue、提交源码疑问和观察客户端模块演进。
- 本地源码评审：`open-java/snail-ai` 子模块
  当前课程以工作区实际 checkout 为准；当文档与源码不一致时，优先回到源码和测试验证。

## 空白

- 当前未发现覆盖 `ChatSessionRuntime`、`ToolRuntime`、`DefaultChatClientFactory` 的完整单元测试；后续学习 L2/L3 时需要更多依赖源码和手工调用链验证。
- 官方客户端 Advisor 文档提到的 5 级流水线与当前自动配置源码存在差异；本主题会显式标注差异，不把文档描述直接当作当前实现。

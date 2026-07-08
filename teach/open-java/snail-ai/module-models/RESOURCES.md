# 模型适配层模块资源

## 知识

### Server feature-model（配置与基础设施）

- [snail-ai-feature-model POM](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/pom.xml)
  Server 模型 feature 的 Maven 边界；依赖三类 model-starter 与 spring-ai 组件。
- [CryptoHelper.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/src/main/java/com/aizuda/snail/ai/model/crypto/CryptoHelper.java)
  SM4 加解密 API Key；配置项 `snail-ai.crypto.secret-key` / `iv`。
- [ModelScopeEnum.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/src/main/java/com/aizuda/snail/ai/model/enums/ModelScopeEnum.java)
  模型作用域：GLOBAL / PERSONAL。
- [ModelStatusEnum.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/src/main/java/com/aizuda/snail/ai/model/enums/ModelStatusEnum.java)
  模型启用状态：ENABLED(1) / DISABLED(0)。
- [AiModelUsageService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/src/main/java/com/aizuda/snail/ai/model/service/AiModelUsageService.java)
  模型使用统计 SPI；由 admin 实现。

### snail-ai-models（适配器 SPI 与模块）

- [模型聚合 POM](../../../../open-java/snail-ai/snail-ai-models/pom.xml)
  定义 `snail-ai-model-common`、Chat、Embedding、Rerank 四个聚合入口。适用于判断模型模块的 Maven 边界。
- [ModelAdapterDefaults.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-common/src/main/java/com/aizuda/snail/ai/model/common/ModelAdapterDefaults.java)
  记录默认 `adapterKey`、模型类型常量和默认 descriptor。适用于理解未显式配置 adapter 时的回退规则。
- [ModelAdapterDescriptor.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-common/src/main/java/com/aizuda/snail/ai/model/common/ModelAdapterDescriptor.java)
  管理端可展示的 adapter 元数据。适用于理解 adapter 列表如何按能力过滤。
- [ChatModelRuntime.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-chat/snail-ai-model-chat-core/src/main/java/com/aizuda/snail/ai/model/chat/ChatModelRuntime.java)
  Chat 模型运行时选择器。适用于学习 `Spec -> adapterKey -> Adapter -> ChatModel` 的核心流程。
- [OpenAiCompatibleChatModelAdapter.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-chat/snail-ai-model-chat-provider-openai-compatible/src/main/java/com/aizuda/snail/ai/model/chat/openai/OpenAiCompatibleChatModelAdapter.java)
  OpenAI-compatible Chat provider。适用于理解 `ConfigExtAttrsDTO` 如何映射到 `OpenAiChatOptions`。
- [EmbeddingModelRuntime.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-embedding/snail-ai-model-embedding-core/src/main/java/com/aizuda/snail/ai/model/embedding/EmbeddingModelRuntime.java)
  Embedding 模型运行时选择器。适用于对照 Chat 线识别三类能力的统一模式。
- [OpenAiCompatibleEmbeddingModelAdapter.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-embedding/snail-ai-model-embedding-provider-openai-compatible/src/main/java/com/aizuda/snail/ai/model/embedding/openai/OpenAiCompatibleEmbeddingModelAdapter.java)
  OpenAI-compatible Embedding provider。适用于理解维度、编码格式、超时和重试配置。
- [RerankModelRuntime.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-rerank/snail-ai-model-rerank-core/src/main/java/com/aizuda/snail/ai/model/rerank/RerankModelRuntime.java)
  Rerank 客户端运行时选择器。适用于理解 Rerank 与 Chat/Embedding 的返回类型差异。
- [QwenRerankModelAdapter.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-rerank/snail-ai-model-rerank-provider-qwen/src/main/java/com/aizuda/snail/ai/model/rerank/http/QwenRerankModelAdapter.java)
  Qwen HTTP rerank provider。适用于理解 `/rerank` 路径、RestClient、返回结果解析和失败降级。
- [ServerModelFacade.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/src/main/java/com/aizuda/snail/ai/model/adapter/server/ServerModelFacade.java)
  Server 侧统一构建门面。适用于观察 Server 如何调用 Chat、Embedding、Rerank 三条 runtime。
- [DefaultChatModelFactory.java](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-model/src/main/java/com/aizuda/snail/ai/agent/core/executor/model/DefaultChatModelFactory.java)
  Agent Client 侧 Chat 模型工厂。适用于理解下发配置如何在客户端构建 ChatModel。
- [ChatModelAdapter.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-chat/snail-ai-model-chat-core/src/main/java/com/aizuda/snail/ai/model/chat/ChatModelAdapter.java)
  Chat provider SPI：`adapterKey()` + `create(ChatModelSpec)`。
- [EmbeddingModelAdapter.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-embedding/snail-ai-model-embedding-core/src/main/java/com/aizuda/snail/ai/model/embedding/EmbeddingModelAdapter.java)
  Embedding provider SPI。
- [RerankModelAdapter.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-rerank/snail-ai-model-rerank-core/src/main/java/com/aizuda/snail/ai/model/rerank/RerankModelAdapter.java)
  Rerank provider SPI；返回 `RerankApiClient`。
- [OpenAiChatModel.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-chat/snail-ai-model-chat-core/src/main/java/org/springframework/ai/openai/OpenAiChatModel.java)
  项目内 fork 的 Spring AI Chat 实现；含 `extraBody`、`ChunkMerger`、tool call 扩展。
- [OpenAiChatModelChunkMergerTest.java](../../../../open-java/snail-ai/snail-ai-models/snail-ai-model-chat/snail-ai-model-chat-core/src/test/java/org/springframework/ai/openai/OpenAiChatModelChunkMergerTest.java)
  验证流式合并后 `reasoning_content` 附加属性保留。

## 智慧（社区）

- 当前主题暂不引入外部社区材料；以本工作区源码、L0 总览和后续源码审查记录作为主要反馈来源。

## 空白

- 未检索外部 Issue、PR 或社区讨论。若后续分析 provider 兼容性缺陷，应补充对应讨论或修复链接。
- 当前只覆盖 L1 模块边界；完整 Chat 流式响应、工具调用、RAG 调用 embedding/rerank 的运行时链路留给后续切片。

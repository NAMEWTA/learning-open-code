# L2-slice-model-runtime 资源

## 知识

- [ModelResolveHandler](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/ModelResolveHandler.java)
  Agent 责任链中选择 Chat 模型、缺省模型、加载失败并终止输出的一手来源。
- [DispatchModelConfigAssembler](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/src/main/java/com/aizuda/snail/ai/model/adapter/server/DispatchModelConfigAssembler.java)
  当前真实源码位置；负责把 Server 侧模型配置解密并组装为 `ChatDispatchRequest.ModelConfig`。
- [ModelRuntimeHandler](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/src/main/java/com/aizuda/snail/ai/model/service/ModelRuntimeHandler.java)
  Server 本地 Chat、Embedding、Rerank 统一运行入口，包含输入校验、配置读取、API Key 解密、调用、usage/向量转换和异常包装。
- [ServerModelFacade 与 ServerModelSpecFactory](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/src/main/java/com/aizuda/snail/ai/model/adapter/server/ServerModelFacade.java)
  Server 侧把 `ModelConfigInfoDTO` 转成三类 spec 并进入 runtime 的核心桥接。
- [snail-ai-models](../../../../open-java/snail-ai/snail-ai-models/)
  Chat、Embedding、Rerank 的 core、provider、starter、adapter 默认值和异常定义。
- [DefaultChatClientFactory](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/executor/client/DefaultChatClientFactory.java)
  Client 侧把 dispatch 模型配置变成 `ChatClient`，并注入 tools 与 advisor。
- [Client 模型适配](../../../../open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-model/src/main/java/com/aizuda/snail/ai/agent/core/executor/model/DefaultChatModelFactory.java)
  `ClientModelConfigValidator`、`ClientChatModelSpecFactory`、`DefaultChatModelFactory` 共同说明 Client 不再解密，而是消费下发的 `apiKey`。
- [RAG Rerank 调用点](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/strategy/rerank/DefaultRerankService.java)
  RAG 搜索重排如何进入 `ModelRuntimeHandler.rerank`，以及失败后按原分数排序降级。
- [Embedding 维度与向量库调用点](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/embedding/EmbeddingModelDimensionService.java)
  RAG 侧通过一次 embedding 探测维度并在失败时使用默认维度的边界。
- [已有 L1：模型适配层](../module-models/)
  已有模块导览，帮助理解 `snail-ai-models` 的 common/core/provider/starter 分层。
- [已有 L1：Agent Client](../module-agent-client/)
  已有模块导览，帮助理解 Client gRPC、`ChatClient`、Advisor、Tool 和 usage 收集。
- [已有 L1：RAG](../module-rag/)
  已有模块导览，帮助定位 embedding、rerank 与 QA 流式调用发生在哪一层。

## 智慧（社区）

- 当前未收录外部社区。本主题是源码考古型切片，最高可信反馈来自在本仓库运行 Agent 对话、RAG QA、向量库初始化和检索重排，并对照日志与调用栈复核。

## 空白

- 仓库内未找到专门描述“模型配置到 runtime”全链路的设计文档，因此字段、异常和降级行为全部以当前源码为准。
- 用户给出的 `DispatchModelConfigAssembler` 优先路径位于 feature-agent，但当前源码实际类位于 `snail-ai-feature-model/.../adapter/server/DispatchModelConfigAssembler.java`，本主题按真实 import 和文件位置记录。
- 未覆盖生产密钥托管、审计脱敏、网络代理和 provider SLA；这些需要结合实际部署环境补充。

# RAG 对话检索注入资源

## 知识

- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/agent/AgentChatService.java`
  Agent 对话入口，创建 `AgentChatContext` 并交给责任链。适用于确认一次对话如何进入 RAG 判断前置流程。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/RagHandler.java`
  RAG 调用模式核心：强制调用并行检索后追加 `systemPrompt`，智能调用注入知识库清单和 `rag_search` 使用说明。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/enums/agent/RagCallModeEnum.java`
  `SMART=1`、`FORCED=2`，未知或空值回退智能调用。适用于判断配置值如何分流。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/resolver/ClientRagToolResolver.java`
  Client 侧 RAG 工具解析器。适用于确认智能模式才注册 `rag_search`，强制模式不注册工具。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/tool/RagSearchTool.java`
  Client 本地工具定义，模型调用 `rag_search` 时实际 Java 工具参数为 `ragId` 与 `queryQuestion`，随后经 gRPC 回调 Server 检索。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/handle/RagSearchCallbackHandler.java`
  `/callback/rag/search` 回调入口，把 Client 工具请求转换为 `RagSearchRequestDTO` 并调用同一套检索服务。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/service/RagSearchService.java`
  检索服务门面，创建 `RagSearchContext` 并执行 `RagSearchPipeline`。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/search/pipeline`
  RAG 检索 pipeline 与 handler 顺序，适用于追踪配置解析、向量检索、BM25、融合、rerank 和 finalize。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/strategy/fusion`
  `RRFFusion` 与 `WeightedSumFusion` 的实现。适用于理解混合检索如何按 `chunkId` 合并。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/strategy/rerank/DefaultRerankService.java`
  rerank 运行入口，调用 `ModelRuntimeHandler.rerank`，失败时退回按分数排序。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/vector/VectorStoreFactory.java`
  根据知识库向量实例、embedding 模型和维度构建向量库。适用于定位 query embedding 与向量后端配置。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/vector/core/AbstractSnailAiVectorStore.java`
  检索时调用 Spring AI `similaritySearch`，query text 在向量库链路内完成 embedding。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-search-storage/snail-ai-search-template/src/main/java/com/aizuda/snail/ai/search/storage/search/SearchEngineFactory.java`
  根据搜索引擎实例构建 BM25 后端。适用于确认全文检索启停和实例配置。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/rag/RagQAService.java`
  Admin 知识库问答入口，检索后把结果替换进 `ModelParams.prompt` 或默认 system prompt。
- `teach/open-java/snail-ai/module-rag/reference/rag-overview.html`
  L1 RAG 模块总览。适用于回看本主题在 RAG 模块中的位置。
- `teach/open-java/snail-ai/module-models/reference/models-overview.html`
  模型适配层参考。适用于继续追 `ModelRuntimeHandler` 如何构建 chat、embedding 和 rerank 客户端。
- `teach/open-java/snail-ai/module-persistence/reference/persistence-overview.html`
  持久化与存储适配参考。适用于区分业务库、向量库和全文搜索索引。
- `teach/open-java/snail-ai/slice-rag-ingestion/reference/rag-ingestion-flow-map.html`
  已有摄入切片参考。适用于确认 `sai_rag_chunk`、向量索引和搜索索引在检索前如何生成。

## 智慧（社区）

- 本主题本次只依赖 Snail AI 仓库源码和已生成教学主题，没有引入外部社区链接。后续若要做生产故障复盘，应把实际 Agent 配置、`sai_rag` 配置 JSON、Client 日志、向量库/ES 查询结果作为学习记录补充。

## 空白

- 暂未覆盖前端如何配置 Agent 的 RAG 调用模式，因为本主题聚焦 Server/Client 检索注入链路。
- 暂未覆盖模型供应商 rerank 分数语义差异，因为本主题目标是能追源码路径和排障边界。

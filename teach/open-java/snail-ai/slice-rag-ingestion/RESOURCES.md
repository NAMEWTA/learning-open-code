# RAG 文档上传摄入资源

## 知识

- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/RagDocumentController.java`
  Admin 文档上传、预览、提交、取消、URL 导入、删除、重处理和分页入口。适用于确认 API 边界。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/rag/RagDocumentService.java`
  文档入库、去重动作、覆盖删除、资源上传、chunk 管理和重处理入口。适用于追踪上传后如何变成 `PENDING` 文档。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/rag/DocumentUploadPreviewService.java`
  preview 到 commit 的两阶段上传、TOCTOU 重新判定、token TTL、临时资源提升或清理。适用于理解二次确认上传。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/task/DocumentProcessingTask.java`
  每 10 秒扫描最多 5 个 `PENDING` 文档并调用 pipeline。适用于定位“为什么上传后没有立即解析”。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/pipeline/DocumentPipeline.java`
  摄入核心：抢占状态、读取资源、解析、切块、chunk 入库、向量库和搜索引擎双写、成功或失败状态更新。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/pipeline/DocumentChunkingService.java`
  根据知识库配置选择 `default`、`delimiter`、`regex`、`smart` 切块策略。适用于排查切片数量和粒度。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/strategy/parser/DocumentParserFactory.java`
  parser 选择工厂，配合 PDF、Word、Excel、Markdown、HTML、TXT parser 使用。适用于判断文件类型是否支持。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/ResourceService.java`
  资源上传、加载、删除和 `DOCUMENT_PREVIEW -> DOCUMENT` 业务类型更新。适用于追踪文件流和资源行。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/vector/VectorStoreFactory.java`
  根据知识库的向量库实例、embedding 模型和维度参数构建 `SnailAiVectorStore`。它会通过 `ModelRuntimeHandler.buildEmbeddingModel(...)` 构建 embedding。适用于定位 embedding 模型配置和向量库配置。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-model/src/main/java/com/aizuda/snail/ai/model/service/ModelRuntimeHandler.java`
  模型运行时门面，`buildEmbeddingModel(...)` 会解密 API Key 并通过 embedding builder 构建 Spring AI `EmbeddingModel`。适用于确认向量化模型的真实构建入口。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/embedding/EmbeddingModelDimensionService.java`
  当知识库没有 `dimensionOfVectorModel` 时，先读模型扩展配置，再尝试一次 embedding API 探测维度，失败后使用默认维度并回写。适用于排查维度为空或维度错误。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/vector/core/AbstractSnailAiVectorStore.java`
  把 `VectorDocument` 转成 Spring AI `Document` 并委托 `VectorStore.add`。适用于理解 embedding 实际由 Spring AI 向量存储链路触发。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-search-storage/snail-ai-search-elasticsearch-storage/src/main/java/com/aizuda/snail/ai/search/storage/search/elasticsearch/ElasticsearchSearchEngine.java`
  全文搜索索引创建、批量写入、查询和删除能力。适用于确认 BM25 索引字段和索引名。
- `open-java/snail-ai/docs/sql/snail_ai_schema.sql`
  MySQL 业务表定义，包含 `sai_rag`、`sai_rag_document`、`sai_rag_chunk`、`sai_resource`、`sai_store_instance` 和 `sai_model_config`。
- `teach/open-java/snail-ai/module-rag/reference/rag-overview.html`
  L1 RAG 模块总览。适用于回看摄入链路在 RAG 模块中的位置。
- `teach/open-java/snail-ai/module-resource/lessons/0001-resource-module-tour.html`
  L1 资源模块导览。适用于理解资源模块如何保存文件和资源元数据。
- `teach/open-java/snail-ai/module-persistence/reference/persistence-overview.html`
  L1 持久化与存储适配参考。适用于区分业务库、向量库和搜索库。
- `teach/open-java/snail-ai/module-models/reference/models-overview.html`
  L1 模型适配层参考。适用于追踪 embedding 模型从配置到 runtime 的构建路径。

## 智慧（社区）

- 本主题本次只依赖仓库源码和已生成 L1 教学主题，没有引入外部社区链接。后续若要做生产故障复盘，可把团队的日志样本、部署拓扑和实际向量库配置作为学习记录补充到本主题。

## 空白

- 暂未覆盖 Snail AI 前端上传页面代码，因为本主题目标是 Server 端垂直切片。
- 暂未覆盖具体向量库后端的性能调优资料，因为本主题只要求能定位摄入链路和失败边界。

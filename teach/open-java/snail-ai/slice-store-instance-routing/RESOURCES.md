# Snail AI 存储实例路由资源

## 知识

- [源码：`StoreInstanceController.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/StoreInstanceController.java)
  Admin 存储实例管理入口。适用于确认 `/store-instance` endpoint、维度约束接口和连接测试入口。
- [源码：`StoreInstanceService.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/StoreInstanceService.java)
  存储实例创建、更新、默认实例清理、分类类型校验、删除引用保护和连接测试。
- [源码：`VectorDimensionConstraintService.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/VectorDimensionConstraintService.java)
  维度约束的核心来源，适用于解释模型上限、后端上限和有效上限。
- [源码：`KnowledgeService.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/knowledge/KnowledgeService.java)
  知识库创建和更新时写入 `vectorStoreInstanceId`、`searchEngineInstanceId`、`dimensionOfVectorModel` 的位置。
- [源码：`StoreInstancePO.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/admin/po/StoreInstancePO.java)
  `sai_store_instance` 的 PO。适用于确认配置 JSON、类型、分类、状态和默认标记字段。
- [源码：`StoreInstanceMapper.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/admin/mapper/StoreInstanceMapper.java)
  存储实例 MyBatis-Plus mapper。适用于确认服务层和工厂层如何按 ID 回查实例配置。
- [源码：`RagPO.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/rag/po/RagPO.java)
  知识库主表对象。适用于确认 RAG 如何保存向量库实例和搜索实例 ID。
- [源码：`VectorStoreFactory.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/vector/VectorStoreFactory.java)
  向量后端路由核心。适用于确认实例查表、类型转换、embedding 模型构建、注册表选择和缓存失效。
- [源码：向量后端实现目录](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/)
  PgVector、Milvus、Elasticsearch Vector 的 lifecycle、settings、client factory 和 store 实现。
- [源码：`SearchEngineFactory.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-search-storage/snail-ai-search-template/src/main/java/com/aizuda/snail/ai/search/storage/search/SearchEngineFactory.java)
  全文搜索后端路由核心。适用于确认当前只注册 Elasticsearch 搜索实现。
- [源码：搜索后端实现目录](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-search-storage/)
  Search API、Elasticsearch 搜索实现、settings 和 lifecycle。
- [源码：`DocumentPipeline.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/pipeline/DocumentPipeline.java)
  RAG 摄入双写入口。适用于确认向量写入、全文写入、`indexName` 和非致命搜索写入失败。
- [源码：`VectorSearchHandler.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/search/pipeline/handler/VectorSearchHandler.java)
  RAG 向量检索阶段调用 `VectorStoreFactory` 的位置。
- [源码：`Bm25SearchHandler.java`](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/search/pipeline/handler/Bm25SearchHandler.java)
  RAG BM25 检索阶段调用 `SearchEngineFactory` 的位置，适用于核对搜索实例 ID 缺失时的运行期异常。
- [SQL：`snail_ai_schema.sql`](../../../../open-java/snail-ai/docs/sql/snail_ai_schema.sql)
  MySQL 初始化脚本。适用于核对 `sai_store_instance` 和 `sai_rag` 字段。
- [L1：`module-persistence`](../module-persistence/reference/persistence-overview.html)
  持久化与存储适配总览，适合作为本切片的上层地图。
- [L1：`module-rag`](../module-rag/reference/rag-overview.html)
  RAG 摄入和检索模块总览，适合理解本切片在 RAG 流程中的位置。
- [L1：`module-models`](../module-models/reference/models-overview.html)
  模型适配层总览，适合理解 embedding 模型和维度来源。

## 智慧（社区）

- [Snail AI Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  上游源码、issue 和变更记录入口。适用于验证当前存储实例路由是否已被新版本调整。

## 空白

- 当前没有找到专门讨论 Snail AI 存储实例路由的外部高质量教程；本主题以源码和仓库内 L1 教学为主要知识来源。

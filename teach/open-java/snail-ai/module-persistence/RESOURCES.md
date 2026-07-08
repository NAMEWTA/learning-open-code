# 持久化与存储适配模块资源

## 知识

- [持久化 PO/Mapper 与存储 API 速查](./reference/persistence-api.html)
  L3 接口清单：按领域列出 PO 字段、Mapper 方法、VectorDocument/VectorSearchResult 与存储异常类型。
- [持久化模块 overview 参考](./reference/persistence-overview.html)
  模块边界、Factory 路由、StoreInstance 管理与部署脚本速查。
- [L0 项目总览课程](../00-overview/lessons/0001-project-map.html)
  用于把持久化模块放回 Server、RAG、Memory 和外部依赖的全局地图中。
- [RAG 功能模块课程](../module-rag/lessons/0001-rag-module-tour.html)
  用于理解 RAG 摄入和检索为什么依赖向量库与搜索引擎后端。
- [snail-ai-server-persistence/pom.xml](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/pom.xml)
  持久化模块的顶层 Maven 聚合，确认业务库、向量库、搜索库三类边界。
- [snail-ai-biz-storage](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage)
  MyBatis-Plus 业务库模板、PO、Mapper，以及 MySQL、PostgreSQL、达梦方言 XML。
- [SnailAiBizStorageAutoConfiguration.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/config/SnailAiBizStorageAutoConfiguration.java)
  Mapper 扫描、按数据库类型选择 XML 目录、分页和防全表更新插件配置。
- [snail-ai-vector-storage](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage)
  `SnailAiVectorStore` 模板、`VectorStoreFactory`、索引命名和 PgVector、Milvus、Elasticsearch 向量实现。
- [VectorStoreFactory.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/vector/VectorStoreFactory.java)
  按存储实例 ID、Embedding 模型和维度创建向量后端，是理解运行期后端选择的核心入口。
- [snail-ai-search-storage](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-search-storage)
  `SearchEngine` 模板、`SearchEngineFactory` 和 Elasticsearch 全文检索实现。
- [SearchEngineFactory.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-search-storage/snail-ai-search-template/src/main/java/com/aizuda/snail/ai/search/storage/search/SearchEngineFactory.java)
  按 `sai_store_instance` 创建搜索引擎后端，当前只注册 Elasticsearch。
- [StoreInstanceController.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/StoreInstanceController.java)
  Admin 存储实例管理入口，覆盖列表、分页、详情、创建、更新、删除、连接测试和维度约束。
- [StoreInstanceService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/StoreInstanceService.java)
  存储实例类型校验、默认实例处理、引用保护和连接测试逻辑。
- [docs/sql](../../../../open-java/snail-ai/docs/sql)
  MySQL、PostgreSQL、达梦初始化脚本，确认 `sai_store_instance`、RAG 表外键式实例 ID 和 chunk 向量字段。
- [docs/docker/docker-compose.yaml](../../../../open-java/snail-ai/docs/docker/docker-compose.yaml)
  本地依赖编排，包含 MySQL、PgVector、Milvus、Elasticsearch 和 MinIO 等服务。
- [BizDbTypeEnum.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/enums/BizDbTypeEnum.java)
  业务库方言检测：MySQL、PostgreSQL、达梦。
- [persistence/app、agent、skill 等 PO 与 Mapper](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/)
  biz-template 下按包划分的领域持久化对象与 Mapper 接口。
- [VectorDocument.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/vector/api/VectorDocument.java)
  向量写入 DTO：id、content、embedding、metadata。
- [VectorSearchResult.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/vector/api/VectorSearchResult.java)
  向量检索结果 DTO：id、content、score、metadata。
- [VectorStoreException.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-vector-storage/snail-ai-vector-template/src/main/java/com/aizuda/snail/ai/vector/storage/exception/VectorStoreException.java)
  向量存储统一异常，继承 `BaseSnailAiException`。
- [SearchEngineException.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-search-storage/snail-ai-search-template/src/main/java/com/aizuda/snail/ai/search/storage/search/exception/SearchEngineException.java)
  搜索引擎运行时异常。

## 智慧（社区）

- 当前主题暂不引入外部社区材料；本轮目标是建立当前源码边界，以本工作区源码、SQL 和部署脚本作为主要证据。

## 空白

- 未检索外部 Issue、PR 或线上部署经验，后续若分析后端兼容性、性能调优或连接测试缺陷，应补充对应讨论链接。
- 当前没有针对 persistence 模块的测试用例清单；后续 L2/L3 切片需要继续搜索测试目录或补充可执行验证路径。

# 使命：Snail AI 存储实例路由

## 为什么
这组课程帮助学习者在调试或扩展 Snail AI RAG 能力时，能从 Admin 配置一路追到真实的向量库和全文检索后端。掌握这条链路后，遇到 PgVector、Milvus、Elasticsearch 配置、维度、索引名或工厂注册问题时，可以快速定位责任层，而不是在 RAG、模型和持久化模块之间来回猜。

## 成功的样子
- 能说明 `sai_store_instance`、`sai_rag`、`VectorStoreFactory` 和 `SearchEngineFactory` 在路由链路中的分工。
- 能判断一个 RAG 知识库最终会写入或查询 PgVector、Milvus、Elasticsearch 中的哪个后端。
- 能解释向量维度为什么同时受 embedding 模型和向量库类型约束。
- 能列出默认实例、未注册类型、空 `indexName`、搜索双写失败等关键 fallback/error 行为。
- 能按 checklist 调试 RAG 摄入、向量检索和 BM25 检索的存储实例路由问题。

## 约束条件
- 本主题只覆盖 L2 垂直切片 `L2-slice-store-instance-routing`，不修改 Snail AI 源码。
- 课程内容以当前子模块 `open-java/snail-ai` 的源码为准。
- 输出范围限定在 `teach/open-java/snail-ai/slice-store-instance-routing/`。
- 已有 L1 主题 `module-persistence`、`module-rag`、`module-models` 作为背景材料，不在本主题重复展开模块总览。

## 不在范围内
- 不展开 RAG parser、chunker、fusion、rerank 的完整实现。
- 不讲模型 provider 适配层细节，只引用 embedding 维度解析对路由的影响。
- 不新增 PgFullText、Mongo 或其他后端实现设计。
- 不讲前端页面如何呈现存储实例表单。

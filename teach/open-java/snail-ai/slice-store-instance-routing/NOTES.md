# 便签

- 用户要求本次只写入 `teach/open-java/snail-ai/slice-store-instance-routing/`，不要编辑源码、`index.md`、`_progress.*` 或其他主题目录。
- 主题目标是 L2 垂直切片：从 Admin 配置、维度约束、默认实例，到 RAG 向量/搜索请求如何选择 PgVector、Milvus、Elasticsearch 等后端。
- 源码中不存在用户给出的 `persistence/store` 包；存储实例 PO/Mapper 实际位于 `persistence/admin`。
- 当前源码的“默认实例”主要影响列表排序和同分类唯一默认标记；知识库创建仍要求显式选择 `vectorStoreInstanceId`，运行时没有按默认实例自动 fallback。

# 便签：RAG 文档上传摄入

- 本主题采用“lesson 讲流程地图，reference 放完整清单”的结构，延续 Snail AI 现有 L1 主题风格。
- 当前源码中 `RagDocumentStatus.PARSING` 存在，但主摄入路径实际从 `PENDING` 抢占到 `PROCESSING`，再到 `SUCCESS` 或 `FAILED`。
- 当前文档删除、重处理清理路径主要覆盖业务库 chunk 和向量库；搜索引擎提供 delete 能力，但 RAG 删除路径中未看到调用，需要在调试全文索引残留时重点核查。

# 使命：RAG 文档上传摄入

## 为什么
学习者需要能从 Admin 上传或导入一个 RAG 文档开始，沿着源码追到资源接收、文档记录、解析、切块、embedding、向量库写入、全文搜索索引和状态更新。掌握这条垂直切片后，才能排查“文档卡住”“向量没写入”“搜索索引缺失”“重处理后结果不一致”等真实问题。

## 成功的样子
- 能说清 `POST /document/upload`、`POST /document/upload/preview`、`POST /document/upload/commit` 和 `POST /document/import/url` 分别进入哪条服务路径。
- 能把 `sai_resource`、`sai_rag_document`、`sai_rag_chunk`、向量索引 `rag_{ragId}`、搜索索引 `rag_{ragId}` 放到同一张流程图里。
- 能解释 `PENDING -> PROCESSING -> SUCCESS/FAILED` 的真实源码路径，以及重处理、覆盖、预览取消、孤儿预览资源清理的边界。
- 能根据日志和表字段快速判断故障发生在资源读取、parser、chunker、embedding、向量库还是搜索引擎双写。

## 约束条件
- 本主题是 L2 垂直切片，lesson 必须保持 15 分钟短课，长清单放到 `reference/`。
- 源项目根目录是 `open-java/snail-ai`，以当前源码为准，不用旧架构文档替代源码事实。

## 不在范围内
- 不展开 RAG 检索召回、融合、rerank、Prompt 注入和流式问答。
- 不讲前端页面实现和上传组件交互细节。
- 不评估具体向量库部署性能、ES 分词质量或模型供应商效果。

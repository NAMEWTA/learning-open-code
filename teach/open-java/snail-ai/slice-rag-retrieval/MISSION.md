# 使命：RAG 对话检索注入

## 为什么
学习者需要能从一次 Agent 对话进入 RAG 检索开始，沿源码追到强制调用、智能调用、检索 pipeline、rerank/融合，以及最终注入到 system prompt 或 Client 工具调用的完整路径。掌握这条 L2 垂直切片后，才能排查“Agent 没查知识库”“查到了但没有注入”“BM25/rerank 没生效”“智能调用工具失败”等真实问题。

## 成功的样子
- 能说明 `RagCallModeEnum.SMART` 与 `RagCallModeEnum.FORCED` 在 Server 和 Client 两侧分别做了什么。
- 能从 `AgentChatService.chat` 追到 `RagHandler.handle`，再追到 `RagSearchService.search` 和检索 pipeline。
- 能画出 query 如何从用户消息、`rag_search` 工具参数或 Admin QA 请求进入向量检索、BM25、融合、rerank 和最终补全。
- 能解释检索结果如何被注入到 `systemPrompt`，或如何作为 `rag_search` 工具返回值进入模型上下文。
- 能根据 debug metrics、日志和表/索引边界定位空结果、配置缺失、模型失败和工具调用失败。

## 约束条件
- 本主题是 L2 垂直切片，lesson 只讲主链路，长清单与排障表放入 `reference/`。
- 源项目根目录是 `open-java/snail-ai`，以当前源码为准；官方文档只能作为辅助，不替代源码事实。
- 本主题衔接已有 `module-rag`、`module-models`、`module-persistence` 和 `slice-rag-ingestion`，不重复讲文档上传摄入。

## 不在范围内
- 不展开 RAG 文档上传、parser、chunker 和双写摄入细节。
- 不讲前端页面交互和具体 UI 组件。
- 不评测不同 embedding、rerank、向量库或 ES 分词方案的效果。

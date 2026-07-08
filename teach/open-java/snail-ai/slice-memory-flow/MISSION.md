# 使命：L2-slice-memory-flow

## 为什么
本主题用于掌握 Snail AI 一次对话里的记忆链路真实顺序，尤其是短期历史何时写入、何时读取，以及长期记忆在当前源码中是否真的被检索注入。学完后可以排查多轮上下文丢失、历史重复、长期记忆无效和 completion 后持久化延迟等问题。

## 成功的样子
- 能按顺序复述：用户消息保存、短期历史加载、长期召回接入点、gRPC dispatch、completion 持久化、短期 memory 更新。
- 能说明 `ContextCollectorHandler(@Order 75)`、`ConversationHandler`、`ChatResultPersistService`、memory stores 和 LLM call 的边界。
- 能判断“架构文档描述的长期记忆”与“当前源码实际执行路径”的差异。
- 能用调试 checklist 定位一次对话为什么没有携带历史或长期记忆。

## 约束条件
- 只基于当前本地源码快照生成课程，不把文档中的规划能力当作已实现事实。
- 本主题只写入 `teach/open-java/snail-ai/slice-memory-flow/`，不更新项目索引、进度文件或源码。
- 课程保持 L2 垂直切片视角，不展开整个 Agent、RAG、模型适配或存储系统。

## 不在范围内
- 不讲 Agent 创建、OpenAPI 入口、MCP、Skill、RAG 全链路细节。
- 不实现长期记忆检索或修复源码缺口。
- 不覆盖前端记忆管理页面和全部管理 API。

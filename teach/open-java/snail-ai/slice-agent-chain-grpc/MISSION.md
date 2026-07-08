# 使命：L2 Agent 责任链到 gRPC 分发

## 为什么
学习者需要能从 Server 端 Agent handler chain 的共享状态一路追到 `/chat/dispatch` gRPC streaming 调用，并判断一次对话卡住时问题发生在上下文装配、Client 选择、DTO 序列化、gRPC 信封还是 Client streaming handler 消费边界。

## 成功的样子
- 能按当前源码 order 说出哪些 Handler 写入 `AgentChatContext` 的关键字段。
- 能把 `AgentChatContext` 字段映射到 `ChatDispatchRequest` 的 top-level 字段和内嵌 DTO。
- 能解释 gRPC 只承载统一信封，业务路由由 `metadata.uri=/chat/dispatch` 和 JSON `body` 决定。
- 能描述 Client 端 `ChatDispatchStreamingHandler` 如何消费请求并返回 text、thinking、completion、error 四类流式结果。
- 能用 checklist 排查 Client 不在线、token/心跳、路由、streaming 错误和超时边界。

## 约束条件
- 源项目根目录固定为 `open-java/snail-ai`，课程以当前 checkout 源码为准。
- 本主题是 L2 垂直切片，lesson 保持 15 分钟内完成，长表格和边界清单放入 reference。
- 只生成教学产物，不修改 Snail AI 源码、项目索引或其他主题目录。

## 不在范围内
- 不展开 Client 内部完整 Advisor、Tool resolver、模型适配器和 MCP/RAG 运行细节。
- 不设计新的 proto、DTO 或超时治理方案。
- 不复述 L1 模块总览，只引用与本切片直接相关的事实。

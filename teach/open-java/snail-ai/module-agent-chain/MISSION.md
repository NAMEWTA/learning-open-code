# 使命：Agent 责任链模块

## 为什么
学习者需要能从 Snail AI 的 Server 端对话入口一路追踪到 gRPC 分发边界，判断一次 Agent 对话请求在哪些 Handler 中被初始化、增强、短路、持久化和转发。

## 成功的样子
- 能说明 `snail-ai-feature-agent` 在整体架构中负责 Server 端业务编排，而不是 Client 端模型执行。
- 能按源码排序解释主要 `AgentChatHandler` 的职责和上下文写入点。
- 能定位流式输出、结果回调和对话持久化的责任边界。
- 能为后续 L2 切片选择合适入口，例如 RAG 注入、gRPC 分发或持久化回调。
- 能区分主链 `AgentChatHandler` 与 Client 回调 `GrpcRequestHandler` 的触发时机、入参载体和持久化差异。
- 能说明 `WebSearchHandler` 的预留状态，以及回调 Handler 与 `ConversationHandler` / `ChatResultPersistService` 的功能重叠边界。

## 约束条件
- 目标读者具备 Java 与 Spring Boot 基础，但不预设熟悉 Snail AI 的模块拆分。
- 每节课程保持 15 分钟内完成，长表格和 Handler 清单进入 reference。
- 本主题只讲 Server 端 `snail-ai-feature-agent`，不展开 Client Advisor 的内部细节。

## 不在范围内
- Client 端 Advisor 流水线、模型适配器内部实现、RAG 检索算法细节。

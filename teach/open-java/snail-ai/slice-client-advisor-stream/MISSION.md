# 使命：Client Advisor 流式处理

## 为什么
掌握 Snail AI Client 侧一次流式对话从 gRPC 入口到模型响应回写 Server 的关键链路。完成后，学习者可以定位 text chunk、thinking、Token 用量、completion、error 和资源清理分别由哪一层负责，便于调试流式输出丢失、usage 为 0、thinking 不展示、活跃计数异常等问题。

## 成功的样子
- 能从 <code>ChatDispatchStreamingHandler</code> 入口画出 <code>ChatSessionRuntime</code>、<code>ClientChatExecutor</code>、<code>DefaultChatClientFactory</code> 与 Advisor 链的调用顺序。
- 能解释 text、thinking、completion、usage、error 各自如何写入 <code>ChatStreamResponse</code> 并通过 gRPC observer 回到 Server。
- 能按 checklist 快速判断问题发生在请求解析、工具解析、Advisor 参数、模型流、Token usage、observer 回写或 cleanup 阶段。

## 约束条件
- 本主题只写入 <code>teach/open-java/snail-ai/slice-client-advisor-stream/</code> 下的教学资料，不修改 Snail AI 源码、项目 <code>index.md</code>、进度文件或其他主题目录。
- 课程面向 L2 垂直切片学习，重点是链路理解和调试判断，不展开完整 Server 对话链、模型适配器实现或工具 resolver 细节。
- 课程依据本地源码快照生成，源码版本记录在 <code>SNAPSHOT.md</code>。

## 不在范围内
- 不讲 Server 侧完整 Agent 责任链、前端 SSE 展示层或持久化服务内部实现。
- 不讲 Spring AI 全量 Advisor 设计，只讲 Snail AI 在此链路中实际装配和使用的部分。
- 不改造代码、不补测试、不调整 Advisor order。

# Memory 与 summarization 资源

## 知识

- [L0 项目总览参考](../00-overview/reference/00-overview.html)
  用于确认 memory 与 summarization 在 deer-flow 整体架构中的位置。
- [lead agent 参考](../module-lead-agent/reference/lead-agent-overview.html)
  用于对照 middleware 链中 DurableContext、Summarization、Memory 的装配顺序。
- [Memory 子系统目录](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/memory/)
  队列、更新器、存储与 summarization hook 的实现集合。
- [MemoryMiddleware](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/memory_middleware.py)
  每轮 run 结束后把对话入队，供异步 LLM 更新长期记忆。
- [DeerFlowSummarizationMiddleware](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/summarization_middleware.py)
  接近 token 上限时压缩 `messages`，并把摘要写入 `ThreadState.summary_text`。
- [DurableContextMiddleware](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/durable_context_middleware.py)
  在 summarization 之前捕获 delegation 与 skill 引用，并在每次 model call 注入 durable 数据块。
- [DynamicContextMiddleware](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/dynamic_context_middleware.py)
  负责把已持久化的 memory 以 `<memory>` 注入当前轮模型请求（与 summarization 互补）。
- [memory_config.py](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/config/memory_config.py)
  `enabled`、`debounce_seconds`、`injection_enabled`、`max_injection_tokens` 等开关。
- [summarization_config.py](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/config/summarization_config.py)
  `trigger`、`keep`、`trim_tokens_to_summarize` 等压缩策略。
- [lead agent 装配](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/lead_agent/agent.py)
  `_create_summarization_middleware` 注册 `memory_flush_hook`；`build_middlewares` 插入三条 middleware。
- [ThreadState.summary_text](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/thread_state.py)
  summarization 产出的 LastValue 通道，由 DurableContext 投影进模型请求。
- [summarization 文档](../../../../open-ai-agent/deer-flow/backend/docs/summarization.md)
  官方配置说明与 trigger/keep 语义。
- [测试：memory queue](../../../../open-ai-agent/deer-flow/backend/tests/test_memory_queue.py)
  校准 debounce 与 per-thread 去重行为。
- [测试：memory updater](../../../../open-ai-agent/deer-flow/backend/tests/test_memory_updater.py)
  校准 LLM 更新与 fact 去重。
- [测试：memory prompt injection](../../../../open-ai-agent/deer-flow/backend/tests/test_memory_prompt_injection.py)
  校准 `<memory>` 注入预算与 guaranteed categories。

## 智慧（社区）

- 暂不纳入外部社区。本轮 L1 模块课只依据仓库当前源码生成，最高信号反馈来自后续 L2 垂直切片与项目内测试。

## 空白

- 尚未引入 LangChain 官方 SummarizationMiddleware 文档作为外部补充；后续 L3 课程可补充版本差异说明。

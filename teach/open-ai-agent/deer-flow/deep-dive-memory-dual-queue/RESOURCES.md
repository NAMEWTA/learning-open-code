# Memory 双入队 资源

## 知识

- [DeerFlow backend AGENTS.md — Memory System](https://github.com/bytedance/deer-flow/blob/main/backend/AGENTS.md) — middleware 链第 19 位 MemoryMiddleware、queue debounce 工作流
- [DeerFlow summarization.md](https://github.com/bytedance/deer-flow/blob/main/backend/docs/summarization.md) — 上下文压缩触发条件与 keep policy
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/memory/queue.py` — `add` / `add_nowait`、`_enqueue_locked`、Timer 处理
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/memory_middleware.py` — `after_agent` debounce 入队
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/memory/summarization_hook.py` — `memory_flush_hook` 摘要前即时入队
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/lead_agent/agent.py` — `memory_flush_hook` 注册到 SummarizationMiddleware
- 本地测试：`open-ai-agent/deer-flow/backend/tests/test_summarization_middleware.py` — `test_memory_flush_hook_*` 系列
- 本地课程：[module-memory-context 导览](../module-memory-context/lessons/0001-memory-context-module-tour.html)、[slice-memory-update-injection](../slice-memory-update-injection/lessons/0001-flow-map.html)

## 智慧（社区）

- [DeerFlow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `memory queue`、`summarization hook`、`debounce` 可找到压缩与记忆竞态相关讨论

## 空白

- 官方文档尚未单独成章对比两条入队路径的时序图；本主题以 `queue.py` 与 `test_memory_flush_hook_*` 为首要依据

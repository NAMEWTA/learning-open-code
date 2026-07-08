# memory 注入与异步更新 资源

## 知识

- [backend AGENTS.md — Memory System](open-ai-agent/deer-flow/backend/AGENTS.md) — memory 组件分工、per-user 隔离、`debounce_seconds` 与注入开关的产品级约定
- [agents/middlewares/memory_middleware.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/memory_middleware.py) — 回合结束后过滤消息并入队
- [agents/memory/queue.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/memory/queue.py) — 防抖队列、per-thread 去重与 `threading.Timer` 触发
- [agents/memory/updater.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/memory/updater.py) — LLM 抽取事实、原子写 `memory.json`
- [agents/middlewares/dynamic_context_middleware.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/dynamic_context_middleware.py) — 读取 memory 并以 `<memory>` 注入当前轮
- [frontend harness/memory.mdx](open-ai-agent/deer-flow/frontend/src/content/zh/harness/memory.mdx) — 面向用户的 memory 行为说明

## 智慧（社区）

- [deer-flow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `memory` / `tiktoken` / `injection` 可见注入超时与 token 计数相关讨论
- [LangChain AgentMiddleware 文档](https://python.langchain.com/docs/concepts/agents/) — 理解 `before_agent` 与 `after_agent` 在图执行中的时机

## 空白

- 官方未单独发布「memory 排障 runbook」；实践上主要依赖 `backend/tests/test_memory_updater.py`、`test_dynamic_context_middleware.py` 与 AGENTS.md 中的 Memory System 小节

# 使命：Memory 双入队机制

## 为什么
长期 memory 靠异步 LLM 抽取事实，但对话既会在每轮 agent 结束后积累，也会在 summarization 压缩前被批量丢弃。我想弄清 DeerFlow 为何同时存在 `queue.add`（debounce）与 `queue.add_nowait`（即时）两条入队路径，以及它们各自的触发边界与 dedupe 行为。

## 成功的样子
- 能画出「正常轮次 → debounce 入队」与「摘要前 flush → 零延迟入队」两条链路
- 解释为何 summarization 不能等 30s debounce，以及 `_enqueue_locked` 如何按 thread/user/agent 合并
- 排查 memory 漏写时，知道先查 summarization hook 是否注册、再查 queue 是否在 `_processing`

## 约束条件
- 以 monorepo 子模块 `open-ai-agent/deer-flow` 当前 harness 源码为准
- 先读过 `module-memory-context` 或 `slice-memory-update-injection` 更佳；本主题为 L4 深度剖析，单节 15 分钟

## 不在范围内
- `MemoryUpdater` 内部 LLM 提示词与 fact dedupe（见 module-memory-context）
- `DynamicContextMiddleware` 如何把 memory 注入下一轮 prompt（见 slice-memory-update-injection）
- summarization 触发阈值与 keep policy 细节（见 backend/docs/summarization.md）

# 使命：Memory 与 summarization

## 为什么
学习者已经知道 lead agent 的 middleware 链与 `ThreadState`，但容易把「跨线程长期记忆」「单线程上下文压缩」和「压缩后仍要可见的运行态」混为一谈。完成本主题后，应能独立判断：某段对话信息会写入 `memory.json`、被 summarization 压成 `summary_text`，还是通过 durable context 继续出现在模型请求里。

## 成功的样子
- 能区分 Memory、Summarization、DurableContext 三条链路的职责与触发时机。
- 能说明 `MemoryMiddleware.after_agent` 与 `memory_flush_hook` 如何共用 debounce 队列。
- 能根据 `config.yaml` 的 `memory.*` 与 `summarization.*` 开关解释行为差异。

## 约束条件
- 本主题是 L1 模块总览，lesson 控制在 15 分钟内完成。
- 课程只建立三条链路的地图，逐文件实现细节留给 L2 垂直切片 `slice-memory-update-injection`。
- 文档使用简体中文，代码标识符和源码路径保留英文。

## 不在范围内
- 不逐行讲解 `MemoryUpdater` 的 LLM prompt 与 fact 合并算法。
- 不覆盖 Gateway `/api/memory` 的 CRUD 交互细节。
- 不深入 `DynamicContextMiddleware` 的日期注入与 OWASP 角色分离实现。

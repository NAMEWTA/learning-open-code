# 使命：会话持久化全链路

## 为什么
理解 Pi Agent Harness 如何将每次 Agent 对话持久化到磁盘，是掌握 Agent 运行时状态管理的关键。当你需要调试会话丢失问题、实现会话导入导出、或为 Agent 添加自定义存储后端时，必须理解从 Agent 对话到 JSONL 文件、再到仓库索引的完整数据流。

## 成功的样子
- 能绘制从 `agent.prompt()` 到 JSONL 文件写入的完整调用时序图
- 能解释 JSONL 文件的 SessionHeader + Entry 行格式，以及 LeafEntry 如何追踪当前会话位置
- 能说明上下文压缩的触发条件、切点选择算法和摘要生成流程
- 能对比 JsonlSessionRepo 和 InMemorySessionRepo 的设计差异，理解 fork 操作的实现

## 约束条件
- 聚焦 pi-agent-core 的 `harness/session/` 和 `harness/compaction/` 源码
- 以 TypeScript 源码阅读为主，暂不涉及 Rust Token Killer 集成
- 学习时间：约 1 小时（含源码精读）

## 不在范围内
- LLM 流式传输协议与 Transport 抽象
- 工具执行生命周期（beforeToolCall / afterToolCall）
- TUI 差异渲染与终端事件处理
- Agent 主循环的双层控制流（已在 L1-module-agent 覆盖）

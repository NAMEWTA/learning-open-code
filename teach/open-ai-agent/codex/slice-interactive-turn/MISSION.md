# 使命：交互 TUI 中一次用户 turn 的执行链路

## 为什么
学习者已完成 L1 的 TUI 模块与 Core Runtime 模块导览，现在需要把两个模块串起来，追踪一条完整的垂直链路：用户打字 → TUI 事件循环 → CodexThread turn 启动 → 模型 API 调用 → 流式 SSE 响应 → TUI 增量渲染。只有走完这条闭环，才能在后续 L2 切片（工具调用执行、app-server turn）和 L3（异常恢复、性能优化）中建立端到端的直觉。

## 成功的样子
- 能画出从 TUI ChatWidget 输入事件到模型流式响应渲染的完整 mermaid 时序图。
- 能识别这条链路上每一层的职责边界：CLI main → tui run_main → App 事件循环 → ChatWidget → app-server session → CodexThread → ModelClient → SSE stream。
- 能在遇到 bug 或性能问题时，快速定位故障属于 TUI 渲染层、app-server 协议层、core turn 编排层还是模型客户端层。
- 能解释至少一条异常路径（模型返回错误、流中断、token 超限）的处理方式。

## 约束条件
- 本主题服务于批量生成的 Codex 架构课程，每节 lesson 控制在 15 分钟内完成。
- 本次 L2 只追踪一次成功 turn 的主路径和一条异常路径，不展开工具调用、多 agent、审批流程、协作模式等复杂场景。
- 教学输出使用简体中文；Rust 标识符、crate 名、文件路径保持英文原文。
- 前置依赖：L1-module-tui（TUI 三层结构）和 L1-module-core-runtime（Thread/Turn 生命周期）。

## 不在范围内
- 不展开 ratatui 渲染细节、tui-textarea 实现或 ANSI 转义码处理。
- 不深入代码解释 `run_turn` 内部的工具路由、compaction、context 片段构建和 MCP 调用。
- 不覆盖 resume、fork、archival 等 session 生命周期操作。
- 不讲多 agent 协作、collaboration mode、review mode、plan mode 等特殊模式。

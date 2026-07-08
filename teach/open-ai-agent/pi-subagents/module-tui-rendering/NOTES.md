# 教学笔记：TUI 结果渲染与 async widget 模块

- 本主题是 teach-goal 的 L1 worker 产物，只覆盖 `open-ai-agent/pi-subagents/src/tui/render.ts` 与 `open-ai-agent/pi-subagents/src/tui/render-helpers.ts` 的模块导览。
- lesson 必须短，重点是读懂“执行结果如何被格式化为终端可读输出和 async 状态组件”；长表格、分支矩阵和测试证据放入 reference。
- 源码路径统一写成 `open-ai-agent/pi-subagents/...` 前缀，避免课程引用中出现未带项目前缀的源码路径。
- 后续 L2 候选：`renderSubagentResult` compact/expanded 逐分支、async widget 自适应布局、chain/parallel 标签与 workflow graph span、ANSI/Unicode 宽度裁剪、空输出/暂停/失败状态策略。

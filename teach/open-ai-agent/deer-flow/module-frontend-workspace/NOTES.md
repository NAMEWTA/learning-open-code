# 教学笔记：Frontend workspace

- 本任务来自 teach-goal L1 子任务，只允许写入 `teach/open-ai-agent/deer-flow/module-frontend-workspace/`。
- lesson 目标保持单一：15 分钟理解 workspace 页面如何组织用户体验并接到后端。
- 长清单放入 `reference/frontend-workspace-overview.html`；lesson 不做源码百科。
- 源码发现：`frontend/src/core/tasks/` 管的是聊天流里的 subtask 事件/状态，scheduled tasks 页面真正的 CRUD API 在 `frontend/src/core/scheduled-tasks/`。

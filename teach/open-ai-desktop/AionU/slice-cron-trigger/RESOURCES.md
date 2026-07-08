# Cron 任务创建与触发全链路资源

## 知识

- [AionU L0 项目总览](../00-overview/reference/00-overview.html)
  用于确认 Electron renderer、common adapter、HTTP/WS 与本地 backend 的总体边界。
- [Cron 定时任务模块参考总览](../module-cron/reference/cron-overview.html)
  用于定位 `/scheduled`、`/scheduled/:job_id`、`ipcBridge.cron` API、任务页组件和测试证据。
- [Conversation Runtime 与 Agent UI 参考](../module-conversation-runtime/reference/conversation-runtime-overview.html)
  用于理解 Cron 执行后会话如何进入 MessageList、会话历史和运行时状态。
- [Common Adapter 与 API 映射参考](../module-common-adapter/reference/common-adapter-overview.html)
  用于确认 `ipcBridge.cron` 不是传统 Electron IPC，而是 HTTP + WebSocket contract。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/CreateTaskDialog.tsx`
  本切片的手动创建与编辑入口，负责把表单转换为 `addJob` 或 `updateJob` 负载。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/TaskDetailPage.tsx`
  任务详情入口，覆盖 run-now、防重入、启停、删除、会话历史刷新。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/cron/useCronJobs.ts`
  任务列表、单会话任务、会话状态 map、执行后未读标记与关联会话查询的核心 hook。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/platforms/aionrs/localCronCommands.ts`
  AI 对话侧本地 Cron 响应处理边界；实际创建/更新由注入 HTTP helper 处理，这里只清理展示内容。
- `open-ai-desktop/AionU/tests/e2e/specs/cron-crud.e2e.ts`
  AI 对话创建、修改、列表可见、详情历史、删除后会话保留、侧边栏历史归属的端到端证据。
- `open-ai-desktop/AionU/tests/unit/cron/`
  hook、状态标签、时区修复和 schedule 工具函数的单元证据集合。

## 智慧（社区）

- 本主题以本地源码、关联 L1/L0 教学和项目测试为准；未引入外部社区判断。

## 空白

- 本轮没有读取后端 Cron scheduler 源码，因此“到点后如何由后端挑选任务、启动 agent session、写回执行状态”只按 renderer 观察到的 API 与事件 contract 说明。

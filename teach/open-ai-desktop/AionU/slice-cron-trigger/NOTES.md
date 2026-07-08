# Cron 任务创建与触发全链路笔记

- 主题身份：AionU teach-goal 的 L2 垂直切片，目标是“Cron 任务创建与触发全链路”。
- 关联上游：L0 `00-overview`，L1 `module-cron`、`module-conversation-runtime`、`module-common-adapter`。
- 阅读结论：手动路径从 `/scheduled` 进入 `CreateTaskDialog`，对话路径由 AI 使用注入 HTTP helper 创建或更新任务，renderer 侧 `localCronCommands` 只处理完成消息的展示清理。
- 状态刷新：`useCronJobs` / `useAllCronJobs` / `useCronJobsMap` 订阅 `cron.job-created`、`cron.job-updated`、`cron.job-removed`；详情页额外订阅 `cron.job-executed` 刷新会话历史。
- 关键边界：manual schedule 的 `expr` 为空，不显示启停开关；`runNow` 用 ref 防止双击重入；旧任务缺失 `schedule.tz` 时会通过 `updateJob` 修复；E2E 要求 AI 更新任务保留同一个 job id。

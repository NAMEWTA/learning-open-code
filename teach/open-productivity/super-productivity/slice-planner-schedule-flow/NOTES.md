# 主题笔记

- 用户要求本批次只写入 `slice-planner-schedule-flow/`，因此不更新项目级 `index.md`、`_progress.json`、`_progress.md` 或其他主题目录。
- 课程口径采用 L2 垂直切片：主线讲状态到投影到 UI，长表、源码索引和候选 L3/L4 放入参考文档。
- 本主题必须反复强调四层边界：`PlannerState.days` 是计划索引，`Task.dueDay/dueWithTime` 是任务事实，`ScheduleDay.entries/ScheduleEvent` 是派生视图，`CalendarIntegrationService` 是外部日历输入。

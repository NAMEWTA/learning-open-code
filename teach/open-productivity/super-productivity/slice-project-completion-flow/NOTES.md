# 便签

- 用户要求本主题作为第三批 L2 主题之一，标题为“项目完成、任务归档与工作上下文收尾全链路”。
- 只允许写入本目录；不要更新项目级 `index.md`、`_progress.json`、`_progress.md` 或其他主题目录。
- 课程必须避免把“项目完成”写成单个 reducer action。当前源码显示：`WorkContextMenuComponent` 编排 dialog/service，`ProjectService` 拆分 task resolution 和 project flag，archive/worklog/timeTracking 另有边界。
- 关键事实：完成项目设置 `isDone`、`doneOn`、`isArchived`；任务归档由 Daily Summary 的 `TaskService.moveToArchive()` 和 `ArchiveService` 驱动，不是 completion reducer 的副作用。
- 关键事实：完成活跃项目后先 `navigateByUrl('/')` 再开庆祝 dialog；active work context 由路由驱动切回 Today，此切换本身不是 persistent op-log action。
- 后续候选：completion info 深挖、archive flush 深挖、worklog 映射深挖、op-log archive operation 冲突深挖、完成项目与当前追踪任务的边界审计。

# 项目完成、任务归档与工作上下文收尾全链路资源

## 知识

- `src/app/core-ui/work-context-menu/work-context-menu.component.html`
  项目菜单入口。适用于确认 active 项目何时显示 Complete、Restore、Reopen。
- `src/app/core-ui/work-context-menu/work-context-menu.component.ts`
  完成项目主编排：加载 completion info、弹出未完成任务处理 dialog、确认、应用 resolution、计算 stats、完成项目、导航并打开庆祝页。
- `src/app/features/project/dialog-complete-resolve-tasks/dialog-complete-resolve-tasks.component.ts`
  未完成任务处理 dialog，只返回 `inbox`、`markDone` 或取消。适用于区分用户决策和状态写入。
- `src/app/features/project/dialog-project-complete/dialog-project-complete.component.ts`
  完成庆祝 dialog，负责主题背景、confetti 和统计展示，不负责业务状态写入。
- `src/app/features/project/project.service.ts`
  完成信息收集、未完成任务移动到 Inbox、标记完成、完成/重开项目。适用于理解 service 层如何拆开 per-task action 和 project flag。
- `src/app/features/project/project-completion-stats.util.ts`
  庆祝页统计计算。适用于理解 top-level 任务计数、避免子任务耗时双算、工作天数和 duration。
- `src/app/features/project/store/project.actions.ts`
  `completeProject`、`reopenProject`、`archiveProject` 等 persistent project action 定义。适用于确认 op-log 捕获边界。
- `src/app/features/project/store/project.reducer.ts`
  项目完成只设置 `isDone`、`doneOn`、`isArchived`；未完成任务处理不在这里做。
- `src/app/features/project/store/project.selectors.ts`
  完成项目作为 archived project 的子集，影响 active task 过滤。
- `src/app/features/tasks/task.service.ts`
  `moveToProject`、`setDone`、`setUnDone`、`moveToArchive`、`getAllTasksForProject`。适用于区分移动、完成、归档、统计读取。
- `src/app/root-store/meta/task-shared.actions.ts`
  task 共享 persistent actions，包括 `moveToOtherProject`、`moveToArchive`、`deleteProject`。
- `src/app/features/tasks/store/task.reducer.ts`
  `moveToArchive` 从 live task store 删除任务，和项目完成的 archived flag 不同。
- `src/app/features/tasks/store/task.selectors.ts`
  archived project id 过滤 active task 视图。适用于解释完成后任务为什么不再出现在活跃列表。
- `src/app/features/archive/archive.service.ts`
  将 done parent tasks 写入 archiveYoung、迁移历史 timeTracking、必要时 flush 到 archiveOld。
- `src/app/features/archive/task-archive.service.ts`
  读取、更新、删除 archiveYoung/archiveOld 中的任务。适用于 worklog 和远端 archive 操作。
- `src/app/features/archive/store/archive.actions.ts`
  `flushYoungToOld` 和压缩归档等 archive persistent action。
- `src/app/features/worklog/worklog.service.ts`
  从 live task state、archive task state 和 timeTracking start/end 合成 history/worklog。
- `src/app/features/worklog/util/get-complete-state-for-work-context.util.ts`
  为 Project/Tag/Today 选择 live 与 archived task 的合并视图。
- `src/app/features/worklog/util/map-archive-to-worklog.ts`
  将任务按日期、父子关系、timeSpentOnDay 和 workStart/workEnd 映射为 worklog。
- `src/app/features/work-context/work-context.service.ts`
  active work context、doneTasks、导航驱动的上下文切换，以及 worklog start/end 手动更新入口。
- `src/app/features/work-context/store/work-context.effects.ts`
  上下文切换时清理 selected task、特殊路由切到 Today，以及数据重载后的 context 校验。
- `src/app/features/time-tracking/time-tracking.service.ts`
  合并 current、archiveYoung、archiveOld 的 timeTracking，并为 worklog 提供 legacy workStart/workEnd map。
- `src/app/op-log/core/persistent-action.interface.ts`
  只有 `meta.isPersistent === true` 的 action 会被捕获。
- `src/app/op-log/capture/operation-capture.meta-reducer.ts`
  本地 persistent action 捕获，remote replay 不二次记录。
- `src/app/op-log/capture/operation-log.effects.ts`
  将 persistent action 写为 operation，按 action meta 的 opType 解释语义。
- `src/app/op-log/apply/archive-operation-handler.service.ts`
  archive-affecting action 的本地/远端副作用边界，尤其是 `moveToArchive` 和 `flushYoungToOld`。
- `teach/open-productivity/super-productivity/slice-time-tracking-flow/`
  相邻 L2：解释任务耗时和 work context start/end 如何进入 timeTracking 和 op-log，适合配合本主题理解 worklog 输出。

## 智慧（社区）

- [Super Productivity upstream GitHub](https://github.com/super-productivity/super-productivity)
  适用于验证项目完成、归档、history/worklog 和同步相关 issue 背景。本文档事实来源仍以本地源码快照为准。

## 空白

- 未找到 maintainer 对“完成项目是否应同时停止当前追踪任务”的产品级说明；课程只按当前源码边界描述，不推断产品意图。
- 未纳入真实用户访谈，因此“归档 vs 完成 vs 删除”的 UX 意图只从代码、注释和测试推断。

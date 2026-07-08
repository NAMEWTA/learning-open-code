# 任务计划到日程渲染的 Planner 与 Schedule 投影全链路资源

## 知识

- `src/app/features/planner/planner.model.ts`
  Planner day、scheduled item、repeat projection 与 calendar event 的类型入口。适用于辨认 Planner 视图里的四类条目。
- `src/app/features/planner/store/planner.actions.ts`
  Planner 持久化 action 定义。适用于判断 `planTaskForDay`、`transferTask`、`moveInList`、`moveBeforeTask` 是否进入 op-log。
- `src/app/features/planner/store/planner.reducer.ts`
  Planner 自有 state 入口。适用于确认 `PlannerState.days` 只保存 `dayDate -> taskIds`。
- `src/app/features/planner/store/planner.selectors.ts`
  Planner day 聚合入口。适用于追踪 `PlannerDay.tasks`、`scheduledIItems`、deadline tasks、repeat projections、calendar events 如何合成。
- `src/app/root-store/meta/task-shared-meta-reducers/planner-shared.reducer.ts`
  Planner action 的跨实体一致性维护。适用于判断跨日移动、按日计划、Today 排序和 `dueDay/dueWithTime` 清理。
- `src/app/root-store/meta/task-shared-meta-reducers/task-shared-scheduling.reducer.ts`
  Task scheduling action 的跨实体一致性维护。适用于判断 `scheduleTaskWithTime`、`unscheduleTask`、`planTasksForToday` 如何改 task 与 Today。
- `src/app/features/work-context/store/work-context.selectors.ts`
  Today 与 Timeline 任务选择器。适用于区分 `planned` 的 `dueWithTime` 任务和 `unPlanned` 的 Today 流动任务。
- `src/app/features/schedule/schedule.service.ts`
  Schedule 视图数据门面。适用于查看 Schedule 如何读取 timeline tasks、planner day map、repeat cfg、calendar events 和 timeline config。
- `src/app/features/schedule/map-schedule-data/map-to-schedule-days.ts`
  Schedule 投影主入口。适用于确认 scheduled tasks 与 non-scheduled tasks 的分流。
- `src/app/features/schedule/map-schedule-data/create-schedule-days.ts`
  未定时任务、Planner day、未定时 repeat projection、预算溢出和跨日流动的核心算法。
- `src/app/features/schedule/map-schedule-data/create-sorted-blocker-blocks.ts`
  scheduled task、scheduled repeat projection、calendar event、workday/lunch block 的 blocked block 创建入口。
- `src/app/features/schedule/map-schedule-data/insert-blocked-blocks-view-entries-for-schedule.ts`
  blocked block 插入与 split 逻辑。适用于排查任务被日历块或定时块拆开的原因。
- `src/app/features/schedule/schedule-week/schedule-week-drag.service.ts`
  Schedule 周视图拖拽 action 映射。适用于判断普通拖拽、Shift 拖拽、拖出网格分别派发什么 action。
- `src/app/features/planner/dialog-schedule-task/dialog-schedule-task.component.ts`
  Planner 排程弹窗入口。适用于区分带时间提交与 due-only 提交。
- `src/app/features/calendar-integration/calendar-integration.service.ts`
  外部日历事件输入。适用于确认 calendar integration 是 Schedule/Planner 的外部只读数据源。

## 智慧（社区）

- Super Productivity 上游 Issues
  适用于验证 Planner、Schedule、repeat projection、Today 排序和日历集成相关历史 bug 的真实用户场景。
- 本仓库相邻 L1 `teach/open-productivity/super-productivity/module-planning-time/`
  适用于回看 Planner、Schedule、time-tracking、focus、idle 在时间模块中的边界。
- 本仓库相邻 L1 `teach/open-productivity/super-productivity/module-task-domain/`
  适用于回看任务、项目、标签、Today 虚拟标签和 NgRx meta-reducer 的任务域规则。
- 相关 L2 `teach/open-productivity/super-productivity/slice-task-create-flow/`
  适用于追踪新增任务时 `dueDay`、`dueWithTime`、repeat cfg 和 planner day 的初始写入。
- 相关 L2 `teach/open-productivity/super-productivity/slice-time-tracking-flow/`
  适用于区分 Schedule 显示的时间安排和真实 time tracking 累计事实。

## 空白

- 未纳入完整 Calendar provider/plugin 写回协议；本主题只覆盖 Schedule/Planner 如何消费日历事件，以及拖拽可写 calendar event 的交接点。
- 未纳入所有 timezone、startOfNextDayDiffMs 和 DST 边界测试；这些适合拆成 L3 时间边界专题。
- 未纳入 op-log 捕获、远端 replay 与 LWW 合并；本主题只标出 persistent action 的来源。

# 计划排程、时间追踪与专注反馈资源

## 知识

- `open-productivity/super-productivity/src/app/root-store/feature-stores.module.ts`
  NgRx feature store 与 effects 注册总入口。适用于判断哪些时间相关模块有持久 store，哪些只是视图或服务。
- `open-productivity/super-productivity/src/app/app.routes.ts` 与 `src/app/routes/context.routes.ts`
  Planner、Schedule、Boards、History、Metrics 的页面入口。适用于从 URL 反推功能边界。
- `open-productivity/super-productivity/src/app/features/planner/`
  计划天视图、planner state、selector、effect 和调度弹窗。适用于理解“计划到某天”与“安排具体时间”的区别。
- `open-productivity/super-productivity/src/app/features/schedule/`
  时间轴、周/月视图、日程数据映射与拖拽。适用于理解 Schedule 如何消费 task、planner、calendar 和 work-context 配置。
- `open-productivity/super-productivity/src/app/features/boards/`
  可配置任务看板、panel 过滤、手动顺序和跨列拖拽副作用。适用于判断 Boards 与 task/planner 的边界。
- `open-productivity/super-productivity/src/app/features/time-tracking/`
  project/tag 维度的工作起止、休息和会话数据。适用于后续 L2 追踪工时状态来源。
- `open-productivity/super-productivity/src/app/features/focus-mode/`
  专注模式 timer store、overlay、session/break 效果和 Metric 写入。适用于理解专注反馈如何与当前任务追踪协同。
- `open-productivity/super-productivity/src/app/features/idle/` 与 `open-productivity/super-productivity/electron/idle-time-handler.ts`
  前端 idle store/effects、空闲对话框和 Electron 系统 idle 输入。适用于理解空闲时间如何回滚并重新分配。
- `open-productivity/super-productivity/src/app/features/reminder/`
  task reminder worker 与倒计时 banner。适用于理解提醒如何围绕 task 的 `remindAt`、`deadlineRemindAt` 工作。
- `open-productivity/super-productivity/src/app/features/metric/`、`src/app/features/history/`、`src/app/features/worklog/`
  每日指标、历史页和工时汇总。适用于理解回顾页如何从 task archive、timeTracking、metric 聚合数据。
- `teach/open-productivity/super-productivity/00-overview/`
  已完成 L0 项目地图。适用于把本主题放回整体 Angular/NgRx/op-log 架构。
- `teach/open-productivity/super-productivity/module-op-log-sync/`
  已完成 L1 op-log 边界。适用于判断哪些 action 会被同步，哪些只是本地 UI 状态。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/johannesjo/super-productivity/issues)
  真实 bug 与设计取舍讨论。适用于验证 idle、planner、focus-mode、sync 相关边界判断是否贴近维护者语境。
- 本仓库相邻教学主题：`module-task-domain`、`module-angular-app-shell`、`module-op-log-sync`
  已生成的学习锚点。适用于交叉检查 task/work-context、Angular shell 与 op-log 的前置边界。

## 空白

- 尚未生成 time-tracking L2 垂直切片，因此本主题只记录状态来源与入口，不覆盖完整写入链路。
- 尚未系统阅读 Android/iOS 后台追踪 effects，本主题只覆盖 Electron idle 与前端 idle 处理的主线。

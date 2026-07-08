# 开始追踪、空闲检测与时间记录全链路资源

## 知识

- `src/app/features/tasks/task/task-hover-controls/task-hover-controls.component.html`
  任务行开始/暂停按钮入口。适用于追踪用户点击如何进入 `TaskComponent`。
- `src/app/features/tasks/task/task.component.ts`
  任务行组件的 `startTask()`、`pauseTask()`、`togglePlayPause()`。适用于定位 UI 到 `TaskService` 的第一跳。
- `src/app/features/tasks/task.service.ts`
  追踪 tick 消费、`addTimeSpent`、batch sync、停止时 flush、idle 补记入口。适用于解释任务耗时与同步 action 的分离。
- `src/app/core/global-tracking-interval/global-tracking-interval.service.ts`
  全局 wall-clock tick 与移动端 resume wake-up tick。适用于判断跨后台/睡眠后的时间差如何进入链路。
- `src/app/features/tasks/store/task.actions.ts`
  `setCurrentTask`、`unsetCurrentTask`、`toggleStart` 等非持久追踪 UI action。适用于区分 current task 与可同步任务数据。
- `src/app/features/tasks/store/task.reducer.ts`
  `addTimeSpent`、本地/远端 `syncTimeSpent`、current task reducer。适用于解释 `task.timeSpentOnDay` 和 `task.timeSpent` 的写入边界。
- `src/app/features/tasks/store/task.reducer.util.ts`
  `updateTimeSpentForTask` 与父任务时间增量更新。适用于判断子任务计时是否级联到父任务。
- `src/app/features/time-tracking/store/time-tracking.actions.ts`
  `syncTimeSpent`、`syncTimeTracking`、`updateWorkContextData` 的 persistent meta。适用于解释哪些时间数据会进入 op-log。
- `src/app/features/time-tracking/store/time-tracking.reducer.ts`
  work context `s/e/b/bt` 状态写入。适用于解释项目/标签维度的工作起止时间。
- `src/app/features/time-tracking/time-tracking.model.ts`
  `TTWorkContextData` 字段含义。适用于解码 `s/e/b/bt`。
- `src/app/features/idle/store/idle.effects.ts`
  idle 检测、扣回误计时间、打开 idle dialog、按结果记任务或 break。适用于分析空闲检测主分叉。
- `src/app/features/focus-mode/store/focus-mode.effects.ts`
  tracking 与 focus session 双向同步、break 自动开始、metric 记录。适用于分析 focus/break 与任务追踪互相驱动。
- `src/app/features/metric/metric.service.ts`
  focus session 完成后写 metric，以及 productivity breakdown 读取 worklog。适用于连接 focus 与指标。
- `src/app/features/metric/store/metric.actions.ts`
  `logFocusSession` 的 persistent meta。适用于确认 focus metric 会进入 op-log。
- `src/app/op-log/capture/operation-capture.meta-reducer.ts`
  persistent action 捕获、remote 过滤、deferred action 缓冲。适用于解释本地动作如何进入 op-log 队列。
- `src/app/op-log/capture/operation-capture.service.ts`
  `syncTimeSpent` 和 `TIME_TRACKING` 的 action-payload entityChanges 提取。适用于解释特殊时间 action 为什么不依赖 state diff。
- `src/app/op-log/capture/operation-log.effects.ts`
  operation 构造、vector clock 增量、payload 校验、append 与 immediate upload。适用于解释持久化写入主路径。
- `src/app/op-log/sync/operation-write-flush.service.ts`
  等待 pending op-log 写入完成的两阶段 flush。适用于排查“同步时少上传一笔时间”。
- `src/app/op-log/persistence/operation-log-store.service.ts`
  `SUP_OPS` 中 `ops` 和 `vector_clock` 的原子写入。适用于分析持久化事务边界。
- `src/app/op-log/persistence/op-log-db-schema.ts`
  `SUP_OPS` 目标 schema。适用于确认 `ops`、`state_cache`、`vector_clock` 等 store 结构。
- `src/app/features/tasks/store/task.reducer.spec.ts`
  `syncTimeSpent` 本地 no-op、远端应用的测试。适用于佐证 reducer 分工。
- `src/app/op-log/capture/operation-capture.service.spec.ts`
  `syncTimeSpent` entityChanges 提取测试。适用于佐证 op-log capture 特殊路径。

## 智慧（社区）

- [Super Productivity upstream GitHub](https://github.com/super-productivity/super-productivity)
  适用于验证时间追踪、idle、focus mode 相关 issue 与回归背景。本文档事实来源仍以本地源码快照为准。

## 空白

- 未纳入产品设计层面的用户访谈或 maintainer 解释；focus/break 的用户意图只能从源码注释、测试和 action 流推断。
- 未展开 Android/iOS 原生层实现；移动端后台补时只记录到 Web 层 effects 的交接点。

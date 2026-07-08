# 课程快照：slice-time-tracking-flow

## 源项目信息
- **源仓库**：`open-productivity/super-productivity`
  - **Git Commit**：`245330bd689ec2b578c4dfd415ec4ae1fbc1fb03`
  - **短 Commit**：`245330b`
  - **分支**：`master`
- **快照时间**：2026-07-07T19:59:32+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `src/app/core/global-tracking-interval/global-tracking-interval.service.ts` | 追踪 tick 来源 | 🟢 核心 |
| `src/app/core/util/batched-time-sync-accumulator.ts` | 任务耗时 batch 累积 | 🟢 核心 |
| `src/app/features/android/store/android-foreground-tracking.effects.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/focus-mode/focus-mode-break/focus-mode-break.component.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/focus-mode/focus-mode-main/focus-mode-main.component.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/focus-mode/store/focus-mode.actions.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/focus-mode/store/focus-mode.effects.ts` | tracking/focus 双向联动 | 🟢 核心 |
| `src/app/features/focus-mode/store/focus-mode.reducer.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/idle/idle.service.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/idle/store/idle.actions.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/idle/store/idle.effects.ts` | idle 扣回与归属分叉 | 🟢 核心 |
| `src/app/features/idle/store/idle.reducer.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/ios/store/ios-background-tracking.effects.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/metric/metric.service.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/metric/store/metric.actions.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/metric/store/metric.reducer.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/metric/store/metric.selectors.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/tasks/store/task-internal.effects.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/tasks/store/task.actions.ts` | current task 与 removeTimeSpent action | 🟢 核心 |
| `src/app/features/tasks/store/task.reducer.spec.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/tasks/store/task.reducer.ts` | 任务耗时 reducer 主入口 | 🟢 核心 |
| `src/app/features/tasks/store/task.reducer.util.ts` | 父子任务耗时级联 | 🟢 核心 |
| `src/app/features/tasks/task-context-menu/task-context-menu-inner/task-context-menu-inner.component.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/tasks/task.service.ts` | 追踪 tick 消费与 flush | 🟢 核心 |
| `src/app/features/tasks/task/task-hover-controls/task-hover-controls.component.html` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/tasks/task/task.component.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/time-tracking/store/time-tracking.actions.ts` | persistent 时间同步 action | 🟢 核心 |
| `src/app/features/time-tracking/store/time-tracking.reducer.ts` | work context 时间摘要 | 🟢 核心 |
| `src/app/features/time-tracking/time-tracking.model.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/worklog/util/get-time-spent-for-day.util.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/features/worklog/worklog.service.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/op-log/capture/operation-capture.meta-reducer.ts` | persistent action 捕获边界 | 🟢 核心 |
| `src/app/op-log/capture/operation-capture.service.spec.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/op-log/capture/operation-capture.service.ts` | 时间 action entityChanges 提取 | 🟢 核心 |
| `src/app/op-log/capture/operation-log.effects.ts` | operation 写入入口 | 🟢 核心 |
| `src/app/op-log/persistence/db-keys.const.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/op-log/persistence/op-log-db-schema.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/op-log/persistence/operation-log-store.service.ts` | SUP_OPS 持久化 | 🟢 核心 |
| `src/app/op-log/sync/operation-log-sync.service.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/op-log/sync/operation-write-flush.service.spec.ts` | 课程分析引用 | 🟡 辅助 |
| `src/app/op-log/sync/operation-write-flush.service.ts` | 上传前等待 pending op-log | 🟢 核心 |
| `src/app/op-log/validation/validate-operation-payload.ts` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-flow-map | `lessons/0001-flow-map.html` | 0001 开始追踪到时间记录路径图 |

## 参考资料

- `reference/time-tracking-flow-reference.html` — 时间追踪全链路参考

## 快照摘要
- 课程数：1
- 引用源文件数：42
- 学习记录数：0
- 参考资料数：1
- 资产文件数：1

# 教学笔记：开始追踪、空闲检测与时间记录全链路

## 教学取向

- 这是 teach-goal L2 垂直切片，目标是让读者能在脑中跑通“点击追踪 → tick → task/timeTracking → idle/focus/metric → op-log”的主路径。
- lesson 保持短课，只放路径图、判断表和一个 60 秒判断练习；长入口清单和故障排查放到 reference。
- 源码符号统一写成源项目内相对路径，避免 SNAPSHOT 把外层仓库目录当成源码路径。

## 写作取舍

- 没有把 Android/iOS 原生层列为主教学文件，只在 reference 说明 `src/app/features/android/store/android-foreground-tracking.effects.ts` 与 `src/app/features/ios/store/ios-background-tracking.effects.ts` 的 Web 层补时/flush 交接点。
- `currentTaskId` 是本地 UI 状态，不进入 op-log；真正持久化的是 `syncTimeSpent`、`syncTimeTracking`、`logFocusSession`、`removeTimeSpent` 等带 persistent meta 的 action。
- idle 处理需要强调“先用 `[Task] Remove time spent` 扣回误计时间，再由用户选择重新归属”，这是理解重复计时 bug 的关键。

## 后续线索

- L3：拆 `src/app/features/tasks/store/task.reducer.ts` 与 `src/app/features/tasks/store/task.reducer.util.ts`，专讲 `timeSpentOnDay`、父子任务增量更新和远端 `syncTimeSpent`。
- L3：拆 `src/app/features/focus-mode/store/focus-mode.effects.ts`，专讲 tracking/focus/break 的双向 effect race guard。
- L4：深挖 `src/app/op-log/sync/operation-write-flush.service.ts`、`src/app/op-log/capture/operation-log.effects.ts` 和 `src/app/op-log/persistence/operation-log-store.service.ts` 的 flush、lock、vector clock 原子性。

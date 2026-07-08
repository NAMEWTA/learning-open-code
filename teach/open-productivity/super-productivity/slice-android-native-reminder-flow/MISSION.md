# 使命：Android 原生提醒调度、AlarmManager、Receiver 与通知 action 全链路

## 为什么
Super Productivity 在 Android 上不依赖 Capacitor LocalNotifications 做定时提醒，而是走 `AlarmManager` + 原生 `BroadcastReceiver`，这样应用被杀死后仍能准时弹出通知，并在通知 action 里完成 Snooze/Done 而无需拉起完整 Web 层。掌握这条 L2 链路后，排查「提醒没响」「重复通知」「通知 Done 后任务状态没更新」「另一台设备已完成后本机仍弹窗」等问题时，能分清是 Angular 调度层、原生闹钟层还是 action 回写层的问题。

## 成功的样子
- 能画出从 `MobileNotificationEffects` 到 `AlarmManager`、再到 `ReminderAlarmReceiver` 弹出通知的时序图。
- 能说明 `ReminderActionReceiver` 如何在后台处理 Snooze/Done，以及 `ReminderDoneQueue` / `ReminderSnoozeQueue` 如何被 Angular 在冷启动或 `onResume` 时消费。
- 能区分 `ReminderAlarmStore`（重启后重注册闹钟）与 `SyncReminderWorker`（跨设备取消/补调度）各自职责。
- 能判断 `ReminderAlarmReceiver.isTaskStale` 的 fail-open 策略何时抑制过期通知。

## 约束条件
- 本主题是 L2 垂直切片，只讲 Android 原生提醒主路径；iOS LocalNotifications 路径仅作对比提及。
- 只写入 `teach/open-productivity/super-productivity/slice-android-native-reminder-flow/`。
- 课程正文控制在短课合约内；长表与完整源码索引放入 reference。
- 源码引用使用仓库内完整相对路径，便于 `generate_snapshot.py` 追踪。

## 不在范围内
- 不展开 NgRx `remindAt` 字段如何由任务编辑 UI 写入（见 `module-task-domain`）。
- 不覆盖 Electron 桌面提醒与 PWA Web Notifications。
- 不讲 SuperSync op-log 全量同步协议，只触及 `SyncReminderWorker` 对提醒的增量管理。

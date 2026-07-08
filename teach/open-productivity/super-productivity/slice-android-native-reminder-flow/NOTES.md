# 教学笔记：Android 原生提醒全链路

- 批量生成模式；默认使命已写入 `MISSION.md`。
- 短课 `0001-flow-map.html` 用 mermaid `sequenceDiagram` 展示调度、触发、action 三阶段；细节表见 reference。
- Android 与 iOS 分叉点在 `CapacitorReminderService.scheduleReminder`；讲 Android 时勿把 LocalNotifications 当主路径。
- `ReminderAlarmReceiver` 的 stale 校验是 fail-open：网络失败时仍弹通知，避免漏提醒。

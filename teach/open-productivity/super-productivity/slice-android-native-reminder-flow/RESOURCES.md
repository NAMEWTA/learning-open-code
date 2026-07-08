# Android 原生提醒全链路资源

## 知识

- [Android AlarmManager 官方文档](https://developer.android.com/reference/android/app/AlarmManager) — `setExactAndAllowWhileIdle` 与精确闹钟权限边界。
- [Android BroadcastReceiver 指南](https://developer.android.com/develop/background-work/background-tasks/broadcasts) — 闹钟触发与通知 action 的 receiver 生命周期。
- `src/app/features/mobile/store/mobile-notification.effects.ts`
  从 NgRx selectors 读取 `remindAt`，调用 `CapacitorReminderService.scheduleReminder` / `cancelReminder` 的主调度 effect。
- `src/app/core/platform/capacitor-reminder.service.ts`
  Android 走 `androidInterface.scheduleNativeReminder`；iOS 走 Capacitor LocalNotifications 的平台分叉点。
- `src/app/features/android/android-interface.ts`
  `SUPAndroid` 桥接类型定义；冷启动时拉取 Done/Snooze/Tap 队列并推入 ReplaySubject。
- `android/app/src/main/java/com/superproductivity/superproductivity/webview/JavaScriptInterface.kt`
  `@JavascriptInterface scheduleNativeReminder` / `cancelNativeReminder` 与队列读取方法。
- `android/app/src/main/java/com/superproductivity/superproductivity/service/ReminderNotificationHelper.kt`
  `AlarmManager` 注册、`NotificationCompat` 构建、Done/Snooze action 的 `PendingIntent`。
- `android/app/src/main/java/com/superproductivity/superproductivity/receiver/ReminderAlarmReceiver.kt`
  闹钟触发后展示通知；触发前可选 SuperSync 快速校验抑制过期提醒。
- `android/app/src/main/java/com/superproductivity/superproductivity/receiver/ReminderActionReceiver.kt`
  通知 action 后台处理：Snooze 重调度、Done 清闹钟并入队。
- `android/app/src/main/java/com/superproductivity/superproductivity/service/ReminderAlarmStore.kt`
  SharedPreferences 持久化闹钟参数，供 `BootReceiver` 在重启/更新后重注册。
- `android/app/src/main/java/com/superproductivity/superproductivity/receiver/BootReceiver.kt`
  监听 `BOOT_COMPLETED` 与 `MY_PACKAGE_REPLACED`，恢复全部未来闹钟。
- `src/app/features/reminder/reminder.module.ts`
  订阅 `onReminderTap$` / `onReminderDone$` / `onReminderSnooze$`，在数据加载后写回 NgRx。
- `android/app/src/main/AndroidManifest.xml`
  三个 reminder 相关 receiver 的注册声明。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)（标签 `android` / `reminder` / `notification`）
  适用于核对精确闹钟权限、后台通知、跨设备提醒竞态等历史修复。
- 本仓库 L1 `teach/open-productivity/super-productivity/module-mobile-pwa-host/`
  适用于回看 Capacitor 宿主、`SUPAndroid` 桥接与移动端整体边界。
- 相邻 L2 `teach/open-productivity/super-productivity/slice-mobile-background-flush-flow/`
  适用于区分提醒 action 队列与 op-log flush / sync 补偿链路。

## 空白

- 未纳入 Capacitor Local Notifications 插件在 Android 上的 fallback 实现细节；本主题以原生 `AlarmManager` 路径为准。
- 未纳入各 OEM 省电策略（小米/华为等）对 `AlarmManager` 的额外限制；排障时需结合设备设置文档。
- 未纳入通知渠道用户自定义与多语言 action 文案；源码中 action 标签为固定英文字符串。

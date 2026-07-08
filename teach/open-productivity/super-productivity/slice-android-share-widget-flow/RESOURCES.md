# Android 分享与 Home Widget 全链路资源

## 知识

- [Android Intent.ACTION_SEND 官方文档](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) — 系统分享 intent 的 `EXTRA_TEXT` / `EXTRA_TITLE` / `EXTRA_SUBJECT` 字段。
- [Android App Widgets 指南](https://developer.android.com/develop/ui/views/appwidgets) — `AppWidgetProvider`、`RemoteViews` 与 `notifyAppWidgetViewDataChanged` 刷新模型。
- [Capacitor Android WebView JavaScript Interface](https://capacitorjs.com/docs/android/custom-code) — `addJavascriptInterface` 与 `evaluateJavascript` 桥接模式（本项目在 `CapacitorMainActivity` 自定义实现）。
- `android/app/src/main/java/com/superproductivity/superproductivity/CapacitorMainActivity.kt`
  分享 intent 解析、`ShareIntentQueue` 持久化、`flushPendingShareIntent` 与 Widget drain 广播注册。
- `android/app/src/main/java/com/superproductivity/superproductivity/widget/TaskListWidgetProvider.kt`
  桌面 Widget 点击处理、`WidgetDoneQueue.setTarget` 与 `ACTION_WIDGET_DONE_DRAIN` 无内容信号。
- `android/app/src/main/java/com/superproductivity/superproductivity/webview/JavaScriptInterface.kt`
  `getPendingShareData`、`getWidgetDoneQueue`、`updateWidget` 等 `@JavascriptInterface` 方法。
- `android/app/src/main/java/com/superproductivity/superproductivity/widget/ShareIntentQueue.kt`
  分享数据 SharedPreferences 持久化（`commit()` 同步写入）。
- `android/app/src/main/java/com/superproductivity/superproductivity/widget/WidgetDoneQueue.kt`
  Widget 勾选 last-wins map；`peek()` 供原生渲染 pending 覆盖层。
- `src/app/features/android/android-interface.ts`
  `SUPAndroid` 类型定义；冷启动 pull 分享/提醒队列；`onWidgetDoneDrainRequest$` Subject。
- `src/app/features/android/store/android.effects.ts`
  `handleShare$` 创建任务与附件；`checkPendingShareOnResume$` 温启动补捞分享。
- `src/app/features/android/store/android-widget.effects.ts`
  Widget 快照推送与 `drainWidgetDoneQueue$`；`getTaskDoneChangesToApply` 过滤逻辑。
- `src/app/features/android/widget-data.service.ts`
  将 `selectAndroidWidgetData` 快照写入 KeyValStore 并触发 `updateWidget()`。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)（标签 `android` / `widget` / `share`）
  适用于核对分享冷启动、Widget 勾选竞态、sync 后 Widget 不刷新等历史修复。
- 本仓库 L1 `teach/open-productivity/super-productivity/module-mobile-pwa-host/`
  适用于回看 Capacitor 宿主、`SUPAndroid` 桥接与移动端整体边界。
- 相邻 L2 `teach/open-productivity/super-productivity/slice-android-native-reminder-flow/`
  适用于对比同类「native 队列 + Angular drain」模式（提醒 Done/Snooze 队列）。

## 空白

- 未纳入 `StartupOverlayManager` 冷启动快速录入与分享 intent 的交互细节。
- 未纳入 `WidgetTaskQueue`（Widget 内新建任务）完整路径；本主题聚焦今日列表勾选与分享。
- 未纳入各 OEM 对后台 `LocalBroadcastManager` 的限制；排障时需结合设备日志。

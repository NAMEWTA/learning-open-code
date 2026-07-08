# 使命：Android 分享 intent、Home Widget、native 队列与 Angular drain 全链路

## 为什么
Super Productivity 在 Android 上既要接住系统「分享到此应用」的冷启动场景，又要让桌面 Widget 在 WebView 未就绪时也能勾选完成任务。两条链路都依赖 SharedPreferences 队列 + `SUPAndroid` 桥的 pull/push 混合交付，而不是单纯靠 Capacitor 插件。掌握这条 L2 切片后，排查「分享没生成任务」「Widget 勾选了但任务没变」「同步后 Widget 列表过期」时，能分清是原生入队、桥接时机还是 Angular drain 层的问题。

## 成功的样子
- 能画出分享 intent 从 `handleIntent` 到 `AndroidEffects.handleShare$` 的时序图，并说明冷启动与温启动两条交付路径。
- 能说明 Widget 今日任务快照如何从 NgRx 推到 `widget_data`，以及 `WidgetDoneQueue` 如何被 `drainWidgetDoneQueue$` 消费。
- 能区分 `ShareIntentQueue`（分享持久化）与 `WidgetDoneQueue`（勾选状态 last-wins map）的写入方与消费方。
- 能判断 `getTaskDoneChangesToApply` 为何跳过已删除或已处于目标状态的任务。

## 约束条件
- 本主题是 L2 垂直切片，只讲分享与 Home Widget 主路径；提醒通知队列仅作对比提及。
- 只写入 `teach/open-productivity/super-productivity/slice-android-share-widget-flow/`。
- 课程正文控制在短课合约内；长表与完整源码索引放入 reference。
- 源码引用使用仓库内完整相对路径，便于 `generate_snapshot.py` 追踪。

## 不在范围内
- 不展开 Widget 布局 XML 与 `RemoteViews` 渲染细节（见 `module-mobile-pwa-host`）。
- 不覆盖 iOS Share Extension 与 iOS Widget。
- 不讲 SuperSync op-log 全量协议，只触及 sync window 结束后 Widget 快照补推。

# 使命：Android 离线启动、legacy WebView 迁移与 Capacitor Activity 切换全链路

## 为什么
Super Productivity 的 Android 端同时承载两代宿主：`FullscreenActivity`（legacy 在线 WebView）与 `CapacitorMainActivity`（离线 Capacitor 桥）。Manifest 仍以 `FullscreenActivity` 为 LAUNCHER，但 `LaunchDecider` 会在冷启动时把新装/离线用户切到 Capacitor。掌握这条 L2 链路后，排查「升级后仍走在线页」「离线包没加载」「WebView 初始化闪退后自动重开」「分享/Widget 冷启动丢事件」等问题时，能分清是 Activity 路由层、WebView 恢复层还是 Angular `SUPAndroid` 桥接层的问题。

## 成功的样子
- 能画出从 LAUNCHER 点击到 `CapacitorMainActivity` 加载离线 bundle、再到 Angular `bootstrap` 的时序图。
- 能说明 `LaunchDecider` 如何在新装、升级（`SupKeyValStore` 存在）与 `BuildConfig.LAUNCH_MODE` 强制值之间选择 `MODE_ONLINE` / `MODE_OFFLINE`。
- 能区分 legacy WebView（`window.SUPAndroid` 存在但 `Capacitor.isNativePlatform()` 为 false）与 Capacitor 原生宿主在平台检测与能力上的差异。
- 能判断 `WebViewRecovery` 的一次性自动重开与 `WebViewBlockActivity` 终端阻断各自何时触发。

## 约束条件
- 本主题是 L2 垂直切片，只讲 Android 冷启动与 Activity 切换主路径；iOS Capacitor 启动仅作对比提及。
- 只写入 `teach/open-productivity/super-productivity/slice-android-offline-startup-flow/`。
- 课程正文控制在短课合约内；长表与完整源码索引放入 reference。
- 源码引用使用仓库内完整相对路径，便于 `generate_snapshot.py` 追踪。

## 不在范围内
- 不展开 NgRx 数据 hydration 与 op-log 加载细节（见 `slice-app-startup-flow`）。
- 不覆盖 Electron 桌面启动链路（见 `slice-electron-startup-close-flow`）。
- 不讲 SuperSync 全量协议，只触及启动时 `SyncReminderScheduler` 与凭证检查。

# 工作笔记

- 短课 `0001-flow-map.html` 用 mermaid `sequenceDiagram` 展示 LAUNCHER → LaunchDecider → Activity 切换 → Angular bootstrap；细节表见 reference。
- legacy WebView 用户仍走 `FullscreenActivity` 加载在线 URL；新装与无 legacy 数据的升级用户经 `LaunchDecider` 切到 `CapacitorMainActivity` 加载离线 bundle。
- `IS_ANDROID_WEB_VIEW`（`window.SUPAndroid`）是 legacy 与 Capacitor 两代的共同桥接检测点；`CapacitorPlatformService.isNative` 显式包含 legacy。
- WebView 初始化失败时 `WebViewRecovery.scheduleRelaunch` 总是回到 `FullscreenActivity`，由 `LaunchDecider` 再次路由到正确 Activity。

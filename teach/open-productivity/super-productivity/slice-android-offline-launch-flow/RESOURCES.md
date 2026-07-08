# Android 离线启动全链路资源

## 知识

- [Capacitor Android 文档](https://capacitorjs.com/docs/android) — `BridgeActivity`、插件注册与 WebView 加载离线 `www` 资源。
- [Android Activity 启动模式](https://developer.android.com/guide/components/activities/tasks-and-back-stack) — `singleTask`、LAUNCHER intent 与 Activity 切换。
- `android/app/src/main/AndroidManifest.xml`
  `FullscreenActivity` 为默认 LAUNCHER；`CapacitorMainActivity` 承载分享/OAuth intent-filter。
- `android/app/src/main/java/com/superproductivity/superproductivity/app/LaunchDecider.kt`
  新装/升级/强制模式判定；`shouldSwitchToNewActivity()` 决定是否切到 Capacitor。
- `android/app/src/main/java/com/superproductivity/superproductivity/FullscreenActivity.kt`
  legacy 在线 WebView 宿主；`onCreate` 首段调用 `LaunchDecider` 后可能 `finish()` 并跳转 Capacitor。
- `android/app/src/main/java/com/superproductivity/superproductivity/CapacitorMainActivity.kt`
  离线 Capacitor 主 Activity；插件注册、`JavaScriptInterface` 注入、启动 overlay、WebView 恢复。
- `android/app/src/main/java/com/superproductivity/superproductivity/webview/WebViewRecovery.kt`
  瞬态 WebView 初始化失败时的一次性自动重开（经 `FullscreenActivity` 回到 `LaunchDecider`）。
- `android/app/src/main/java/com/superproductivity/superproductivity/webview/WebViewCompatibilityChecker.kt`
  WebView 版本预检、阻断屏与重试预算。
- `android/app/src/main/java/com/superproductivity/superproductivity/webview/JavaScriptInterface.kt`
  `SUPAndroid` 桥；`flushPendingShareIntent` 与启动 overlay 回调。
- `android/app/src/main/java/com/superproductivity/superproductivity/widget/StartupOverlayManager.kt`
  冷启动原生添加任务条，与 Angular `StartupOverlayService` 交接。
- `android/README_OFFLINE.md`
  Connectivity-Free Mode 与 `LAUNCH_MODE` 构建配置说明。
- `src/app/util/is-android-web-view.ts`
  `IS_ANDROID_WEB_VIEW = !!window.SUPAndroid`；legacy 与 Capacitor 共用桥接检测。
- `src/app/core/platform/capacitor-platform.service.ts`
  将 legacy WebView 纳入 `isNative` 与 `platform === 'android'` 判定。
- `src/app/features/android/android-interface.ts`
  `SUPAndroid` 类型定义；冷启动拉取分享/提醒/Widget 队列。
- `src/app/features/android/store/android.effects.ts`
  `onResume$` 温启动 drain；与冷启动 `StartupOverlayService` 互补。
- `src/app/core/startup-overlay/startup-overlay.service.ts`
  Angular bootstrap 后处理 overlay 文案与 Widget 任务队列。
- `src/main.ts`
  bootstrap 末尾调用 `StartupOverlayService.processAndDismiss()`。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)（标签 `android` / `webview` / `capacitor`）
  适用于核对 WebView 恢复 #7518、legacy 迁移、键盘/状态栏等历史修复。
- 本仓库 L1 `teach/open-productivity/super-productivity/module-mobile-pwa-host/`
  适用于回看 Capacitor 宿主与移动端整体边界。
- 相邻 L2 `teach/open-productivity/super-productivity/slice-app-startup-flow/`
  适用于区分 Activity 切换完成后的 Angular 数据初始化。
- 相邻 L2 `teach/open-productivity/super-productivity/slice-android-share-widget-flow/`
  适用于分享 intent 与 Widget 队列在冷启动时的 drain 细节。

## 空白

- 未纳入 F-Droid / Play flavor 在 In-App Review 与 `WINDOW_PROPERTY_F_DROID` 上的差异实现。
- 未纳入各 OEM WebView 提供商（三星/华为等）版本检测的完整兼容矩阵。
- 未纳入 `SupKeyValStore` 到 IndexedDB 的数据迁移脚本细节；本主题只以「文件存在 → MODE_ONLINE」为路由依据。

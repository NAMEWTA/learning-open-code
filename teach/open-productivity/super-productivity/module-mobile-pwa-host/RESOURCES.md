# Capacitor 移动端与 PWA 宿主资源

## 知识

- 源码：`open-productivity/super-productivity/src/main.ts`
  Angular bootstrap、Service Worker 条件注册、Capacitor back button、Android/iOS 退后台 flush 的主入口。适用于判断 Web/PWA/native 生命周期边界。
- 源码：`open-productivity/super-productivity/capacitor.config.ts`
  Capacitor appId、webDir、插件配置、Android includePlugins、iOS WebView 行为配置。适用于判断 native shell 配置入口。
- 源码：`open-productivity/super-productivity/android/app/src/main/AndroidManifest.xml`
  Android activity、permission、receiver、foreground service、widget 声明。适用于判断系统能力入口和权限边界。
- 源码：`open-productivity/super-productivity/android/app/src/main/java/com/superproductivity/superproductivity/CapacitorMainActivity.kt`
  新离线 Capacitor Android activity，注册 native plugins、注入 `window.SUPAndroid`、处理 share/reminder/widget/lifecycle。适用于 Android 桥接链路。
- 源码：`open-productivity/super-productivity/android/app/src/main/java/com/superproductivity/superproductivity/webview/JavaScriptInterface.kt`
  Android `@JavascriptInterface` 能力表。适用于从 TypeScript 方法反查 native 实现。
- 源码：`open-productivity/super-productivity/ios/App/App/CustomViewController.swift`
  iOS 自定义 `CAPBridgeViewController`，注册 WebDAV 和 StoreReview 插件。适用于 iOS 自定义 native plugin 边界。
- 源码：`open-productivity/super-productivity/src/app/root-store/feature-stores.module.ts`
  Android/iOS/mobile effects 的条件注册表。适用于判断平台 feature 是否会在当前运行环境启动。
- 源码：`open-productivity/super-productivity/src/app/features/android/`、`src/app/features/ios/`、`src/app/features/mobile/`
  Angular 侧平台 feature。适用于读 share、widget、foreground tracking、focus mode、background tracking、native notification 调度。
- 源码：`open-productivity/super-productivity/ngsw-config.json` 与 `src/manifest.json`
  PWA 缓存组、API freshness cache、manifest standalone/图标/作用域配置。适用于判断浏览器 PWA 行为。
- [Capacitor Configuration 官方文档](https://capacitorjs.com/docs/config)
  用于核对 `webDir`、Android `includePlugins`、iOS WebView 配置等 Capacitor 高层配置项。
- [Angular Service Worker Configuration 官方文档](https://angular.dev/ecosystem/service-workers/config)
  用于核对 `ngsw-config.json` 中 assetGroups 与 dataGroups 的语义。
- [MDN Web App Manifest](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest)
  用于核对 `src/manifest.json` 的 `display`、`start_url`、`scope`、icons 等 PWA manifest 字段。
- [Android WebView `addJavascriptInterface` 官方 API](https://developer.android.com/reference/android/webkit/WebView#addJavascriptInterface(java.lang.Object,%20java.lang.String))
  用于理解 Android `window.SUPAndroid` 暴露 native 方法时的桥接边界。

## 智慧（社区）

- [super-productivity GitHub Issues](https://github.com/johannesjo/super-productivity/issues)
  适用于查找移动端 WebView、Android reminder、PWA 缓存、iOS WebDAV 等真实问题背景。
- [Capacitor GitHub Discussions](https://github.com/ionic-team/capacitor/discussions)
  适用于验证 Capacitor WebView、plugin、native lifecycle 的跨项目经验，但课程判断仍以本仓库源码为准。

## 空白

- 尚未纳入 Google Play / App Store 发布政策细节；本 L1 主题只覆盖运行时宿主边界。
- 尚未纳入每个 Android receiver/service 的完整行为矩阵；后续 L2/L3 需要按 reminder、widget、foreground tracking 分别补。

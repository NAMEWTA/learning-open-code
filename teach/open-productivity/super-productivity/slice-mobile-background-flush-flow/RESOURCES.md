# 移动端后台恢复、持久化刷新与同步补偿全链路资源

## 知识

- [Super Productivity README](../../../../open-productivity/super-productivity/README.md)
  项目定位、平台范围与同步能力概览。适用于确认本切片为什么同时涉及 Web、Android、iOS 与 PWA。
- [源文件：`src/main.ts`](../../../../open-productivity/super-productivity/src/main.ts)
  Angular bootstrap、Capacitor `appStateChange`、`BackgroundTask.beforeExit`、service worker 注册/反注册的主入口。
- [源目录：`src/app/features/android/`](../../../../open-productivity/super-productivity/src/app/features/android/)
  Android WebView 桥、前后台 Subject、前台 tracking service 补时、后台 flush 与 SuperSync 凭证桥。
- [源目录：`src/app/features/ios/`](../../../../open-productivity/super-productivity/src/app/features/ios/)
  iOS `appStateChange` 到 `iosInterface.onResume$` 的桥接，以及恢复后补时/flush 分工。
- [源目录：`src/app/core/data-init/`](../../../../open-productivity/super-productivity/src/app/core/data-init/)
  启动 hydration、`isAllDataLoadedInitially$` 和同步触发订阅的就绪边界。
- [源目录：`src/app/core/persistence/`](../../../../open-productivity/super-productivity/src/app/core/persistence/)
  legacy `pf` 数据库、local/session storage 和旧数据迁移入口，用于区分旧持久化与 `SUP_OPS`。
- [源目录：`src/app/op-log/`](../../../../open-productivity/super-productivity/src/app/op-log/)
  operation capture、flush、hydration、remote apply、download/upload、deferred action 和 validation 的核心实现。
- [配置：`ngsw-config.json`](../../../../open-productivity/super-productivity/ngsw-config.json)
  PWA 缓存边界；用于判断缓存更新是否参与数据落盘与同步。
- [Android 原生入口：`android/app/src/main/java/com/superproductivity/superproductivity/CapacitorMainActivity.kt`](../../../../open-productivity/super-productivity/android/app/src/main/java/com/superproductivity/superproductivity/CapacitorMainActivity.kt)
  `SUPAndroid` 注入、`onPause$`/`onResume$` 推送、intent 队列和前台服务回调边界。
- [Android 原生桥：`android/app/src/main/java/com/superproductivity/superproductivity/webview/JavaScriptInterface.kt`](../../../../open-productivity/super-productivity/android/app/src/main/java/com/superproductivity/superproductivity/webview/JavaScriptInterface.kt)
  Web 层调用原生存储、前台 tracking service、SuperSync 凭证桥的接口定义。

## 智慧（社区）

- [Super Productivity GitHub Discussions](https://github.com/super-productivity/super-productivity/discussions)
  适用于把“后台恢复后丢时/未同步/缓存版本异常”的排查结论拿到维护者社区验证。
- [Super Productivity issue tracker](https://github.com/super-productivity/super-productivity/issues)
  适用于检索具体回归编号，例如后台冻结、IndexedDB 打开失败、sync 状态卡住等历史问题。

## 空白

- Android WorkManager 的提醒同步、Widget 队列和通知 action 只保留边界说明；需要另建 L3/L4 主题细读。
- `@sp/sync-core` 包内部的 `applyRemoteOperations`、`replayOperationBatch` 算法未在本 L2 展开；需要深挖时另建 L4。

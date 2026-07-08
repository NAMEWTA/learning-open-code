# 使命：PWA service worker 缓存、更新检测、API freshness 与 native 注销全链路

## 为什么
Super Productivity 在 Web/PWA 上靠 Angular service worker 缓存壳层与静态资源，在 Capacitor/Electron 上则主动注销 SW，避免 WebView 误走 PWA 路径。学习者需要把「离线能打开」「新版本没生效」「Issue API 读到旧数据」「Android 上通知走哪条分支」这些现象映射到真实源码，而不是把 PWA cache、桌面更新检查、op-log 同步混为一谈。

## 成功的样子
- 能按顺序说明 `ngsw-config.json` → `src/main.ts` 注册/注销 → `InitialPwaUpdateCheckService` → `SyncEffects` 的更新检测时机。
- 能区分 PWA 的 `SwUpdate.checkForUpdate()` 与 Electron 的 `UpdateCheckService`（GitHub releases）各自适用平台。
- 能解释 `api-freshness` dataGroup 覆盖哪些 URL、与 op-log 业务数据无关。
- 能在 native/Electron 场景指出 `main.ts` 为何 `unregister()` 全部 SW，以及 `NotifyService` 为何优先走 Capacitor LocalNotifications。

## 约束条件
- 本主题是 L2 垂直切片，只讲 PWA cache/update 主路径与平台分叉；op-log flush、sync provider 细节见相邻切片。
- 短课控制在 15 分钟内；长入口清单、时序表和排障表放入 reference。
- 只写入 `teach/open-productivity/super-productivity/slice-pwa-cache-update-flow/`。
- 源码中不存在独立的 `src/app/core/pwa/` 目录；PWA 逻辑分散在 `main.ts`、`ngsw-config.json` 与 `core/initial-pwa-update-check.service.ts`。

## 不在范围内
- 不展开 op-log hydration、sync wrapper 或 IndexedDB 持久化算法。
- 不逐行讲解 Angular `@angular/service-worker` 内部实现。
- 不覆盖 Android AlarmManager、iOS URLSession 等 native 提醒/同步细节。

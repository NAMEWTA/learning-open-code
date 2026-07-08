# PWA 缓存与更新全链路资源

## 知识

- [`ngsw-config.json`](../../../../open-productivity/super-productivity/ngsw-config.json)
  Angular service worker 缓存策略：app shell prefetch、criticalAssets、lazy assets 与 `api-freshness` dataGroup。
- [`src/main.ts`](../../../../open-productivity/super-productivity/src/main.ts)
  `ServiceWorkerModule.register`、生产/stage 手动 `register('ngsw-worker.js')`、Electron/native 下 `unregister()` 全链路入口。
- [`src/app/core/initial-pwa-update-check.service.ts`](../../../../open-productivity/super-productivity/src/app/core/initial-pwa-update-check.service.ts)
  PWA 更新检测：`SwUpdate.checkForUpdate()`、8 秒超时、确认对话框与 `window.location.reload()`。
- [`src/app/imex/sync/sync.effects.ts`](../../../../open-productivity/super-productivity/src/app/imex/sync/sync.effects.ts)
  初始同步触发前等待 `afterInitialUpdateCheck$`，避免更新弹窗与首次 sync 争抢。
- [`src/app/core/update-check/update-check.service.ts`](../../../../open-productivity/super-productivity/src/app/core/update-check/update-check.service.ts)
  **桌面 Electron 专用** GitHub releases 版本检查；与 PWA SW 更新是平行机制。
- [`src/app/core/update-check/is-update-check-possible.util.ts`](../../../../open-productivity/super-productivity/src/app/core/update-check/is-update-check-possible.util.ts)
  平台 gate：非 Electron 返回 false，注释明确 Web 走 service worker。
- [`src/app/core/notify/notify.service.ts`](../../../../open-productivity/super-productivity/src/app/core/notify/notify.service.ts)
  PWA 通知经 `ngsw-worker.js` registration；native 优先 Capacitor LocalNotifications。
- [`src/app/core/http/translate-http-loader-with-fallback.class.ts`](../../../../open-productivity/super-productivity/src/app/core/http/translate-http-loader-with-fallback.class.ts)
  离线 i18n 降级；说明 SW cache 被 bypass 时（如 Safari Reading List）的兜底路径。
- [`src/app/util/is-native-platform.ts`](../../../../open-productivity/super-productivity/src/app/util/is-native-platform.ts)
  `IS_NATIVE_PLATFORM` 判定；与 `main.ts` SW 启用条件联动。
- [`angular.json`](../../../../open-productivity/super-productivity/angular.json)
  各 build configuration 的 `serviceWorker: "ngsw-config.json"` 开关。
- [`e2e/tests/app-features/offline-i18n-load-failure.spec.ts`](../../../../open-productivity/super-productivity/e2e/tests/app-features/offline-i18n-load-failure.spec.ts)
  离线 i18n 与 SW cache bypass 的回归测试场景（issue #7854）。
- [Angular Service Worker 官方文档](https://angular.dev/ecosystem/service-workers)
  `assetGroups`、`dataGroups`、`freshness` 策略语义的外部权威来源。
- [相邻参考：Capacitor 移动端与 PWA 宿主](../module-mobile-pwa-host/reference/mobile-pwa-host-overview.html)
  平台边界、manifest、Capacitor config 与 SW 职责对照。
- [相邻参考：移动端后台恢复切片](../slice-mobile-background-flush-flow/reference/mobile-background-flush-flow-reference.html)
  说明 PWA cache 不写业务数据、数据一致性仍靠 op-log/sync。

## 智慧（社区）

- [super-productivity GitHub Issues — service worker / PWA / offline](https://github.com/johannesjo/super-productivity/issues?q=service+worker)
  真实离线、更新、通知与 i18n 故障报告。
- [Issue #7854 — offline i18n load failure](https://github.com/super-productivity/super-productivity/issues/7854)
  Safari Reading List bypass SW 导致 status-0 的修复背景。

## 空白

- 源码无独立 `src/app/core/pwa/` 模块；PWA 逻辑分散于上述文件，本切片以链路串联代替模块 tour。
- `src/app/features/mobile/` 不含 SW 更新代码；移动端 SW 更新仍走 Web 层 `InitialPwaUpdateCheckService`（Capacitor WebView 在 native 壳内通常已注销 SW）。

# iOS WebDAV 桥接与同步 provider 资源

## 知识

- [Capacitor iOS Custom Native Code](https://capacitorjs.com/docs/ios/custom-code) — `CAPBridgeViewController` 子类中 `registerPluginInstance` 的注册模式。
- [Apple URLSessionConfiguration](https://developer.apple.com/documentation/foundation/urlsessionconfiguration) — `requestCachePolicy`、`urlCache` 与默认共享 `URLCache` 行为。
- [Super Productivity sync-and-op-log 文档](https://github.com/super-productivity/super-productivity/tree/master/docs/sync-and-op-log) — 文件型 provider 与 content-rev 冲突模型。
- `ios/App/App/CustomViewController.swift`
  Capacitor 桥加载时注册 `WebDavHttpPlugin` 与 `StoreReviewPlugin`。
- `ios/App/App/WebDavHttpPlugin.swift`
  自定义 `URLSession`（`reloadIgnoringLocalCacheData`、`urlCache = nil`）、`request` 方法与 WebDAV 方法空 body 处理。
- `src/app/op-log/sync-providers/file-based/webdav/capacitor-webdav-http/index.ts`
  `registerPlugin('WebDavHttp')` 与 web 端 `fetch` 回退。
- `src/app/op-log/sync-providers/file-based/webdav/capacitor-webdav-http/app-webdav-native-http.ts`
  将 Capacitor 插件接入 package 的 `NativeHttpExecutor` 端口。
- `packages/sync-providers/src/file-based/webdav/webdav-http-adapter.ts`
  native/fetch 路由、`NO_CACHE_HEADERS`、缓存诊断日志与 CORS 检测。
- `packages/sync-providers/src/file-based/webdav/webdav-base-provider.ts`
  组装 `WebDavHttpAdapter` + `WebdavApi`，实现 `FileSyncProvider` 文件操作。
- `packages/sync-providers/src/file-based/webdav/webdav-api.ts`
  PROPFIND/GET/PUT、content-hash rev、上传前 GET 冲突检测。
- `src/app/op-log/sync-providers/file-based/webdav/webdav.ts`
  `createWebdavProvider()` 注入 `APP_WEBDAV_NATIVE_HTTP` 与平台信息。
- `src/app/op-log/sync-providers/wrapped-provider.service.ts`
  将 WebDAV 包成 `OperationSyncCapable`（`FileBasedSyncAdapterService`）。
- `src/app/imex/sync/sync-wrapper.service.ts`
  同步编排：download 先于 upload、冲突 UI、transient 网络错误重试。
- `src/app/imex/sync/sync-trigger.service.ts`
  自动/手动同步触发与 interval 调度。
- `src/app/features/ios/ios-interface.ts`
  iOS `appStateChange` → `onResume$`；与 WebDAV 桥接解耦，经 flush 间接影响同步时机。
- `packages/sync-providers/tests/file-based/webdav/webdav-http-adapter.spec.ts`
  native 路径 no-cache 请求头与缓存诊断日志回归测试。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)（标签 `sync` / `webdav` / `ios`）
  适用于核对 #7144 类缓存致静默覆盖、iOS SSL/超时错误码等历史修复。
- 本仓库 L1 `teach/open-productivity/super-productivity/module-op-log-sync/`
  适用于回看文件型 provider 与 op-log 快照边界。
- 相邻 L2 `teach/open-productivity/super-productivity/slice-op-log-sync-flow/`
  适用于理解 `SyncWrapperService` 下载/上传顺序与 provider 分叉。
- 相邻 L2 `teach/open-productivity/super-productivity/slice-mobile-background-flush-flow/`
  适用于理解 `ios-interface.onResume$` 如何先于同步触发 flush。

## 空白

- 未纳入 `WebDavHttpPlugin.m` Objective-C 桥接宏细节（仅影响 Capacitor 方法导出）。
- 未纳入 E2E `e2e/tests/sync/webdav-*.spec.ts` 用例矩阵；排障时需结合 CI 日志。
- 未纳入各反向代理/CDN 对 `Cache-Control` 的实际遵从行为；需结合 `cacheHeaders` 诊断日志。

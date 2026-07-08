# 使命：iOS WebDAV Capacitor 插件、URLSession no-cache 与同步 provider 全链路

## 为什么
Super Productivity 在 iOS 上无法像浏览器那样用 `fetch({ cache: 'no-store' })` 访问 WebDAV，也不能依赖 `CapacitorHttp`（对 WebDAV 空响应与 JSON 自动解析有已知缺陷）。项目因此注册了自定义 `WebDavHttp` 插件，并在 `URLSession` 层强制禁用 HTTP 缓存——否则 `sync-data.json` 的 GET 可能返回陈旧副本，既掩盖远端变更，又让上传前的 content-hash 冲突检测失效，导致静默覆盖较新的远端数据（#7144）。掌握这条 L2 切片后，排查「iOS WebDAV 同步丢数据」「双端内容不一致却未报冲突」「恢复前台后未拉取远端」时，能分清是插件注册、no-cache 防线、适配器路由还是 `imex/sync` 编排层的问题。

## 成功的样子
- 能画出从 `SyncWrapperService` 到 `WebDavHttpPlugin.swift` 的时序图，并说明 `CustomViewController` 在何处注册插件。
- 能说明 JS 侧 `WebDavHttpAdapter`、`APP_WEBDAV_NATIVE_HTTP` 与 Swift 侧 `URLSessionConfiguration` 三层 no-cache 各自防什么。
- 能解释 `WebdavApi.upload` 上传前 GET 比对 content-hash 时，为何 iOS 缓存会使冲突检测失效。
- 能区分 `ios-interface.ts` 的 `onResume$`（补时 + flush）与 WebDAV HTTP 桥接的职责边界。

## 约束条件
- 本主题是 L2 垂直切片，聚焦 iOS native WebDAV HTTP 与文件型 sync provider 主路径。
- 只写入 `teach/open-productivity/super-productivity/slice-ios-webdav-bridge-flow/`。
- 课程正文控制在短课合约内；长表与完整源码索引放入 reference。
- 源码引用使用仓库内完整相对路径，便于 `generate_snapshot.py` 追踪。

## 不在范围内
- 不展开 Nextcloud 用户 ID 发现、CalDAV 日历客户端等复用 `WebDavHttp` 的旁路。
- 不覆盖 Android `WebDavHttpPlugin.kt` 实现细节（仅作对比提及）。
- 不讲 SuperSync WebSocket 与 operation API 全量协议；文件型 provider 的 op-log 快照格式见 `slice-op-log-sync-flow`。

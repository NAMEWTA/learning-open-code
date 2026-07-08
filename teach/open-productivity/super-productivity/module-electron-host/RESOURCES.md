# Electron 桌面宿主、窗口、IPC 与系统集成资源

## 知识

- [electron/main.ts](../../../../open-productivity/super-productivity/electron/main.ts)
  单实例入口与 `startApp()` 调用。适用于确认桌面宿主从哪里开始。
- [electron/start-app.ts](../../../../open-productivity/super-productivity/electron/start-app.ts)
  app ready、IPC 初始化、窗口创建、托盘、idle/powerMonitor、协议处理和退出清理的主进程编排入口。适用于建立 L1 总览地图。
- [electron/main-window.ts](../../../../open-productivity/super-productivity/electron/main-window.ts)
  `BrowserWindow` 创建、preload 注入、导航拦截、窗口菜单、关闭前协议和 fullscreen/titlebar 事件。适用于理解窗口安全边界。
- [electron/navigation-guard.ts](../../../../open-productivity/super-productivity/electron/navigation-guard.ts)
  判断主窗口是否仍停留在应用自身 origin。适用于理解为什么外部页面不能进入带 `window.ea` 的特权窗口。
- [electron/open-url.ts](../../../../open-productivity/super-productivity/electron/open-url.ts) 与 [electron/shared-with-frontend/is-external-url-allowed.ts](../../../../open-productivity/super-productivity/electron/shared-with-frontend/is-external-url-allowed.ts)
  外链 scheme allowlist、本地 `file:` URL、UNC/remote file URL 与可执行扩展 guard。适用于核对新窗口、外链和本地路径打开的安全边界。
- [electron/preload.ts](../../../../open-productivity/super-productivity/electron/preload.ts)
  通过 `contextBridge.exposeInMainWorld('ea', ea)` 暴露 typed bridge。适用于判断 renderer 如何调用桌面能力。
- [electron/electronAPI.d.ts](../../../../open-productivity/super-productivity/electron/electronAPI.d.ts)
  `window.ea` 的 TypeScript 契约清单。适用于从 renderer 调用反查 IPC 能力。
- [electron/ipc-handler.ts](../../../../open-productivity/super-productivity/electron/ipc-handler.ts) 与 [electron/ipc-handlers/](../../../../open-productivity/super-productivity/electron/ipc-handlers/)
  IPC handler 聚合与 app-control、app-data、system、global-shortcuts、jira 子入口。适用于定位主进程 handler。
- [electron/indicator.ts](../../../../open-productivity/super-productivity/electron/indicator.ts)
  tray、当前任务、进度图标和 task widget 联动。适用于桌面状态展示问题。
- [electron/local-file-sync.ts](../../../../open-productivity/super-productivity/electron/local-file-sync.ts)
  LocalFile provider 的主进程文件桥。适用于本地文件同步与路径安全边界。
- [electron/plugin-node-executor.ts](../../../../open-productivity/super-productivity/electron/plugin-node-executor.ts) 与 [electron/plugin-oauth.ts](../../../../open-productivity/super-productivity/electron/plugin-oauth.ts)
  插件 Node 执行授权、脚本执行、OAuth loopback 和系统浏览器打开。适用于插件桌面能力排查。
- [electron/local-rest-api.ts](../../../../open-productivity/super-productivity/electron/local-rest-api.ts)
  本地 HTTP API 的主进程 server 与 renderer 转发桥。适用于 CLI/脚本接入桌面应用。
- [Electron BrowserWindow 官方文档](https://www.electronjs.org/docs/latest/api/browser-window)
  `BrowserWindow`、`webPreferences`、preload、context isolation 与窗口事件说明。适用于核对窗口配置含义。
- [Electron contextBridge 官方文档](https://www.electronjs.org/docs/latest/api/context-bridge)
  preload 隔离上下文向 renderer 暴露 API 的官方说明。适用于判断 bridge 设计是否合理。
- [Electron ipcMain 官方文档](https://www.electronjs.org/docs/latest/api/ipc-main)
  主进程 IPC 监听与 `handle`/`invoke` 模型说明。适用于对照本项目 IPC 注册方式。
- [Electron Security 官方教程](https://www.electronjs.org/docs/latest/tutorial/security)
  Electron 安全建议。适用于理解为什么主窗口关闭 Node integration、启用 context isolation，并阻断非应用 origin 导航。

## 智慧（社区）

- [super-productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)
  适用于验证桌面启动、托盘、Linux/Wayland、插件权限、文件同步和本地 REST API 的真实问题背景。
- [super-productivity GitHub Pull Requests](https://github.com/super-productivity/super-productivity/pulls)
  适用于观察 Electron 边界变更、窗口安全加固和 IPC 测试补充的评审上下文。

## 空白

- 本课未扩展到 Electron 打包、自动更新、代码签名、公证和各应用商店分发资料；后续进入发布链路时应单独补充官方打包与平台规范。

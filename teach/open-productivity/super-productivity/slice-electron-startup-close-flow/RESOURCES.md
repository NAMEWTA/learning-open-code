# Electron 启动、窗口创建与关闭前同步全链路资源

## 知识

- [Electron 官方文档：app API](https://www.electronjs.org/docs/latest/api/app)
  用于核对 `requestSingleInstanceLock`、`ready`、`before-quit`、`window-all-closed` 等进程级生命周期事件。
- [Electron 官方文档：BrowserWindow](https://www.electronjs.org/docs/latest/api/browser-window)
  用于核对窗口创建参数、`loadURL`、`ready-to-show`、`close`、`closed` 等窗口生命周期语义。
- [Electron 官方文档：ipcMain](https://www.electronjs.org/docs/latest/api/ipc-main)
  用于区分 `ipcMain.on` 单向事件和 `ipcMain.handle`/`ipcRenderer.invoke` 请求响应式本地能力。
- [Electron 官方文档：contextBridge](https://www.electronjs.org/docs/latest/api/context-bridge)
  用于理解 preload 在 `contextIsolation: true` 下暴露 `window.ea` 的责任边界。
- [Angular 官方文档：bootstrapApplication](https://angular.dev/api/platform-browser/bootstrapApplication)
  用于区分 Angular renderer bootstrap 与 Electron main process 启动流程。
- 源码：`electron/main.ts`、`electron/start-app.ts`、`electron/main-window.ts`
  本主题的主进程入口、app 事件注册、窗口创建与关闭保护核心源码。
- 源码：`electron/ipc-handler.ts`、`electron/ipc-handlers/`、`electron/preload.ts`
  本主题的 IPC 注册、本地能力处理器和 renderer bridge 核心源码。
- 源码：`src/app/core/electron/exec-before-close.service.ts`、`src/app/imex/sync/sync.effects.ts`、`src/app/features/finish-day-before-close/`
  本主题的 renderer 侧关闭前等待项、同步保护和 finish-day 决策源码。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)
  适用于验证启动黑屏、托盘、退出、同步失败等用户真实故障场景。
- [Electron 官方 Discord 与社区入口](https://www.electronjs.org/community)
  适用于核对跨平台窗口生命周期和 Electron 版本行为差异。

## 空白

- 本主题未引入外部博客或二手教程；窗口关闭和 IPC 行为以官方文档与当前源码为准。
- 同步算法内部、插件 Node 执行授权、托盘任务组件适合拆成后续 L3/L4 主题，不在本资源清单展开。

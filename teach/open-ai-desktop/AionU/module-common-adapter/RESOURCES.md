# Common adapter 与 API 映射资源

## 知识

- 仓库源码：`open-ai-desktop/AionU/packages/desktop/src/common/adapter/main.ts`
  main 侧统一桥接入口。适用于：理解 `office-ai-bridge-adapter` 如何接收 renderer 请求、广播回窗口并转发给 WebSocket 客户端。
- 仓库源码：`open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts`
  本主题的核心接口总表。适用于：按能力域查看某个接口最终落在 IPC、HTTP 还是 WS。
- 仓库源码：`open-ai-desktop/AionU/packages/desktop/src/common/adapter/httpBridge.ts`
  HTTP/WS 工厂层。适用于：理解 `httpGet/httpPost/wsEmitter` 如何伪装成 `bridge.buildProvider/buildEmitter` 的同形接口。
- 仓库源码：`open-ai-desktop/AionU/packages/desktop/src/common/adapter/apiModelMapper.ts`
  典型 mapper 示例。适用于：理解 conversation / model 相关 payload 为何需要在前后端之间重写字段与默认语义。
- 仓库源码：`open-ai-desktop/AionU/packages/desktop/src/common/adapter/teamMapper.ts`
  team 领域映射器。适用于：看 role、status、workspace mode 等值如何在后端枚举和前端状态间归一化。
- 仓库源码：`open-ai-desktop/AionU/packages/desktop/src/common/adapter/fileSnapshotMapper.ts`、`workspaceMapper.ts`
  小而关键的修正案例。适用于：理解 snake_case / camelCase、绝对路径 / 相对路径不一致时为什么必须有 mapper。
- 仓库源码：`open-ai-desktop/AionU/packages/desktop/src/preload/main.ts`
  renderer 与 main 的第一层边界。适用于：确认 `electronAPI.emit/on` 如何把统一 adapter channel 暴露给 renderer。
- 仓库源码：`open-ai-desktop/AionU/packages/desktop/src/process/bridge/index.ts`
  main 侧 provider 注册入口。适用于：理解哪些能力仍保留在 Electron IPC。
- 测试辅助：`open-ai-desktop/AionU/tests/e2e/helpers/httpBridge.ts`
  从测试角度复述 adapter 设计。适用于：确认 renderer 迁移到 HTTP 后，E2E 如何在同一网络上下文里直驱 backend。
- [Electron contextBridge](https://electronjs.org/docs/latest/api/context-bridge)
  Electron 官方 API。适用于：理解 preload 为什么应该只暴露最小白名单能力。
- [Electron ipcMain](https://electronjs.org/docs/latest/api/ipc-main)
  Electron 官方 API。适用于：理解 `ipcMain.handle()` 与 `ipcRenderer.invoke()` 的配对语义。
- [Electron IPC Tutorial](https://electronjs.org/docs/latest/tutorial/ipc)
  Electron 官方教程。适用于：对照 AionU 的自定义 channel 命名和主渲染进程协作模式。
- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
  浏览器 WebSocket 一手文档。适用于：理解 `wsEmitter`、自动重连和浏览器侧实时事件消费模型。

## 智慧（社区）

- AionU 仓库现有教学主题：`teach/open-ai-desktop/AionU/module-preload-ipc/`、`teach/open-ai-desktop/AionU/module-renderer-core/`
  最贴近当前代码库的“社区上下文”。适用于：把 common adapter 放回已完成模块的叙事链中，避免孤立看桥接层。
- Electron 官方 Discord / 社区入口：<https://www.electronjs.org/community>
  适用于：当你需要确认跨进程安全边界、context isolation 或 IPC 设计惯例时，优先对照官方社区讨论。

## 空白

- 当前主题没有直接对应 AionU backend Rust 路由实现的教学文档；若后续要把 `/api/*` 路径继续追到底，需要新增 backend 侧专题。
- `ipcBridge.ts` 覆盖面非常大，本轮只做 L1 总览；若要学习某一域，例如 `mcpService`、`channel`、`cron`，需要拆出独立 L2/L3 主题。

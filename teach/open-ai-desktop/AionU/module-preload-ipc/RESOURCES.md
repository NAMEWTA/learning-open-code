# Preload 与 IPC 安全边界 资源

## 知识

- [源码：`packages/desktop/src/preload/main.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/preload/main.ts)
  主窗口 preload 的一手入口。适用于：理解 `contextBridge` 暴露面、同步注入的 backend 状态、托盘事件转 DOM 事件。
- [源码：`packages/desktop/src/common/adapter/main.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/adapter/main.ts)
  renderer 与 main 之间的统一桥。适用于：梳理 `ADAPTER_BRIDGE_EVENT_KEY`、`ipcMain.handle`、窗口广播和超大 payload 保护。
- [源码：`packages/desktop/src/process/bridge/`](../../../../open-ai-desktop/AionU/packages/desktop/src/process/bridge)
  主进程桥接集合。适用于：查看哪些能力被注册成 provider，以及哪些事件会回推给 renderer。
- [源码：`packages/desktop/src/common/adapter/ipcBridge.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts)
  IPC 契约定义。适用于：按域查看窗口控制、dialog、theme、webui、application 等接口名。
- [测试：`tests/unit/feedback/feedbackBridge.test.ts`](../../../../open-ai-desktop/AionU/tests/unit/feedback/feedbackBridge.test.ts)
  反馈桥的行为佐证。适用于：确认 `feedback:capture-screenshot`、`feedback:collect-logs` 的预期返回与失败分支。
- [课程：L0 项目地图](../00-overview/lessons/0001-project-map.html)
  主题前置总览。适用于：先建立 AionU 的三进程坐标，再进入本模块。

## 智慧（社区）

- 本仓库教学工作区：`teach/open-ai-desktop/AionU/`
  适用于：结合后续模块课交叉验证 preload、main、renderer 三方边界，不把单文件理解当成整体结论。

## 空白

- 目前未补充外部 Electron 官方安全文档摘录；若后续要补 L2/L3 安全专题，应增加 Electron `contextIsolation`、`contextBridge`、IPC 安全实践的一手资料。

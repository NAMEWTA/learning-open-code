# REST/WS adapter 替代传统 IPC 的设计资源

## 知识

- [`packages/desktop/src/common/adapter/ipcBridge.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts)
  本主题的主证据。文件头直接说明旧 IPC bridge 已被 REST/WS adapter 替换，Electron-native 能力保留 IPC；后续导出体现每个能力域的真实传输选择。
- [`packages/desktop/src/common/adapter/httpBridge.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/adapter/httpBridge.ts)
  解释 provider-like invoke、HTTP 响应解包、`BackendHttpError`、WebUI same-origin 分支、WS singleton、`wsEmitter/wsMappedEmitter` 的核心实现。
- [`packages/desktop/src/common/adapter/browser.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/adapter/browser.ts)
  对照 Electron renderer 与 WebUI browser 两种运行时：有 preload 时复用 `electronAPI`，无 preload 时用 `/ws` 建立浏览器 runtime bridge。
- [`packages/desktop/src/common/adapter/main.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/adapter/main.ts)
  main 侧传统 bridge adapter：统一 channel、窗口广播、payload 上限、WebSocket broadcaster 注册点。用于区分“传统 bridge 事件回流”和后端实时事件。
- [`packages/desktop/src/preload/main.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/preload/main.ts)
  说明 `window.__backendPort` 如何通过 preload 暴露给 renderer，让 HTTP helper 和 E2E helper 走同一后端端口。
- [`tests/e2e/helpers/httpBridge.ts`](../../../../open-ai-desktop/AionU/tests/e2e/helpers/httpBridge.ts)
  E2E 直接在 renderer context 里发 HTTP 请求，验证 backend 状态时复用和 app 相同的端口、base URL、响应解包规则。
- [`tests/e2e/helpers/bridge/invoke.ts`](../../../../open-ai-desktop/AionU/tests/e2e/helpers/bridge/invoke.ts)
  E2E 兼容层：优先把 legacy dotted IPC key 映射到 HTTP route，找不到 route 才回落到旧 `subscribe-*` IPC 协议。
- [`packages/desktop/src/common/api/*`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/api/)
  相邻但不同的 common API：它负责多 provider client、协议转换和 key 轮转，不是 renderer adapter 的 REST 路由层。维护时要避免把两个 `api` 概念混在一起。

## 智慧（社区）

- [AionUi GitHub 仓库](https://github.com/iOfficeAI/AionUi)
  适用于查看真实 PR、issue、release 讨论，特别是 adapter 迁移、WebUI、E2E 稳定性和后端边界变更。

## 空白

- 未找到专门讨论 AionU adapter 迁移设计的外部架构文档；本主题以源码、E2E helper 和已生成的 L1/L2 教学材料作为主要证据。
- 同级 L3 API 参考尚未生成，因此本主题不会假设已有完整 route contract 文档。

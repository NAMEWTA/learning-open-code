# Backend 启动失败恢复全链路资源

## 知识

- `packages/desktop/src/index.ts`
  Electron main 入口。用于确认 backend 启动失败状态、同步 IPC 查询、数据库恢复 IPC handler、默认桌面模式失败后继续创建窗口的行为。
- `packages/desktop/src/process/startup/backendStartupFailure.ts`
  失败分类器。用于判断 reason 优先级、安装资源缺失识别、GLIBC 不兼容、数据库边界阶段和通用失败兜底。
- `packages/desktop/src/process/startup/recoverCorruptedDatabase.ts`
  可恢复数据库损坏的确认后动作。用于确认恢复动作必须处在 recoverable failure 状态，并按 stop、restart、markReady、reload 顺序执行。
- `packages/desktop/src/preload/main.ts`
  Electron contextBridge 边界。用于确认 renderer 如何读取 startup failure，以及恢复按钮如何调用 `backend:recover-corrupted-database`。
- `packages/desktop/src/renderer/main.tsx`
  React 根入口。用于确认 failure dialog 与正常 AppProvider/Router 二选一。
- `packages/desktop/src/renderer/components/layout/InstallationIntegrityDialog.tsx`
  安装完整性与本地数据故障弹窗。用于确认下载、诊断上报和可恢复数据库重建按钮的 UI 行为。
- `tests/unit/bootstrap/backendStartupFailure.test.ts`
  分类器与弹窗 action 的单元证据。用于确认各 reason 的输入签名和 UI action 分流。
- `tests/unit/bootstrap/recoverCorruptedDatabase.test.ts`
  数据库恢复动作的单元证据。用于确认非 recoverable 状态会拒绝，重启失败不会 mark ready 或 reload。
- `tests/unit/bootstrap/recoverCorruptedDatabasePreload.test.ts`
  preload IPC 暴露的单元证据。用于确认 renderer 调用会落到 main 的恢复 channel。
- `tests/e2e/specs/installation-integrity.e2e.ts`
  安装完整性弹窗 E2E 证据。用于确认 debug 注入的 incomplete installation 会显示弹窗、诊断按钮和下载按钮，并记录用户诊断上报。
- `teach/open-ai-desktop/AionU/slice-desktop-startup/reference/desktop-startup-flow-map.html`
  关联 L2。用于回看普通桌面启动到首屏的正常链路，以及 backend failure 作为启动边界的所在位置。

## 智慧（社区）

- 暂未收录外部社区讨论。本主题是源码考古切片，可靠依据以 AionU 当前源码、单元测试和 E2E 测试为准。

## 空白

- 没有覆盖 aioncore 内部产生 `BOOTSTRAP_DATA_INIT_FAILED` 的 Rust 或后端实现来源；本主题只解释 Electron 桌面壳如何消费这些 boundary code 与 stage。

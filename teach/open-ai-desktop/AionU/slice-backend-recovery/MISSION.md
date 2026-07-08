# 使命：Backend 启动失败恢复全链路

## 为什么
用户需要在 AionU 桌面启动失败时，能从 Electron main 的错误分类一路追到 renderer 可见弹窗，并判断哪些失败可以引导用户恢复，哪些只能提示诊断或重新安装。掌握这条链路后，后续修改启动、安装完整性或数据库恢复逻辑时，可以避免把窗口出现误判为 backend 已可用。

## 成功的样子
- 能按源码说清 backend 启动失败如何被分类并传入 renderer。
- 能区分安装资源缺失、数据库迁移失败、本地数据修复失败和可恢复数据库损坏的 UI 行为。
- 能解释“确认重建数据库”如何从 renderer 经 preload IPC 回到 main 并重新启动 backend。
- 能用 unit 与 E2E 测试界定本链路已经证明和没有证明的范围。

## 约束条件
- 源项目 `open-ai-desktop/AionU/` 只读。
- 本主题只写入 `teach/open-ai-desktop/AionU/slice-backend-recovery/`。
- 保持 L2 垂直切片粒度，不扩写为完整桌面启动百科。

## 不在范围内
- 不讲 aioncore 内部数据库修复算法。
- 不讲普通会话、Team、Cron 或 WebUI 业务链路。
- 不把通用 app-launch 烟雾测试当作安装完整性恢复链路的直接证明。

# Backend lifecycle 与 SQLite 竞争规避资源

## 知识

- `open-ai-desktop/AionU/packages/web-host/src/backend-launcher.ts`
  BackendLifecycleManager 的主证据：状态、端口、spawn 参数、健康检查、停止、崩溃重启和错误详情。
- `open-ai-desktop/AionU/packages/web-host/src/backend-launcher.test.ts`
  行为证据：等待 aioncore 报告端口、传递 `--data-dir`、记录数据库边界错误、限制恢复标志复用。
- `open-ai-desktop/AionU/packages/desktop/src/index.ts`
  Desktop main 的编排证据：先初始化 process，再启动 backend；WebUI 分支复用已经启动的 backend。
- `open-ai-desktop/AionU/packages/desktop/src/process/startup/backendStartup.ts`
  启动策略包装：成功暴露端口，失败采集诊断，按模式决定是否退出。
- `open-ai-desktop/AionU/packages/desktop/src/process/utils/webuiConfig.ts`
  桌面设置页 WebUI 复用 backend 的直接证据，并解释 `dataDir` 必须与桌面 IPC 路径一致。
- `open-ai-desktop/AionU/packages/desktop/src/process/services/database/`
  legacy SQLite 迁移、driver、schema pragma 和连接关闭契约，是理解竞争窗口的本地证据。
- `teach/open-ai-desktop/AionU/module-web-runtime/reference/web-runtime-overview.html`
  L1 前置资料：WebHost/WebCLI 的入口、接口和分层。
- `teach/open-ai-desktop/AionU/module-process-infra/reference/process-infra-overview.html`
  L1 前置资料：main process 基础设施、initStorage 和 database 服务位置。
- `teach/open-ai-desktop/AionU/slice-webui-remote/reference/webui-remote-flow-map.html`
  L2 前置资料：WebUI 入口如何选择 `useExistingBackend`。
- `teach/open-ai-desktop/AionU/slice-backend-recovery/reference/backend-recovery-flow-map.html`
  L2 前置资料：backend failure UI 与可恢复数据库损坏路径。

## 智慧（社区）

- 本主题当前不推荐外部社区作为主要来源。它关注 AionU 当前源码中的进程生命周期与本地数据目录契约，最可靠反馈来自维护时复现、单元测试和启动日志。

## 空白

- 缺少 aioncore Rust 侧 SQLite 打开、migration、恢复标志消费的源码剖析。本课只从 TypeScript main/WebHost 侧说明 owner、数据目录和错误边界。
- 缺少真实用户环境中的 `database is locked` 诊断样本。后续若有崩溃报告或 Sentry 事件，应补充到 reference 的故障判断表。

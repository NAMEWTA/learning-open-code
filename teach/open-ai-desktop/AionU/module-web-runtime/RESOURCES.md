# WebHost 与 WebCLI 运行时 资源

## 知识

- [`open-ai-desktop/AionU/packages/web-host/src/index.ts`](../../../../open-ai-desktop/AionU/packages/web-host/src/index.ts)
  `@aionui/web-host` 的一手组合入口。适用于：确认 `startWebHost()` 只负责编排 backend 与 static server，而不持有配置真相。
- [`open-ai-desktop/AionU/packages/web-host/src/backend-launcher.ts`](../../../../open-ai-desktop/AionU/packages/web-host/src/backend-launcher.ts)
  backend 生命周期核心实现。适用于：理解端口选择、spawn 参数、健康检查、超时诊断与停止策略。
- [`open-ai-desktop/AionU/packages/web-host/src/static-server.ts`](../../../../open-ai-desktop/AionU/packages/web-host/src/static-server.ts)
  WebUI 静态服务与反向代理实现。适用于：理解 SPA 资源、`/api/*` 代理，以及 `/ws`、`/api/stt/stream` 的 TCP splice 设计。
- [`open-ai-desktop/AionU/packages/web-cli/src/index.ts`](../../../../open-ai-desktop/AionU/packages/web-cli/src/index.ts)
  独立 CLI 启动入口。适用于：确认参数解析、资源目录推断、frontend-only 降级、`resetpass` 和信号退出链。
- [`open-ai-desktop/AionU/packages/web-cli/src/browser.ts`](../../../../open-ai-desktop/AionU/packages/web-cli/src/browser.ts)
  浏览器自动打开策略。适用于：解释为什么本地模式默认自动打开浏览器，而远程模式默认不打开。
- [`open-ai-desktop/AionU/packages/web-cli/src/ensureAdminPassword.ts`](../../../../open-ai-desktop/AionU/packages/web-cli/src/ensureAdminPassword.ts)
  首启管理员密码自举逻辑。适用于：理解 `needs_setup` 探测、`/api/webui/reset-password` 调用和提示文案约束。
- [`open-ai-desktop/AionU/packages/web-host/tests/start-web-host.test.ts`](../../../../open-ai-desktop/AionU/packages/web-host/tests/start-web-host.test.ts)
  组合器级测试证据。适用于：验证 `startWebHost()` 的职责边界确实被压缩为“起 backend、起 static-server、返回 handle”。
- [`open-ai-desktop/AionU/packages/web-host/src/static-server.unit.test.ts`](../../../../open-ai-desktop/AionU/packages/web-host/src/static-server.unit.test.ts)
  静态服务和代理行为测试。适用于：确认 `/login`、`/logout`、`/api/*`、WebSocket upgrade 和 SPA fallback 的外部行为。
- [`open-ai-desktop/AionU/tests/unit/web-cli/ensureAdminPassword.test.ts`](../../../../open-ai-desktop/AionU/tests/unit/web-cli/ensureAdminPassword.test.ts)
  WebCLI 首启密码与容错测试。适用于：确认轮询、默认用户名回退、`resetCommand` 传播和警告分支。
- [`open-ai-desktop/AionU/docs/guides/webui.md`](../../../../open-ai-desktop/AionU/docs/guides/webui.md)
  面向用户的 WebUI 启动指南。适用于：把 CLI 能力映射到跨平台启动方式与远程访问场景。
- [Node.js `http` 模块文档](https://nodejs.org/api/http.html)
  本模块依赖的官方网络原语。适用于：对照 `http.createServer()`、代理请求与 socket 生命周期的基础行为。

## 智慧（社区）

- [AionUi Issues](https://github.com/iOfficeAI/AionUi/issues)
  官方问题追踪区。适用于：查 WebUI 启动、打包、远程访问或 Bun/Node 兼容问题是否已有真实案例与维护者结论。

## 空白

- 仓库内缺少专门面向 `packages/web-host` 的架构说明文档，当前主要依赖源码头注释和测试反推设计意图
- `docs/guides/webui.md` 更偏用户操作手册，缺少 “CLI 参数 -> 运行时实现” 的开发者视角，需要本主题补齐

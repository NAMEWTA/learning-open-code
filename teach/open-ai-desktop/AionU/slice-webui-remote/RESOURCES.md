# WebUI 启动与远程访问资源

## 知识

- [L0：AionU 项目总览参考](../00-overview/reference/00-overview.html)
  用于确认 WebUI 在整体架构中的位置：Electron main、WebHost、WebCLI、renderer 和 backend 的关系。
- [L1：WebHost 与 WebCLI 运行时参考](../module-web-runtime/reference/web-runtime-overview.html)
  用于快速回看 `web-host`、`web-cli`、静态服务、首启密码和远程访问的模块边界。
- [L1：Electron 主入口与生命周期参考](../module-main-entry/reference/main-entry-overview.html)
  用于定位 `packages/desktop/src/index.ts` 的运行模式分支和 `--webui` headless 路径。
- [L1：docs/resources 模块参考](../module-docs-resources/reference/docs-resources-overview.html)
  用于判断 `docs/guides/webui.md` 属于用户操作指南，并注意文档可能滞后于实现。
- `open-ai-desktop/AionU/packages/desktop/src/index.ts`
  Electron 主入口，包含 `--webui`、`--remote`、`--resetpass` 分支和 WebHost 启动调用。
- `open-ai-desktop/AionU/packages/desktop/src/process/utils/webuiConfig.ts`
  WebUI 端口、远程访问、用户配置、桌面偏好恢复和桌面管理式 WebUI 生命周期。
- `open-ai-desktop/AionU/packages/web-host/src/index.ts`
  WebHost 组合入口，决定使用已有 backend 还是独立启动 backend，并启动静态服务。
- `open-ai-desktop/AionU/packages/web-host/src/static-server.ts`
  静态资源服务、API 代理、登录路径转发、WebSocket/STT TCP splice 和远程绑定边界。
- `open-ai-desktop/AionU/packages/web-cli/src/index.ts`
  独立 `aionui-web` CLI 的命令、路径、端口、远程访问、frontend-only 降级和 resetpass。
- `open-ai-desktop/AionU/packages/web-cli/src/ensureAdminPassword.ts`
  首次启动管理员密码自举逻辑，说明密码生成失败时不阻断服务启动。
- `open-ai-desktop/AionU/docs/guides/webui.md`
  用户指南，提供跨平台启动和远程访问说明；本主题会标注其中默认端口和排障端口的漂移。
- `open-ai-desktop/AionU/tests/e2e/specs/webui.e2e.ts`
  Playwright E2E 证据，验证 WebUI 设置页、默认端口展示、远程开关和启停切换。

## 智慧（社区）

- AionU 源仓 issue 与 PR 讨论
  适用于确认 WebUI 行为变更、文档漂移和远程访问安全边界的历史语境。当前课程只使用本地源码快照，不依赖实时社区结论。

## 空白

- 本轮未联网检索外部社区反馈；远程访问的安全默认值以当前源码和测试为准。
- aioncore 认证接口的服务端实现不在本主题必读清单内；本主题只从 WebUI 调用侧描述 `/api/auth/status` 与 `/api/webui/reset-password` 的使用边界。

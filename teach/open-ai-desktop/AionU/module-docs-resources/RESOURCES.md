# AionU docs/resources 模块资源

## 知识

- [L0 项目总览参考](../00-overview/reference/00-overview.html)
  本模块的上游锚点。适用于确认 AionU 的总体架构、顶层目录职责和后续 L1 模块拆分。
- [AionU root README](../../../../open-ai-desktop/AionU/readme.md)
  产品叙事、README 多语言入口、资源图片引用和社区链接。适用于判断 `resources/` 哪些资产承担用户侧说明职责。
- [Docs README](../../../../open-ai-desktop/AionU/docs/README.md)
  文档按读者意图分层的总入口。适用于区分 guides、contributing、architecture、specs、prds、readme 的预期边界。
- [File structure guide](../../../../open-ai-desktop/AionU/docs/contributing/file-structure.md)
  目录放置规则、进程边界、命名规则、UI/CSS/test 约束。适用于判断新文档或新源码应放到哪里。
- [Development guide](../../../../open-ai-desktop/AionU/docs/contributing/development.md)
  本地开发、AionCore 前置条件、脚本参考和多实例开发说明。适用于贡献者入口和脚本文档漂移检查。
- [WebUI guide](../../../../open-ai-desktop/AionU/docs/guides/webui.md)
  WebUI 模式跨平台启动、远程访问和排障说明。适用于连接 `module-web-runtime`。
- [Headless deployment guide](../../../../open-ai-desktop/AionU/docs/guides/deploy-server.md)
  无头服务器部署、Xvfb、远程访问、代理自动回退。适用于理解 WebUI 运行形态的用户文档。
- [Hub testing guide](../../../../open-ai-desktop/AionU/docs/guides/hub-testing.md)
  Hub backend 测试分层、fixture extension 和 ACP smoke。适用于扩展示例与测试证据。
- [Theme token reference](../../../../open-ai-desktop/AionU/docs/theming/tokens.md)
  AionU 主题 token 权威清单。适用于理解 `examples/*/themes` 与 UI 主题系统的契约。
- [Root package.json](../../../../open-ai-desktop/AionU/package.json)
  脚本、依赖、Node engine、aioncoreVersion。适用于确认 docs 中的脚本说明是否与真实命令一致。
- [Electron Vite config](../../../../open-ai-desktop/AionU/packages/desktop/electron.vite.config.ts)
  renderer `publicDir`、多页面入口和静态拷贝配置。适用于判断 `public/` 如何进入 renderer/WebUI。
- [Electron Builder config](../../../../open-ai-desktop/AionU/packages/desktop/electron-builder.yml)
  `public/**/*`、extraResources、icons、bundled-aioncore、hub 和平台打包资源。适用于连接 `module-build-release`。
- [PWA service worker](../../../../open-ai-desktop/AionU/public/sw.js)
  WebUI 缓存策略、离线 fallback 和脚本/style content-type 防护。适用于理解 `public/` 的运行时职责。
- [PWA manifest](../../../../open-ai-desktop/AionU/public/manifest.webmanifest)
  WebUI PWA 名称、图标、scope、theme_color。适用于解释浏览器安装入口。
- [PWA registration](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/services/registerPwa.ts)
  运行时注册 `./sw.js` 的入口。适用于把 `public/sw.js` 连接到 renderer。
- [Pet renderer](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pet/petRenderer.ts)
  通过 `../pet-states/*.svg` 加载桌面宠物状态。适用于说明 `public/pet-states` 是运行时资源。
- [Extension hello-world manifest](../../../../open-ai-desktop/AionU/examples/hello-world-extension/aion-extension.json)
  全量扩展示例，覆盖 acpAdapters、mcpServers、assistants、agents、skills、themes、settingsTabs。
- [E2E full extension manifest](../../../../open-ai-desktop/AionU/examples/e2e-full-extension/aion-extension.json)
  E2E fixture 示例，覆盖 channelPlugins、themes、assistants、settingsTabs 等贡献类型。
- [Feishu extension manifest](../../../../open-ai-desktop/AionU/examples/ext-feishu/aion-extension.json)
  WebUI extension routes、static assets 和 channel plugin 示例。适用于扩展 WebUI 贡献边界。
- [WeCom extension README](../../../../open-ai-desktop/AionU/examples/ext-wecom-bot/README.md)
  企业微信 Bot 示例运行方式和 webhook URL。适用于远程渠道示例。
- [Extension API surface in ipcBridge](../../../../open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts)
  renderer 查询 extension themes、assistants、agents、skills、settings tabs、WebUI contributions 的 HTTP adapter。
- [Extension capabilities E2E](../../../../open-ai-desktop/AionU/tests/e2e/specs/ext-capabilities.e2e.ts)
  验证扩展 contribute 类型都可加载、可查询、可打开。适用于把 examples 与实际 UI 查询面连接起来。
- [Hub types](../../../../open-ai-desktop/AionU/packages/desktop/src/common/types/agent/hub.ts)
  AionHub index 中 declarative contributes 的类型。适用于理解 `resources/hub` 离线 fallback。
- [prepareHubResources.js](../../../../open-ai-desktop/AionU/scripts/prepareHubResources.js)
  构建前下载 AionHub index 与扩展包到 `resources/hub/`。适用于连接发布资源与扩展生态。
- [pack-web-cli.js](../../../../open-ai-desktop/AionU/scripts/pack-web-cli.js)
  WebCLI tarball 打包脚本，复制 renderer 静态文件与 bundled aioncore。适用于连接 Web 运行时和发布包。
- [Windows installer scripts](../../../../open-ai-desktop/AionU/resources/windows/windows-installer-x64.nsh)
  NSIS 架构检查和 installer include 示例。适用于理解 `resources/windows` 的安装器职责。
- [Installer messages](../../../../open-ai-desktop/AionU/resources/windows/installer-messages.nsh)
  Windows installer 中英文失败提示。适用于说明资源目录也包含安装器文案契约。
- [AionUI feature template](../../../../open-ai-desktop/AionU/.aionui/FEATURE_DEV_TEMPLATE.md)
  面向 AI/开发协作的功能需求模板。适用于理解 `.aionui/` 是协作契约而非运行时资源。
- [Channels feature plan](../../../../open-ai-desktop/AionU/.aionui/FEATURE_CHANNELS.md)
  Channels 架构、插件生命周期、统一消息格式和实现状态。适用于与远程渠道 PRD 对照。

## 智慧（社区）

- [AionUi GitHub repository](https://github.com/iOfficeAI/AionUi)
  适用于提交文档/资源缺口 issue、对照 release 资产、验证上游是否补齐 architecture/specs/schema。
- [AionUi Discord](https://discord.gg/2QAwJn7Egx)
  README 推荐的英文社区。适用于询问文档意图、扩展示例设计和 WebUI 部署经验。
- [AionUi Twitter / X](https://twitter.com/AionUI)
  README 推荐的信息入口。适用于观察资源、截图和功能叙事如何随发布变化。

## 空白

- `docs/README.md` 指向 `docs/architecture/overview.md` 和 `docs/specs/`，但当前检出没有 `docs/architecture/` 或 `docs/specs/` 目录。
- `examples/hello-world-extension/aion-extension.json` 引用 `../../schemas/aion-extension-v1.json`，但当前检出没有 `schemas/` 目录。
- `docs/contributing/development.md` 的 standalone server 脚本清单包含 `build:renderer:web`、`build:server` 等命令，而当前 `package.json` 未提供这些脚本；需要后续确认是文档滞后还是脚本已迁移。
- `scripts/README.md` 仍描述 Electron Forge / webpack 旧构建流，与当前 `electron-vite` + `electron-builder` 主路径存在漂移。

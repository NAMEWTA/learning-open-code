# 插件生命周期全链路资源

## 知识

- `src/app/core/startup/startup.service.ts`
  插件系统启动入口。适用于确认插件初始化为什么在数据加载和同步之后发生。
- `src/app/plugins/plugin.service.ts`
  插件发现、启用、懒加载、`onReady`、Node 授权与卸载的主编排器。适用于排查“manifest 已发现但代码没跑”的问题。
- `src/app/plugins/plugin-loader.service.ts`
  manifest、`plugin.js`、`index.html`、图标和 i18n 文件加载器。适用于判断 iframe-only 插件何时允许没有 `plugin.js`。
- `src/app/plugins/plugin-runner.ts` 与 `src/app/plugins/plugin-api.ts`
  插件代码执行和 `PluginAPI` 实例绑定。适用于理解 `plugin.js` 为什么能调用宿主 API。
- `src/app/plugins/plugin-bridge.service.ts`
  插件 API 到应用服务、OAuth、Node executor、issue provider registry 的桥。适用于追踪 API 调用边界。
- `src/app/plugins/ui/plugin-index/plugin-index.component.ts` 与 `src/app/plugins/util/plugin-iframe.util.ts`
  iframe `srcdoc`、postMessage bridge、bridge token、允许的 iframe API 方法。适用于分析插件 UI 与宿主通信。
- `src/app/plugins/oauth/plugin-oauth-bridge.service.ts`、`src/app/plugins/oauth/plugin-oauth.service.ts`、`electron/plugin-oauth.ts`
  OAuth renderer bridge、PKCE 流程、本地 loopback server 和系统浏览器入口。适用于排查 OAuth 登录失败。
- `electron/plugin-node-executor.ts`
  Electron main process 的 nodeExecution 授权、token 绑定和脚本执行。适用于判断本地文件/Node 能力是否可用。
- `src/app/plugins/issue-provider/`
  issue provider registry、HTTP helper、adapter 和 sync adapter。适用于追踪插件 provider 如何进入任务导入、刷新和双向同步。
- `packages/plugin-api/src/types.ts` 与 `packages/plugin-api/src/issue-provider-types.ts`
  插件作者可见的 TypeScript 契约。适用于核对 manifest、OAuth、Node 脚本和 issue provider 定义字段。
- `packages/plugin-dev/README.md`
  插件开发目录、打包要求和 iframe-only 插件文件要求。适用于从开发者视角理解插件包结构。
- `packages/plugin-dev/github-issue-provider/src/plugin.ts` 与 `packages/plugin-dev/google-calendar-provider/src/plugin.ts`
  真实 issue provider 样例。前者展示普通 token/header provider，后者展示 OAuth provider。
- `src/assets/community-plugins.json` 与 `src/app/plugins/ui/plugin-management/plugin-management.component.ts`
  社区插件列表和管理页展示入口。适用于区分“展示在列表中”和“已安装/已发现/已启用”。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)
  适用于检索插件、OAuth、nodeExecution、issue provider 相关缺陷和设计讨论。
- [Super Productivity GitHub Discussions](https://github.com/super-productivity/super-productivity/discussions)
  适用于验证插件开发思路、提问第三方插件接入边界。

## 空白

- 当前仓库内没有单独的插件系统架构白皮书；本主题以源码、官方插件 API 包 README 和内置插件样例作为主要知识来源。

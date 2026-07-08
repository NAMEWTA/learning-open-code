# 插件系统、插件 API 与运行时加载资源

## 知识

- `open-productivity/super-productivity/src/app/core/startup/startup.service.ts`
  运行时插件初始化入口。适用于区分启动后延迟任务、数据加载/同步等待和 `PluginService.initializePlugins()`。
- `open-productivity/super-productivity/src/main.ts` 与 `src/app/plugins/plugin-initializer.ts`
  Angular provider token 接线。适用于说明 `PLUGIN_INITIALIZER_PROVIDER` 不是当前实际执行插件初始化的 `APP_INITIALIZER` 链。
- `open-productivity/super-productivity/src/app/plugins/plugin.service.ts`
  插件发现、enabled 状态、内置/上传插件、lazy load、Node grant、卸载清理的主门面。
- `open-productivity/super-productivity/src/app/plugins/plugin-loader.service.ts`、`plugin-runner.ts`、`plugin-api.ts`、`plugin-bridge.service.ts`
  插件资源加载、代码执行、公开 API 包装和受控应用服务桥接。适用于追插件 API 如何进入任务、项目、标签、UI、OAuth 和 Node 执行。
- `open-productivity/super-productivity/packages/plugin-api/src/types.ts` 与 `issue-provider-types.ts`
  插件作者可见的 TypeScript 合同。适用于核对 manifest、hooks、OAuth、secret、Node 执行和 issue provider definition。
- `open-productivity/super-productivity/electron/plugin-oauth.ts`、`electron/plugin-node-executor.ts`、`electron/preload.ts`
  桌面主进程 OAuth loopback、Node 执行授权和 renderer bridge。适用于判断哪些能力不能放在 Angular service 中。
- `open-productivity/super-productivity/src/app/plugins/issue-provider/`
  插件 issue provider registry、adapter、HTTP helper 与 sync adapter。适用于判断插件 provider 如何接入 issue feature。
- `open-productivity/super-productivity/packages/plugin-dev/README.md`、`packages/vite-plugin/src/index.ts`
  插件开发与构建辅助。适用于理解插件包结构、dist 产物、manifest/icon/i18n/index.html 复制流程。
- `open-productivity/super-productivity/src/assets/community-plugins.json`
  社区插件目录数据源。适用于理解 Settings 插件页展示社区插件时使用的是静态 JSON 清单。

## 智慧（社区）

- [super-productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)
  适用于验证插件加载、OAuth、Node 执行和 issue provider 行为是否对应真实用户问题。
- [super-productivity Discussions](https://github.com/super-productivity/super-productivity/discussions)
  适用于讨论插件 API 设计、社区插件发布和迁移 provider 的使用体验。

## 空白

- 暂未纳入每个内置插件的 README 和测试矩阵；L2 深挖某个插件时需要单独补充。
- 未检索第三方插件仓库的最新实现；本 L1 只以主仓库源码和内置示例为准。

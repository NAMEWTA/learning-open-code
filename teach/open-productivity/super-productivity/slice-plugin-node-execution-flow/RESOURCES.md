# 插件 Node execution grant 全链路资源

## 知识

- `src/app/plugins/plugin.service.ts`
  `_ensureNodeExecutionGrant()`、`_fireOnReady()`、`checkNodeExecutionPermission()`、`_nodeExecutionDeniedThisSession` 与 `clearNodeExecutionConsent()`。适用于排查启用/onReady 时 grant 是否拿到、用户拒绝后是否重复弹窗。
- `src/app/plugins/plugin-bridge.service.ts`
  renderer 侧 grant token 缓存、`requestNodeExecutionGrant()`、`_executeNodeScript()`、`consumePluginNodeExecutionApi()` 一次性接管。适用于追踪 IPC 调用与 bootstrap 竞态守门。
- `electron/preload.ts`
  `consumePluginNodeExecutionApi()` 一次性 handoff，封装 `PLUGIN_REQUEST_NODE_EXECUTION_GRANT`、`PLUGIN_EXEC_NODE_SCRIPT` 等 invoke。适用于理解 renderer 如何拿到受控 node API。
- `electron/plugin-node-executor.ts`
  main process 授权、native consent dialog、session grant Map、webContents 绑定、脚本执行（vm 与 spawn）。适用于判断真正执行发生在哪一层。
- `electron/plugin-node-consent-store.ts`
  uploaded 插件的持久化 ask-once consent；只有 main 在 Allow 后可写入，renderer 只能 clear。适用于理解跨会话免重复弹窗与 disable/re-upload 失效机制。
- `electron/shared-with-frontend/plugin-node-execution.model.ts`
  renderer 与 Electron API 共享的 IPC 契约类型。适用于核对 requestGrant / executeScript / clearConsent 签名。
- `src/app/plugins/util/plugin-iframe.util.ts`
  iframe 内 `executeNodeScript` 通过 postMessage 代理到宿主；危险能力仍受 main consent 守门。适用于区分 host-side 与 iframe 插件的 node 调用路径。
- `src/app/plugins/ui/plugin-management/plugin-management.component.ts`
  用户手动启用 nodeExecution 插件时的 `checkNodeExecutionPermission()` 入口。适用于区分交互式启用与启动时 `_fireOnReady` 申请 grant。
- `packages/plugin-api/src/types.ts`
  `nodeExecution` permission 与 `PluginNodeScriptRequest` 类型。适用于核对 manifest 声明与插件作者 API。
- `packages/plugin-dev/sync-md/src/manifest.json`
  内置 nodeExecution 插件样例。适用于对照 built-in verified dialog 路径。
- `electron/plugin-node-executor.test.cjs`
  grant、webContents 绑定、persisted consent、pluginId 消毒等安全回归测试。适用于验证边界行为而非业务逻辑。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)
  适用于检索 nodeExecution、plugin consent、#8512 等相关缺陷与设计讨论。
- [Super Productivity GitHub Discussions](https://github.com/super-productivity/super-productivity/discussions)
  适用于验证第三方插件 node 能力接入与桌面安全边界。

## 空白

- 当前仓库内没有单独的 nodeExecution 安全白皮书；本主题以 `electron/plugin-node-executor.ts` 内联注释、consent store 注释与 `plugin-node-executor.test.cjs` 为主要权威来源。

# 笔记：Renderer Shell 模块

## 关键事实

- renderer 入口在 `src/renderer/src/main.tsx`，先记录 bootstrap breadcrumb、安装 renderer crash diagnostics，再设置 document theme、检查 `#root`，最后用 React `StrictMode` 挂载 `I18nProvider`、根级 `RecoverableRenderErrorBoundary` 和 `App`。
- `App.tsx` 是 always-mounted shell，不只是页面组件。它集中 lazy-load 页面和 modal，订阅 IPC 事件，控制自定义窗口 chrome，执行启动水合，维护 beforeunload session flush，并把 store getter 注入 runtime graph sync。
- 启动水合顺序是：先读取 settings；再提前发起 UI、keybindings 和 onboarding 读取；随后拉取 repos；repos 完成后让 project/folder scope 与 worktrees、lineage 扫描部分重叠；再按 host 合并 workspace session，水合 workspace/tabs/editor/browser，随后 SSH reconnect、等待 first-window services、重连 persisted terminals，最后设置 hydration succeeded。
- `src/renderer/src/store/index.ts` 用 Zustand 聚合多个 slice。`App` 通过 selector 和 `useShallow` 取需要的状态/动作，避免每个动作单独订阅造成高频 store mutation 下的额外 re-render。
- `tabs.ts` 维护 `unifiedTabsByWorktree`、`groupsByWorktree`、`activeGroupIdByWorktree` 和 `layoutByWorktree`，并在 `reconcileWorktreeTabModel()` 中把 legacy terminal/browser/editor 状态修正成可渲染的统一 tab 模型。
- `sync-runtime-graph.ts` 不直接 import store，而是通过 `setRuntimeGraphStoreStateGetter()` 注入 getter，避免 store 构造循环。同步开启后用 16ms timer 合并高频更新，并把 mounted terminal panes、后台 automation PTY 和 mobile session tab snapshots 发给 `window.api.runtime.syncWindowGraph()`。
- runtime graph 同步依赖 `workspaceSessionReady` 开关；session writer subscriber 可以先创建，但真正写入还受 `workspaceSessionReady` 和 `hydrationSucceeded` 门控，避免水合失败时把空状态覆盖回磁盘。

## 待澄清

- `App.tsx` 内部还有大量 UI 分支和快捷键处理，本主题只记录 shell 级责任。组件级拆解需要后续单独主题。
- mobile companion 的 renderer 页面与 runtime pairing UI 将在 `module-mobile-companion` 中继续展开。

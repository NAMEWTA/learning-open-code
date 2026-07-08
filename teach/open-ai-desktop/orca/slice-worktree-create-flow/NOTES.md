# 笔记：Worktree 创建链路

## 关键事实

- `NewWorkspaceComposerModal.tsx` 是薄 UI shell。quick create 的提交最终进入 `useComposerState.ts` 的 `submitQuick()`，普通 prompt create 进入同一 hook 的长提交路径；modal 自己不直接调用 main IPC。
- `useComposerState.ts` 在提交切点之前完成所有交互式决策：repo 是否可用、setup hook trust、base branch/compare base/push target、branch override、linked issue/PR/Linear/GitLab 元数据、sparse checkout、Agent 是否启用、startup plan 能否交给 backend。
- quick create 不同步等待 `git worktree add`。hook 生成可序列化的 `WorktreeCreationRequest` 后调用 `runBackgroundWorktreeCreation()`，清理 draft，并让 modal 关闭或重置到下一次创建。
- `pending-worktree-creation.ts` 把请求设计成可重试记录。它包含 repo、base、setup、sparse、linked review、Agent startup、note、ephemeral VM recipe、progress mode 等字段；pending entry 只保存在 renderer session 内存，不持久化。
- `worktree-creation-flow.ts` 为每次创建生成 `creationId`，立即显示 pending creation surface，然后异步调用 store 的 `createWorktree()`。创建成功后，如果用户仍在看这个 pending panel，就用 `worktree-activation.ts` 的 `activateAndRevealWorktree()`；如果用户已经离开，则用 `ensureWorktreeHasInitialTerminal()` 在后台补初始终端，不抢焦点。
- `new-workspace.ts` 的 `ensureAgentStartupInTerminal()` 是 renderer 侧 Agent handoff：只有 backend 没有返回 `startupTerminal.spawned` 时，renderer 才把 `startupPlan` 投递到目标 terminal，避免重复启动 Agent。
- `store/slices/worktrees.ts` 的 `createWorktree()` 最多尝试 25 个名字/分支候选，处理本地或远端 branch conflict。它按 repo 的 runtime target 分流：local target 调 `window.api.worktrees.create()`，非 local target 调 runtime RPC `worktree.create`。
- `preload/index.ts` 只暴露受控桥：`worktrees.create` 对应 `ipcRenderer.invoke('worktrees:create')`，`onCreateProgress` 只转发本地 main helper 发来的 `fetching`/`creating` phase。SSH/runtime 路径可能没有这两个细粒度 phase，而是走 indeterminate 进度。
- `useIpcEvents.ts` 用 `creationId` 把 `createWorktree:progress` 路由回对应 pending entry；没有 `creationId` 的旧事件会被忽略，避免并发后台创建互相覆盖状态。
- `main/ipc/worktrees.ts` 的 `worktrees:create` 是桌面本地 IPC 入口。它先校验 repo，解析 telemetry source 和 automation provenance，再按 folder repo、SSH repo、本地 git repo 分别调用 `createFolderWorkspace()`、`createRemoteWorktree()`、`createLocalWorktree()`。
- `createLocalWorktree()` 的顺序是：读取设置和 Git options，解析 username，调用 `resolveWorktreeCreateBase()`，按需要刷新 remote tracking base 或 best-effort fetch，验证 setup policy 和 sparse checkout，循环解析分支名/路径，执行 `addWorktree()` 或 `addSparseWorktree()`，re-list 找到真实 worktree，写 metadata/lineage，注册 roots，按需创建 symlink，准备 setup runner，最后尝试 backend startup/setup terminal。
- `createRemoteWorktree()` 与本地 helper 在 Git/base/metadata/setup/default tabs 上保持同构，但通过 SSH git/filesystem provider 操作远端路径。desktop SSH IPC helper 本身不消费 `startup`、不返回 `startupTerminal`；managed SSH runtime 会在 `orca-runtime.ts` 包装 `createRemoteWorktree()` 之后再 spawn startup/setup terminal。
- `resolveWorktreeCreateBase()` 是 base 策略核心：显式 base 直接返回；没有持久化 base 时使用默认 base；持久化 base 与默认 base 相同则保留；陈旧持久化 base 只有在仍可用时才保留，否则回退默认 base。
- `git/worktree.ts` 的 `addWorktree()` 封装真实 `git worktree add`，新分支默认使用 `--no-track -b`，可写入 branch base，设置 `push.autoSetupRemote=true`，并用 `WORKTREE_ADD_TIMEOUT_MS` 限制 checkout 卡死。
- runtime RPC 的 `worktree.create` 会把 mobile、CLI 或 remote runtime 参数传给 `OrcaRuntimeService.createManagedWorktree()`。runtime 版本复用同样的 base/ref、Git 创建、metadata、setup/startup 语义，并维护 no-double-spawn：managed local/SSH runtime 已经生成 setup/startup terminal 时，RPC 返回值或 activation payload 不能再让 renderer 重复生成。
- `ephemeral-vm-worktree-creation.ts` 是 worktree 创建前的 VM 旁支：它把 recipe provisioning 变成 pending phase，准备 runtime repo，成功后 attach runtime 到 workspace，失败时做 best-effort cleanup。
- `CreateWorktreeResult` 不只是返回 worktree；它还能携带 `setup`、`defaultTabs`、`startupTerminal`、`warning`、`localBaseRefRefresh`、`localBaseRefUpdateSuggestion`、`workspaceLineage` 和 timing phases。
- `worktree-id.ts` 说明 worktree id 的基本格式是 `repoId::worktreePath`。folder workspace 可以在 path 后带 session UUID suffix，filesystem 调用要用 `splitWorktreeIdForFilesystem()` 去掉 suffix。
- 测试护栏分布在多层：renderer flow 测后台 pending 和 handoff，store test 测 pending 状态，base test 测 base 选择策略，main IPC test 测 startup/setup terminal，runtime RPC test 测参数映射。

## 待澄清

- `useComposerState.ts` 同时承载 smart GitHub、review provider、Agent 参数、VM recipe 和 setup policy，后续如果要逐项精读，应拆成 review/work-item 专题。
- SSH relay provider 的 `addWorktree()` 具体协议细节不在本主题展开，只记录 `createRemoteWorktree()` 的边界与调用顺序。

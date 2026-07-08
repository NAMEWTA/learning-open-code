# Worktree 创建链路资源

## 知识

- [src/renderer/src/components/NewWorkspaceComposerModal.tsx](../../../../open-ai-desktop/orca/src/renderer/src/components/NewWorkspaceComposerModal.tsx)  
  New Workspace 的 modal shell，负责打开/关闭、quick agent 选择和提交入口，真正创建逻辑委托给 composer hook。
- [src/renderer/src/hooks/useComposerState.ts](../../../../open-ai-desktop/orca/src/renderer/src/hooks/useComposerState.ts)  
  创建请求的 renderer 汇聚点，解析 workspace name、base branch、setup trust、linked work item、sparse checkout、Agent startup plan，并生成 `WorktreeCreationRequest`。
- [src/renderer/src/lib/pending-worktree-creation.ts](../../../../open-ai-desktop/orca/src/renderer/src/lib/pending-worktree-creation.ts)  
  定义后台创建请求、pending entry 和 `preparing`/`fetching`/`creating`/`provisioning-vm` 进度模型。
- [src/renderer/src/lib/worktree-creation-flow.ts](../../../../open-ai-desktop/orca/src/renderer/src/lib/worktree-creation-flow.ts)  
  后台创建编排：创建 correlation id、显示 pending surface、调用 store create、处理成功/失败、交接终端和 note 写回。
- [src/renderer/src/lib/worktree-activation.ts](../../../../open-ai-desktop/orca/src/renderer/src/lib/worktree-activation.ts)  
  创建完成后的激活与后台 terminal seed helper，支撑 `activateAndRevealWorktree()` 和 `ensureWorktreeHasInitialTerminal()`。
- [src/renderer/src/lib/new-workspace.ts](../../../../open-ai-desktop/orca/src/renderer/src/lib/new-workspace.ts)  
  renderer 侧 Agent startup handoff，负责在 backend 未 spawn 时把 startup plan 投递到目标 terminal。
- [src/renderer/src/lib/ephemeral-vm-worktree-creation.ts](../../../../open-ai-desktop/orca/src/renderer/src/lib/ephemeral-vm-worktree-creation.ts)  
  VM recipe 创建前置准备、provisioning progress、runtime attach 与失败 cleanup 的旁支实现。
- [src/renderer/src/store/slices/worktrees.ts](../../../../open-ai-desktop/orca/src/renderer/src/store/slices/worktrees.ts)  
  renderer store 的 `createWorktree` action，负责本地 IPC 与 runtime RPC 分流、冲突重试、结果合并和 pending 状态维护。
- [src/preload/index.ts](../../../../open-ai-desktop/orca/src/preload/index.ts)  
  暴露 `window.api.worktrees.create()`、`prefetchCreateBase()` 和 `onCreateProgress()`，是 renderer 到 main 的受控桥。
- [src/renderer/src/hooks/useIpcEvents.ts](../../../../open-ai-desktop/orca/src/renderer/src/hooks/useIpcEvents.ts)  
  订阅 `createWorktree:progress` 并按 creation id 更新对应 pending entry。
- [src/main/ipc/worktrees.ts](../../../../open-ai-desktop/orca/src/main/ipc/worktrees.ts)  
  main IPC 的 `worktrees:create` handler，解析 repo、telemetry、automation provenance，并分流到 folder/local/SSH 创建 helper。
- [src/main/ipc/worktree-remote.ts](../../../../open-ai-desktop/orca/src/main/ipc/worktree-remote.ts)  
  本地与 SSH worktree 创建 helper，覆盖 base ref 解析、fetch、分支/路径冲突、sparse checkout、metadata 和 setup/default tabs；只有本地 helper 直接 backend-spawn startup terminal。
- [src/main/worktree-create-base.ts](../../../../open-ai-desktop/orca/src/main/worktree-create-base.ts)  
  worktree 创建 base ref 的小型策略函数：显式 base 优先，持久化 base 可用则保留，否则回退到检测到的默认 base。
- [src/main/git/worktree.ts](../../../../open-ai-desktop/orca/src/main/git/worktree.ts)  
  本地 `git worktree add` 封装，负责 `--no-track`、base ref 写入、local base refresh 建议和超时保护。
- [src/main/runtime/rpc/methods/worktree.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/methods/worktree.ts)  
  runtime RPC 的 `worktree.create` method，把移动端、CLI 或远端 runtime 请求映射到 `createManagedWorktree()`。
- [src/main/runtime/orca-runtime.ts](../../../../open-ai-desktop/orca/src/main/runtime/orca-runtime.ts)  
  runtime 管理型创建路径，支撑 CLI/mobile/runtime 入口，并在 managed local/SSH 路径处理 setup/startup terminal 的 no-double-spawn 合约。
- [src/shared/types.ts](../../../../open-ai-desktop/orca/src/shared/types.ts)  
  `CreateWorktreeArgs`、`CreateWorktreeResult`、`WorktreeStartupLaunch` 等跨进程类型。
- [src/shared/worktree-id.ts](../../../../open-ai-desktop/orca/src/shared/worktree-id.ts)  
  `repoId::worktreePath` 格式解析与 folder workspace suffix 处理。
- [src/renderer/src/lib/worktree-creation-flow.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/lib/worktree-creation-flow.test.ts)  
  验证后台创建、VM provisioning、issue command、active/background handoff 和 Agent trust preflight。
- [src/renderer/src/store/slices/worktrees.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/store/slices/worktrees.test.ts)  
  验证 pending creation 状态、phase 更新、VM cleanup 和 active surface 规则。
- [src/main/worktree-create-base.test.ts](../../../../open-ai-desktop/orca/src/main/worktree-create-base.test.ts)  
  验证显式 base、可用持久化 base、陈旧持久化 base 的选择策略。
- [src/main/ipc/worktrees.test.ts](../../../../open-ai-desktop/orca/src/main/ipc/worktrees.test.ts)  
  验证 local create 后 startup/setup terminal 生成、timing phase 和 create helper 行为。
- [src/main/runtime/rpc/methods/worktree.test.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/methods/worktree.test.ts)  
  验证 `worktree.create` RPC 参数会完整传入 runtime server。

## 智慧（社区）

- 本主题暂不依赖外部社区资料。关键理解来自 Orca 自己的跨进程边界、Git helper 和测试。

## 空白

- `createRemoteWorktree()` 的 relay provider 内部实现属于后续 SSH relay session flow，本主题只引用它的调用边界。
- review provider 的 smart branch/start point 细节分散在 composer 和 main helper 中，后续如需学习可拆成单独 review workspace 专题。

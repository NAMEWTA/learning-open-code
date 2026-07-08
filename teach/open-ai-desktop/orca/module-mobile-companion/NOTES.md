# 笔记：移动端 Companion 模块

## 关键事实

- 移动端是 Expo/React Native app。`mobile/app/_layout.tsx` 是根布局，包住 `RpcClientProvider`，处理 `orca://pair` deep link、通知点击跳转、splash 隐藏和 Stack 路由注册。
- 首页 `mobile/app/index.tsx` 读取 paired hosts，调用 `useAllHostClients()` 获取每个 host 的共享 client，拉取 `stats.summary`、`worktree.ps`、`accounts.list`、`settings.get`、`preflight.check`、`linear.status`，并把 worktree/accounts 快照缓存到本地。
- Pairing 有两步：`pair.tsx` 把 `orca://pair` 或 initial URL 转到 `/pair-confirm`；`pair-confirm.tsx` 连接 QR 中的 endpoint/deviceToken/publicKey，发 `status.get` 验证 runtime，再通过 `saveHost()` 保存 host metadata 和 token。
- `host-store.ts` 把 host metadata 放 AsyncStorage，把 device token 放 Expo SecureStore；native token 使用 `WHEN_UNLOCKED_THIS_DEVICE_ONLY`，避免进 iCloud/备份迁移。
- `client-context.tsx` 把“每屏一个 WebSocket”收敛成“每 host 一个共享 `RpcClient`”，屏幕通过 `useHostClient()` 或 `useAllHostClients()` acquire/release，并用 foreground/network triggers 促发恢复。
- `rpc-client.ts` 是移动端通信底座：WebSocket open 后走 E2EE hello/auth，`sendRequest()` 等待 connected 后发 encrypted RPC，`subscribe()` 注册 streaming listener 并在 reconnect 后 replay，terminal/browser binary frames 走单独解码。
- Host detail 路由 `mobile/app/h/[hostId]/index.tsx` 读取 `repo.list`、`worktree.ps`、`ui.get`，并写回 `ui.set`、`worktree.activate`、`worktree.sleep`、`worktree.rm` 等操作。
- Session 路由 `mobile/app/h/[hostId]/session/[worktreeId].tsx` 订阅 `terminal.subscribe` 和 `session.tabs.subscribe`，同时发 `terminal.send`、`terminal.list`、`session.tabs.createTerminal`、`files.read`、`markdown.saveTab`、`browser.screencast` 等 RPC。
- Resume card 先用本机 last visited worktree；没有时用 `pickResumeWorktree()` 选择桌面 active worktree，再 fallback 到最近 terminal output。

## 待澄清

- L2 mobile pairing flow 需要继续下钻桌面 main runtime 的 pairing offer、device registry、runtime RPC server 和移动端 confirm/saveHost 的端到端链路。
- Session screen 过大，本 L1 只给出路由和 RPC 边界；terminal WebView、browser screencast、source-control/PR review 应按独立链路继续拆。

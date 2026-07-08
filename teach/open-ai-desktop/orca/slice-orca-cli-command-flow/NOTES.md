# Orca CLI 命令执行全链路笔记

## 核心判断

- `src/cli/index.ts` 是命令控制面入口；它不执行业务，只做 parse/help/validate/client/dispatch。
- `validateCommandAndFlags()` 早于 `new RuntimeClient()` 后的 runtime lookup，这能让 unknown command/flag 先报语法错误。
- `COMMAND_SPECS` 是用户可见 contract，handler 表是执行入口。两者必须同时存在，但职责不同。
- handler 基本是 thin adapter：取 flag、解析 selector、组 params、调用 `client.call(method, params)`、格式化输出。
- `open/status/serve` 是 core 分叉：`open` 调 `client.openOrca()`，`status` 可不要求 runtime ready，`serve` 直接 foreground 启动 app server。
- `environment`、`serve`、`agent`、`vm` 会抑制 remote env var fallback，避免 ORCA_ENVIRONMENT 让本地管理命令误连远程。
- remote pairing code 和 saved environment 是互斥入口，`RuntimeClient` 构造时解析。
- 本地 RuntimeClient 读 userData metadata，拿 authToken 和 transport endpoint，发送 newline-delimited JSON。
- 远程 RuntimeClient 走 shared WebSocket request，并在普通 RPC 前用 `status.get` 做 runtime protocol compatibility check。
- `active/current` 这种 cwd shortcut 只能本地解析；远程 runtime 的 cwd 属于服务器，不能拿客户端 cwd 推断 server worktree。
- `terminal.wait`、`orchestration.check --wait` 是 long-poll；CLI 和 runtime server 都有专门 timeout/keepalive/cap 逻辑。
- main runtime RPC server 是安全边界；CLI handler 传来的 method 还要经过 auth、schema parse、dispatcher 和 method manifest。

## 容易误解

- `COMMAND_SPECS` 不等于 handler 注册表；spec 只声明命令形状，真正调用由 `dispatch.ts` 的 handler table 决定。
- `--json` 不是简单把 formatter 换成 JSON；错误时本地 CLI 会构造 failure envelope，runtime failure 会原样输出 envelope。
- `status.get` 在本地有 CLI 状态包装；远程 status 证明 paired runtime reachable，不代表本机桌面 app running。
- `orca serve` 不是普通 runtime RPC，它负责启动 headless runtime server。
- 浏览器命令可以省略 worktree；本地会尝试从 cwd 推断，远程会让 server-side focus 决定。
- keepalive 是 long-poll transport 行为，不是每个短 RPC 都有。

## 后续可深挖

- CLI command spec 生成和 root help 的一致性维护。
- packaged CLI asset、Windows launcher、Linux AppImage wrapper。
- `orca.cli` relay method 如何把远端 shell 命令转回桌面 runtime。
- 每个 runtime RPC method 的业务实现，例如 `worktree.create`、`browser.click`、`terminal.create`。

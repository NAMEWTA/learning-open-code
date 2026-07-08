# 使命：Orca CLI 命令执行全链路

## 为什么

用户要系统学习 Orca，需要能把一条 `orca ...` 命令从 shell 入口追到 runtime RPC 方法。这个 L2 主题把参数解析、命令规格校验、handler dispatch、本地/远程 RuntimeClient、main runtime RPC 边界和测试护栏串成一条可验证链路。

## 成功的样子

- 能解释为什么语法错误会先于 runtime lookup 报出，而不是误报 “Orca is not running”。
- 能从一个命令路径追到 `COMMAND_SPECS`、`dispatch()`、对应 handler 和 `client.call()` 的 method/params。
- 能区分 `open/status/serve`、普通 RPC 命令、special shim、remote pairing/environment 四类入口差异。
- 能说明本地 CLI 如何通过 metadata、auth token、Unix socket/named pipe 发送 newline JSON frame。
- 能说明远程 CLI 如何通过 pairing code 或 saved environment 走 WebSocket，并在普通 RPC 前做协议兼容检查。
- 能根据测试定位 remote cwd shortcut、long-poll timeout、keepalive、auth、unknown flag 这些关键不变量。

## 约束条件

- 短课控制在 15 分钟内，只建立主路径和关键分叉。
- 参考页可以展开更多命令族和测试，但所有结论必须能回到 Orca 当前源码。
- 本主题是 L2 跨模块切片，建立在 CLI/relay 与 shared contracts 的 L1 主题之上。

## 不在范围内

- 不逐个讲完全部 CLI 命令的业务语义。
- 不深入每个 runtime RPC 方法内部的业务实现，比如 worktree 创建、浏览器自动化、terminal PTY 细节。
- 不讲安装 CLI wrapper、平台打包和 shell completion。

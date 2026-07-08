# 使命：SSH Relay 会话保活全链路

## 为什么

用户要系统学习 Orca，需要理解 SSH 远端会话为什么能在应用重启、网络闪断、系统睡眠后继续保留终端状态。这个 L2 主题把 renderer 启动恢复、main SSH 连接、relay 部署、远端 daemon socket、JSON-RPC multiplexer、PTY replay 和 workspace session 串成一条可验证链路。

## 成功的样子

- 能从 renderer 的启动恢复或用户点击 SSH Connect 追到 `ssh:connect`、`SshConnection`、`SshRelaySession` 和远端 `relay.js --connect`。
- 能解释 detached relay、Unix socket/Windows named pipe、grace timer、`relay.configureGraceTime` 和 `graceTimeSeconds = 0` 的真实语义。
- 能区分 SSH transport 断线、relay mux 断线、版本握手不匹配、PTY 已过期这几类失败。
- 能说明远端 PTY 如何通过 durable lease、`pty.attach`、replay buffer 和 renderer delayed reattach 恢复。
- 能根据测试定位这条链路的关键不变量，而不是只凭终端 UI 行为猜测。

## 约束条件

- 短课控制在 15 分钟内，只用 3 个代表性源码文件建立主路径。
- 参考页可以展开更多源码和测试，但所有结论必须能回到 Orca 当前源码。
- 本主题是 L2 跨模块切片，必须建立在 CLI/relay、main runtime、shared contracts 的 L1 主题之上。

## 不在范围内

- 不逐行讲解 Git、filesystem、port scan、agent hook 的全部 relay handler。
- 不深入远端 CLI 命令完整执行链路；那属于 `slice-orca-cli-command-flow`。
- 不把 relay 重连机制拆到每个 frame 和 buffer 分支；更细的时序可在 `deep-dive-relay-reconnect` 展开。

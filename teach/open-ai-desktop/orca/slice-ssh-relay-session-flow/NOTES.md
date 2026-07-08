# SSH Relay 会话保活笔记

## 核心判断

- 主进程 `ssh:connect` 是用户入口，但长期拥有远端 PTY 的不是 SSH exec channel，而是 detached `relay.js` daemon。
- fresh connect 和 reconnect 都会进入 `deployAndLaunchRelay()`；它先尝试连接已有 socket，失败才 fresh launch。
- fresh launch 也先启动 detached daemon，再执行 `relay.js --connect --sock-path ...`，所以客户端始终通过 bridge 和 daemon 通信。
- `SshRelaySession` 管 provider 生命周期，`SshConnection` 管 SSH transport 生命周期，两者不是同一个状态机。
- `SshChannelMultiplexer` 的 dispose reason 是 relay-level loss 的信号，`ssh.ts` 通过 relay-lost backoff 重试。
- `relay.configureGraceTime` 更新的是 relay 内 `PtyHandler` 的 grace timeout；0 表示不自动过期。
- host sleep 前主进程会把 grace 设置为 0，避免系统睡眠期间远端 PTY 被普通 grace 窗口回收。
- renderer 启动时先恢复 SSH，再恢复 terminal session；passphrase 目标会转为 deferred，不在启动时堆叠凭据对话框。
- 远端 PTY lease 是 main store 的 durable 索引，真正的 live PTY 仍在远端 relay 内存里；grace 过期后只能标记 expired 并冷启动。
- workspace session 写在远端 `~/.orca/sessions`，它是 durable JSON；和 PTY replay buffer 不是同一种持久性。

## 容易误解

- `connected` 的 SSH transport 不等于 relay provider 已 ready。`ssh.ts` 会在 relay session ready 后再广播可用 connected。
- `--connect` 不是启动新 PTY 的命令，它只是把新的 SSH channel 桥到同一个 relay socket。
- `detach()` 不是 `dispose()`。detach 让本地 provider 下线，但保留远端 PTY lease 给后续 reattach。
- relay replay buffer 是最近 100KB 输出，不是完整终端历史。
- 版本握手发生在 dispatcher 接管 socket 之前；sentinel 只有 handshake 通过后才写给 main。

## 后续可深挖

- `RelayDispatcher` 的 multi-client 广播和 `requestAnyClient()` 选择策略。
- `ClientRequestAborts` 如何让 stale client 的长请求停止。
- `relay.status` 能如何辅助调试 grace、socket client 和 PTY 数量。
- Windows WMI detached relay 和 named pipe fallback 的平台差异。

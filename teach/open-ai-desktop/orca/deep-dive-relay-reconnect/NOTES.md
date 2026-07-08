# Relay 断线重连与 Grace Socket 笔记

## 核心判断

- 重连能保留终端的前提是旧 detached relay daemon 仍在 grace window 内，且 socket/pipe 能重新接入。
- `relay.js --connect` 不是 fresh launch，它只是把新的 SSH exec channel 桥接到旧 daemon socket。
- fresh launch 后主进程仍然通过 `--connect` 访问新 daemon；主进程永远不直接持有 detached daemon stdout。
- handshake sentinel 是 bridge 对 main 的 ready 信号；版本握手未通过时不应输出 sentinel。
- POSIX socket 清理必须先确认 socket identity，避免旧 relay shutdown 时 unlink 新 relay 的 socket。
- Dispatcher 的 generation 和 per-client abort 是“旧 client 不污染新 session”的关键，不只是 keepalive。
- `graceTimeSeconds = 0` 表示不自动过期；只有 empty detached startup 会被短窗口保护，避免无客户端无 PTY 的 daemon 永久滞留。
- `PtyHandler.attach()` 的 replay 是同一 relay 进程内最近 100KB buffer；`revive()` 是 relay 进程内序列化/重建 PTY 包装，不等同于跨进程恢复。

## 容易误解

- 看到 socket 文件存在不代表旧 daemon 可用；部署层还会尝试实际 connect/handshake。
- 版本不匹配不是普通网络抖动。最终冒泡到 session 时会走 terminal error，跳过 relay-lost backoff。
- SSH transport connected 不等于 relay provider ready；`SshRelaySession` 的健康检查和 provider 注册必须完成。
- Windows named pipe 不能按 Unix socket 的 stale unlink 模型处理，所以有 active marker 和 fallback pipe。

## 后续可深挖

- 用真实 relay 日志制作“从日志判断故障层”的练习。
- 结合 `relay.status` 补一个运行时诊断速查表。

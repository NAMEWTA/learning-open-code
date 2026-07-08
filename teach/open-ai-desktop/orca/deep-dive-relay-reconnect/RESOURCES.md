# Relay 断线重连与 Grace Socket 资源

## 知识

- [src/main/ssh/ssh-relay-deploy.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-deploy.ts)  
  部署层核心入口：版本目录、target-specific socket、POSIX `--connect` 复用、fresh detached launch、Windows named pipe fallback。
- [src/main/ssh/ssh-relay-deploy-helpers.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-deploy-helpers.ts)  
  `waitForSentinel()` 负责 sentinel 前 startup buffer、exit 42 到 `RelayVersionMismatchError` 的映射。
- [src/main/ssh/ssh-relay-session.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-session.ts)  
  main 侧 session 状态机：establish/reconnect、mux loss watcher、provider teardown、PTY lease reattach、host sleep grace。
- [src/main/ssh/ssh-channel-multiplexer.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-channel-multiplexer.ts)  
  main 侧 relay mux：request/notification、ack、keepalive、timeout、`rpc.cancel` 和 `connection_lost` dispose。
- [src/main/ssh/relay-protocol.ts](../../../../open-ai-desktop/orca/src/main/ssh/relay-protocol.ts)  
  main 侧 frame/sentinel/keepalive 常量，与 relay 侧协议保持兼容。
- [src/main/ipc/ssh.ts](../../../../open-ai-desktop/orca/src/main/ipc/ssh.ts)  
  relay-lost bounded backoff、terminal relay error 分流、power monitor suspend/resume 处理。
- [src/relay/relay.ts](../../../../open-ai-desktop/orca/src/relay/relay.ts)  
  远端 daemon 主入口：socket ownership、stale socket probe、`--connect` bridge、grace timer、SIGHUP 忽略和 shutdown。
- [src/relay/relay-handshake.ts](../../../../open-ai-desktop/orca/src/relay/relay-handshake.ts)  
  daemon socket 和 `--connect` bridge 之间的版本握手；匹配后才允许 sentinel 和 dispatcher 接管。
- [src/relay/protocol.ts](../../../../open-ai-desktop/orca/src/relay/protocol.ts)  
  relay 侧 frame 编解码、handshake message、keepalive、payload 上限和 decoder drain。
- [src/relay/dispatcher.ts](../../../../open-ai-desktop/orca/src/relay/dispatcher.ts)  
  relay 内多 client JSON-RPC dispatcher：primary/socket client、generation、stale request、client-specific abort。
- [src/relay/pty-handler.ts](../../../../open-ai-desktop/orca/src/relay/pty-handler.ts)  
  PTY map、100KB replay buffer、`pty.attach`、`serialize`/`revive` 和 grace timer。
- [src/shared/ssh-types.ts](../../../../open-ai-desktop/orca/src/shared/ssh-types.ts)  
  SSH relay grace 的 shared 常量、0 值语义、min/max/default 边界。
- [src/main/ssh/ssh-relay-version-mismatch-error.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-version-mismatch-error.ts)  
  terminal mismatch 错误类型，用于跳过普通 relay-lost backoff。
- [src/main/ssh/ssh-relay-handshake-mismatch.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-handshake-mismatch.ts)  
  从 bridge stderr 和 exit code 构造版本不匹配错误。
- [src/main/ssh/ssh-relay-endpoints.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-endpoints.ts)  
  POSIX socket、Windows named pipe、agent hook endpoint 目录和 active marker 路径。
- [src/main/ssh/ssh-relay-instance-id.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-instance-id.ts)  
  target id 到 relay socket name 的隔离规则。
- [src/main/ssh/ssh-relay-deploy.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-deploy.test.ts)  
  覆盖 grace 默认值/0/上限、版本目录、target socket、Windows pipe fallback。
- [src/main/ssh/ssh-relay-deploy-helpers.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-deploy-helpers.test.ts)  
  覆盖 `waitForSentinel()` 对 sentinel、startup stderr、超时和 exit 42 的处理。
- [src/main/ssh/ssh-relay-cross-version-isolation.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-cross-version-isolation.test.ts)  
  验证新版本部署不引用旧版本目录或旧 socket，避免跨版本误连。
- [src/main/ssh/ssh-relay-session.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-session.test.ts)  
  覆盖 reconnect provider teardown、PTY reattach、replay 去重、stale PTY 失效、host sleep grace。
- [src/main/ssh/ssh-relay-session-terminal-error.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-session-terminal-error.test.ts)  
  验证 initial connect 与 reconnect 中的 `RelayVersionMismatchError` 会走 terminal callback。
- [src/main/ssh/ssh-channel-multiplexer.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-channel-multiplexer.test.ts)  
  验证 request timeout、`rpc.cancel`、keepalive、write failure、transport close 和 dispose cleanup。
- [src/main/ssh/relay-protocol.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/relay-protocol.test.ts)  
  验证 frame header、ack、keepalive 和 payload size 边界。
- [src/relay/relay-handshake-roundtrip.test.ts](../../../../open-ai-desktop/orca/src/relay/relay-handshake-roundtrip.test.ts)  
  使用真实 socket pair 验证 handshake ok、两端 leftover bytes 保留和 mismatch exit。
- [src/relay/protocol-handshake.test.ts](../../../../open-ai-desktop/orca/src/relay/protocol-handshake.test.ts)  
  验证 handshake frame 编码、解析、mismatch message、未知 handshake type 拒绝和 message type 区分。
- [src/relay/dispatcher.test.ts](../../../../open-ai-desktop/orca/src/relay/dispatcher.test.ts)  
  验证 socket client 优先、独立 frame state、stale response drop、request context abort 和 ack。
- [src/relay/pty-handler.test.ts](../../../../open-ai-desktop/orca/src/relay/pty-handler.test.ts)  
  验证 grace timer、unlimited grace、configured grace、replay/attach 和 PTY cleanup。
- [src/relay/subprocess.test.ts](../../../../open-ai-desktop/orca/src/relay/subprocess.test.ts)  
  覆盖真实 relay 子进程生命周期、`relay.status` 诊断和 detached/grace 相关运行时行为。
- [src/main/ipc/ssh.test.ts](../../../../open-ai-desktop/orca/src/main/ipc/ssh.test.ts)  
  验证 relay-lost bounded backoff、post-ready stabilization、host sleep unlimited grace。

## 智慧（社区）

- 本主题不依赖外部社区材料。可靠知识主要来自 Orca 当前源码、测试与已完成的 L1/L2 教学主题。

## 空白

- 没有覆盖真实远端系统日志样本；如后续用户提供 Linux/macOS/Windows relay 日志，可补充故障诊断案例。
- 没有展开所有 remote CLI bridge 请求，因为完整命令执行链路已在 `slice-orca-cli-command-flow` 覆盖。

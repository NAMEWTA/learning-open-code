# SSH Relay 会话保活资源

## 知识

- [src/renderer/src/App.tsx](../../../../open-ai-desktop/orca/src/renderer/src/App.tsx)  
  renderer 启动水合链路，先恢复 SSH target，再等待 first-window services，最后调用 `reconnectPersistedTerminals()`；passphrase target 和 15 秒超时 target 的 deferred 分类也在这里完成。
- [src/renderer/src/store/slices/terminals.ts](../../../../open-ai-desktop/orca/src/renderer/src/store/slices/terminals.ts)  
  记录 pending reconnect worktree/tab/session id，并在 SSH repo 尚未 connected 时保存 `deferredSshSessionIdsByTabId`，供 TerminalPane 后续 reattach。
- [src/renderer/src/components/terminal-pane/pty-connection.ts](../../../../open-ai-desktop/orca/src/renderer/src/components/terminal-pane/pty-connection.ts)  
  TerminalPane 的真实 reattach 入口：按 tab/leaf session id 触发 SSH connect、等待凭据、调用 `transport.connect({ sessionId })`。
- [src/renderer/src/components/terminal-pane/pty-transport.ts](../../../../open-ai-desktop/orca/src/renderer/src/components/terminal-pane/pty-transport.ts)  
  renderer 到 `window.api.pty.spawn()` 的 transport 包装，负责把 `sessionId`、connectionId、callbacks 和 replay/cold restore 结果带回 pane。
- [src/main/ipc/ssh.ts](../../../../open-ai-desktop/orca/src/main/ipc/ssh.ts)  
  SSH IPC 控制面：`ssh:connect`、active `SshRelaySession`、power monitor、relay-lost backoff、port forward restore 和 reset/terminate handlers。
- [src/main/ipc/pty.ts](../../../../open-ai-desktop/orca/src/main/ipc/pty.ts)  
  main PTY IPC：SSH spawn 成功后写入 remote PTY lease；`SSH_SESSION_EXPIRED` 时标记 lease 过期。
- [src/main/ssh/ssh-connection-manager.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-connection-manager.ts)  
  每个 target 的 SSH connection pool，避免并发 connect orphan 旧连接，并提供 reconnect/disconnect 查询。
- [src/main/ssh/ssh-connection.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-connection.ts)  
  SSH transport 生命周期、credential cache、ssh2/system SSH fallback、disconnect handler 和 bounded reconnect。
- [src/main/ssh/ssh-relay-session.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-session.ts)  
  每个 SSH target 的 relay session 单一权威，负责 deploy、provider 注册、reconnect、mux loss watcher、PTY lease reattach 和 replay 去重。
- [src/main/ssh/ssh-relay-deploy.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-deploy.ts)  
  远端 relay 部署与启动：版本目录、socket probe、detached launch、`--connect` bridge、Windows named pipe fallback。
- [src/main/ssh/ssh-relay-deploy-helpers.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-deploy-helpers.ts)  
  relay 部署 helper，包含 `waitForSentinel()` 对 bridge exit code 42 的 `RelayVersionMismatchError` 映射。
- [src/main/ssh/ssh-channel-multiplexer.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-channel-multiplexer.ts)  
  main 侧 JSON-RPC multiplexer，包含 request/notification、ack、keepalive、timeout、cancel 和 dispose 语义。
- [src/main/ssh/relay-protocol.ts](../../../../open-ai-desktop/orca/src/main/ssh/relay-protocol.ts)  
  main 侧 relay frame 协议常量、sentinel、keepalive/timeout 和 payload 上限。
- [src/main/providers/ssh-pty-provider.ts](../../../../open-ai-desktop/orca/src/main/providers/ssh-pty-provider.ts)  
  远端 PTY provider，代理 `pty.spawn`、`pty.attach`、resize、signal、serialize/revive，并把 relay PTY id 映射为 app PTY id。
- [src/relay/relay.ts](../../../../open-ai-desktop/orca/src/relay/relay.ts)  
  远端 daemon 入口，注册 handler、启动 socket server、处理 detached/stdin transport、grace timer、`--connect` 和 shutdown。
- [src/relay/dispatcher.ts](../../../../open-ai-desktop/orca/src/relay/dispatcher.ts)  
  relay 内 JSON-RPC dispatcher，支持 primary client 与多个 socket client，独立维护 client seq/ack/decoder。
- [src/relay/relay-handshake.ts](../../../../open-ai-desktop/orca/src/relay/relay-handshake.ts)  
  `--connect` 与 daemon socket 的版本握手，匹配后才输出 sentinel；版本不匹配通过 exit 42 暴露给部署 helper，是否 fresh launch 由 deploy path 决定。
- [src/relay/protocol.ts](../../../../open-ai-desktop/orca/src/relay/protocol.ts)  
  relay 侧自包含 protocol，实现 handshake frame、JSON-RPC frame、keepalive frame 和 decoder drain。
- [src/relay/pty-handler.ts](../../../../open-ai-desktop/orca/src/relay/pty-handler.ts)  
  远端 PTY 生命周期、100KB replay buffer、grace timer、spawn/attach/shutdown/serialize/revive。
- [src/relay/workspace-session-handler.ts](../../../../open-ai-desktop/orca/src/relay/workspace-session-handler.ts)  
  远端 workspace session 存储，写入 `~/.orca/sessions`，用 revision 和 presence TTL 管理多客户端协作。
- [src/shared/ssh-types.ts](../../../../open-ai-desktop/orca/src/shared/ssh-types.ts)  
  SSH target、connection state、relay grace 常量、remote PTY lease state 的 shared contract。
- [src/main/ssh/ssh-relay-session.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-session.test.ts)  
  覆盖 establish/reconnect、provider teardown、PTY reattach、replay 去重、过期 PTY、host sleep grace 和 port forward cleanup。
- [src/main/ssh/ssh-relay-deploy.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-deploy.test.ts)  
  覆盖 relay grace 默认值/无限期/上限、版本目录、target-specific socket 和 Windows fallback pipe。
- [src/main/ssh/ssh-relay-cross-version-isolation.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-relay-cross-version-isolation.test.ts)  
  验证新版本 deploy 不引用旧版本安装目录或旧 socket，避免跨版本误连。
- [src/relay/relay-handshake-roundtrip.test.ts](../../../../open-ai-desktop/orca/src/relay/relay-handshake-roundtrip.test.ts)  
  真实 socket pair 验证 handshake 通过、leftover bytes 保留和 mismatch 行为。
- [src/relay/protocol-handshake.test.ts](../../../../open-ai-desktop/orca/src/relay/protocol-handshake.test.ts)  
  验证 handshake frame 的编码、解析和独立 message type。
- [src/main/ssh/ssh-channel-multiplexer.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/ssh-channel-multiplexer.test.ts)  
  验证 keepalive、request timeout、cancel、handler 清理和 transport close 的 `CONNECTION_LOST`。
- [src/main/ssh/relay-protocol.test.ts](../../../../open-ai-desktop/orca/src/main/ssh/relay-protocol.test.ts)  
  验证 frame 编解码、ack、keepalive 和 message size 边界。
- [src/renderer/src/components/terminal-pane/pty-connection.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/components/terminal-pane/pty-connection.test.ts)  
  验证 deferred SSH reattach、passphrase 取消不自动连接、过期 session 冷启动 fallback 和 replay 写入。
- [src/renderer/src/app-startup-routing.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/app-startup-routing.test.ts)  
  验证 renderer 启动时 first-window startup services 先于 terminal reconnect。
- [src/renderer/src/store/slices/ssh.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/store/slices/ssh.test.ts)  
  验证 deferred SSH reconnect target/session 清理行为。

## 智慧（社区）

- 本主题暂不依赖外部社区资料。关键理解来自 Orca 自己的 relay daemon、SSH session state machine 和测试。

## 空白

- `deep-dive-relay-reconnect` 仍需进一步拆解 frame ack、socket client 切换、grace timer 与 stale request abort 的细粒度时序。
- 远端 CLI 的 `orca.cli` 请求如何从 relay 回调桌面 runtime，本主题只说明边界，不展开完整命令链路。

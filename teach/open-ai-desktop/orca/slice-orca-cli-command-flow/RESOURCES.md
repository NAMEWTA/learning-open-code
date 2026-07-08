# Orca CLI 命令执行全链路资源

## 知识

- [src/cli/index.ts](../../../../open-ai-desktop/orca/src/cli/index.ts)  
  CLI 主入口，处理 special shim、help、JSON 模式、spec 校验、remote selection 抑制和 `RuntimeClient` 构造。
- [src/cli/args.ts](../../../../open-ai-desktop/orca/src/cli/args.ts)  
  参数解析与命令规格校验，包含 boolean flag、repeatable flag、positionals normalize、global flags 和 browser `--page` 例外。
- [src/cli/specs/index.ts](../../../../open-ai-desktop/orca/src/cli/specs/index.ts)  
  `COMMAND_SPECS` 聚合点，决定 CLI 可见命令和允许 flag 的声明来源。
- [src/cli/specs/core.ts](../../../../open-ai-desktop/orca/src/cli/specs/core.ts)  
  core、repo、worktree、terminal 命令规格；`worktree current` 没有 selector flag，是 remote cwd shortcut 误用的关键证据。
- [src/cli/specs/serve.ts](../../../../open-ai-desktop/orca/src/cli/specs/serve.ts)  
  `orca serve` 的 foreground server command spec，声明 port、pairing-address、mobile-pairing、recipe-json 等 flag。
- [src/cli/specs/browser-basic.ts](../../../../open-ai-desktop/orca/src/cli/specs/browser-basic.ts)  
  browser 基础命令规格，展示 browser allowed flags 与 `--worktree`/`--page` 的声明入口。
- [src/cli/specs/browser-advanced.ts](../../../../open-ai-desktop/orca/src/cli/specs/browser-advanced.ts)  
  browser 高级命令规格，覆盖 cookie、viewport、intercept、capture、mouse、storage 等命令组。
- [src/cli/specs/orchestration.ts](../../../../open-ai-desktop/orca/src/cli/specs/orchestration.ts)  
  orchestration 命令规格，包含 `check --wait` stderr heartbeat 文案和 `ask` 的 timeout flag。
- [src/cli/dispatch.ts](../../../../open-ai-desktop/orca/src/cli/dispatch.ts)  
  handler 注册表，合并所有命令组并拒绝重复 key，最终用 `commandPath.join(' ')` 查 handler。
- [src/cli/runtime-client.ts](../../../../open-ai-desktop/orca/src/cli/runtime-client.ts)  
  兼容 barrel，向旧导入位置导出 `RuntimeClient`、`serveOrcaApp` 和错误类型。
- [src/cli/runtime/client.ts](../../../../open-ai-desktop/orca/src/cli/runtime/client.ts)  
  RuntimeClient 主逻辑：本地 metadata/socket、远程 pairing/environment、协议兼容、`openOrca()` 和 long-poll timeout policy。
- [src/cli/runtime/metadata.ts](../../../../open-ai-desktop/orca/src/cli/runtime/metadata.ts)  
  解析 CLI 默认 userData 路径，读取 runtime metadata，并验证 transport/authToken。
- [src/cli/runtime/status.ts](../../../../open-ai-desktop/orca/src/cli/runtime/status.ts)  
  本地 `status.get` 快路径，区分 not running、stale bootstrap、starting、ready。
- [src/cli/runtime/launch.ts](../../../../open-ai-desktop/orca/src/cli/runtime/launch.ts)  
  `orca open` 和 `orca serve` 的 app 启动路径，包含 foreground headless server 与 recipe JSON 分支。
- [src/cli/runtime/transport.ts](../../../../open-ai-desktop/orca/src/cli/runtime/transport.ts)  
  本地 Unix socket/named pipe transport，负责 request id、authToken、newline frame、keepalive refresh、runtimeId 防漂移。
- [src/cli/runtime/websocket-transport.ts](../../../../open-ai-desktop/orca/src/cli/runtime/websocket-transport.ts)  
  远程 WebSocket bridge，把 shared remote runtime client 错误映射为 CLI 错误。
- [src/cli/selectors.ts](../../../../open-ai-desktop/orca/src/cli/selectors.ts)  
  `active/current`、browser target、terminal handle、remote cwd shortcut 的解析边界。
- [src/cli/format.ts](../../../../open-ai-desktop/orca/src/cli/format.ts)  
  统一结果和错误输出，`--json` 下输出 RPC envelope，普通模式给 runtime unavailable 补 next step。
- [src/cli/help.ts](../../../../open-ai-desktop/orca/src/cli/help.ts)  
  root help 与 command help 文案，体现 CLI 面向用户的命令结构。
- [src/cli/handlers/core.ts](../../../../open-ai-desktop/orca/src/cli/handlers/core.ts)  
  `open`、`status`、`serve` 和 `claude-teams` 等核心入口。
- [src/cli/handlers/worktree.ts](../../../../open-ai-desktop/orca/src/cli/handlers/worktree.ts)  
  worktree 命令组，把 repo/worktree/parent/agent/startup flag 映射为 `worktree.*` RPC。
- [src/cli/handlers/terminal.ts](../../../../open-ai-desktop/orca/src/cli/handlers/terminal.ts)  
  terminal 命令组，包含 active terminal resolution、remote create 限制、`terminal.wait` timeout 和 exit code。
- [src/cli/handlers/browser-nav.ts](../../../../open-ai-desktop/orca/src/cli/handlers/browser-nav.ts)  
  browser navigation 命令组，展示 target resolution 和 per-command timeout override。
- [src/cli/handlers/browser-interact.ts](../../../../open-ai-desktop/orca/src/cli/handlers/browser-interact.ts)  
  browser interaction 命令组，展示 element/text/mouse flag 到 `browser.*` RPC 的薄映射。
- [src/cli/handlers/orchestration.ts](../../../../open-ai-desktop/orca/src/cli/handlers/orchestration.ts)  
  orchestration 命令组，包含 `check --wait` stderr heartbeat、structured payload、ask 的特殊 JSON 输出。
- [src/main/runtime/runtime-rpc.ts](../../../../open-ai-desktop/orca/src/main/runtime/runtime-rpc.ts)  
  main runtime RPC server 安全边界：metadata 发布、auth、long-poll cap、keepalive、WebSocket device token 和 dispatcher 调用。
- [src/main/runtime/rpc/unix-socket-transport.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/unix-socket-transport.ts)  
  main 侧本地 transport，读取 newline-delimited JSON，并只为 long-poll 启动 keepalive。
- [src/main/runtime/rpc/ws-transport.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/ws-transport.ts)  
  main 侧 WebSocket transport，负责连接上限、pre-auth timeout、heartbeat 和静态 web client。
- [src/main/runtime/rpc/core.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/core.ts)  
  RPC method、streaming method、request/response envelope、Zod schema 和 registry 基础类型。
- [src/main/runtime/rpc/dispatcher.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/dispatcher.ts)  
  runtime RPC dispatcher，解析 params、调用 method handler、映射错误并记录 feature interaction。
- [src/main/runtime/rpc/methods/index.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/methods/index.ts)  
  runtime RPC method manifest，集中列出 server 暴露的全部方法组。
- [src/main/runtime/rpc/methods/status.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/methods/status.ts)  
  最小 RPC 方法例子：`status.get` 直接返回 runtime status。
- [src/shared/runtime-bootstrap.ts](../../../../open-ai-desktop/orca/src/shared/runtime-bootstrap.ts)  
  runtime metadata 和 transport 查找的 shared contract。
- [src/shared/runtime-rpc-envelope.ts](../../../../open-ai-desktop/orca/src/shared/runtime-rpc-envelope.ts)  
  CLI 和 runtime 共用的 success/failure envelope 类型。
- [src/shared/remote-runtime-client.ts](../../../../open-ai-desktop/orca/src/shared/remote-runtime-client.ts)  
  远程 runtime request 客户端，支撑 CLI WebSocket 路径。
- [src/shared/protocol-version.ts](../../../../open-ai-desktop/orca/src/shared/protocol-version.ts)  
  runtime protocol 版本常量。
- [src/shared/protocol-compat.ts](../../../../open-ai-desktop/orca/src/shared/protocol-compat.ts)  
  client/server protocol 兼容判定。
- [src/shared/runtime-types.ts](../../../../open-ai-desktop/orca/src/shared/runtime-types.ts)  
  CLI status、worktree、terminal、browser 等 runtime result 类型来源。
- [src/cli/args.test.ts](../../../../open-ai-desktop/orca/src/cli/args.test.ts)  
  参数解析与 flag 校验测试，覆盖 `--flag=value`、repeatable flag、unknown flag。
- [src/cli/index.test.ts](../../../../open-ai-desktop/orca/src/cli/index.test.ts)  
  CLI 入口高覆盖测试，覆盖 help、serve、environment remote 抑制、remote cwd shortcut、terminal wait、positionals 冲突。
- [src/cli/handlers/orchestration.test.ts](../../../../open-ai-desktop/orca/src/cli/handlers/orchestration.test.ts)  
  orchestration handler 单元测试，覆盖 `check --timeout-ms`、`ask --timeout-ms`、structured payload 和 lifecycle group recipient guard。
- [src/cli/runtime-client.test.ts](../../../../open-ai-desktop/orca/src/cli/runtime-client.test.ts)  
  RuntimeClient 本地 socket、openOrca、structured failure、invalid response 测试。
- [src/cli/runtime/client-timeout-policy.test.ts](../../../../open-ai-desktop/orca/src/cli/runtime/client-timeout-policy.test.ts)  
  long-poll timeout policy 测试。
- [src/cli/runtime/transport.test.ts](../../../../open-ai-desktop/orca/src/cli/runtime/transport.test.ts)  
  本地 transport keepalive refresh 和 runtime unavailable 测试。
- [src/cli/runtime/websocket-transport.test.ts](../../../../open-ai-desktop/orca/src/cli/runtime/websocket-transport.test.ts)  
  remote pairing、saved environment 和 protocol compatibility 测试。
- [src/main/runtime/runtime-rpc.test.ts](../../../../open-ai-desktop/orca/src/main/runtime/runtime-rpc.test.ts)  
  runtime server auth、status、long-poll keepalive、runtime_busy 和 WebSocket scope 测试。
- [src/main/runtime/orchestration-cli-subprocess.test.ts](../../../../open-ai-desktop/orca/src/main/runtime/orchestration-cli-subprocess.test.ts)  
  subprocess 级测试，验证 `orchestration check --wait` 的 stderr JSON heartbeat、stdout 干净 JSON payload 和 line flush。
- [src/main/runtime/rpc/schemas.test.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/schemas.test.ts)  
  runtime method param schema 测试。
- [src/main/runtime/rpc/dispatcher-feature-interactions.test.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/dispatcher-feature-interactions.test.ts)  
  dispatcher 调用后记录 feature interaction 的测试。

## 智慧（社区）

- 本主题暂不依赖外部社区资料。关键理解来自 Orca 自己的 CLI/runtime RPC 源码和测试。

## 空白

- CLI 安装 wrapper、packaged asset 和 shell 集成可在单独主题里补。
- `orca.cli` 通过 SSH relay 回调远端命令的链路属于 relay 深挖主题，本主题只覆盖桌面/远程 runtime RPC 客户端主路径。

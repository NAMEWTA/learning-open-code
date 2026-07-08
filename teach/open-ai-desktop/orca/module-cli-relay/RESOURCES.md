# CLI 与远端 Relay 模块资源

## 知识

- [src/cli/index.ts](../../../../open-ai-desktop/orca/src/cli/index.ts)
  CLI 主入口，负责特殊 shim、参数解析、help、RuntimeClient 创建和 dispatch。
- [src/cli/dispatch.ts](../../../../open-ai-desktop/orca/src/cli/dispatch.ts)
  命令路径到 handler 的注册表，适合理解 CLI 命令如何落到具体执行函数。
- [src/cli/specs/index.ts](../../../../open-ai-desktop/orca/src/cli/specs/index.ts)
  CLI 命令规格聚合入口，适合查命令分组。
- [src/cli/runtime-client.ts](../../../../open-ai-desktop/orca/src/cli/runtime-client.ts)
  RuntimeClient 的兼容导出层，说明 CLI runtime client 已拆到 `src/cli/runtime/`。
- [src/relay/relay.ts](../../../../open-ai-desktop/orca/src/relay/relay.ts)
  SSH 远端 relay 主入口，包含 connect mode、daemon mode、grace period 和 handler 装配。
- [src/relay/dispatcher.ts](../../../../open-ai-desktop/orca/src/relay/dispatcher.ts)
  relay JSON-RPC dispatcher，处理 frame、keepalive、请求超时和多客户端状态。
- [src/relay/protocol.ts](../../../../open-ai-desktop/orca/src/relay/protocol.ts)
  relay 自包含协议定义，包含 frame header、handshake、keepalive 和 payload 限制。

## 智慧（社区）

- [Orca GitHub 仓库](https://github.com/stablyai/orca)
  通过 issues 和 PR 查 CLI/SSH/relay 行为变更、回归和真实使用场景。

## 空白

- 本模块主要依赖仓库内一手源码；暂不引入外部 SSH/JSON-RPC 教程，避免偏离 Orca 自身协议实现。

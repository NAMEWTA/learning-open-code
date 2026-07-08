# 共享协议与类型模块资源

## 知识

- [src/shared/runtime-rpc-envelope.ts](../../../../open-ai-desktop/orca/src/shared/runtime-rpc-envelope.ts)
  runtime RPC 成功、失败和 keepalive frame 的 Zod schema 与 TypeScript 类型。
- [src/shared/runtime-types.ts](../../../../open-ai-desktop/orca/src/shared/runtime-types.ts)
  runtime、terminal、browser、mobile session 和 graph sync 的核心类型。
- [src/shared/ssh-types.ts](../../../../open-ai-desktop/orca/src/shared/ssh-types.ts)
  SSH target、relay grace、连接状态、PTY lease 和端口转发类型。
- [src/shared/worktree-id.ts](../../../../open-ai-desktop/orca/src/shared/worktree-id.ts)
  worktree id 与 repo id 的解析函数，是多处状态映射的基础。
- [src/shared/workspace-session-schema.ts](../../../../open-ai-desktop/orca/src/shared/workspace-session-schema.ts)
  workspace session JSON 的 Zod 校验边界，保护 renderer 状态恢复。
- [src/shared/protocol-version.ts](../../../../open-ai-desktop/orca/src/shared/protocol-version.ts)
  runtime protocol version、兼容窗口和 capability 清单。
- [src/shared/types.ts](../../../../open-ai-desktop/orca/src/shared/types.ts)
  大型共享业务类型入口，适合按类型簇查找 UI/main/IPC 契约。

## 智慧（社区）

- [Orca GitHub 仓库](https://github.com/stablyai/orca)
  查协议兼容、mobile/desktop 版本漂移和跨端字段迁移问题。

## 空白

- 本模块是仓库内部契约层，没有外部标准文档；未来若引入公开 runtime 协议文档，应补充到此处。

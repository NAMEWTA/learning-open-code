# 主进程 Runtime 与 Daemon 模块资源

## 知识

- [src/main/index.ts](../../../../open-ai-desktop/orca/src/main/index.ts)  
  主进程装配入口，创建 `OrcaRuntimeService`、启动 `OrcaRuntimeRpcServer`，并把 daemon 初始化纳入首窗启动服务。
- [src/main/runtime/orca-runtime.ts](../../../../open-ai-desktop/orca/src/main/runtime/orca-runtime.ts)  
  主进程运行时状态所有者，管理 renderer graph、terminal handle、PTY 数据、mobile 会话、worktree 和 automation。
- [src/main/runtime/runtime-rpc.ts](../../../../open-ai-desktop/orca/src/main/runtime/runtime-rpc.ts)  
  runtime 控制面服务器，负责 Unix socket/named pipe、WebSocket、auth token、device token、E2EE pairing、long-poll keepalive 和 metadata 发布。
- [src/main/runtime/mobile-pairing-files.ts](../../../../open-ai-desktop/orca/src/main/runtime/mobile-pairing-files.ts)  
  移动端配对持久化文件常量，约束 device registry 与 E2EE keypair 一起迁移。
- [src/main/daemon/daemon-init.ts](../../../../open-ai-desktop/orca/src/main/daemon/daemon-init.ts)  
  daemon PTY provider 初始化、legacy adapter 保留、degraded fallback、restart 7 步和 cleanup 逻辑。
- [src/main/daemon/daemon-entry.ts](../../../../open-ai-desktop/orca/src/main/daemon/daemon-entry.ts)  
  独立 daemon 进程入口，解析 socket/token 参数、启动 daemon、处理 PTY native 异常和关闭信号。
- [src/main/runtime/runtime-rpc.test.ts](../../../../open-ai-desktop/orca/src/main/runtime/runtime-rpc.test.ts)  
  运行时 RPC 的 pairing、metadata、long-poll keepalive、runtime_busy 和连接关闭行为测试。
- [src/main/daemon/daemon-init.test.ts](../../../../open-ai-desktop/orca/src/main/daemon/daemon-init.test.ts)  
  daemon 初始化、重启、legacy provider、degraded provider 和监听器顺序的行为测试。

## 智慧（社区）

- [Orca GitHub 仓库](https://github.com/stablyai/orca)  
  通过 issues 和 PR 查 daemon 持久终端、移动端配对、runtime RPC 行为变化和真实回归场景。

## 空白

- 本主题主要依赖仓库内一手源码和测试；暂不引入通用 Electron IPC 或 node-pty 教程，避免偏离 Orca 自身的 runtime/daemon 设计。

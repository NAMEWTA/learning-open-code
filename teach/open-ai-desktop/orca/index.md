# Orca 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | Orca 技术栈、运行边界、目录职责与后续学习路线 |
| CLI 与远端 Relay | `./module-cli-relay/` | Orca 命令入口、远端 relay 协议与模块边界 |
| 共享协议与类型 | `./module-shared-contracts/` | shared 契约层、runtime/SSH/worktree 类型边界 |
| 主进程 Runtime 与 Daemon | `./module-main-runtime/` | runtime 状态层、RPC 控制面与 daemon PTY 宿主 |
| 主进程 IPC 边界 | `./module-main-ipc/` | preload API、IPC handlers 与本地/SSH/daemon 路由 |
| Renderer Shell 应用壳 | `./module-renderer-shell/` | React 入口、App shell、Zustand store 与 runtime graph 同步 |
| 移动端 Companion | `./module-mobile-companion/` | Expo app、pairing、host 列表与 WebSocket RPC client |
| Worktree 创建链路 | `./slice-worktree-create-flow/` | New Workspace 到 git worktree add、metadata 与终端交接 |
| SSH Relay 会话保活 | `./slice-ssh-relay-session-flow/` | SSH 连接、远端 relay、grace socket 与 PTY reattach |
| Orca CLI 命令执行链路 | `./slice-orca-cli-command-flow/` | 参数解析、handler、RuntimeClient 与 runtime RPC 边界 |
| 移动端配对与会话恢复 | `./slice-mobile-pairing-flow/` | 桌面 QR、E2EE 握手、host 保存与 Resume 恢复 |
| Relay 重连与 Grace Socket | `./deep-dive-relay-reconnect/` | Relay --connect、版本握手、grace socket 与 stale request |
| 开发规范、目录规范与命名规范 | `./dev-conventions/` | oxlint/oxfmt 工具链、src 分层目录、文件与代码命名约定 |

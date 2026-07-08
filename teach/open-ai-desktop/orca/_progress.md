# Orca 教学文档进度

> 最后更新：2026-07-07T21:01:40+08:00

## 总体状态

- 已完成：12 / 12 goals（100%）
- 当前阶段：当前计划内 L0/L1/L2/L4 教学主题已完成
- 当前工作区：`teach/open-ai-desktop/orca/`

## 按层级统计

| 层级 | 完成 | 总数 | 状态 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | 完成 |
| L1 模块总览 | 6 | 6 | 完成 |
| L2 垂直切片 | 4 | 4 | 完成 |
| L3 微观 API | 0 | 0 | 已发现 3 个候选，待入队细化 |
| L4 深度剖析 | 1 | 1 | 完成 |

## 最近完成

| Goal | 标题 | 主入口 | 审查 |
|------|------|--------|------|
| `L4-relay-reconnect` | Relay 断线重连与 Grace Socket 机制 | `deep-dive-relay-reconnect/lessons/0001-problem-frame.html` | 有条件通过，Major/Minor 已修复 |
| `L2-mobile-pairing-flow` | 移动端配对与会话恢复全链路 | `slice-mobile-pairing-flow/lessons/0001-flow-map.html` | 有条件通过，Major 已修复 |
| `L2-orca-cli-command-flow` | Orca CLI 命令执行全链路 | `slice-orca-cli-command-flow/lessons/0001-flow-map.html` | 有条件通过，Major 已修复 |
| `L2-ssh-relay-session-flow` | SSH Relay 会话保活全链路 | `slice-ssh-relay-session-flow/lessons/0001-flow-map.html` | 有条件通过，Major 已修复 |
| `L2-worktree-create-flow` | 创建 Worktree 并启动 Agent 全链路 | `slice-worktree-create-flow/lessons/0001-worktree-create-flow.html` | 有条件通过，Major 已修复 |
| `L1-mobile-companion` | 移动端 Companion 模块 | `module-mobile-companion/lessons/0001-mobile-companion-module-tour.html` | 有条件通过，Important 已修复 |
| `L1-renderer-shell` | Renderer 应用壳与状态模块 | `module-renderer-shell/lessons/0001-renderer-shell-module-tour.html` | 有条件通过，Important 已修复 |
| `L1-main-ipc` | 主进程 IPC 边界模块 | `module-main-ipc/lessons/0001-main-ipc-module-tour.html` | 有条件通过，Important 已修复 |
| `L1-main-runtime` | 主进程 Runtime 与 Daemon 模块 | `module-main-runtime/lessons/0001-main-runtime-module-tour.html` | 有条件通过，Important 已修复 |
| `L1-shared-contracts` | 共享协议与类型模块 | `module-shared-contracts/lessons/0001-shared-contracts-module-tour.html` | 复审通过 |
| `L1-cli-relay` | CLI 与远端 Relay 模块 | `module-cli-relay/lessons/0001-cli-relay-module-tour.html` | 有条件通过，Important 已修复 |
| `L0-project-overview` | Orca 项目总览 | `00-overview/lessons/0001-project-map.html` | 有条件通过，Important 已修复 |

## 当前队列

| Goal | 层级 | 标题 | 状态 | 依赖 |
|------|------|------|------|------|
| 无 | - | 当前计划内 goals 已完成 | - | - |

## 本轮记录

- L0 `00-overview` 完成：项目导览短课、总览参考、真实元文件、快照和审查记录均已落盘。
- L1 `module-cli-relay` 完成：worker 超时后由主 Agent 接管；审查提出 filetree、关键依赖、调用示例问题，已修复并通过主题审计。
- L1 `module-shared-contracts` 完成：worker 超时后由主 Agent 接管；初审 Critical 已修复，复审通过。
- L1 `module-main-runtime` 完成：独立审查为有条件通过；已修复导航/台账同步、短课文件树和快照引用问题。
- L1 `module-main-ipc` 完成：独立审查为有条件通过；已修复 registerCoreHandlers 边界、filesystem watcher 归属、索引表格和短课源码范围问题。
- L1 `module-renderer-shell` 完成：独立审查为有条件通过；已修复启动水合并发表述、session writer 门控说明、资源清单和进度 sources。
- L1 `module-mobile-companion` 完成：独立审查为有条件通过；已修复项目级台账同步、快照核心来源覆盖、Resume card 两层策略、pair-scan 资源和协议兼容说明。
- L2 `slice-worktree-create-flow` 完成：覆盖 New Workspace quick/background 创建、pending surface、store 分流、preload/main IPC、runtime RPC、local/SSH Git helper、metadata、setup/startup terminal handoff 和测试护栏；独立审查提出 SSH/runtime/startup terminal 边界与 terminal handoff 源文件缺失，已修复。
- L2 `slice-ssh-relay-session-flow` 完成：覆盖 renderer 启动 SSH 恢复、main SSH/relay session、detached relay daemon、`--connect` bridge、grace timer、版本握手、relay-lost backoff、PTY lease/replay/deferred reattach 与测试护栏；独立审查指出 version mismatch/stale socket 恢复、deferred target 分类和 grace clamp 责任边界，已修复。
- L2 `slice-orca-cli-command-flow` 完成：覆盖 CLI parse/help/spec 校验、handler dispatch、RuntimeClient 本地/远程 transport、main runtime RPC auth/schema/keepalive 边界和测试护栏；独立审查指出 remote `worktree current` 练习、具体 spec 文件、orchestration 测试和 `ask` long-poll 对比缺口，已修复。
- L2 `slice-mobile-pairing-flow` 完成：覆盖桌面 Settings QR、main mobile IPC、runtime pairing offer、device registry、E2EE WebSocket、mobile scan/deep link/paste、host-store、共享 RpcClient、foreground recovery、Resume 和测试护栏；独立审查指出 README 旧 TLS fingerprint 说明、shared payload scope 与 mobile local schema 边界、Resume 跨 host 排序和保存失败文案缺口，已修复。
- L4 `deep-dive-relay-reconnect` 完成：覆盖 deploy socket 复用/fresh launch、handshake sentinel、socket identity、grace timer、dispatcher stale request、main mux/backoff、PTY reattach/replay/revive 边界和测试护栏；独立审查指出 POSIX `ALIVE` 语义、`waitForSentinel()`/subprocess 测试引用、protocol-handshake 表述和项目索引缺口，已修复。
- 项目级审计当前通过：`audit_topic.py teach/open-ai-desktop/orca --all`。

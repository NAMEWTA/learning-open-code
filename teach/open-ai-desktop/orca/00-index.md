# Orca · 架构教学 Wiki

> 整体进度：12/12 goals · 100% · 当前计划内 L0/L1/L2/L4 已完成  
> 最后更新：2026-07-07T21:01:40+08:00

---

## 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | 100% |
| L1 模块总览 | 6 | 6 | 100% |
| L2 垂直切片 | 4 | 4 | 100% |
| L3 微观 API | 0 | 0 | 待 L2/L1 派生 |
| L4 深度剖析 | 1 | 1 | 100% |

---

## L0 · 项目总览

- **[项目导览短课](00-overview/lessons/0001-project-map.html)**  
  15 分钟建立 Orca 的多进程源码地图。
- **[Orca 项目总览参考](00-overview/reference/00-overview.html)**  
  技术栈、目录职责、架构图、源码豁免和后续 Backlog。

---

## L1 · 模块总览

### module-cli-relay — CLI 与远端 Relay 模块

- **[模块导览短课](module-cli-relay/lessons/0001-cli-relay-module-tour.html)**  
  理解 `src/cli` 与 `src/relay` 的入口、分层和执行边界。
- **[模块总览参考](module-cli-relay/reference/cli-relay-overview.html)**  
  CLI handler、RuntimeClient、relay frame、dispatcher 和关键依赖。
- **关联垂直切片**：
  - **[slice-orca-cli-command-flow](slice-orca-cli-command-flow/lessons/0001-flow-map.html)**（已生成）
  - **[slice-ssh-relay-session-flow](slice-ssh-relay-session-flow/lessons/0001-flow-map.html)**（已生成）
- **关联深度剖析**：
  - **[deep-dive-relay-reconnect](deep-dive-relay-reconnect/lessons/0001-problem-frame.html)**（已生成）

### module-shared-contracts — 共享协议与类型模块

- **[模块导览短课](module-shared-contracts/lessons/0001-shared-contracts-module-tour.html)**  
  理解 `src/shared` 如何承担跨 renderer/main/CLI/mobile 的契约层。
- **[模块总览参考](module-shared-contracts/reference/shared-contracts-overview.html)**  
  runtime RPC、SSH、workspace、worktree、协议版本和 schema 速查。
- **关联微观 API 候选**：
  - `RuntimeRpcEnvelopeSchema`
  - `worktree-id.ts`
  - `workspace-session-schema.ts`

### module-main-runtime — 主进程 Runtime 与 Daemon 模块

- **[模块导览短课](module-main-runtime/lessons/0001-main-runtime-module-tour.html)**  
  理解 runtime 状态层、RPC 控制面和 daemon PTY 宿主的职责边界。
- **[模块总览参考](module-main-runtime/reference/main-runtime-overview.html)**  
  主进程 runtime 接口、RPC server、pairing、long-poll、daemon restart 和测试佐证。
- **关联垂直切片**：
  - **[slice-worktree-create-flow](slice-worktree-create-flow/lessons/0001-worktree-create-flow.html)**（已生成）
  - **[slice-ssh-relay-session-flow](slice-ssh-relay-session-flow/lessons/0001-flow-map.html)**（已生成）
  - **[slice-mobile-pairing-flow](slice-mobile-pairing-flow/lessons/0001-flow-map.html)**（已生成）

### module-main-ipc — 主进程 IPC 边界模块

- **[模块导览短课](module-main-ipc/lessons/0001-main-ipc-module-tour.html)**  
  理解 renderer API、preload channel 和 main handler 的受控边界。
- **[模块总览参考](module-main-ipc/reference/main-ipc-overview.html)**  
  preload bridge、核心 handler 注册、PTY/Git/mobile IPC、provider 路由和测试佐证。
- **关联垂直切片**：
  - **[slice-worktree-create-flow](slice-worktree-create-flow/lessons/0001-worktree-create-flow.html)**（已生成）

### module-renderer-shell — Renderer 应用壳与状态模块

- **[模块导览短课](module-renderer-shell/lessons/0001-renderer-shell-module-tour.html)**  
  理解 renderer 入口、App shell、Zustand store 和 runtime graph 同步的职责边界。
- **[模块总览参考](module-renderer-shell/reference/renderer-shell-overview.html)**  
  启动水合、session 写回、统一 tab 模型、IPC 事件消费和测试佐证。
- **关联垂直切片**：
  - **[slice-worktree-create-flow](slice-worktree-create-flow/lessons/0001-worktree-create-flow.html)**（已生成）

### module-mobile-companion — 移动端 Companion 模块

- **[模块导览短课](module-mobile-companion/lessons/0001-mobile-companion-module-tour.html)**  
  理解 Expo app 入口、pairing、host 首页、共享 RPC client 和移动端 session 路由边界。
- **[模块总览参考](module-mobile-companion/reference/mobile-companion-overview.html)**  
  Pairing payload、host-store、client provider、RPC 传输、worktree/session 路由和测试佐证。
- **关联垂直切片**：
  - **[slice-mobile-pairing-flow](slice-mobile-pairing-flow/lessons/0001-flow-map.html)**（已生成）

---

## L2 · 垂直切片

- **[slice-worktree-create-flow](slice-worktree-create-flow/lessons/0001-worktree-create-flow.html)** — 创建 Worktree 并启动 Agent 全链路  
  参考：[`worktree-create-flow-overview.html`](slice-worktree-create-flow/reference/worktree-create-flow-overview.html)
- **[slice-ssh-relay-session-flow](slice-ssh-relay-session-flow/lessons/0001-flow-map.html)** — SSH Relay 会话保活全链路  
  参考：[`ssh-relay-session-flow-map.html`](slice-ssh-relay-session-flow/reference/ssh-relay-session-flow-map.html)
- **[slice-orca-cli-command-flow](slice-orca-cli-command-flow/lessons/0001-flow-map.html)** — Orca CLI 命令执行全链路  
  参考：[`orca-cli-command-flow-map.html`](slice-orca-cli-command-flow/reference/orca-cli-command-flow-map.html)
- **[slice-mobile-pairing-flow](slice-mobile-pairing-flow/lessons/0001-flow-map.html)** — 移动端配对与会话恢复全链路  
  参考：[`mobile-pairing-flow-map.html`](slice-mobile-pairing-flow/reference/mobile-pairing-flow-map.html)

---

## L4 · 深度剖析

- **[deep-dive-relay-reconnect](deep-dive-relay-reconnect/lessons/0001-problem-frame.html)** — Relay 断线重连与 Grace Socket 机制  
  参考：[`relay-reconnect-notes.html`](deep-dive-relay-reconnect/reference/relay-reconnect-notes.html)

---

## 源码覆盖状态

| 指标 | 当前状态 |
|------|----------|
| 已有主题引用源文件 | L0：17 个；CLI/Relay：10 个；Shared：8 个；Runtime/Daemon：9 个；IPC：11 个；Renderer：11 个；Mobile：19 个；Worktree Create：23 个；SSH Relay Session：22 个；Orca CLI Command：50 个；Mobile Pairing：40 个；Relay Reconnect：29 个 |
| 已完成模块/切片 | `00-overview`、`module-cli-relay`、`module-shared-contracts`、`module-main-runtime`、`module-main-ipc`、`module-renderer-shell`、`module-mobile-companion`、`slice-worktree-create-flow`、`slice-ssh-relay-session-flow`、`slice-orca-cli-command-flow`、`slice-mobile-pairing-flow`、`deep-dive-relay-reconnect` |
| 待覆盖主要源码面 | 无；当前计划内 goals 已完成 |
| 豁免范围 | 见 `00-overview/reference/00-overview.html` 中的源码豁免清单 |

# Orca 项目总览资源

## 知识

- [Orca README](../../../../open-ai-desktop/orca/README.md)
  项目定位、核心功能、支持的 agent 类型和用户可感知工作流入口。适用于判断 L2 垂直切片优先级。
- [package.json](../../../../open-ai-desktop/orca/package.json)
  技术栈、脚本、构建链路和运行时依赖。适用于识别 Electron、React、CLI、测试和发布边界。
- [electron.vite.config.ts](../../../../open-ai-desktop/orca/electron.vite.config.ts)
  Electron main、preload、renderer 的构建入口与启动诊断注入点。适用于理解桌面应用启动路径。
- [AGENTS.md](../../../../open-ai-desktop/orca/AGENTS.md)
  项目协作规则、设计系统、跨平台、SSH 和 Git provider 兼容性约束。适用于理解源码设计的非功能性压力。
- [src/main/index.ts](../../../../open-ai-desktop/orca/src/main/index.ts)
  Electron 主进程入口，集中装配窗口、runtime、daemon、IPC、agent hooks、telemetry 和更新服务。
- [src/main/persistence.ts](../../../../open-ai-desktop/orca/src/main/persistence.ts)
  本地 `orca-data.json` 状态、迁移、加密凭据和 flush 逻辑。适用于理解桌面端长期状态如何落盘。
- [src/main/sqlite/sync-database.ts](../../../../open-ai-desktop/orca/src/main/sqlite/sync-database.ts)
  基于 `node:sqlite` 的同步数据库适配器。适用于理解 OpenCode 会话扫描等 SQLite 读取路径。
- [src/preload/index.ts](../../../../open-ai-desktop/orca/src/preload/index.ts)
  渲染进程与主进程之间的 preload API 契约。适用于审计安全边界和 IPC 面。
- [src/cli/index.ts](../../../../open-ai-desktop/orca/src/cli/index.ts)
  `orca` 命令入口、参数解析、runtime client 分发和 agent team shim。适用于 CLI 垂直切片。
- [src/relay/relay.ts](../../../../open-ai-desktop/orca/src/relay/relay.ts)
  远端 relay 入口，负责 SSH 侧 JSON-RPC、PTY、文件、Git、preflight、plugin overlay 和断线重连。
- [mobile/README.md](../../../../open-ai-desktop/orca/mobile/README.md)
  移动端 companion app 的启动和开发线索。适用于后续 mobile 模块总览。

## 智慧（社区）

- [Orca GitHub 仓库](https://github.com/stablyai/orca)
  Issues、Pull Requests、Releases 和 Discussions 是理解设计取舍、缺陷修复和演进节奏的主要社区来源。
- [Orca Discord](https://discord.gg/fzjDKHxv8Q)
  README 推荐的用户社区。适用于验证真实工作流、跨平台问题和 agent 使用习惯。

## 空白

- 当前 L0 只使用仓库内一手资料与官方社区入口；没有引入第三方评测文章，避免把营销或过期观点混入架构学习。

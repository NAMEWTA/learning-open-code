# pi-orchestrator 模块总览 资源

## 知识

- [packages/orchestrator/package.json](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/package.json) — 包元数据、唯一依赖（pi-coding-agent）、exports 定义。适用于：了解包的对外接口和依赖关系。
- [packages/orchestrator/src/index.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/index.ts) — 模块主入口，聚合所有子模块的 re-export。适用于：了解包的完整公开接口清单。
- [packages/orchestrator/src/cli.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/cli.ts) — CLI 入口（#!/usr/bin/env node），包含 7 个子命令：serve/list/spawn/status/stop/rpc/rpc-stream。适用于：追踪 CLI 启动流程和所有可用命令。
- [packages/orchestrator/src/serve.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/serve.ts) — 服务启动入口：创建 Unix Socket 服务器、恢复实例、启动 Radius 心跳。适用于：理解 orchestrator 的整体启动流程。
- [packages/orchestrator/src/supervisor.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/supervisor.ts) — OrchestratorSupervisor 核心类：管理在线实例（spawn/stop/list/getInstance）、RPC 进程绑定、Radius 协调器集成。适用于：理解多实例生命周期管理的核心逻辑。
- [packages/orchestrator/src/rpc-process.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/rpc-process.ts) — RpcProcessInstance 类：通过 child_process.spawn 启动 pi-coding-agent 的 RPC 入口，通过 stdin/stdout 的 JSONL 协议通信。适用于：理解 orchestrator 如何控制编码 Agent 子进程。
- [packages/orchestrator/src/handler.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/handler.ts) — IPC 请求处理函数：将 6 种请求类型路由到 supervisor 对应方法，并组装响应。适用于：理解请求分发层的职责。
- [packages/orchestrator/src/ipc/protocol.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/ipc/protocol.ts) — IPC 协议类型定义：6 种请求/响应类型、InstanceSummary 结构、消息编解码函数。适用于：理解 IPC 通信的完整契约。
- [packages/orchestrator/src/ipc/server.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/ipc/server.ts) — IPC 服务器：基于 Node.js net 模块的 Unix Socket 服务器，支持 rpc_stream 持久连接模式。适用于：理解服务端如何接收和响应 IPC 请求。
- [packages/orchestrator/src/ipc/client.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/ipc/client.ts) — IPC 客户端：sendIpcRequest() 通过 Unix Socket 连接发送请求并等待单行响应。适用于：理解客户端如何与 orchestrator 服务通信。
- [packages/orchestrator/src/storage.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/storage.ts) — 文件持久化层：实例列表（instances.json）和机器记录（machine.json）的 CRUD 操作。适用于：理解 orchestrator 的数据持久化策略。
- [packages/orchestrator/src/radius.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/radius.ts) — Radius 云服务集成：机器/Pi 注册、心跳保持、自动重注册、退避重试。适用于：理解 orchestrator 的远程管理能力。
- [packages/orchestrator/src/types.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/types.ts) — 核心类型定义：InstanceStatus（5 种状态）、InstanceRecord、MachineRecord。适用于：了解 orchestrator 的数据模型。
- [packages/orchestrator/src/config.ts](https://github.com/earendil-works/pi/blob/main/packages/orchestrator/src/config.ts) — 配置模块：版本号、目录路径（~/.pi/orchestrator/）、Socket 路径、Bun 二进制检测。适用于：了解文件系统布局和路径约定。

## 智慧（社区）

- [Pi Discord](https://discord.com/invite/3cU7Bz4UPx) — 官方 Discord 社区。适用于：orchestrator 实验性功能、Radius 集成等高级话题讨论。

## 空白

- pi-orchestrator 标注为 "experimental"，官方文档和社区讨论极少。本课程完全基于源码分析产出。
- Radius 云服务（radius.pi.dev）的外部 API 文档未公开，目前无法获取完整接口规范。

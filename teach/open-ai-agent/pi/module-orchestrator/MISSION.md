# 使命：pi-orchestrator 模块总览

## 为什么
pi-orchestrator 是 Pi monorepo 中最上层的实验性包，它通过 Unix Socket IPC 将 pi-coding-agent 扩展为可远程管理的多实例编排服务。理解它的 IPC 协议设计、实例生命周期管理和 Radius 云服务集成，是掌握 Pi 分布式/多 Agent 协作方向的关键前提。

## 成功的样子
- 能说出 pi-orchestrator 在 monorepo 架构中的位置及其唯一依赖（pi-coding-agent）
- 能画出 CLI → IPC Server → Handler → Supervisor → RpcProcess 的五层调用链路图
- 能列出 IPC 协议支持的 6 种请求类型（spawn/list/stop/status/rpc/rpc_stream）
- 理解"单进程 → 子进程 JSONL RPC"的实例模型和 5 种状态机
- 了解 Radius 云服务在远程编排中的作用（机器注册、Pi 注册、心跳保持）

## 约束条件
- 具备 TypeScript/Node.js 编程基础，已通过 L0 总览课程了解 Pi 整体架构
- 已通过 L1-module-coding-agent 课程了解 pi-coding-agent 的 RPC 接口
- 学习时间碎片化，每节课不超过 15 分钟
- 以源码阅读为主，不要求运行完整项目

## 不在范围内
- RpcProcess 子进程的逐行 JSONL 协议解析细节
- Radius 云服务的 API 设计文档
- pi-coding-agent 的工具注册和 Hook 系统（module-coding-agent 已覆盖）
- 性能优化与并发控制的具体策略

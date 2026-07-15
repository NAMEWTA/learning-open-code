# 使命：ACP 适配器与注册中心

## 为什么
理解 Hermes Agent 如何通过 Agent Client Protocol（ACP）暴露为 Zed、Codex、Claude Code 等编辑器可直接调用的标准 Agent。掌握 acp_adapter/ 的桥接架构后，才能在自己的 Agent 项目中实现 ACP 兼容，或为 Hermes Agent 扩展自定义 ACP 行为。

## 成功的样子
- 能画出 acp_adapter/ 的内部组件交互图（entry -> server -> session + events -> tools）
- 能说出 HermesACPAgent 如何实现 acp.Agent 接口的 8 个核心方法（initialize、authenticate、prompt、cancel 等）
- 能解释 SessionManager 如何通过 SessionDB 实现跨进程重启的会话持久化
- 能理解 ACP 事件桥接机制：AIAgent 的工作线程如何通过 asyncio.run_coroutine_threadsafe 将回调转为 ACP 通知

## 约束条件
- 学习方式：阅读教学课程 + 对照源码验证
- 先修要求：已完成 L0 Hermes Agent 项目总览，理解 ACP 协议的基本概念
- 本模块聚焦 acp_adapter/ 和 acp_registry/，不深入 acp Python SDK 本身的实现

## 不在范围内
- ACP 协议规范的逐条解读（属于 ACP 协议文档范畴）
- Zed、Codex 等 ACP 客户端的使用教程（属于编辑器使用手册）
- hermes_cli/ 中其他 CLI 命令的实现
- tools/ 目录下具体工具的审批逻辑内部实现

# ACP 适配器与注册中心 资源

## 知识

- [acp_adapter/ — 源码目录](https://github.com/NousResearch/hermes-agent/tree/main/acp_adapter)
  11 个 Python 文件（约 240 KB），实现 Hermes Agent 的 ACP 适配器。entry.py 为 CLI 入口，server.py 为核心 Agent 实现，session.py 管理会话生命周期，events.py 桥接工作线程到 ACP 事件流，tools.py 提供 Hermes 工具到 ACP ToolKind 的映射。

- [acp_registry/agent.json — 注册描述文件](https://github.com/NousResearch/hermes-agent/blob/main/acp_registry/agent.json)
  ACP 注册中心的 Agent 元数据（id、name、版本、分发方式），供 ACP 客户端自动发现和安装 Hermes Agent。

- [ACP 协议规范](https://github.com/agent-client-protocol/agent-client-protocol)
  Agent Client Protocol 的官方仓库，定义了 Agent 与编辑器客户端之间的标准通信接口（初始化握手、会话管理、消息提示、工具调用、权限审批）。

- [Hermes Agent ACP 功能文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)
  Hermes Agent 官方文档中的 ACP 功能说明，涵盖安装、配置、与 Zed/Codex 编辑器的集成方式。

## 智慧（社区）

- [Nous Research Discord](https://discord.gg/nousresearch)
  官方 Discord 社区，适用于 ACP 集成问题、功能请求、架构讨论。

- [r/nousresearch](https://reddit.com/r/nousresearch)
  Nous Research 官方 subreddit，适用于 Hermes Agent 使用经验分享与问题排查。

- [Zed ACP 集成文档](https://zed.dev/docs/assistant/agents)
  Zed 编辑器对 ACP Agent 的集成文档，理解客户端视角的 ACP 协议使用方式。

## 空白

- ACP 协议规范中部分细节（如 `session/load` 的历史重放要求）缺乏独立的实现指南，主要依赖各 Agent 的源码实现作为参考。
- acp_adapter/ 中各模块的设计决策（如为何使用 ContextVar 隔离编辑审批、为何 ThreadPoolExecutor max_workers=4）缺乏独立的设计文档说明。

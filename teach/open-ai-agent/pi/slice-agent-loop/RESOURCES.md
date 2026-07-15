# Agent 对话循环全链路 资源

## 知识

- [源码：packages/agent/src/agent-loop.ts](https://github.com/earendil-works/pi/blob/main/packages/agent/src/agent-loop.ts)
  Agent 主循环的完整实现（749 行）。本课程的核心分析对象，包含 runLoop、streamAssistantResponse、executeToolCalls 三大核心函数。适用于：理解双层循环控制流、事件发放时序、工具执行 pipeline。

- [源码：packages/agent/src/agent.ts](https://github.com/earendil-works/pi/blob/main/packages/agent/src/agent.ts)
  Agent 类定义（576 行）。封装 prompt()/continue() 入口、状态管理、事件分发。适用于：理解用户 API 如何桥接到 agent-loop.ts 的底层函数。

- [源码：packages/agent/src/types.ts](https://github.com/earendil-works/pi/blob/main/packages/agent/src/types.ts)
  核心类型定义（429 行）。AgentEvent 联合类型、AgentLoopConfig、StreamFn 契约。适用于：查阅事件结构、钩子签名、配置选项。

- [参考文档：../module-agent/reference/agent-overview.html](../module-agent/reference/agent-overview.html)
  pi-agent-core 的接口清单与事件类型速查表。适用于：快速查阅 Agent 类 API 和 AgentEvent 的完整枚举。

## 智慧（社区）

- [Pi GitHub Issues](https://github.com/earendil-works/pi/issues)
  项目 Issue 追踪。适用于：了解 agent loop 相关的已知问题、设计讨论、社区反馈。

## 空白

- 目前未找到 pi-agent-core 的独立技术博客或第三方深度分析文章。该包作为 Pi monorepo 的内部模块，外部社区讨论主要集中在 pi-coding-agent 的 CLI 使用体验上。

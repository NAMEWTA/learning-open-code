# pi-agent-core 模块资源

## 知识

- [源码：packages/agent/src/index.ts](https://github.com/earendil-works/pi/blob/main/packages/agent/src/index.ts)
  pi-agent-core 主入口文件，汇总所有公开导出。适用于：了解模块的完整公开 API 面。

- [源码：packages/agent/src/agent.ts](https://github.com/earendil-works/pi/blob/main/packages/agent/src/agent.ts)
  Agent 类完整实现（575 行），包含状态管理、消息队列、事件订阅、生命周期控制。适用于：理解 Agent 的面向用户 API 设计。

- [源码：packages/agent/src/agent-loop.ts](https://github.com/earendil-works/pi/blob/main/packages/agent/src/agent-loop.ts)
  Agent 主循环实现（749 行），包含双层循环控制、LLM 流式响应处理、工具调用执行（串行/并行）。适用于：理解 Agent 运行时的核心控制流。

- [源码：packages/agent/src/types.ts](https://github.com/earendil-works/pi/blob/main/packages/agent/src/types.ts)
  类型定义文件，涵盖 AgentState、AgentEvent、AgentTool、AgentLoopConfig 等核心类型。适用于：查阅 API 类型契约。

- [源码：packages/agent/src/harness/](https://github.com/earendil-works/pi/tree/main/packages/agent/src/harness/)
  运行时基础设施目录，包含消息处理、会话持久化、上下文压缩、环境适配等模块。适用于：深入理解 Agent 运行时的支撑组件。

- [npm 包：@earendil-works/pi-agent-core](https://www.npmjs.com/package/@earendil-works/pi-agent-core)
  npm 发布页，包含 README 和版本历史。

## 智慧（社区）

- [Pi GitHub Issues](https://github.com/earendil-works/pi/issues)
  问题跟踪与功能讨论。适用于：了解已知问题、设计决策讨论。

- [Pi Discord](https://discord.gg/pi)
  官方 Discord 社区，开发者交流与技术支持。

## 空白

- 尚未发现 pi-agent-core 的独立使用教程或博客文章（多数内容围绕 pi-coding-agent CLI 使用）。
- 缺少 pi-agent-core 与 pi-coding-agent 之间接口契约的独立文档。

# 使命：pi-agent-core — Agent 运行时模块总览

## 为什么
学习 pi-agent-core 的内部架构，以便理解 Pi 的 Agent 运行时如何实现传输抽象、状态管理、工具调用和 attachment 支持。掌握此模块后，能够基于 pi-agent-core 构建自定义 Agent 应用，或在 pi-coding-agent 中定位 Agent 行为问题的根因。

## 成功的样子
- 能画出 pi-agent-core 的内部分层结构图（核心循环 → 消息处理 → 会话持久化 → 上下文压缩 → 环境适配）
- 能说出 Agent 类的关键公开 API（prompt、continue、steer、followUp、subscribe）及其用法
- 能理解 Agent 主循环的双层设计（外层 follow-up → 内层 tool-call + steering）
- 能阅读 agent.ts 和 agent-loop.ts 源码并解释关键类型（AgentMessage、AgentEvent、AgentTool）

## 约束条件
- 教学语言为简体中文
- 代码标识符保留原始英文命名
- 每节课 15 分钟内完成，800-1200 中文字

## 不在范围内
- pi-ai（LLM API 层）的详细实现
- pi-coding-agent 的 CLI 入口和工具实现
- pi-tui 的终端渲染细节
- 具体 Provider（OpenAI/Anthropic/Google）的 API 差异

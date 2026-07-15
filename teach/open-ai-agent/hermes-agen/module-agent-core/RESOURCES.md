# Agent 核心引擎 资源

## 知识

- [agent/conversation_loop.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/agent/conversation_loop.py)
  核心对话循环实现（295 KB），`run_conversation()` 函数体约 3900 行，包含模型调用、工具分发、重试降级、压缩触发的完整流程。适用于深入理解一次对话回合的生命周期。

- [agent/context_compressor.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/agent/context_compressor.py)
  自动上下文压缩器（149 KB），使用辅助模型对对话历史生成结构化摘要，在 token 预算内保护 head（系统提示词）和 tail（最近消息）。适用于理解长对话的 token 管理策略。

- [agent/memory_manager.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/agent/memory_manager.py)
  记忆管理器（43 KB），编排外部 MemoryProvider 插件，在回合前后拉取/同步记忆并注入系统提示词。适用于理解跨会话记忆持久化机制。

- [agent/tool_executor.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/agent/tool_executor.py)
  工具调用执行引擎（79 KB），支持串行和并发（最多 8 线程）两种调度模式，含权限守卫、预算控制、结果持久化。适用于理解 agent 如何安全执行模型请求的工具调用。

- [agent/curator.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/agent/curator.py)
  技能策展器（83 KB），空闲时触发后台 review agent，自动维护 agent 创建技能的声明周期（归档/合并/打补丁）。适用于理解自进化学习闭环的实现。

- [agent/prompt_builder.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/agent/prompt_builder.py)
  系统提示词构建器（94 KB），负责组装身份声明、平台提示、技能索引、上下文文件注入。适用于理解系统提示词的构成要素。

- [agent/agent_init.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/agent/agent_init.py)
  Agent 初始化（104 KB），`init_agent()` 函数 ~1400 行，处理 60+ 参数的凭证解析、provider 自动检测、context engine 引导。适用于理解 AIAgent 实例的构建过程。

- [Hermes Agent 官方文档](https://github.com/NousResearch/hermes-agent)
  项目 README 和 docs/ 目录包含架构设计文档、安全模型、中间件说明。

## 智慧（社区）

- [r/nousresearch](https://reddit.com/r/nousresearch)
  Nous Research 官方 subreddit，适用于：架构讨论、使用问题、新功能反馈。

- [Hermes Agent Discord](https://discord.gg/nousresearch)
  官方 Discord 社区，适用于：实时问答、bug 报告、功能请求。

## 空白

- agent/ 模块各子层的详细设计文档（如对话循环状态机、压缩算法选择理由）在公开资料中较少，主要依赖源码注释和 docstring。
- curator 的自动技能质量评估机制缺乏独立的设计说明文档。

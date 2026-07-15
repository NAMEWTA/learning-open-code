# 使命：Agent 对话全链路

## 为什么
理解 Hermes Agent 从 CLI 输入到 LLM 响应的完整数据流链路，掌握一次对话请求穿越 CLI 入口、Agent 初始化、对话循环、LLM API 调用、响应构建、上下文压缩这六个阶段时的关键函数、数据变换和异常处理机制。这能让你在调试 Agent 行为异常、自定义工具调用流程或扩展新模型适配时，快速定位问题所在的精确环节。

## 成功的样子
- 画出从 `cli.py` → `run_agent.AIAgent` → `conversation_loop.run_conversation()` → `chat_completion_helpers` → Provider API → 响应组装 → `context_compressor` 的完整调用链
- 解释 `build_turn_context()` 在每轮对话开始时做了哪些准备工作（系统提示词恢复、消息清洗、前置压缩）
- 说出 Provider 故障时 `try_activate_fallback()` 的链式切换机制，以及 `_sync_failover_system_message()` 如何同步模型身份到提示词
- 根据日志中的 api_call_count 和 _turn_exit_reason 判断一次对话回合的终止原因

## 约束条件
- 源码体量巨大（`conversation_loop.py` 295KB、`chat_completion_helpers.py` 147KB、`context_compressor.py` 149KB），无法一次性精读，需分层拆解
- 需交叉引用已完成的 L1 课程：`module-agent-core`（四层架构）、`module-agent-entry`（CLI 入口）、`module-tools`（工具注册）

## 不在范围内
- 单个工具（terminal_tool、browser_tool）的内部实现细节——由 `slice-tool-execution-approval` 覆盖
- 技能创建与自改进完整流程——由 `slice-skill-lifecycle` 覆盖
- 多平台消息网关的投递机制——由 `slice-multi-platform-message` 覆盖

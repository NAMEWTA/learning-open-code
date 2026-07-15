# Agent 对话全链路 资源

## 知识

- [源码：agent/conversation_loop.py (295KB)](../../../../open-ai-agent/hermes-agen/agent/conversation_loop.py)
  对话主循环核心文件，包含 `run_conversation()`（L518）、`_perform_api_call()`（L1306）、`_restore_or_build_system_prompt()`（L277）、`_sync_failover_system_message()`（L492）。适用于：理解主循环结构、回合终止条件、中断处理。

- [源码：agent/chat_completion_helpers.py (147KB)](../../../../open-ai-agent/hermes-agen/agent/chat_completion_helpers.py)
  LLM API 调用封装，包含 `interruptible_api_call()`（L174）、`build_api_kwargs()`（L606）、`build_assistant_message()`（L879）、`try_activate_fallback()`（L1172）。适用于：理解多 Provider 适配、流式/非流式调用、Provider 故障链式切换。

- [源码：agent/prompt_builder.py (53KB)](../../../../open-ai-agent/hermes-agen/agent/prompt_builder.py)
  系统提示词组装，包含 `build_environment_hints()`（L1047）、`computer_use_guidance()`（L470）。适用于：理解平台感知、技能清单注入、上下文文件扫描。

- [源码：cli.py (前 100 行)](../../../../open-ai-agent/hermes-agen/cli.py)
  Fire CLI 入口，命令解析与 AIAgent 构造入口。适用于：追踪一条用户消息如何进入系统。

- [源码：run_agent.py (AIAgent 类)](../../../../open-ai-agent/hermes-agen/run_agent.py)
  AIAgent 核心类，L393 定义，包含 60+ 构造参数。`run_conversation()` 在此做薄层转发到 `conversation_loop.py`。

- [源码：agent/context_compressor.py (149KB)](../../../../open-ai-agent/hermes-agen/agent/context_compressor.py)
  上下文压缩与摘要生成。适用于：理解 token 预算超限时如何自动压缩对话历史。

## 智慧（社区）

- [Hermes Agent GitHub Issues](https://github.com/user/hermes-agent/issues)
  可观察真实用户遇到的对话循环异常、Provider 兼容性问题、上下文压缩 bug。适用于：理解生产环境中的边界情况。

## 空白

- 缺少各 Provider（OpenAI/Anthropic/OpenRouter/Bedrock）的 API 调用差异对比文档——目前 `build_api_kwargs()` 中的分支逻辑散落在代码中，无统一说明。
- 缺少 `conversation_loop.py` 中 30+ 个 `api_call_count` 条件分支的决策表——需要后续梳理成速查表。

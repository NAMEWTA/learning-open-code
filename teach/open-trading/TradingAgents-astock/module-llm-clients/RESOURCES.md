# LLM 客户端适配层 资源

## 知识

- [LangChain Chat Models 文档](https://python.langchain.com/docs/integrations/chat/)
  LangChain 统一 Chat Model 接口的官方文档。适用于：理解 ChatOpenAI / ChatAnthropic / ChatGoogleGenerativeAI 等底层 SDK 的通用调用模式。
- [OpenAI Responses API vs Chat Completions](https://platform.openai.com/docs/guides/responses)
  OpenAI 新版 Responses API 的官方说明。适用于：理解 `use_responses_api=True` 的含义以及 content 为何返回 list 而非 string。
- [DeepSeek API 文档 — thinking mode](https://api-docs.deepseek.com/guides/reasoning_model)
  DeepSeek 推理模型的 reasoning_content 往返机制。适用于：理解 `DeepSeekChatOpenAI` 为何需要覆写 `_get_request_payload` 和 `_create_chat_result`。
- 源码入口: `tradingagents/llm_clients/__init__.py` — 只导出 `BaseLLMClient` 和 `create_llm_client` 两个符号

## 智慧（社区）

- [LangChain Discord](https://discord.gg/langchain) — LangChain 社区，适合 Chat Model 集成和自定义 Client 实现的讨论
- [TradingAgents-Astock Issues](https://github.com/simonlin1212/TradingAgents-astock/issues) — 项目 Issue 跟踪，包含 LLM 兼容性问题（如 #42 API Key 环境变量命名错误）的修复记录

## 空白

- OpenRouter 和 Azure 没有在 model_catalog 中注册模型列表（OpenRouter 动态获取，Azure 接受任意部署名），这两个 provider 的模型选择行为未在代码中显式文档化
- 各 provider 的结构化输出（with_structured_output）支持程度差异未建立统一的能力矩阵
- 双 LLM 策略下 quick_think/deep_think 的切换时机与 cost 量化分析缺失

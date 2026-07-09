# LLM 供应商路由与适配链路 资源

## 知识

- [factory.py](https://github.com/simonlin1212/TradingAgents-astock/blob/main/tradingagents/llm_clients/factory.py) — 工厂路由入口，11 种 provider → 4 个 Client 类的映射
- [base_client.py](https://github.com/simonlin1212/TradingAgents-astock/blob/main/tradingagents/llm_clients/base_client.py) — 抽象基类 `BaseLLMClient` 与 `normalize_content()` 归一化函数
- [openai_client.py](https://github.com/simonlin1212/TradingAgents-astock/blob/main/tradingagents/llm_clients/openai_client.py) — OpenAI 兼容客户端（承载 8 种 provider），含 DeepSeek 特殊处理
- [anthropic_client.py](https://github.com/simonlin1212/TradingAgents-astock/blob/main/tradingagents/llm_clients/anthropic_client.py) — Anthropic Claude 客户端
- [google_client.py](https://github.com/simonlin1212/TradingAgents-astock/blob/main/tradingagents/llm_clients/google_client.py) — Google Gemini 客户端，含 thinking_level 映射
- [azure_client.py](https://github.com/simonlin1212/TradingAgents-astock/blob/main/tradingagents/llm_clients/azure_client.py) — Azure OpenAI 客户端
- [model_catalog.py](https://github.com/simonlin1212/TradingAgents-astock/blob/main/tradingagents/llm_clients/model_catalog.py) — 9 供应商 × 2 模式模型注册表
- [validators.py](https://github.com/simonlin1212/TradingAgents-astock/blob/main/tradingagents/llm_clients/validators.py) — 模型名白名单校验
- [default_config.py](https://github.com/simonlin1212/TradingAgents-astock/blob/main/tradingagents/default_config.py) — 默认 LLM 配置（quick_think_llm / deep_think_llm）
- [LangChain ChatOpenAI 文档](https://python.langchain.com/docs/integrations/chat/openai/) — OpenAI 兼容 Chat Model 官方文档
- [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat) — Chat Completions 协议规范（8 种 provider 的通用协议基础）

## 智慧（社区）

- [LangChain Discord](https://discord.gg/langchain) — LangChain 社区，适用于 ChatModel 集成问题
- [TradingAgents Issues](https://github.com/simonlin1212/TradingAgents-astock/issues) — 项目自身 Issue 区，模型兼容性问题常在此讨论

## 空白

- 各 provider 的 API 差异细节（如 DeepSeek thinking mode 协议、Gemini thinking_level 映射规则）分散在各家官方文档中，暂无统一对比资料
- 双 LLM 策略的成本/延迟基准测试数据——目前只有设计层面的定性描述

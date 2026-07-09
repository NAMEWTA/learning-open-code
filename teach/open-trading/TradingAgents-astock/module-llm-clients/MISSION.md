# 使命：LLM 客户端适配层——11 种 provider 统一接口

## 为什么
理解 TradingAgents-Astock 如何用一套统一接口屏蔽 11 种 LLM 供应商（OpenAI/Anthropic/Google/Azure/DeepSeek/xAI/Qwen/GLM/MiniMax/Ollama/OpenRouter）的差异。掌握工厂路由、模型注册表与内容归一化机制，为后续自定义接入新供应商或调试 LLM 调用问题打下基础。

## 成功的样子
- 能画出 11 种 provider 到 4 个具体 Client 类的映射关系图
- 能解释 `normalize_content()` 为什么存在以及它解决了什么问题
- 能说出双 LLM 策略（quick_think/deep_think）在 default_config.py 和 model_catalog.py 两处的体现

## 约束条件
- 具备 Python 基础，了解 ABC 抽象基类与依赖注入概念
- 已阅读 L0 项目总览，了解项目整体架构与双 LLM 策略

## 不在范围内
- LangChain ChatOpenAI/ChatAnthropic 等 SDK 的内部实现细节
- Agent 层如何调用 LLM（属于 module-agents）
- Graph 层如何注入 LLM 实例（属于 module-graph）

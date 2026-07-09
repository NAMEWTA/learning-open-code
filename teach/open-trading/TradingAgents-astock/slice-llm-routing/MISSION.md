# 使命：LLM 供应商路由与适配链路

## 为什么
TradingAgents-Astock 同时支持 11 种 LLM provider，通过工厂模式在运行时按配置字符串路由到 4 个具体客户端类。理解这条从 `llm_provider` 配置键到最终 API 调用的完整链路，是后续扩展新 provider、调试模型切换问题、优化双 LLM 策略的基础。

## 成功的样子
- 能画出 `default_config(llm_provider) → factory.create_llm_client() → 具体 Client.get_llm() → LangChain ChatModel → API 调用` 的完整路由链路
- 能解释 `_OPENAI_COMPATIBLE` 元组的 8 合 1 复用设计、懒加载 import 策略、以及 provider 参数透传机制
- 能说出双 LLM（quick_think / deep_think）在配置层、注册表层、工厂层的体现方式，以及 graph 层如何为 14 个 quick Agent 和 2 个 deep Agent 分别创建客户端

## 约束条件
- 已完成 L0 项目全景图和 L1 module-llm-clients 模块总览
- 本节聚焦 LLM 路由与适配链路，不涉及 Agent 分析逻辑和 Graph 工作流编排
- 每节短课 ≤1500 中文、≤4 个 h2 章节

## 不在范围内
- Agent 层的多空辩论与角色逻辑（归属 module-agents / slice-analysis-pipeline）
- Graph 层的节点编排与状态传递（归属 module-graph）
- 数据获取链路（归属 slice-data-fetching）

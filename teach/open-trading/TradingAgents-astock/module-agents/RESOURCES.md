# Agent 系统模块 资源

## 知识

- [TradingAgents 论文 (arXiv:2412.20138)](https://arxiv.org/abs/2412.20138) — 原版多 Agent 投研框架的学术论文，理解 Bull/Bear 辩论机制的设计初衷
- [LangGraph 官方文档 — StateGraph](https://langchain-ai.github.io/langgraph/concepts/low_level/) — 理解 Agent 节点如何通过 state 字典共享上下文
- [LangChain Tool Calling 指南](https://python.langchain.com/docs/how_to/tool_calling/) — 理解 Analyst Agent 如何绑定工具集 (bind_tools)
- [Pydantic BaseModel 文档](https://docs.pydantic.dev/latest/concepts/models/) — 结构化输出 Schema（ResearchPlan / TraderProposal / PortfolioDecision）的基类
- 源码入口: `tradingagents/agents/__init__.py` — 所有 Agent 工厂函数的统一导出点

## 智慧（社区）

- [TradingAgents GitHub Issues](https://github.com/TauricResearch/TradingAgents/issues) — 原版社区讨论，关注 Agent 角色扩展和辩论机制的演进
- [LangChain Discord](https://discord.gg/langchain) — LangGraph/LangChain 社区，适合 Agent 编排架构的深入讨论

## 空白

- A 股特定监管规则（涨跌停、T+1、ST 制度）在 Agent prompt 中的编码方式尚无系统性文档
- 7 个 Analyst 报告之间的信息冗余度与互补性的量化分析缺失
- 结构化输出降级（fallback to freetext）在 9 个 LLM 供应商上的成功率对比缺失

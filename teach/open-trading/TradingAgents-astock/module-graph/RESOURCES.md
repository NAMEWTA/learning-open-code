# LangGraph 工作流引擎 资源

## 知识

- [LangGraph 官方文档 — StateGraph](https://langchain-ai.github.io/langgraph/concepts/low_level/)
  StateGraph API、条件边、状态 Schema 定义。适用于：理解 setup.py 中的 `workflow.add_node` / `add_conditional_edges` 调用。

- [LangGraph Checkpointing 指南](https://langchain-ai.github.io/langgraph/concepts/persistence/)
  SqliteSaver 断点续跑原理及 thread_id 机制。适用于：理解 checkpointer.py 的 `get_tuple` / `checkpoint_step` 设计。

- [TradingAgents 论文 — arXiv:2412.20138](https://arxiv.org/abs/2412.20138)
  原版 TradingAgents 框架的学术论文，包含 multi-agent 辩论和风险分析的算法描述。适用于：理解为什么要串联 Analyst 以及辩论轮次设计的理论依据。

- [TradingAgents-Astock 源码](https://github.com/simonlin1212/TradingAgents-astock)
  本 fork 的完整源码仓库，graph 模块位于 `tradingagents/graph/`。

## 智慧（社区）

- [LangGraph GitHub Discussions](https://github.com/langchain-ai/langgraph/discussions)
  LangGraph 官方讨论区，可查阅复杂工作流设计模式和 checkpointer 使用问题。

## 空白

- 暂无专门讲解"LLM Agent 工作流中 Analyst 串联 vs 并行的设计权衡"的资源——当前知识来源于论文的算法描述和源码阅读
- 缺乏 A 股场景下 graph pipeline 调优的实践文章

# 使命：LangGraph 工作流引擎模块——状态图拓扑与传播

## 为什么
理解 TradingAgents-Astock 如何用 LangGraph StateGraph 将 7 个 Analyst、辩论、风控串联为一条可审计的决策 pipeline，是掌握整个框架的核心。只有读懂 graph 层的节点拓扑、状态传播、条件路由、断点续跑和双 LLM 分配策略，才能自行定制分析流程、添加新 Agent 角色或调试 pipeline 卡死问题。

## 成功的样子
- 能画出 setup.py 中 7 阶段 pipeline 的完整节点-边拓扑图，解释每个 Analyst 为什么串联而非并行
- 能追踪从 TradingAgentsGraph.propagate() 到最终的 Buy/Sell 信号经历的每一步状态变更
- 能说明 conditional_logic 的两种条件路由模式（工具调用循环 / 辩论轮次计数）及其在图中的位置
- 能解释 checkpointer 如何实现崩溃恢复，以及 SQLite 分 ticker 存储的设计理由

## 约束条件
- 已具备 Python 基础，了解 LangGraph / 状态机基本概念
- 已通过 L0 课程了解项目全貌
- 代码阅读为主，不需要本地运行

## 不在范围内
- LangGraph 框架的通用教程（状态图基础、ToolNode API 等通用知识请参阅 LangGraph 官方文档）
- 各 Analyst 内部 prompt 设计（属于 module-agents 的范畴）
- 数据层实现（属于 module-dataflows 的范畴）

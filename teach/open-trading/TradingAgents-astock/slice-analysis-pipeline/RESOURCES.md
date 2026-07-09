# 分析决策链路 资源

## 知识

### 一级源文件（本文分析的 8 个核心文件）

| 文件 | 用途 | 关键度 |
|------|------|--------|
| `tradingagents/graph/trading_graph.py` | 主入口类 `TradingAgentsGraph`——生命周期、双 LLM、checkpoint | 🔴 核心 |
| `tradingagents/graph/propagation.py` | `Propagator`——初始状态构建（7 个报告域 + 2 个辩论状态） | 🔴 核心 |
| `tradingagents/graph/setup.py` | `GraphSetup.setup_graph()`——LangGraph 节点/边拓扑定义 | 🔴 核心 |
| `tradingagents/graph/conditional_logic.py` | `ConditionalLogic`——工具循环路由 + 辩论轮次控制 | 🔴 核心 |
| `tradingagents/graph/signal_processing.py` | `SignalProcessor`——从 PM 决策提取 5 档评级 | 🟡 辅助 |
| `tradingagents/graph/reflection.py` | `Reflector`——延迟反思（CSI 300 基准比较） | 🟡 辅助 |
| `tradingagents/agents/quality_gate.py` | 数据质量门控——硬检查 + LLM 复审两道关卡 | 🔴 核心 |
| `tradingagents/agents/schemas.py` | 结构化输出 Schema——ResearchPlan / TraderProposal / PortfolioDecision | 🔴 核心 |

### 二级源文件（补充理解用）

- `tradingagents/agents/utils/rating.py` — `parse_rating()` 5 档评级解析器
- `tradingagents/agents/utils/agent_states.py` — `AgentState` / `InvestDebateState` / `RiskDebateState` 类型定义
- `tradingagents/graph/checkpointer.py` — SQLite 断点续跑机制
- `tradingagents/agents/` — 各 Analyst 的 `create_*` 工厂函数

### 前置课程（交叉引用）

- [L0 项目全景图](../00-overview/lessons/0001-project-map.html) — 整体架构与 7 Analyst 角色一览
- [L1 Graph 模块总览](../module-graph/lessons/0001-graph-module-tour.html) — 6 个 graph/ 文件的分工
- [L1 Agents 模块总览](../module-agents/lessons/0001-agents-module-tour.html) — 7 Analyst + 辩论角色定义
- [L1 Dataflows 模块总览](../module-dataflows/lessons/0001-dataflows-module-tour.html) — 数据获取层架构

## 智慧（社区）

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) — 上游原版框架（美股）
- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/) — StateGraph / conditional edges / checkpointing

## 空白

- 暂无第三方对 TradingAgents 决策链路的深度分析文章或博客
- 上游开源社区未提供系统性的代码走读文档

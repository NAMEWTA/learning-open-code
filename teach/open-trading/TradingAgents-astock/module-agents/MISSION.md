# 使命：Agent 系统模块——7 分析师 + 辩论 + 风控 + 决策

## 为什么
理解 TradingAgents-Astock 的核心——多 Agent 协作投研框架的内部结构。掌握 17 个 Agent 节点的职责划分、工厂模式创建机制、及从研报生成到最终决策的完整角色链路，为后续自定义 Agent 或接入新数据源打下基础。

## 成功的样子
- 能默画出 agents 模块的 5 层架构（analysts / researchers / risk_mgmt / managers / trader）及每层包含的角色
- 能解释每个 Agent 的工厂函数签名（`create_xxx(llm) -> node_function`）及为什么要这样设计
- 能说出 3 个结构化输出 Schema（ResearchPlan / TraderProposal / PortfolioDecision）各自属于哪个 Agent 及其字段含义

## 约束条件
- 具备 Python 基础，了解 LangChain/LangGraph 基本概念
- 已阅读 L0 项目总览，知道项目整体架构

## 不在范围内
- LangGraph StateGraph 的节点连接与路由逻辑（属于 module-graph）
- LLM 供应商选择与适配（属于 module-llm-clients）
- 单个 Agent 的内部 prompt 工程细节（属于 L3 微观分析）

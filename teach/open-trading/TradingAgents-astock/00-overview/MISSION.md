# 使命：TradingAgents-Astock 项目总览

## 为什么
掌握一个生产级多 Agent 投研框架的完整架构——从数据采集、7 角色分析师研报生成、多空辩论到最终投资决策的全链路。学完后能够独立部署、配置、调试 TradingAgents-Astock，理解每个模块的设计意图，为后续深入分析各层源码奠定全局认知基础。

## 成功的样子
- 能够画出 TradingAgents-Astock 的完整数据流架构图（数据层 → 分析师 → 辩论 → 决策），并向他人清晰讲解
- 能够根据需求选择 LLM 供应商并正确配置 `config` 字典，成功运行一次完整的股票分析
- 能够说出 7 个 Analyst 角色各自的职责、使用的数据工具、以及为什么 A 股需要新增 3 个特化角色
- 能够定位任意一个功能（数据获取、Agent 逻辑、LLM 调用、Web UI）在源码树中的位置

## 约束条件
- 具备 Python 编程基础，了解 AI Agent 和 LLM 的基本概念
- 学习环境需能访问 GitHub 和至少一个 LLM API（MiniMax / DeepSeek / 通义千问等）
- 每次学习会话约 15-30 分钟，采用短课模式逐步推进

## 不在范围内
- 具体的量化交易策略设计与回测（属于策略分析课程）
- 前端 Streamlit UI 的组件级实现细节（属于 UI 专题课程）
- 单个 Analyst Agent 的 prompt 工程与调优（属于 Agent 专题课程）
- Kubernetes / Docker Swarm 等容器编排部署（属于运维专题课程）

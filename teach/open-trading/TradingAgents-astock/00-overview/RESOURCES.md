# TradingAgents-Astock 项目总览 资源

## 知识

- [README.md](https://github.com/simonlin1212/tradingagents-astock/blob/main/README.md) — 项目官方说明文档，涵盖架构概览、7 Analyst 角色说明、数据源、快速开始、配置参考和常见问题排错。适用于：任何需要了解项目全貌、首次运行配置、功能特性速查的场景。
- [CLAUDE.md](https://github.com/simonlin1212/tradingagents-astock/blob/main/CLAUDE.md) — AI 编码 Agent 协作指南，包含架构决策记录、数据层说明、已知问题与注意事项、开发规范。适用于：理解项目设计约束、数据源演进历史、开发约定和待处理 PR 的背景。
- [pyproject.toml](https://github.com/simonlin1212/tradingagents-astock/blob/main/pyproject.toml) — Python 包定义文件，包含依赖清单、入口点注册、可选依赖分组。适用于：了解项目的第三方依赖栈（LangChain/LangGraph/Pandas/mootdx/Streamlit 等）和 CLI 入口点映射。
- [论文: TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138) — 原版 TradingAgents 的学术论文（arXiv:2412.20138），阐述了多 Agent 辩论架构的理论基础、实验设计和性能评估。适用于：理解原版框架的学术背景、辩论机制设计原理、与基线方法的对比。
- [CHANGES_FROM_UPSTREAM.md](https://github.com/simonlin1212/tradingagents-astock/blob/main/CHANGES_FROM_UPSTREAM.md) — 与上游 TauricResearch/TradingAgents 的完整改动记录，按周组织，包含新增文件、修改文件、数据源架构、踩坑记录。适用于：理解本 Fork 与上游的差异、A 股特化改造的演进过程。
- [CHANGELOG.md](https://github.com/simonlin1212/tradingagents-astock/blob/main/CHANGELOG.md) — 按版本组织的变更历史，遵循 Keep a Changelog 格式。适用于：追踪各版本的 bug 修复、社区 PR 合并、新增功能的具体时间线。

## 智慧（社区）

- [GitHub Issues](https://github.com/simonlin1212/tradingagents-astock/issues) — 项目官方 Issue 跟踪，包含用户反馈、bug 报告、功能需求。适用于：了解常见问题、社区使用场景、参与讨论。
- [上游 TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) — 原版框架仓库（65K+ Stars），包含更广泛的社区讨论和 Issue 归档。适用于：对比原版与 Fork 的设计差异、查阅原版框架的社区经验。

## 空白

- 暂无针对"多 Agent 投研框架"的系统性中文教程或书籍——本项目本身即是填补此空白的产物
- 无针对 A 股市场的 AI Agent 投研最佳实践社区或论坛——目前主要依赖项目 Issue 区交流
- LangGraph 官方文档中对"金融 Agent 工作流"的案例覆盖较少——需结合本项目源码自行理解

# 使命：CLI 命令行界面模块

## 为什么
理解 TradingAgents-Astock 的 CLI 模块如何通过 Typer + Rich + Questionary 构建一个完整的交互式命令行分析工具——从用户引导式问答（ticker/日期/分析师/LLM 提供商/思考模式 8 步交互）到 LangGraph 工作流的实时流式展示，再到最终报告的磁盘保存与终端渲染。掌握这套 CLI 架构后，能够在自己的 Python 项目中复刻类似的交互式 CLI 框架。

## 成功的样子
- 能画出 CLI 模块在项目整体架构中的位置（入口层，调用 graph 层）
- 能说出 `cli/main.py` 的 8 步交互式引导流程（ticker、date、language、analysts、research_depth、llm_provider、shallow/deep thinker、provider-specific config）
- 能解释 Typer app 的命令注册方式（`analyze` 命令 + checkpoint 选项）
- 能解释 `save_report_to_disk` 的 5 级子目录报告保存结构
- 能追踪一条完整的 CLI 交互链路：用户输入 → config 组装 → TradingAgentsGraph 初始化 → stream 分析 → 报告保存/展示

## 约束条件
- 具备 Python 基础，了解命令行工具的基本用法
- 学习时间：单节课 15 分钟内完成

## 不在范围内
- Agent 角色的 prompt 设计与辩论逻辑（见 module-agents）
- LangGraph 工作流图的节点编排与条件路由（见 module-graph）
- 数据获取层的 vendor 路由与数据源（见 module-dataflows）
- LLM 客户端工厂与 provider 路由（见 module-llm-clients）

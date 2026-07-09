# 使命：CLI 命令执行链路垂直切片

## 为什么
理解 TradingAgents-Astock 从终端命令行输入到完整分析报告的全链路执行过程，掌握 CLI 层各模块的协作关系，为后续自定义 CLI 行为（如添加新命令、修改交互流程、集成外部工具）打下基础。

## 成功的样子
- 能画出 CLI 命令执行的 6 阶段链路图，标注每阶段的关键函数和所属文件
- 能独立追踪从 `tradingagents analyze` 到 `complete_report.md` 写入磁盘的完整调用栈
- 能说出 `get_user_selections()` → `run_analysis()` → `graph.stream()` → `save_report_to_disk()` 之间的数据流转方式

## 约束条件
- 已学完 L0 项目全景和 L1 CLI 模块总览，具备 CLI 模块文件结构和 8 步交互流程的前置知识
- 以代码阅读和链路追踪为主，不涉及实际运行 CLI
- 每节课程 15 分钟内可完成

## 不在范围内
- TradingAgentsGraph 内部节点编排和 Agent 辩论逻辑（属于 L1 module-graph 和 L2 slice-analysis-pipeline 的范围）
- LLM Provider 的 API 调用细节（属于 L1 module-llm-clients 的范围）
- Streamlit Web UI 的数据流（属于 L2 slice-web-ui-flow 的范围）

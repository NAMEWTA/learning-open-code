# 使命：Streamlit Web UI 模块

## 为什么
理解 TradingAgents-Astock 的 Web 前端是如何将多 Agent 分析流水线包装成交互式 UI 的——掌握 Streamlit 状态管理、后台线程模型、以及如何将 12 阶段 pipeline 进度实时推送到浏览器，为进一步定制或集成到自己项目建立前端认知基础。

## 成功的样子
- 能画出 Web 模块的 5 个状态机全貌和组件三层架构
- 能说清楚 runner 后台线程如何通过 ProgressTracker 与 Streamlit UI 通信
- 能看懂 Thread + Event + Lock 的暂停/恢复/停止控制逻辑
- 知道历史记录如何持久化和恢复未完成任务

## 约束条件
- 具备 Python 基础，了解 Streamlit 基本概念（session_state、rerun）
- 15 分钟内可完成的短课

## 不在范围内
- Streamlit 框架本身的深入教程
- LangGraph 节点内部实现细节（见 module-graph）
- Agent 分析逻辑（见 module-agents）

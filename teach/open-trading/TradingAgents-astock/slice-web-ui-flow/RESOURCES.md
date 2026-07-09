# Web UI 交互全链路 资源

## 知识

- [Streamlit Session State API](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state) — session_state 读写与跨 rerun 持久化机制。适用于：理解 app.py 中 tracker 对象的生命周期。
- [Streamlit st.rerun() 文档](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun) — 强制重新执行脚本的语义与最佳实践。适用于：理解进度轮询循环为何使用 sleep + rerun。
- [Python threading — Event 对象](https://docs.python.org/3/library/threading.html#event-objects) — Event.set()/clear()/wait() 的阻塞-唤醒语义。适用于：理解 ProgressTracker 的暂停/恢复闸门。
- [LangGraph Streaming](https://langchain-ai.github.io/langgraph/how-tos/streaming/) — graph.stream() 返回的 chunk 结构与迭代语义。适用于：理解 _detect_completed_stages() 如何从 chunk 中提取阶段完成信号。
- [fpdf2 文档 — Unicode 与字体](https://pyfpdf.github.io/fpdf2/Unicode.html) — CJK 字体嵌入与 TTC collection font number 概念。适用于：理解 pdf_export.py 的多平台字体探测逻辑。
- [TradingAgents-Astock Web 模块源码](https://github.com/simonlin1212/TradingAgents-astock/tree/main/web) — 本次分析的全部源码入口。

## 智慧（社区）

- [Streamlit 论坛 — Session State](https://discuss.streamlit.io/c/using-streamlit/session-state/14) — 状态管理实战讨论。适用于：多页面 / 多用户场景下的 session_state 边界问题。
- [TradingAgents-Astock Issues](https://github.com/simonlin1212/TradingAgents-astock/issues) — Web UI 相关 issue（如 #36 sidebar 折叠按钮问题、#55 股票名展示归一化、#66 .env 加载顺序）。

## 空白

- Streamlit 多用户并发场景下的后台线程隔离方案（当前为单用户本地模式）
- fpdf2 在 Windows 环境下的中文字体自动探测成功率数据（社区反馈较少）

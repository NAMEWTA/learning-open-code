# CLI 命令执行链路 资源

## 知识

- [Typer 官方文档 - Commands](https://typer.tiangolo.com/tutorial/commands/)
  Typer 命令注册、参数选项（`typer.Option`）、shell 自动补全机制。适用于：理解 `analyze` 命令的 `--checkpoint`/`--clear-checkpoints` 选项定义。
- [Rich 官方文档 - Live Display](https://rich.readthedocs.io/en/stable/live.html)
  Rich Live 组件的实时刷新机制（4 fps）、Layout 分屏布局、Panel/Table/Markdown 渲染。适用于：理解 `update_display()` 和 `create_layout()` 的实现。
- [LangGraph Streaming](https://langchain-ai.github.io/langgraph/how-tos/streaming/)
  LangGraph `graph.stream()` 的事件类型、chunk 结构与消息去重。适用于：理解流式循环中 `chunk["messages"]` 的分类处理。
- [Questionary 官方文档](https://questionary.readthedocs.io/)
  Questionary 的 select/checkbox/text 交互式提示组件。适用于：理解 8 步交互引导的 UI 层实现。
- [TradingAgents-Astock CLAUDE.md](https://github.com/simonlin1212/TradingAgents-astock/blob/main/CLAUDE.md)
  项目维护者编写的架构文档，包含数据层、安全边界（`safe_ticker_component`）和已知问题说明。

## 智慧（社区）

- [TradingAgents-Astock Issues](https://github.com/simonlin1212/TradingAgents-astock/issues)
  项目 Issue 跟踪。重点关注 #51（ticker 路径穿越防护）——展示了 CLI 输入校验如何演化为安全边界。

## 空白

- Typer + LangGraph 流式输出的集成模式暂无社区最佳实践总结
- Rich Live 组件在长时间流式分析场景下的内存和性能特征暂无公开资料
- `MessageBuffer` 状态管理模式（消息去重+Agent 状态推进+报告段落累积）的通用化提取暂无讨论

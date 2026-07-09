# CLI 命令行界面模块 资源

## 知识

- [Typer 官方文档](https://typer.tiangolo.com/)
  FastAPI 团队出品的 CLI 框架，基于 Click + type hints。适用于：理解 CLI 命令注册、参数验证、shell 自动补全的底层机制。
- [Rich 官方文档](https://rich.readthedocs.io/)
  终端美化库，提供 Panel、Table、Markdown、Layout、Live 等组件。适用于：理解 CLI 模块中的实时流式展示实现。
- [LangGraph Streaming 文档](https://langchain-ai.github.io/langgraph/how-tos/)
  LangGraph 的 stream 模式与事件类型说明。适用于：理解 `graph.stream()` 返回的 chunk 结构。
- [TradingAgents-Astock CLAUDE.md](https://github.com/simonlin1212/TradingAgents-astock/blob/main/CLAUDE.md)
  项目维护者编写的架构文档。适用于：理解数据层、Agent 层与 CLI 的调用关系。

## 智慧（社区）

- [TradingAgents-Astock Issues](https://github.com/simonlin1212/TradingAgents-astock/issues)
  项目 Issue 跟踪。CLI 相关的 #51（ticker 路径安全）值得关注——展示了 CLI 模块的输入校验如何演化为安全边界。

## 空白

- Questionary 库文档较少，其 checkbox/select/text 交互模式的最佳实践暂无系统整理
- Rich Live 组件在高刷新率下的性能调优经验暂无公开资料
- Typer + LangGraph 流式输出的集成模式暂无社区最佳实践总结

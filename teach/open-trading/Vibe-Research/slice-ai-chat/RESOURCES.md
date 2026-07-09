# AI 对话全链路 资源

## 知识

- [OpenAI Function Calling 官方文档](https://platform.openai.com/docs/guides/function-calling)
  理解 `tools` / `tool_choice` 参数与 `tool_calls` 响应的标准格式。适用于：讲解 chat.py 中 function-calling 循环时的协议依据。
- [Server-Sent Events (SSE)](https://html.spec.whatwg.org/multipage/server-sent-events.html)
  理解前端如何消费流式响应（`data:` 前缀行协议）。适用于：讲解 llm.ts 中 NDJSON 逐行解析时，与 SSE 的异同。
- [MCP 协议规范 (Model Context Protocol)](https://spec.modelcontextprotocol.io/)
  理解 `initialize` → `tools/list` → `tools/call` 的 handshake 与 JSON-RPC 2.0 消息格式。适用于：讲解 mcp_server.py 的标准协议设计。
- [Vibe-Research README](https://github.com/zhanglingzhe0825/Vibe-Research)
  项目整体说明，包含 AI 接入的使用指南和三种模式对比。适用于：快速了解前端用户如何配置 AI。

## 智慧（社区）

- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)
  讨论本地部署模型、CLI 工具和 OpenAI 兼容网关的社区。适用于：了解各 CLI 工具的版本变化、订阅策略和本机调优经验。
- [Claude Code Discord](https://discord.gg/anthropic)
  Anthropic 官方 Discord，Claude Code 用户交流。适用于：了解 Claude Code MCP 集成的最佳实践和常见问题。

## 空白

- 暂无成熟的"四种 CLI 投递方式对比"的外部文章或评测，教学材料主要依据 cli_runtime.py 源码注释和实际行为推断。
- 豆包/硅基流动等国产模型的 function-calling 兼容性差异没有官方对比文档，需通过实际测试验证。

# SDK startThread/run 链路 资源

## 知识

- [codex-rs app-server README](https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md) — app-server JSON-RPC 协议、Thread/Turn/Item 原语、生命周期与事件通知的权威文档
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — app-server 协议设计的参照标准，理解 JSON-RPC 双向通信的基础
- [Node.js child_process.spawn 文档](https://nodejs.org/api/child_process.html) — TypeScript SDK 通过 spawn + readline 与 Rust 二进制通信的底层机制

## 智慧（社区）

- [OpenAI Codex GitHub Issues](https://github.com/openai/codex/issues) — 报告 SDK 集成问题、查阅已知 Bug、寻找社区解决方案
- [OpenAI Developer Forum](https://community.openai.com/) — Codex SDK 使用经验交流和最佳实践讨论

## 空白

- Python SDK 官方文档目前较为简略，thread/run 的行为契约主要通过源码和测试用例推断
- TypeScript SDK 无独立文档站点，公开 API 的使用说明主要来自源码注释和 app-server README
- 两个 SDK 的连接断开重连机制目前无公开文档描述，实现细节需要通过 exec.ts 和 client.py 的异常处理代码反向推导

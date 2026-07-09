# App-server Thread/Turn JSON-RPC 链路 资源

## 知识

- [codex-rs/app-server/README.md](../../../../open-ai-agent/codex/codex-rs/app-server/README.md) — app-server 官方说明，Thread/Turn/Item 三原语定义
- [codex-rs/app-server/src/message_processor.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/message_processor.rs) — JSON-RPC 反序列化、初始化门禁、请求分发（核心路由层）
- [codex-rs/app-server/src/request_processors/thread_processor.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/request_processors/thread_processor.rs) — thread/start、thread/resume、thread/fork 等生命周期处理（4573 行）
- [codex-rs/app-server/src/request_processors/thread_lifecycle.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/request_processors/thread_lifecycle.rs) — 线程监听器生命周期、卸载、事件派发
- [codex-rs/app-server/src/request_processors/turn_processor.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/request_processors/turn_processor.rs) — turn/start、turn/steer、turn/interrupt、review 处理
- [codex-rs/app-server-protocol/src/protocol/v2/thread.rs](../../../../open-ai-agent/codex/codex-rs/app-server-protocol/src/protocol/v2/thread.rs) — v2 ThreadStartParams 类型定义（thread/start 参数）
- [codex-rs/app-server-protocol/src/protocol/v2/turn.rs](../../../../open-ai-agent/codex/codex-rs/app-server-protocol/src/protocol/v2/turn.rs) — v2 TurnStartParams 类型定义（turn/start 参数）
- [codex-rs/app-server-protocol/src/protocol/common.rs](../../../../open-ai-agent/codex/codex-rs/app-server-protocol/src/protocol/common.rs) — ClientRequest 枚举与共享协议类型（Initialize 等变体）
- [codex-rs/app-server-protocol/src/protocol/v1.rs](../../../../open-ai-agent/codex/codex-rs/app-server-protocol/src/protocol/v1.rs) — v1 InitializeParams / InitializeResponse 等历史类型
- [codex-rs/app-server-protocol/src/rpc.rs](../../../../open-ai-agent/codex/codex-rs/app-server-protocol/src/rpc.rs) — JSON-RPC 2.0 消息类型（Request、Notification、Response、Error）
- [codex-rs/core/src/codex_thread.rs](../../../../open-ai-agent/codex/codex-rs/core/src/codex_thread.rs) — 底层 CodexThread 抽象（submit、submit_user_input、steer_input 等）
- [codex-rs/app-server/src/transport.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/transport.rs) — 传输层抽象与连接状态管理
- [JSON-RPC 2.0 规范](https://www.jsonrpc.org/specification) — 协议基础，理解 Request/Notification/Response/Error 的语义

## 智慧（社区）

- [Codex CLI GitHub Discussions](https://github.com/openai/codex/discussions) — 官方讨论区，适合提出协议集成问题
- [OpenAI Developer Forum](https://community.openai.com/) — API 与 SDK 集成相关讨论

## 空白

- Codex 目前没有公开的协议规范文档（类似 LSP specification），wire 格式仅能从 Rust 源码的类型定义和 serde 标注反推
- 缺少官方 SDK 集成指南或 app-server 协议最佳实践文档
- 社区中暂未发现独立的 app-server 协议分析文章或第三方客户端实现参考

# Core Thread/Turn 与模型上下文资源

## 知识

- [本地源码：`codex-rs/core/Cargo.toml`](../../../../open-ai-agent/codex/codex-rs/core/Cargo.toml)
  说明 `codex-core` 的 crate 依赖边界。适用于判断哪些能力已经拆到 protocol、tools、mcp、sandboxing、skills、config、model-provider 等 crate。
- [本地源码：`codex-rs/core/src/lib.rs`](../../../../open-ai-agent/codex/codex-rs/core/src/lib.rs)
  `codex-core` 的公开导出面。适用于梳理哪些类型对 TUI、exec、app-server 和测试支持是外部可见的。
- [本地源码：`codex-rs/core/src/thread_manager.rs`](../../../../open-ai-agent/codex/codex-rs/core/src/thread_manager.rs)
  线程创建、恢复、fork、subagent 与共享服务装配入口。适用于学习 `ThreadManager` 与 `NewThread`。
- [本地源码：`codex-rs/core/src/codex_thread.rs`](../../../../open-ai-agent/codex/codex-rs/core/src/codex_thread.rs)
  thread 对象的提交、事件读取、配置快照、注入、后台终端和 MCP runtime 入口。适用于理解 `CodexThread` 的调用面。
- [本地源码：`codex-rs/core/src/session/`](../../../../open-ai-agent/codex/codex-rs/core/src/session/)
  session 状态、turn 构造、context window、MCP runtime、multi-agent、input queue 和持久化重建。适用于后续 L2 垂直切片。
- [本地源码：`codex-rs/core/src/tasks/`](../../../../open-ai-agent/codex/codex-rs/core/src/tasks/)
  `RegularTask`、`ReviewTask`、`CompactTask`、`UserShellCommandTask` 的统一任务接口。适用于区分普通 turn、评审、压缩和用户 shell。
- [本地源码：`codex-rs/core/src/context/`](../../../../open-ai-agent/codex/codex-rs/core/src/context/)
  model-visible context fragment 定义。适用于检查 AGENTS.md 中“所有上下文片段必须有边界和 hard cap”的规则。
- [本地源码：`codex-rs/core/src/client.rs`](../../../../open-ai-agent/codex/codex-rs/core/src/client.rs)
  `ModelClient` 与 `ModelClientSession`。适用于理解 session-scoped provider/auth 状态和 turn-scoped streaming 请求。
- [本地源码：`codex-rs/core/src/event_mapping.rs`](../../../../open-ai-agent/codex/codex-rs/core/src/event_mapping.rs)
  把 Responses API 的 `ResponseItem` 映射成 `TurnItem`。适用于后续 UI/app-server 事件解释。
- [本地源码：`codex-rs/protocol/src/`](../../../../open-ai-agent/codex/codex-rs/protocol/src/)
  跨模块协议类型，包含 `Op`、`Event`、`EventMsg`、`SessionConfiguredEvent`、权限、模型和用户输入类型。
- [本地源码：`codex-rs/core-api/src/lib.rs`](../../../../open-ai-agent/codex/codex-rs/core-api/src/lib.rs)
  面向 thread management 的 public facade。适用于富客户端、SDK、app-server 侧阅读公共 API 边界。
- [源项目规范：`open-ai-agent/codex/AGENTS.md`](../../../../open-ai-agent/codex/AGENTS.md)
  说明 Rust crate 边界、`codex-core` 膨胀风险、model-visible context 规则和测试建议。适用于判断设计约束。

## 智慧（社区）

- [OpenAI Codex GitHub Issues](https://github.com/openai/codex/issues)
  适用于把源码阅读结论放回真实 bug、API 变更和架构讨论中检验。
- [OpenAI Codex GitHub Pull Requests](https://github.com/openai/codex/pulls)
  适用于观察维护者如何约束 `codex-core` 边界、测试策略和 app-server/protocol 兼容性。

## 空白

- 当前本地仓库没有独立的 `codex-core` 架构白皮书；本主题以源码、AGENTS.md 和后续垂直切片课程作为主要事实来源。
- 尚未整理一份公开的核心维护者访谈或设计历史材料；若后续需要解释设计取舍，应优先从 PR 讨论和提交历史补充。

# 交互 TUI 中一次用户 turn 的执行链路 — 资源

## 知识

- [codex-rs/cli/src/main.rs](../../../open-ai-agent/codex/codex-rs/cli/src/main.rs)
  TUI 模式的入口点：`run_interactive_tui()` 调用 `codex_tui::run_main()`。适用于理解 CLI 参数解析、TERM 检查和 TUI 启动逻辑。

- [codex-rs/tui/src/lib.rs](../../../open-ai-agent/codex/codex-rs/tui/src/lib.rs)
  TUI 库的总入口 `pub async fn run_main(...)`，包含 config 加载、app-server 启动/连接、onboarding 流程、resume/fork 选择和应用启动的完整编排。

- [codex-rs/tui/src/app.rs](../../../open-ai-agent/codex/codex-rs/tui/src/app.rs)
  TUI App 的主事件循环 `App::run()`，用 `select!` 合并 app_event_rx、active_thread_rx、tui_events 和 app_server_events 四个事件流。

- [codex-rs/tui/src/chatwidget.rs](../../../open-ai-agent/codex/codex-rs/tui/src/chatwidget.rs)
  TUI 聊天组件 ChatWidget，处理用户输入提交 (`submit_op`)、app-server 通知转译 (`ServerNotification` → UI 状态) 和渲染协调。

- [codex-rs/core/src/codex_thread.rs](../../../open-ai-agent/codex/codex-rs/core/src/codex_thread.rs)
  CodexThread 是 TUI 与 core 之间的线程级接口。`submit_user_input_with_client_user_message_id()` 将用户输入注入 session 队列；`steer_input()` 支持运行中追加输入。

- [codex-rs/core/src/session/turn.rs](../../../open-ai-agent/codex/codex-rs/core/src/session/turn.rs)
  `run_turn()` 函数是单个 turn 的核心编排循环：pre-sampling compact → 构建 step context → 模型采样 → 工具执行 → 事件产出，直到模型返回最终回答或 turn 被中断。

- [codex-rs/core/src/client.rs](../../../open-ai-agent/codex/codex-rs/core/src/client.rs)
  `ModelClient` 是 session-scoped 的模型 API 客户端，管理 auth/provider/WebSocket 连接。`ModelClientSession` 是 turn-scoped 的流式会话，缓存 WebSocket 连接和 sticky routing token。

- [codex-rs/app-server-protocol/](../../../open-ai-agent/codex/codex-rs/app-server-protocol/)
  TUI 与 app-server 之间的 JSON-RPC 协议定义：`ServerNotification`、`ServerRequest`、`Turn`、`TurnStatus` 等类型。适用于理解 TUI 如何监听并消费 app-server 产生的事件。

## 智慧（社区）

- [Codex CLI 官方开发者文档](https://developers.openai.com/codex/cli/)
  OpenAI 官方 Codex CLI 文档，包含安装、配置、命令参考和架构概览。

- [ratatui 官方文档](https://ratatui.rs/)
  Codex TUI 使用的终端 UI 框架。适用于理解底层渲染、布局和事件处理机制。

## 空白

- 本主题追踪的链路涉及 app-server、core 和 TUI 三层，但目前没有独立的外部社区讨论 Codex 内部架构的白皮书或技术博客。学习和理解主要依赖源码阅读。
- SSE (Server-Sent Events) 流式协议在 `codex-api` crate 中实现，课程仅关注其在 client.rs 中的使用方式，不深入 transport 层细节。

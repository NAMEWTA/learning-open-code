# TUI 交互式终端界面资源

## 知识

- [源码：`codex-rs/tui/Cargo.toml`](../../../../open-ai-agent/codex/codex-rs/tui/Cargo.toml)
  `codex-tui` crate 的二进制、库目标与依赖边界。适用于判断 TUI 依赖哪些 core、protocol、app-server、terminal 与渲染库。
- [源码：`codex-rs/tui/src/lib.rs`](../../../../open-ai-agent/codex/codex-rs/tui/src/lib.rs)
  TUI 运行入口，包含 `run_main`、配置加载、认证、app-server 选择、终端恢复与 `App::run` 组装。
- [源码：`codex-rs/tui/src/app.rs`](../../../../open-ai-agent/codex/codex-rs/tui/src/app.rs)
  顶层应用状态与事件循环，适用于学习 TUI 如何同时处理内部事件、终端事件、活跃 thread 事件和 app-server 事件。
- [源码：`codex-rs/tui/src/chatwidget.rs`](../../../../open-ai-agent/codex/codex-rs/tui/src/chatwidget.rs)
  聊天主体 UI 状态，适用于学习 transcript、流式输出、状态同步与向 core 提交 `AppCommand` 的边界。
- [源码：`codex-rs/tui/src/bottom_pane/`](../../../../open-ai-agent/codex/codex-rs/tui/src/bottom_pane/)
  输入区、composer、弹层、footer 与审批交互。适用于学习按键路由、提交结果和任务运行提示。
- [源码：`codex-rs/tui/src/status_indicator_widget.rs`](../../../../open-ai-agent/codex/codex-rs/tui/src/status_indicator_widget.rs)
  运行中状态组件，适用于学习 elapsed、interrupt hint 与状态明细如何显示。
- [源码：`codex-rs/tui/styles.md`](../../../../open-ai-agent/codex/codex-rs/tui/styles.md)
  终端样式约定，适用于统一理解 TUI 中 header、primary、secondary 和 ANSI 颜色选择。
- [ratatui 官方文档](https://ratatui.rs/)
  Rust 终端 UI 框架资料。适用于补充理解 widget、layout、render 等基础概念。
- [crossterm 官方仓库](https://github.com/crossterm-rs/crossterm)
  跨平台终端事件与控制库。适用于理解 TUI 如何接收键盘、粘贴、resize 等终端事件。

## 智慧（社区）

- [OpenAI Codex GitHub Issues](https://github.com/openai/codex/issues)
  真实用户报告 TUI、终端兼容、认证和交互问题的场所。适用于验证架构理解是否能解释实际故障。
- [ratatui Discord 与社区入口](https://ratatui.rs/community/)
  ratatui 使用者交流终端渲染、布局和测试经验的社区。适用于排查 TUI 渲染设计问题。

## 空白

- 当前没有单独面向 `codex-tui` 内部架构的官方长文档；本主题主要依赖源码、测试和相邻库文档。

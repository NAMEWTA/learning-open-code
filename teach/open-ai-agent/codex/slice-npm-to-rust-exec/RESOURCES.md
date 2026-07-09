# 从 npm 包装到 Rust exec 的启动链路 — 资源

## 知识

- [codex-cli/package.json](../../../../open-ai-agent/codex/codex-cli/package.json) — npm 包元数据，`bin` 字段将 `codex` 命令映射到 `bin/codex.js`。
- [codex-cli/bin/codex.js](../../../../open-ai-agent/codex/codex-cli/bin/codex.js) — Node.js 入口脚本，平台 target triple 检测、platform package 查找、spawn 与信号转发。
- [codex-rs/cli/src/main.rs](../../../../open-ai-agent/codex/codex-rs/cli/src/main.rs) — Rust CLI 主入口，`MultitoolCli` 定义、`cli_main` 子命令分发与 `Subcommand::Exec` 分支。
- [codex-rs/exec/src/main.rs](../../../../open-ai-agent/codex/codex-rs/exec/src/main.rs) — `codex-exec` 独立二进制入口，`arg0_dispatch_or_else` 与 `TopCli` 解析。
- [codex-rs/exec/src/cli.rs](../../../../open-ai-agent/codex/codex-rs/exec/src/cli.rs) — `codex exec` 子命令的 CLI 参数定义，`Cli` 结构体、`Command` 枚举与共享选项。

## 智慧（社区）

- [OpenAI Codex GitHub issues](https://github.com/openai/codex/issues) — 搜索 "codex.js"、"spawn"、"binary not found" 等关键词，观察真实用户的启动问题。
- [OpenAI Codex CLI 文档](https://developers.openai.com/codex/cli) — 官方安装与使用文档，理解 npm/Homebrew/脚本安装路径的差异。

## 空白

- 暂未收录外部长文或书籍；本主题的事实密度主要来自当前源码。
- npm optional package 的跨平台构建与发布（`.github/workflows/`）不在本切片范围内，属于 L1-module-build-release 的范畴。
- `arg0_dispatch_or_else` 的内部实现（codex-arg0 crate）细节未展开，属于 L3 深度解析候选。

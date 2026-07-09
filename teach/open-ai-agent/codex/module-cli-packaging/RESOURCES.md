# CLI 与 npm 包装层资源

## 知识

- [Codex README](../../../../open-ai-agent/codex/README.md) — 项目定位、安装方式和产品入口边界；适用于判断 CLI、IDE、desktop app、Codex Web 的职责边界。
- [codex-cli/package.json](../../../../open-ai-agent/codex/codex-cli/package.json) — `@openai/codex` npm 包的 `bin` 映射、包元数据和发布文件范围；适用于理解用户执行 `codex` 时首先落到哪里。
- [codex-cli/bin/codex.js](../../../../open-ai-agent/codex/codex-cli/bin/codex.js) — 平台 target triple 映射、optional package 查找、原生二进制 `spawn` 和信号转发；适用于排查安装后无法启动的问题。
- [codex-rs/cli/Cargo.toml](../../../../open-ai-agent/codex/codex-rs/cli/Cargo.toml) — `codex-cli` Rust crate 的二进制入口和关键 workspace 依赖；适用于识别 CLI 分发层连接的运行模块。
- [codex-rs/cli/src/main.rs](../../../../open-ai-agent/codex/codex-rs/cli/src/main.rs) — `MultitoolCli`、`Subcommand` 和 `cli_main` 分发主干；适用于判断每个子命令的落点。
- [codex-rs/cli/src/mcp_cmd.rs](../../../../open-ai-agent/codex/codex-rs/cli/src/mcp_cmd.rs) — `codex mcp` 的子命令结构和配置写入示例；适用于后续 MCP 管理垂直切片。
- [codex-rs/cli/src/plugin_cmd.rs](../../../../open-ai-agent/codex/codex-rs/cli/src/plugin_cmd.rs) — `codex plugin` 的 marketplace、安装、列表、删除入口；适用于后续扩展系统课程。
- [codex-rs/cli/src/remote_control_cmd.rs](../../../../open-ai-agent/codex/codex-rs/cli/src/remote_control_cmd.rs) — remote-control 如何启动或管理 app-server daemon；适用于 app-server 关联入口课程。
- [codex-rs/exec/src/cli.rs](../../../../open-ai-agent/codex/codex-rs/exec/src/cli.rs) — `codex exec` 非交互参数结构；适用于后续 npm 到 Rust exec 垂直切片。
- [codex-rs/exec/src/main.rs](../../../../open-ai-agent/codex/codex-rs/exec/src/main.rs) — `codex-exec` 独立入口与 `arg0` 分发；适用于比较主 CLI 和独立 exec 二进制。

## 智慧（社区）

- [OpenAI Codex GitHub issues](https://github.com/openai/codex/issues) — 用于观察真实用户遇到的安装、平台包、CLI 子命令和运行时问题。
- [OpenAI Codex GitHub pull requests](https://github.com/openai/codex/pulls) — 用于追踪 CLI 分发层、app-server、MCP、plugin 等边界近期如何演进。

## 空白

- 暂未收录外部长文或书籍；本模块的事实密度主要来自当前源码和官方仓库文档。
- release workflow 与 npm optional package 的构建产物关系尚未在本课展开，后续构建发布 L1 需要补充 `.github/workflows/` 与发布脚本资源。

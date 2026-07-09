# Codex 项目总览与学习地图资源

## 知识

- [源码：`open-ai-agent/codex/README.md`](../../../../open-ai-agent/codex/README.md)
  项目定位、安装方式，以及 Codex CLI、Codex IDE、Codex App、Codex Web 的边界说明。适用于所有入口级课程。
- [源码：`open-ai-agent/codex/AGENTS.md`](../../../../open-ai-agent/codex/AGENTS.md)
  Rust 开发规范、crate 边界、测试策略、app-server API 规则和评审重点。适用于理解架构决策与贡献约束。
- [源码：`open-ai-agent/codex/codex-rs/Cargo.toml`](../../../../open-ai-agent/codex/codex-rs/Cargo.toml)
  Rust workspace 成员与内部依赖声明。适用于划分 L1 模块组和定位 crate。
- [源码：`open-ai-agent/codex/codex-cli/bin/codex.js`](../../../../open-ai-agent/codex/codex-cli/bin/codex.js)
  npm 包如何选择平台原生二进制并转发参数。适用于理解 Node 包装层。
- [源码：`open-ai-agent/codex/codex-rs/cli/src/main.rs`](../../../../open-ai-agent/codex/codex-rs/cli/src/main.rs)
  Rust CLI 命令枚举和主入口。适用于追踪用户命令进入 TUI、exec、app-server、sandbox 等分支的第一站。
- [源码：`open-ai-agent/codex/codex-rs/app-server/README.md`](../../../../open-ai-agent/codex/codex-rs/app-server/README.md)
  app-server 的 JSON-RPC 协议、Thread/Turn/Item 模型、生命周期和 API 面。适用于 IDE、SDK、桌面集成学习。
- [源码：`open-ai-agent/codex/sdk/python/README.md`](../../../../open-ai-agent/codex/sdk/python/README.md)
  Python SDK 的线程、回合、认证和运行示例。适用于 SDK 集成路径。
- [源码：`open-ai-agent/codex/sdk/typescript/README.md`](../../../../open-ai-agent/codex/sdk/typescript/README.md)
  TypeScript SDK 如何包装 `codex` CLI 并通过 JSONL 事件交互。适用于 SDK 与 CLI 边界分析。
- [源码：`open-ai-agent/codex/BUILD.bazel`](../../../../open-ai-agent/codex/BUILD.bazel) 与 [`MODULE.bazel`](../../../../open-ai-agent/codex/MODULE.bazel)
  Bazel 平台、Rust toolchain、Cargo 导入和补丁入口。适用于构建与发布链路学习。
- [源码目录：`open-ai-agent/codex/.github/workflows/`](../../../../open-ai-agent/codex/.github/workflows/)
  Rust CI、Bazel、SDK、Python runtime、release 等自动化入口。适用于后续交付链路课程。

## 智慧（社区）

- [GitHub Issues：openai/codex](https://github.com/openai/codex/issues)
  适用于观察真实用户问题、兼容性边界、安装故障和功能讨论。
- [GitHub Pull Requests：openai/codex](https://github.com/openai/codex/pulls)
  适用于学习维护者如何拆分变更、补测试和守住 crate/API 边界。
- [OpenAI Codex 文档](https://developers.openai.com/codex)
  适用于把源码实现与官方用户文档对齐，尤其是配置、安全、CLI 功能和 skills。

## 空白

- 本地源码没有包含完整的官方线上文档正文，`docs/*.md` 多数是跳转入口；涉及最新用户文档时应优先核对官方文档站。
- 本主题暂不收录第三方博客或视频，避免 L0 地图被二手解读污染。

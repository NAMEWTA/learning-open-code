# 使命：从 npm 包装到 Rust exec 的启动链路

## 为什么
用户已完成 L1-module-cli-packaging 模块导览，理解了 codex CLI 的两段入口架构（npm 包装层 + Rust CLI 分发层）。现在需要沿"`codex exec`"这一条具体命令，从用户敲下回车开始，逐层追踪到 Rust exec 子进程启动的完整调用链。掌握这条垂直切片后，用户将能够自行追踪 codex 中任意一条子命令的启动路径。

## 成功的样子
- 能画出从 `package.json` bin 声明到 `codex_exec::run_main` 的完整时序图。
- 能解释 `codex.js` 的平台检测、二进制定位、spawn 和信号转发的每一步决策。
- 能说清 `arg0_dispatch_or_else` 的作用，以及 `codex-rs/cli` 和 `codex-rs/exec` 两个 main.rs 的关系。
- 能在 Rust 二进制缺失时，根据错误提示判断是哪个平台包未安装。

## 约束条件
- 本主题是 L2 垂直切片，单节 lesson 控制在 15 分钟内完成。
- 正文目标 800-1200 中文字，硬上限 1500 中文字。
- 最多 4 个主章节、3 个源码文件、3 个短代码片段（每个不超过 35 行）。
- 只写入 `teach/open-ai-agent/codex/slice-npm-to-rust-exec/`，不修改源项目。

## 不在范围内
- 不展开 `codex_exec::run_main` 内部的 agent 循环、模型调用、工具执行。
- 不讲 Bazel 构建、CI 发布、npm optional package 的打包过程。
- 不分析 TUI、app-server、MCP server 等其他子命令的启动路径。

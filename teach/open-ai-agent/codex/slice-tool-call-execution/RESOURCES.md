# 工具调用执行链路 资源

## 知识

- [Codex 源码：`codex-rs/tools/src/tool_executor.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/tools/src/tool_executor.rs)
  `ToolExecutor` trait 定义——所有工具运行时的共享契约。适用于：理解工具如何将模型可见 spec 与可执行 runtime 绑定。

- [Codex 源码：`codex-rs/core/src/tools/router.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/core/src/tools/router.rs)
  `ToolRouter` 将模型返回的 `ResponseItem::FunctionCall` 解析为内部 `ToolCall`，并路由到 `ToolRegistry` 执行。适用于：追踪从模型输出到工具调用的入口转换。

- [Codex 源码：`codex-rs/core/src/tools/registry.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/core/src/tools/registry.rs)
  `ToolRegistry` 是工具执行的中央调度器——查找工具、Pre/Post hook、telemetry、生命周期通知、输出序列化。适用于：理解一次工具调用的完整生命周期。

- [Codex 源码：`codex-rs/core/src/tools/orchestrator.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/core/src/tools/orchestrator.rs)
  `ToolOrchestrator` 负责审批决策→沙箱选择→执行尝试→沙箱降级重试。适用于：理解安全策略如何在执行前介入。

- [Codex 源码：`codex-rs/execpolicy/src/policy.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/execpolicy/src/policy.rs)
  执行策略引擎——按程序名匹配规则，决策 Allow/Prompt/Forbidden。适用于：理解命令白名单/黑名单的判断逻辑。

- [Codex 源码：`codex-rs/core/src/tools/handlers/shell.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/core/src/tools/handlers/shell.rs)
  Shell 命令 handler 实现，`run_exec_like` 是核心执行路径。适用于：追踪一次 bash 命令从 handler 到 exec-server 的完整调用链。

- [Codex 源码：`codex-rs/exec-server/src/client.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/exec-server/src/client.rs)
  Exec-server 客户端——通过 JSON-RPC 与沙箱进程通信，支持 exec、文件读写、进程信号等操作。适用于：理解沙箱内命令的实际执行机制。

## 智慧（社区）

- [Claude Code Discord](https://discord.gg/anthropic)
  官方 Discord 社区，Claude Code 用户和开发者讨论工具使用、自定义 hooks、权限策略等话题。适用于：向实际用户请教工具执行行为与最佳实践。

## 空白

- 缺少 exec-server 内部沙箱实现的详细文档（bwrap/landlock 在 Linux 上的具体行为）
- 缺少统一执行引擎（unified exec）与传统 shell command 后端的性能对比数据
- 缺少 execpolicy 规则文件（`.execpolicy`）的完整语法参考

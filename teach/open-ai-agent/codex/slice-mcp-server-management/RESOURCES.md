# MCP Server 管理链路 资源

## 知识

- [Codex 源码：`codex-rs/cli/src/mcp_cmd.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/cli/src/mcp_cmd.rs)
  CLI 端 `mcp add/login/list/remove/logout` 六个子命令的完整实现。适用于：理解用户侧 MCP 配置的入口操作和 OAuth 登录流程编排。

- [Codex 源码：`codex-rs/config/src/mcp_edit.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/config/src/mcp_edit.rs)
  `ConfigEditsBuilder` 和 `load_global_mcp_servers()`——config.toml 的读写与序列化。适用于：理解如何以最小 diff 方式编辑 TOML 中的 `[mcp_servers]` 段。

- [Codex 源码：`codex-rs/config/src/mcp_types.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/config/src/mcp_types.rs)
  `McpServerConfig`、`McpServerTransportConfig`、`RawMcpServerConfig` 类型定义。适用于：查看配置模型的全量字段、反序列化规则与 transport 互斥校验。

- [Codex 源码：`codex-rs/codex-mcp/src/connection_manager.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/codex-mcp/src/connection_manager.rs)
  `McpConnectionManager`——连接池、启动状态事件、工具聚合、资源列表、跨服务器 tool call 路由。适用于：理解运行时 MCP 服务器的生命周期管理和工具发现。

- [Codex 源码：`codex-rs/codex-mcp/src/rmcp_client.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/codex-mcp/src/rmcp_client.rs)
  `AsyncManagedClient` 和 `ManagedClientStartup`——异步客户端封装、启动重试、工具缓存。适用于：理解单个 MCP 服务器的启动状态机和 Codex Apps 专属的 reconnect 机制。

- [Codex 源码：`codex-rs/rmcp-client/src/rmcp_client.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/rmcp-client/src/rmcp_client.rs)
  `RmcpClient`——底层 MCP 协议客户端，支持 stdio / streamable_http / in_process 三种 transport，initialize 握手。适用于：理解 MCP 连接的底层建立过程。

- [Codex 源码：`codex-rs/mcp-server/src/lib.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/mcp-server/src/lib.rs)
  内置 MCP server 实现——通过 stdin/stdout JSON-RPC 与客户端通信。适用于：理解 Codex 作为 MCP server 角色时的消息处理循环。

- [Codex 源码：`codex-rs/codex-mcp/src/mcp/mod.rs`](https://github.com/anthropics/claude-code/blob/main/codex-rs/codex-mcp/src/mcp/mod.rs)
  `McpConfig`、`configured_mcp_servers()`、`effective_mcp_servers()`——从 Codex 全局配置到 MCP 运行时视图的转换。适用于：理解 config 对象到 connection manager 的桥接。

## 智慧（社区）

- [Model Context Protocol 官方规范](https://modelcontextprotocol.io/specification/2025-06-18/)
  MCP 协议规范——transports、lifecycle、tools、resources。适用于：理解 Codex 的 rmcp-client 所遵循的协议标准。

- [Claude Code Discord](https://discord.gg/anthropic)
  官方 Discord 社区，Claude Code 用户和开发者讨论 MCP 集成、自定义 server、OAuth 等话题。

## 空白

- 缺少 Codex Apps MCP 后端（wham/apps）的实际部署架构和 API 文档
- 缺少 stdio server launcher 在 Linux 上的 bwrap/landlock 沙箱细节
- 缺少 exec-server transport（executor_process_transport）的完整协议文档

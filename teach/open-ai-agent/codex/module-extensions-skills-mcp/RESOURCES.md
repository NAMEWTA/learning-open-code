# Codex 扩展系统资源

## 知识

- [Codex L0 项目地图](../../00-overview/lessons/0001-project-map.html)
  用于把本主题放回 Codex CLI、core、tools、MCP、extensions 的整体架构中。
- [Codex L0 项目总览参考](../../00-overview/reference/00-overview.html)
  用于快速确认 Rust workspace 模块组与后续 L1/L2 backlog。
- `open-ai-agent/codex/docs/skills.md`
  本仓库中的 Skills 文档入口，当前指向官方 Codex Skills 文档。
- `open-ai-agent/codex/codex-rs/core-skills/`
  Skills 发现、解析、快照、显式 mention 收集和 prompt 注入的核心来源。
- `open-ai-agent/codex/codex-rs/ext/skills/`
  Skills extension 把 skill catalog、read/list 工具和 turn input contributor 接入 extension API。
- `open-ai-agent/codex/codex-rs/plugin/` 与 `open-ai-agent/codex/codex-rs/core-plugins/`
  Plugin manifest、plugin provider、marketplace/store、skills/MCP/apps/hooks 能力装配的来源。
- `open-ai-agent/codex/codex-rs/codex-mcp/` 与 `open-ai-agent/codex/codex-rs/rmcp-client/`
  MCP server 配置解析、连接管理、工具正规化、stdio/HTTP 客户端与 OAuth 支持。
- `open-ai-agent/codex/codex-rs/mcp-server/`
  Codex 自身作为 MCP server 暴露给外部 MCP client 的实现。
- `open-ai-agent/codex/codex-rs/hooks/`
  Hook 事件、schema、发现、信任状态、命令执行和结果解析的实现。
- `open-ai-agent/codex/codex-rs/ext/extension-api/`
  内置扩展注册接口，定义 context、MCP、tool、turn lifecycle 等 contributor 边界。

## 智慧（社区）

- [OpenAI Codex GitHub 仓库](https://github.com/openai/codex)
  适用于验证扩展系统设计讨论、issue、PR 变更背景。
- [Model Context Protocol 官方文档](https://modelcontextprotocol.io/)
  适用于理解 Codex MCP client/server 代码背后的协议术语。

## 空白

- 本主题没有检索外部社区案例；当前目标是源码导览，现实使用经验可在后续 L2 调试课补充。

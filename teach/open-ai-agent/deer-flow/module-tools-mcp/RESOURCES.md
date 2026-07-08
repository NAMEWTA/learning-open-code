# Tools 与 MCP 资源

## 知识

- `backend/packages/harness/deerflow/tools/tools.py`
  工具聚合主入口。适用于理解配置工具、内置工具、subagent、vision、MCP、ACP 和去重顺序。
- `backend/packages/harness/deerflow/tools/builtins/tool_search.py`
  deferred MCP tool catalog 和 `tool_search` 的核心。适用于理解 MCP schema 延迟暴露、catalog hash 和 promote state。
- `backend/packages/harness/deerflow/mcp/`
  MCP client、cache、OAuth、session pool 和工具包装实现。适用于排查 MCP server 配置、缓存刷新、stdio session 复用和本地路径重写。
- `backend/app/gateway/routers/mcp.py`
  Gateway MCP 配置 API。适用于理解管理端如何读取、遮蔽、更新 MCP 配置并重置工具缓存。
- `backend/packages/harness/deerflow/config/tool_config.py` 与 `backend/packages/harness/deerflow/config/tool_search_config.py`
  配置 schema。适用于确认 `tools[*]`、`tool_groups` 和 `tool_search.enabled` 的运行时含义。
- `backend/tests/test_mcp_client_config.py`、`backend/tests/test_mcp_oauth.py`、`backend/tests/test_deferred_tool_crosscontext.py`
  回归测试锚点。适用于把源码判断落到可验证行为上。
- [L0 项目总览参考](../00-overview/reference/00-overview.html)
  说明 tools/MCP 在 DeerFlow 总体架构中的扩展能力入口位置。
- [Lead agent 模块参考](../module-lead-agent/reference/lead-agent-overview.html)
  说明 agent 装配阶段如何调用工具加载、skill policy 和 deferred tools。
- [Gateway 模块参考](../module-gateway/reference/gateway-overview.html)
  说明 Gateway router 暴露面，包含 MCP 配置 API 所在的服务边界。

## 智慧（社区）

- 本主题优先使用项目源码和回归测试作为事实来源。需要现实案例时，可从 DeerFlow 仓库中带有 MCP、tool_search、session pool、tool deduplication 关键词的 issue/PR 继续追踪。

## 空白

- 尚未额外收集 MCP 官方协议文档和第三方 server 开发指南。本 L1 目标是 DeerFlow 内部装配链路，这些材料留给后续 MCP 协议专题。

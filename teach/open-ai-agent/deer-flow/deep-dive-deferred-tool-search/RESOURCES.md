# MCP 延迟工具发现 资源

## 知识

- [DeerFlow backend AGENTS.md — Tool System / Deferred MCP tools](https://github.com/bytedance/deer-flow/blob/main/backend/AGENTS.md) — middleware 链第 21 位、`assemble_deferred_tools` 与 subagent 复用
- [DeerFlow module-tools-mcp 课程](../module-tools-mcp/lessons/0001-tools-mcp-module-tour.html) — 工具加载顺序与 MCP 打标入口
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/tools/builtins/tool_search.py` — catalog、tool_search 工具、fail-closed 装配
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/deferred_tool_filter_middleware.py` — bind 前隐藏 schema、未 promote 时拦截 tool call
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/config/tool_search_config.py` — `tool_search.enabled` 配置项
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/thread_state.py` — `merge_promoted` reducer 与 catalog hash 作用域
- 本地测试：`open-ai-agent/deer-flow/backend/tests/test_deferred_tool_crosscontext.py` — 跨 context、policy 泄漏、fail-closed、#2884 隔离
- 本地测试：`open-ai-agent/deer-flow/backend/tests/test_deferred_promotion_integration.py` — 两回合 promote 端到端

## 智慧（社区）

- [DeerFlow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `tool_search`、`#3272`、`#2884`、`deferred` 可找到 ContextVar 重构与 fail-closed 讨论

## 空白

- 官方用户文档尚未单独成章对比「关闭 vs 开启 tool_search」的 token 实测数据；本主题以源码 invariant 与测试为首要依据

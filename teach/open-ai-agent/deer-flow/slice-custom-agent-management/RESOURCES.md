# 自定义 agent 创建与更新 资源

## 知识

- [DeerFlow backend AGENTS.md — Gateway agents router](https://github.com/bytedance/deer-flow/blob/main/backend/AGENTS.md) — `/api/agents` CRUD 与 `agents_api.enabled` 开关说明
- [DeerFlow frontend AGENTS.md](https://github.com/bytedance/deer-flow/blob/main/frontend/AGENTS.md) — workspace agents 路由与 `core/agents` 数据层边界
- 本地源码：`open-ai-agent/deer-flow/backend/app/gateway/routers/agents.py` — HTTP 入口与错误码
- 本地源码：`open-ai-agent/deer-flow/frontend/src/core/agents/api.ts` — 前端 REST 封装
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/tools/builtins/setup_agent_tool.py` — bootstrap 创建工具
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/tools/builtins/update_agent_tool.py` — 聊天内自更新工具
- 本地测试：`open-ai-agent/deer-flow/frontend/tests/unit/core/agents/api.test.ts` — API 禁用与名称检查错误分支
- 本地测试：`open-ai-agent/deer-flow/backend/tests/test_update_agent_tool.py` — 更新工具校验与原子写入

## 智慧（社区）

- [DeerFlow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `agents_api`、`setup_agent`、`migrate_user_isolation` 可找到真实故障案例与修复讨论

## 空白

- 官方文档尚未单独成章讲解「自定义 agent 向导 vs REST CRUD」双路径；本主题课程以源码与测试为首要依据

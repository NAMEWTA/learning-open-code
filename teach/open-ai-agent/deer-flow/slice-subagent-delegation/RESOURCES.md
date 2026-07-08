# Subagent 委派全链路 资源

## 知识

- [DeerFlow backend AGENTS.md — Subagent System](https://github.com/bytedance/deer-flow/blob/main/backend/AGENTS.md) — task tool、executor、并发限制与 step 持久化说明
- [DeerFlow frontend AGENTS.md — Subtask step history](https://github.com/bytedance/deer-flow/blob/main/frontend/AGENTS.md) — `core/tasks/` 与 SubtaskCard 数据流
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/tools/builtins/task_tool.py` — 委派入口、轮询与 SSE 事件
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/subagents/executor.py` — 后台执行引擎
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/runs/worker.py` — `_SubagentEventBuffer` 批量持久化
- 本地契约：`open-ai-agent/deer-flow/contracts/subagent_status_contract.json` — 跨语言状态枚举
- 本地源码：`open-ai-agent/deer-flow/frontend/src/core/tasks/subtask-result.ts` — 前端解析 `additional_kwargs`
- 本地源码：`open-ai-agent/deer-flow/frontend/src/components/workspace/messages/subtask-card.tsx` — workspace 子任务卡片 UI
- 本地测试：`open-ai-agent/deer-flow/backend/tests/test_subagent_status_contract.py` — Python/TS 契约一致性
- 本地测试：`open-ai-agent/deer-flow/backend/tests/test_worker_subagent_persistence.py` — 事件缓冲与 flush 行为

## 智慧（社区）

- [DeerFlow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `subagent`、`task_tool`、`max_turns` 可找到真实超时与状态漂移案例

## 空白

- 官方用户文档尚未单独成章讲解 subagent 委派的前端卡片与 run events 回填；本主题以源码、契约 fixture 与测试为首要依据

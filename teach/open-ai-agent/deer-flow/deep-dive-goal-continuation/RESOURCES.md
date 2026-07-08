# goal 续跑深度剖析 资源

## 知识

- [backend AGENTS.md — Thread Runs goal 续跑说明](open-ai-agent/deer-flow/backend/AGENTS.md) — 产品级合约：续跑上限、no-progress breaker、evaluator 复用
- [runtime/goal.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/goal.py) — evaluator、`should_continue_goal`、`progress_key`、checkpoint 读写与乐观锁
- [runtime/runs/worker.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/runs/worker.py) — `_prepare_goal_continuation_input` 决策树与竞态守卫
- [agents/goal_state.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/goal_state.py) — `GoalState`、`GoalEvaluation`、`GoalBlocker` 类型契约
- [test_goal_runtime.py](open-ai-agent/deer-flow/backend/tests/test_goal_runtime.py) — evaluator 解析、续跑判定、progress_key 行为锚点
- [test_goal_worker.py](open-ai-agent/deer-flow/backend/tests/test_goal_worker.py) — worker 层竞态、abort、durable receipt 回归用例
- [L2 切片：goal 自动续跑](../slice-goal-continuation/lessons/0001-flow-map.html) — 主链路地图（本主题的前置阅读）

## 智慧（社区）

- [deer-flow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `goal` / `continuation` 可看到续跑边界与 evaluator 行为的真实讨论
- [LangGraph checkpoint 文档](https://langchain-ai.github.io/langgraph/concepts/persistence/) — `pending_writes` 与 `channel_versions` 为何影响续跑时机

## 空白

- Claude Code `/goal` 原始设计文档未单独收录；deer-flow 在 harness 层复刻 goal loop，排障主要依赖 AGENTS.md 与上述测试文件

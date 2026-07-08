# run goal 自动续跑 资源

## 知识

- [backend AGENTS.md — Thread Runs goal 续跑说明](open-ai-agent/deer-flow/backend/AGENTS.md) — Gateway run 结束后 evaluator、blocker、续跑上限与 no-progress breaker 的产品级约定
- [deerflow/runtime/goal.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/goal.py) — goal 读写、evaluator 调用、`should_continue_goal` 与隐藏续跑消息构造
- [deerflow/runtime/runs/worker.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/runs/worker.py) — `run_agent` 主循环与 `_prepare_goal_continuation_input` 并发守卫
- [deerflow/agents/goal_state.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/goal_state.py) — `GoalState`、`GoalEvaluation`、`GoalBlocker` 类型契约

## 智慧（社区）

- [deer-flow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `goal` / `continuation` 可看到续跑边界与 evaluator 行为的真实讨论
- [LangGraph checkpoint 文档](https://langchain-ai.github.io/langgraph/concepts/persistence/) — 理解 `channel_values.goal` 与 `pending_writes` 为何影响续跑时机

## 空白

- 面向终端用户的「goal loop 运维手册」尚未单独成文；排障主要依赖 `backend/tests/test_goal_worker.py`、`test_goal_runtime.py` 与 AGENTS.md 中的 RunManager 合约说明

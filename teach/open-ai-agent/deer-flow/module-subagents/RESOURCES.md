# Subagent 系统资源

## 知识

- `backend/packages/harness/deerflow/tools/builtins/task_tool.py`
  task tool 的对外入口、配置解析、后台执行启动、轮询、SSE 事件写出和结构化 ToolMessage 返回。
- `backend/packages/harness/deerflow/subagents/executor.py`
  subagent 后台执行引擎，负责创建 LangGraph agent、加载 skills、捕获 AI/Tool step、处理超时和取消。
- `backend/packages/harness/deerflow/subagents/step_events.py`
  将 subagent 消息压缩为 step payload，并把 `task_*` 自定义事件转换为可持久化的 `subagent.*` run event。
- `backend/packages/harness/deerflow/subagents/status_contract.py`
  后端与前端共享的结构化状态元数据规则，避免从模型可见文本中猜测终态。
- `contracts/subagent_status_contract.json`
  跨语言状态枚举夹具，固定 `completed`、`failed`、`cancelled`、`timed_out`、`polling_timed_out`、`max_turns_reached`。
- `backend/packages/harness/deerflow/agents/middlewares/delegation_ledger.py`
  从 AI `task` tool call 与 ToolMessage 元数据中提取 delegation ledger，给 lead agent 提供“已委托工作”上下文。
- `backend/packages/harness/deerflow/agents/middlewares/subagent_limit_middleware.py`
  对单次模型响应中的并行 `task` tool call 做硬限制，避免 prompt-only 约束失效。
- `backend/packages/harness/deerflow/runtime/runs/worker.py`
  `_SubagentEventBuffer` 将 subagent 事件批量写入 run event store，使 step 在刷新后仍可回看。
- `frontend/src/components/workspace/messages/subtask-card.tsx`
  用户可见 subtask card，直播消费 step，展开历史 run 时回填 `subagent.step`。
- `frontend/src/core/tasks/steps.ts` 与 `frontend/src/core/tasks/api.ts`
  前端 step 标准化、排序、合并和按 `task_id` 分页回填。
- `backend/tests/test_subagent_step_events.py`、`backend/tests/test_task_tool_core_logic.py`、`backend/tests/test_subagent_status_contract.py`
  后端主契约测试：事件映射、task tool 编排和状态元数据。
- `frontend/tests/e2e/subtask-card.spec.ts`、`frontend/tests/unit/core/tasks/*.test.ts`
  前端卡片与 step 回填测试线索。

## 智慧（社区）

- 本主题暂不收录外部社区材料；当前目标是对齐 deer-flow 仓库内的源码和测试事实。

## 空白

- 尚未整理 upstream PR/issue 讨论中的设计背景。若后续要学习为什么选择 batched run event persistence，可补充对应 issue 或 PR 讨论。

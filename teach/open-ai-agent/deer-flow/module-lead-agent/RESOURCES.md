# Agent lead runtime 资源

## 知识

- [L0 项目总览参考](../00-overview/reference/00-overview.html)
  用于确认 lead agent 在 deer-flow 整体架构中的位置。
- [LangGraph 入口声明](../../../../open-ai-agent/deer-flow/backend/langgraph.json)
  用于确认 `lead_agent` graph、auth 和 checkpointer 的注册位置。
- [lead agent 构造主线](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/lead_agent/agent.py)
  本主题最主要来源，覆盖模型选择、工具过滤、prompt 构建和 middleware 装配。
- [system prompt 构建](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/lead_agent/prompt.py)
  用于理解 SOUL、skills、subagent、deferred tools 与静态 prompt 的组合。
- [通用 agent 工厂](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/factory.py)
  用于对比 `make_lead_agent` 与 SDK 级 `create_deerflow_agent` 的边界。
- [ThreadState 数据边界](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/thread_state.py)
  用于理解 LangGraph state reducer 如何承载 sandbox、artifact、todo、delegation 和 skill context。
- [共享 runtime middleware builder](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/tool_error_handling_middleware.py)
  用于确认基础 middleware 顺序和 lead/subagent 共享边界。
- [Gateway run 接线](../../../../open-ai-agent/deer-flow/backend/app/gateway/services.py)
  用于理解 HTTP run 请求如何解析到 `make_lead_agent`。
- [后台 run worker](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/runs/worker.py)
  用于理解 graph 构造后如何通过 `agent.astream(...)` 执行并发布事件。
- [测试：lead agent 模型解析](../../../../open-ai-agent/deer-flow/backend/tests/test_lead_agent_model_resolution.py)
  用于校准请求模型、agent 配置模型与默认模型的优先级。
- [测试：lead agent prompt](../../../../open-ai-agent/deer-flow/backend/tests/test_lead_agent_prompt.py)
  用于校准 SOUL、skills、subagent 和 deferred tools prompt 的拼接行为。
- [测试：lead agent skills](../../../../open-ai-agent/deer-flow/backend/tests/test_lead_agent_skills.py)
  用于校准 skill allowed-tools policy 与工具暴露边界。
- [测试：create_deerflow_agent](../../../../open-ai-agent/deer-flow/backend/tests/test_create_deerflow_agent.py)
  用于校准 SDK 级 agent factory 与 feature-driven middleware 组合。

## 智慧（社区）

- 暂不纳入外部社区。本轮 L1 模块课只依据仓库当前源码生成，最高信号反馈来自后续 L2/L3 代码走查、测试用例和项目内审查。

## 空白

- 尚未引入 LangGraph 官方文档作为外部补充；后续若编写 API 级课程，再补充官方文档并校准版本差异。

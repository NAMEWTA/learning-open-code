# 使命：Subagent 委派全链路

## 为什么
我想在 DeerFlow 里让 lead agent 把复杂子任务委派给专用 subagent，并在 workspace 聊天里实时看到子任务卡片、步骤时间线与最终结果。需要弄清从 `task` 工具调用到后台执行、SSE 事件、持久化与前端状态契约的完整链路，以便排查「卡片一直转圈」「步骤丢失」「状态与后端不一致」等问题。

## 成功的样子
- 能画出 lead agent 调用 `task` → `task_tool` 轮询 → `SubagentExecutor` 后台线程 → `worker` 持久化 → 前端 `SubtaskCard` 的主路径
- 看到 `Unknown subagent type` 或 `max_turns_reached` 时，能判断是配置层、执行层还是前后端状态契约层的问题
- 知道 `subagent_status` 结构化元数据与 `contracts/subagent_status_contract.json` 的对应关系，而不是靠解析 ToolMessage 正文

## 约束条件
- 以当前 monorepo 子模块源码为准
- 先掌握 L0 总览与 module-subagents、module-lead-agent、module-runtime-persistence 模块导览

## 不在范围内
- subagent 自定义 agent 的 config.yaml 编写细节（见 module-subagents 与 slice-custom-agent-management）
- GuardrailMiddleware 对委派工具调用的策略细节（见 module-lead-agent）

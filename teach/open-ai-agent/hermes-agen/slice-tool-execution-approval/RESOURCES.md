# 工具执行与审批全链路 资源

## 知识

- [agent/tool_executor.py](../../../../open-ai-agent/hermes-agen/agent/tool_executor.py) — 工具调用分发器，`_execute_tool_calls_concurrent` 和 `_execute_tool_calls_sequential` 两个入口
- [tools/registry.py](../../../../open-ai-agent/hermes-agen/tools/registry.py) — 工具注册中心，AST 扫描自发现，30s TTL 缓存
- [tools/approval.py](../../../../open-ai-agent/hermes-agen/tools/approval.py) — 三层安全闸门：HARDLINE(12条阻断) → DANGEROUS(47条需审批) → Smart(LLM判断)
- [agent/agent_runtime_helpers.py](../../../../open-ai-agent/hermes-agen/agent/agent_runtime_helpers.py) — `invoke_tool()` 统一调度入口（agent 级工具 + registry 分发）
- [tools/terminal_tool.py](../../../../open-ai-agent/hermes-agen/tools/terminal_tool.py) — 终端命令执行，六种后端
- [tools/delegate_tool.py](../../../../open-ai-agent/hermes-agen/tools/delegate_tool.py) — 子代理委托，DELEGATE_BLOCKED_TOOLS 黑名单

## 智慧（社区）

- [Mercury Agent 权限硬化屏蔽列表](https://github.com/cosmicstack-labs/mercury-agent) — HARDLINE 方案的灵感来源
- [OpenAI Codex Smart Approvals](https://github.com/openai/codex) — Smart 审批（辅助 LLM 判断）的设计参考

## 空白

- Smart 审批所使用的 auxiliary LLM 模型选择与配置文档缺失（仅有代码内 system prompt）
- 审批层的单元测试覆盖情况尚未整理

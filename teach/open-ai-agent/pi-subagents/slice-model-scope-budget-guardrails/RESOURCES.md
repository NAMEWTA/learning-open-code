# 模型范围、预算与安全边界 资源

## 知识

- `open-ai-agent/pi-subagents/src/runs/shared/model-scope.ts` — modelScope 纯函数决策与 settings 解析
- `open-ai-agent/pi-subagents/src/runs/shared/model-fallback.ts` — 模型解析时调用 `checkModelScope`，区分 explicit / inherited
- `open-ai-agent/pi-subagents/src/runs/shared/tool-budget.ts` — toolBudget 校验、状态机与 `PI_SUBAGENT_TOOL_BUDGET` 编解码
- `open-ai-agent/pi-subagents/src/runs/shared/turn-budget.ts` — turnBudget 系统提示追加与 abort 判定
- `open-ai-agent/pi-subagents/src/runs/shared/subagent-prompt-runtime.ts` — 子进程侧 prompt 重写、父消息剥离、tool budget 拦截
- `open-ai-agent/pi-subagents/src/shared/fork-context.ts` — fork 会话分支与 Anthropic thinking 块清理
- `open-ai-agent/pi-subagents/src/profiles/profiles.ts` — profile 写入 `agentOverrides.model`，上游影响模型候选
- `open-ai-agent/pi-subagents/src/runs/foreground/subagent-executor.ts` — 解析 budgets、modelScope、fork resolver 并下发 execution
- `open-ai-agent/pi-subagents/src/runs/foreground/execution.ts` — 前台 spawn 前拼接 turnBudget 提示、buildModelCandidates
- `open-ai-agent/pi-subagents/src/agents/agents.ts` — `discoverAgents` 合并 project/user 的 `subagents.modelScope`
- `open-ai-agent/pi-subagents/README.md` — 扩展配置与 settings 字段说明

## 智慧（社区）

- [pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues) — model scope、budget 相关行为变更与边界讨论

## 空白

- 暂无独立的官方「guardrails 设计文档」；本切片以源码注释与 unit 测试为唯一权威来源

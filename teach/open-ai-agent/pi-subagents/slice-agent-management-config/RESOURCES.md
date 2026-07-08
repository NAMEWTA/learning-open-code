# Agent 管理、覆盖与配置解析资源

## 知识

- [pi-subagents README](https://github.com/nicobailon/pi-subagents/blob/main/README.md) — 用户面对 agent 目录、settings 与 subagent 管理动作的说明
- `open-ai-agent/pi-subagents/src/runs/foreground/subagent-executor.ts` — 管理动作入口，调用 `handleManagementAction` 并注入 `loadConfig()`
- `open-ai-agent/pi-subagents/src/agents/agent-management.ts` — list/get/create/update/delete/eject/disable/enable/reset 实现
- `open-ai-agent/pi-subagents/src/agents/agents.ts` — `discoverAgents` / `discoverAgentsAll`、settings 读取与 override 应用
- `open-ai-agent/pi-subagents/src/agents/frontmatter.ts` — agent/chain Markdown frontmatter 解析
- `open-ai-agent/pi-subagents/src/agents/agent-selection.ts` — `mergeAgentsForScope` 同名合并
- `open-ai-agent/pi-subagents/src/extension/config.ts` — extension 级 `config.json` 读写（如 proactive skill 配置）
- `open-ai-agent/pi-subagents/test/unit/agent-overrides.test.ts` — defaultModel 与 agentOverrides 优先级
- `open-ai-agent/pi-subagents/test/unit/agent-management.test.ts` — CRUD、JSON 解析错误、package 命名
- `open-ai-agent/pi-subagents/test/unit/agent-eject-disable.test.ts` — disable/enable/reset/eject 边界
- `open-ai-agent/pi-subagents/test/unit/agent-selection.test.ts` — scope 合并单元测试
- `open-ai-agent/pi-subagents/test/unit/agent-frontmatter.test.ts` — frontmatter 字段与 block 值

## 智慧（社区）

- [pi-subagents Issues](https://github.com/nicobailon/pi-subagents/issues) — agent 覆盖、settings 与 package agent 的实战问题
- [Pi coding agent 生态](https://github.com/earendil-works) — extension 配置与 subagent 工具链讨论

## 空白

- 暂无独立的 agent override 官方设计文档；行为以源码与 unit test 为准
- 中文社区对 `agentOverrides` 与 frontmatter 逐字段优先的案例较少，建议对照本主题 reference 速查页

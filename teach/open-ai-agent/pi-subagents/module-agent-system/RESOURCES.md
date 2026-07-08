# Agent 系统模块资源

## 知识

- [L0 项目整体架构与学习地图](../00-overview/lessons/0001-project-map.html)
  用于确认本课位置：executor 消费已解析的 `AgentConfig`，agents 模块负责把来源和覆盖规则解析成运行时角色。
- [L0 总览参考图谱](../00-overview/reference/00-overview.html)
  用于复查项目级目录职责、后续 L1/L2 主题边界，以及本课和执行层课程的衔接点。
- [`src/agents/agents.ts`](../../../../open-ai-agent/pi-subagents/src/agents/agents.ts)
  Agent 与 chain discovery 主入口，包含 builtin、package、user、project 读取、settings override、默认模型、禁用和最终合并。
- [`src/agents/agent-selection.ts`](../../../../open-ai-agent/pi-subagents/src/agents/agent-selection.ts)
  最小优先级规则来源：builtin、package 先入表，user/project 再按 scope 覆盖。
- [`src/agents/agent-management.ts`](../../../../open-ai-agent/pi-subagents/src/agents/agent-management.ts)
  管理动作入口，说明哪些动作可写 user/project，哪些来源只读，以及 create/update/delete/eject/disable/enable/reset 的边界。
- [`src/agents/frontmatter.ts`](../../../../open-ai-agent/pi-subagents/src/agents/frontmatter.ts)
  Markdown agent/chain 文件的 frontmatter 解析器，解释普通字段与嵌套 block 字段如何进入配置。
- [`src/agents/agent-memory.ts`](../../../../open-ai-agent/pi-subagents/src/agents/agent-memory.ts)
  可选 agent memory 的解析、路径安全检查和 system prompt 注入逻辑。
- [`test/unit/agent-selection.test.ts`](../../../../open-ai-agent/pi-subagents/test/unit/agent-selection.test.ts)
  直接验证来源优先级：package 覆盖 builtin，user/project 覆盖 package，`both` 下 project 覆盖 user。
- [`test/unit/agent-overrides.test.ts`](../../../../open-ai-agent/pi-subagents/test/unit/agent-overrides.test.ts)
  验证 defaultModel、disableBuiltins、disableThinking、agentOverrides、frontmatter 字段优先级和错误暴露。
- [`test/unit/agent-management.test.ts`](../../../../open-ai-agent/pi-subagents/test/unit/agent-management.test.ts)
  验证管理动作的创建、更新、删除、只读包 agent、JSON chain 保留和模型映射输出。

## 智慧（社区）

- 本地反馈回路：`open-ai-agent/pi-subagents/test/unit/agent-*.test.ts`
  修改或理解 agents 模块时，优先用这些单元测试验证判断，而不是只依赖 README 或推测。

## 空白

- 本轮未联网核验上游 GitHub issues、PR 讨论或社区经验帖；如果后续课程要讲真实用户踩坑，需要单独检索并补充高质量外部讨论。

# Skills 系统资源

## 知识

- [L0 项目总览参考](../00-overview/reference/00-overview.html)
  用于确认 Skills 系统在 deer-flow 整体架构中的位置。
- [DeerFlow README：Skills & Tools](../../../../open-ai-agent/deer-flow/README.md)
  项目自述对 Skills 的定位、progressive loading、slash 激活和 sandbox 路径作了用户级说明。适用于建立概念入口。
- [Skills runtime 源码目录](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/skills/)
  skill 类型、frontmatter parser、catalog、describe_skill、install、storage 与 allowed-tools policy 的主实现。适用于所有源码级判断。
- [Lead agent 装配源码](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/lead_agent/agent.py)
  skills 如何进入 agent factory、工具过滤和 prompt 参数的关键路径。适用于理解架构位置。
- [Lead agent prompt 源码](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/lead_agent/prompt.py)
  `<skill_system>`、`<available_skills>`、`<skill_index>`、disabled skills 与 skill evolution 提示的渲染点。
- [SkillActivationMiddleware](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/skill_activation_middleware.py)
  `/skill-name` 显式激活、隐藏 HumanMessage 注入、可用 skill 白名单和 request-scoped secrets 绑定的核心实现。
- [Gateway skills router](../../../../open-ai-agent/deer-flow/backend/app/gateway/routers/skills.py)
  Web/API 层的 list、install、toggle、custom skill lifecycle、history 和 rollback 入口。
- [配置模板中的 skills section](../../../../open-ai-agent/deer-flow/config.example.yaml)
  `skills.container_path`、`skills.deferred_discovery`、custom agent `skills` 白名单和 durable `skill_context` 配置说明。
- [Skills 相关 pytest](../../../../open-ai-agent/deer-flow/backend/tests/)
  `test_lead_agent_skills.py`、`test_slash_skills.py`、`test_skill_context.py`、`test_skills_custom_router.py` 等回归用例。适用于验证边界条件。

## 智慧（社区）

- [DeerFlow 上游 Issues](https://github.com/bytedance/deer-flow/issues)
  适用于核对 skills 行为是否是设计选择、历史兼容或仍在演进的问题。
- [DeerFlow 上游 Pull Requests](https://github.com/bytedance/deer-flow/pulls)
  适用于追踪 skills、MCP、sandbox 与 custom agent 边界变更的真实审查语境。

## 空白

- 本模块当前只基于仓库源码、README、配置模板和测试生成；未单独筛选外部 Agent Skill 规范文档或社区教程。若后续要讲 skill authoring 标准，需要补充 AgentSkills 规范与 DeerFlow `.skill` 打包实践资源。

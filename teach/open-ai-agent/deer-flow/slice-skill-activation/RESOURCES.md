# skill slash 激活与递进加载 资源

## 知识

- [DeerFlow backend AGENTS.md — Skills System](https://github.com/bytedance/deer-flow/blob/main/backend/AGENTS.md) — slash 激活、递进发现、`required-secrets` 与 middleware 链顺序
- [DeerFlow module-skills 课程](../module-skills/lessons/0001-skills-module-tour.html) — `SKILL.md` 格式、`extensions_config.json` 与安装 API
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/skill_activation_middleware.py` — slash 解析、注入与密钥绑定
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/agents/middlewares/skill_context.py` — `read_file` 配对捕获与 `render_skill_context`
- 本地源码：`open-ai-agent/deer-flow/backend/packages/harness/deerflow/skills/slash.py` — `/skill-name` 语法与保留命令
- 本地示例：`open-ai-agent/deer-flow/skills/public/chart-visualization/SKILL.md` — 可被 slash 激活的 public skill 样本
- 本地测试：`open-ai-agent/deer-flow/backend/tests/test_skill_request_scoped_secrets.py` — slash 与 in-context 密钥来源

## 智慧（社区）

- [DeerFlow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `slash skill`、`skill_context`、`SkillActivationMiddleware` 可找到真实回归与 #3861/#3938 讨论

## 空白

- 官方用户文档尚未单独成章对比「slash 激活 vs read_file 递进加载」；本主题以 harness 源码与测试为首要依据

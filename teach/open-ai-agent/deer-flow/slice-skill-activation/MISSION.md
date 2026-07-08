# 使命：skill slash 激活与递进加载

## 为什么
我想在 DeerFlow 里用 `/skill-name` 显式启用某个技能，并理解 agent 通过 `read_file` 逐步加载技能时，系统如何把 SKILL.md 正文、元数据引用与密钥注入区分开。需要能沿 middleware 链排障「技能未激活」「已禁用」「正文未进上下文」等问题。

## 成功的样子
- 能区分 slash 激活（当轮注入完整 SKILL.md）与递进加载（checkpoint 只存 name/path/description，后续回合注入紧凑提醒）
- 画出从用户输入到 `SkillActivationMiddleware` 与 `DurableContextMiddleware` 的主时序，并列举典型失败返回
- 知道 `skills/public/` 与 harness `deerflow/skills/` 在解析、存储与 allowlist 上的分工

## 约束条件
- 以当前 monorepo 子模块源码为准；先读过 module-skills 与 module-lead-agent 导览更佳
- 课程控制在 15 分钟短课体量，细节查 reference 速查页

## 不在范围内
- request-scoped secrets 与 sandbox env 注入的完整安全审计（见 backend AGENTS.md Skills 节 #3861）
- `deferred_discovery` 下 `describe_skill` 工具的完整交互（见 module-skills）

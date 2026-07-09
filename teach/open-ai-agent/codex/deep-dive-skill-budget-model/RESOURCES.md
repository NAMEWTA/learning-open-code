# Skill 上下文预算模型 资源

## 知识

### 源码入口（核心）
- `open-ai-agent/codex/codex-rs/core-skills/src/render.rs` — 预算模型主实现（1574 行），包含 `default_skill_metadata_budget`（2% 上下文窗口预算）、三级降级渲染（`render_skill_lines_from_lines`）、描述截断（`truncate_default_context_skill_description`）、别名压缩（`build_aliased_available_skills`）、描述预算分配算法（`render_lines_with_description_budget`）
- `open-ai-agent/codex/codex-rs/core-skills/src/model.rs` — 数据模型（242 行），包含 `SkillMetadata`（name/description/scope/path）、`SkillLoadOutcome`（skills/enabled/disabled）、`HostSkillsSnapshot`
- `open-ai-agent/codex/codex-rs/core-skills/src/injection.rs` — 显式提及与全文注入（547 行），包含 `build_skill_injections`（显式 skill 全文加载）、`collect_explicit_skill_mentions`（从用户输入提取 `$skill-name` 和结构化 skill 选择）

### 关键常量
| 常量 | 值 | 说明 |
|------|-----|------|
| `SKILL_METADATA_CONTEXT_WINDOW_PERCENT` | 2 | 技能元数据占上下文窗口的百分比 |
| `DEFAULT_SKILL_METADATA_CHAR_BUDGET` | 8000 | 无上下文窗口信息时的字符预算回退 |
| `MAX_DEFAULT_CONTEXT_SKILL_DESCRIPTION_CHARS` | 1024 | 单个 skill 描述的最大字符数（超长截断） |
| `SKILL_DESCRIPTION_TRUNCATION_WARNING_THRESHOLD_CHARS` | 100 | 平均截断超过此值时触发警告 |
| `APPROX_BYTES_PER_TOKEN` | 4 | 字节→token 近似换算（用于 token 预算模式） |

### 测试文件
- `open-ai-agent/codex/codex-rs/core-skills/src/render.rs` 内联测试（922-1574 行） — 覆盖默认预算计算、描述截断行为、预算压力下平权截断、优先级保留（System > Admin > Repo > User）、别名压缩退火、marketplace root 提取等场景

### 官方文档
- [Codex AGENTS.md](https://github.com/openai/codex/blob/main/AGENTS.md) — Codex 项目整体架构与模块职责说明
- [Codex docs/skills.md](https://github.com/openai/codex/blob/main/docs/skills.md) — Skills 系统文档入口

## 智慧（社区）

- [OpenAI Codex GitHub Discussions](https://github.com/openai/codex/discussions) — Codex 官方讨论区
- [OpenAI Developer Forum](https://community.openai.com/) — OpenAI 开发者社区

## 空白

- 暂无 Codex 团队关于"为什么选择 2% 而非其他比例"的设计文档或博客
- 暂无 token-based 预算与 character-based 预算在实际模型（GPT-5、Claude 4）上的精度对比数据
- 描述预算分配算法（逐字符轮转）在不同 skills 数量下的时间复杂度未公开 profile

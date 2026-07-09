# Skill 发现、读取与上下文注入链路 — 资源

## 知识

- [docs/skills.md](../../../../open-ai-agent/codex/docs/skills.md) — Skill 系统对外文档入口，链接到 developers.openai.com 官方文档。
- [codex-rs/core-skills/src/loader.rs](../../../../open-ai-agent/codex/codex-rs/core-skills/src/loader.rs) — Skill 发现与加载核心：`skill_roots()` 五种来源、`discover_skills_under_root()` 目录扫描、`parse_skill_file()` 解析 SKILL.md。
- [codex-rs/core-skills/src/model.rs](../../../../open-ai-agent/codex/codex-rs/core-skills/src/model.rs) — 核心数据模型：`SkillMetadata`、`SkillLoadOutcome`、`HostSkillsSnapshot`、`SkillError`。
- [codex-rs/core-skills/src/service.rs](../../../../open-ai-agent/codex/codex-rs/core-skills/src/service.rs) — `SkillsService`：缓存、config 规则、product 过滤、`snapshot_for_config()` 与 `snapshot_for_cwd()` 两个入口。
- [codex-rs/core-skills/src/injection.rs](../../../../open-ai-agent/codex/codex-rs/core-skills/src/injection.rs) — Skill 上下文注入：`build_skill_injections()` 读取 SKILL.md 全文、`collect_explicit_skill_mentions()` Text/$SkillName 提及解析。
- [codex-rs/core-skills/src/render.rs](../../../../open-ai-agent/codex/codex-rs/core-skills/src/render.rs) — 可用 Skill 列表渲染：预算模型、`SkillLine` 渲染、别名压缩（AliasPlan）、截断策略。
- [codex-rs/core-skills/src/skill_instructions.rs](../../../../open-ai-agent/codex/codex-rs/core-skills/src/skill_instructions.rs) — `SkillInstructions`：将注入内容包装为 `<skill>` 标签的 `ContextualUserFragment`。
- [codex-rs/core/src/context/available_skills_instructions.rs](../../../../open-ai-agent/codex/codex-rs/core/src/context/available_skills_instructions.rs) — `AvailableSkillsInstructions`：将渲染后的 Skill 目录包装为 `developer` 角色的上下文片段。
- [codex-rs/app-server/src/skills_watcher.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/skills_watcher.rs) — `SkillsWatcher`：监听 Skill 文件变化，触发缓存清空和 `SkillsChanged` 通知。
- [codex-rs/core/src/skills.rs](../../../../open-ai-agent/codex/codex-rs/core/src/skills.rs) — core 层 Skill 集成：从 `codex_core_skills` 重新导出 API、`maybe_emit_implicit_skill_invocation()`。
- [codex-rs/core/src/session/mod.rs](../../../../open-ai-agent/codex/codex-rs/core/src/session/mod.rs) (L3266-3291) — 系统提示词组装点：调用 `build_available_skills()` 并 push 到 `developer_sections`。

## 智慧（社区）

- [OpenAI Codex 官方 Skills 文档](https://developers.openai.com/codex/skills) — 从用户视角理解 Skill 系统的设计意图。
- [OpenAI Codex GitHub Issues](https://github.com/openai/codex/issues) — 搜索 "skill"、"SKILL.md"、"skills not loading" 观察真实使用问题。

## 空白

- Skill 扩展层（`codex-rs/ext/skills/`）的独立渲染逻辑不在本切片范围内，属于扩展机制深入探索。
- `plugin_namespace` 解析（`codex_utils_plugins::plugin_namespace_for_skill_path`）未展开，涉及跨 crate 依赖。
- `detect_implicit_skill_invocation_for_command()` 的隐式调用检测算法未展开，属于 L3 深度解析候选。

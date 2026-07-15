# 技能生命周期全链路 资源

## 知识

### 源码入口（按生命周期顺序）

| 阶段 | 源码文件 | 关键内容 |
|------|---------|---------|
| Task Complete | `agent/curator.py:1958` | `maybe_run_curator()` 公共入口 |
| Curator 门控 | `agent/curator.py:219` | `should_run_now()` 三条件门控 |
| 状态转换 | `agent/curator.py:291` | `apply_automatic_transitions()` 状态机 |
| 来源追踪 | `tools/skill_provenance.py:37` | `_write_origin` ContextVar |
| 技能标记 | `tools/skill_usage.py:646` | `mark_agent_created()` |
| 归档操作 | `tools/skill_usage.py:696` | `archive_skill()` |
| 保护列表 | `tools/skill_usage.py:66` | `PROTECTED_BUILTIN_SKILLS` |
| LLM 审查 | `agent/curator.py:1809` | `_run_llm_review()` (默认关闭) |
| 报告写入 | `agent/curator.py:1079` | `_write_run_report()` |

### 关键数据文件

- `~/.hermes/skills/.usage.json` — 技能使用遥测侧车文件，curator 状态机判定依据
- `~/.hermes/logs/curator/{timestamp}/run.json` — 每次 curator 运行的决策记录
- `~/.hermes/logs/curator/{timestamp}/REPORT.md` — 人类可读的 curator 运行报告
- `~/.hermes/skills/.curator_state` — curator 持久化状态（last_run_at, run_count）
- `~/.hermes/skills/.archive/` — 归档技能存放目录（扁平布局）

### 阅读顺序建议

1. `tools/skill_provenance.py` (79 行) — 最短，理解前台/后台分界
2. `tools/skill_usage.py` 中 `PROTECTED_BUILTIN_SKILLS`、`archive_skill()`、`mark_agent_created()`
3. `agent/curator.py` 中 `should_run_now()` → `apply_automatic_transitions()` → `run_curator_review()`

## 智慧（社区）

- [Nous Research Discord](https://discord.gg/nousresearch) — Hermes Agent 官方社区，可讨论 curator 行为与配置
- [agentskills.io](https://agentskills.io) — AgentSkills 开放标准，理解 SKILL.md 格式的设计意图

## 空白

- curator 配置项 `prune_builtins` 的实际使用场景与风险案例 — 暂未找到社区讨论
- 多个 agent 实例共享 `~/.hermes/skills/` 时的 `.usage.json` 竞态条件 — 源码中有文件锁但缺乏并发场景验证报告

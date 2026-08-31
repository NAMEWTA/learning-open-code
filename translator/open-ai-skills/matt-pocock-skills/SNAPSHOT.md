# 翻译快照：matt-pocock-skills

## 源项目信息
- **仓库路径**：`open-ai-skills/matt-pocock-skills`
- **Git Commit**：`8b36d4fb2635b3c21998dcd8144439c9e5ba7302`
- **短 Commit**：`8b36d4f`
- **分支**：`main`
- **快照时间**：2026-08-06T00:00:00+08:00
- **翻译完成时间**：2026-08-06T00:00:00+08:00
- **项目类型**：skill-collection
- **翻译性质**：全量增量翻译（上次快照：`66f92b6`）

## 本次增量翻译范围

| 类别 | 数量 | 处理 |
|------|------|------|
| 变更文件 | 53 | 增量更新/重译（SKILL.md × 13、README × 5、docs × 25、auxiliary × 7、config × 2、meta × 3、script × 1、workflow × 1） |
| 新增文件 | 12 | 全量翻译（SKILL.md × 1、docs × 4、auxiliary × 3、meta × 1、config × 2、script × 1） |
| 新增跳过 | 36 | 35 个 `agents/openai.yaml`（配置元数据保持英文）+ `LICENSE`（法律文件） |
| 删除文件 | 10 | 标记 skipped（`deprecated/` 4 个、`personal/` 3 个、`writing-great-skills` 2 个、docs 1 个） |

**主要变更主题**（源 `66f92b6` → `8b36d4f`）：
- `to-prd`/`to-issues` → `to-spec`/`to-tickets` 重命名，`writing-great-skills` → `writing-for-agents` 重命名
- `wizard`、`to-questionnaire`、`wait-what` 毕业为推广技能；6 个技能退役删除
- Claude Code 官方插件市场发布（plugin.json/marketplace.json/install-block/adr-0002）
- Codex 双 harness 支持（35 个 `agents/openai.yaml`）
- `grilling` 从一次一个问题重构为轮次/前沿模式
- `prototype` 从终端 TUI 改为共享 HTML 文件 + 一手资料保留
- `ask-matt` 路由器大改（阶段边界、wayfinder 路由）

## 翻译文件统计（累计）

| 类型 | 数量 |
|------|------|
| SKILL.md | 35 |
| README | 7 |
| 辅助 .md 文件 | 31 |
| 文档（docs/） | 27 |
| 配置文件 | 5 |
| 元数据文件 | 4 |
| Shell/JS 脚本 | 6 |
| CI/CD 工作流 | 1 |
| **已完成** | **114** |
| **跳过**（openai.yaml、LICENSE、源已删除、自动生成文件） | **50** |
| **总计** | **164** |

## 翻译摘要
- 总文件数：164
- 已翻译：114
- 已跳过：50（35 个 openai.yaml 配置元数据 + LICENSE + 10 个源已删除 + 2 个上一轮删除记录 + `.git`/`package-lock.json` 历史遗留误录）
- 待翻译：0
- 质量抽查：通过（6 个文件，0 个问题）
- 源文件修改：无（已验证 git status 确认）
- 翻译器版本：1.0.0

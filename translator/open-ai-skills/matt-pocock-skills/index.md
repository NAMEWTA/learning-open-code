# matt-pocock-skills 翻译索引

## 项目信息

- **源项目路径**：`open-ai-skills/matt-pocock-skills`
- **项目类型**：skill-collection（技能集合）
- **描述**：Matt Pocock 的 AI 编程技能集合，包含工程、生产力、个人等分类的技能定义

## 翻译记录

| 日期 | 源 Commit | 翻译范围 | 状态 |
|------|----------|---------|------|
| 2026-07-10 | `66f92b6` | 全量翻译（110 个文件） | ✅ 完成 |
| 2026-08-06 | `8b36d4f` | 增量翻译（6 个文件：wizard 移至 engineering 并更新、新增 writing-for-agents / wait-what / to-questionnaire） | ✅ 完成 |
| 2026-08-06 | `8b36d4f` | 全量增量（53 个变更 + 12 个新增翻译 + 10 个删除标记 + 36 个跳过） | ✅ 完成 |

## 翻译覆盖范围

| 分类 | 文件数 | 说明 |
|------|--------|------|
| 工程 SKILL.md | 18 | 日常编码使用的核心技能（含迁入的 wizard） |
| 生产力 SKILL.md | 8 | 通用工作流工具（含 to-questionnaire、wait-what、writing-for-agents） |
| 开发中 SKILL.md | 5 | 尚未发布的新技能（含新增的 setup-ts-deep-modules） |
| 杂项 SKILL.md | 4 | 很少使用但保留的工具 |
| 已弃用 SKILL.md | 0 | 已全部删除（空分类） |
| 分类 README | 5 | 各分类的索引说明 |
| 根 README | 1 | 项目总览和快速开始 |
| 文档页面 (docs/) | 27 | 面向用户的技能文档 |
| 辅助 .md 文件 | 31 | ADR、安装块、阶段边界、术语表、模板等 |
| JSON 配置 | 5 | plugin.json、marketplace.json、package.json、changeset 配置、dependency-cruiser |
| 元数据文件 | 4 | CLAUDE.md、CONTEXT.md、CHANGELOG.md、AGENTS.md、.gitignore |
| Shell/JS 脚本 | 6 | 安装/链接/向导/版本同步脚本 |
| CI/CD 工作流 | 1 | GitHub Actions release 工作流 |
| **已完成** | **114** | |
| 跳过 | 50 | openai.yaml 配置元数据（35）+ LICENSE（1）+ 源已删除（12）+ 自动生成/误录（2） |

## 翻译质量

- 所有文件通过中文文档排版规范检查
- 中英文/数字间正确添加空格
- 代码块、命令引用、技术术语完整保留
- Frontmatter `name` 字段未修改
- 源文件零修改

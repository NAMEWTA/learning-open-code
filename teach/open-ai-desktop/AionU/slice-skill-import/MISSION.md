# 使命：助手或 Skill 导入全链路

## 为什么
本主题帮助读者在修改 AionU 设置页、Skill 导入、assistant 默认技能或相关 E2E 时，能快速判断一次用户操作会穿过哪些 UI、hook、文案、adapter 和后端状态刷新点。学完后，读者应能定位导入失败、默认 skill 未持久化、列表未刷新这类问题的真实责任层。

## 成功的样子
- 能从 Skills Hub 的手动导入按钮追到 `POST /api/skills/import` 和导入后的 `GET /api/skills`。
- 能说明 AssistantSettings 中默认 skill 选择如何进入 `enabled_skills` 与 `defaults.skills.value`。
- 能识别至少一条失败路径，例如 `SKILL_IMPORT_FILE_TOO_LARGE` 如何阻止 assistant 保存继续执行。
- 能根据改动范围选择应补的 E2E 或 DOM 测试证据。

## 约束条件
- 源项目 `open-ai-desktop/AionU/` 只读。
- 本主题只写入 `teach/open-ai-desktop/AionU/slice-skill-import/`。
- 不修改项目级 `index.md`、`00-index.md`、`_progress.json` 或 `_progress.md`。
- 课程保持 L2 垂直切片视角，不展开 aioncore 后端内部实现。

## 不在范围内
- 不讲 conversation runtime 中 skill materialize 的运行时使用链路。
- 不讲 MCP server 导入和 Tools 设置全链路。
- 不重写或修复现有 E2E，只把它们作为证据阅读。

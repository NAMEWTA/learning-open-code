# 教学笔记：构建与发布模块

- 本主题按 L1 模块总览处理，不修改项目级 `_progress.json`、`_progress.md` 或 `index.md`。
- lesson 只讲“从 `bun run dist:mac` 到可验证产物”的主线；完整接口、脚本清单和风险放在 `reference/build-release-overview.html`。
- 需要交叉链接 `../00-overview/`、`../module-main-entry/`、`../module-web-runtime/`，但不修改这些目录。
- 新发现：`Dockerfile` 与当前 `package.json` 构建命令存在疑似漂移，reference 中标为风险，不作为主发布路径。

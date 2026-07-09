# 教学笔记：Sandbox、权限与配置系统

- 本主题是 `teach-goal` 的 L1 worker 产物，只能写入 `teach/open-ai-agent/codex/module-sandbox-config/`。
- lesson 以“最小配置如何变成 sandbox 执行”为单一目标；reference 承担完整清单、源码索引和阅读顺序。
- L0 链接使用 `../../00-overview/lessons/0001-project-map.html` 与 `../../00-overview/reference/00-overview.html`，便于回到项目全景。
- 源码抽查重点：`config_toml.rs`、`permissions_toml.rs`、`core/src/config/mod.rs`、`core/src/config/permissions.rs`、`sandboxing/src/manager.rs`、Linux/Windows sandbox README 或入口文件、`execpolicy/README.md`。

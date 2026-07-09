# 使命：Codex 项目总览与学习地图

## 为什么
用户希望从 0 到 1 精通 OpenAI Codex CLI 的架构与实现细节，最终能够独立阅读源码、定位功能归属，并为后续模块级学习建立稳定地图。本主题先建立项目定位、目录职责、核心模块边界和后续学习路线，避免一开始陷入 100 多个 Rust crate 的细节迷宫。

## 成功的样子
- 能用一句话说明 Codex CLI 与 Codex IDE、Codex Web、Codex App 的关系。
- 能根据顶层目录判断一个问题应先查 `codex-rs`、`codex-cli`、`sdk`、`docs`、`scripts` 还是 CI/发布配置。
- 能把 `codex-rs/Cargo.toml` 中的 workspace members 归并为 CLI/TUI、core、app-server、tools、sandbox、model/backend、SDK 支撑等模块组。
- 能从总览参考文档中挑出后续 L1/L2 学习 backlog，而不是逐文件无序阅读。

## 约束条件
- 本主题是 L0 锚点，只建立学习地图，不展开单个 crate 的完整源码链路。
- 每节 lesson 必须在 15 分钟内完成，长表格、模块清单和 backlog 放入 `reference/`。
- 所有教学内容以当前本地源码快照为准，后续源码更新后需通过 `SNAPSHOT.md` 判断是否需要同步。

## 不在范围内
- 不讲 Rust 语法基础、Tokio/ratatui/axum 的通用教程。
- 不逐个展开 124 个 workspace member。
- 不修改 Codex 源码、不生成根项目进度台账。

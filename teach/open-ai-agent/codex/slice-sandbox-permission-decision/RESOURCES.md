# Sandbox 权限决策链路 资源

## 知识

- [Codex Security Documentation](https://developers.openai.com/codex/security) — 官方安全文档，涵盖沙箱模型、审批策略和权限配置。适用于：理解 Codex 安全设计的整体意图。
- `docs/sandbox.md` — 仓库内沙箱概念文档入口。适用于：快速确认沙箱类型和能力矩阵。
- `codex-rs/execpolicy/src/` — 执行策略引擎源码。适用于：理解 Allow/Prompt/Forbidden 三态决策和规则匹配算法。
- `codex-rs/sandboxing/src/manager.rs` — 沙箱管理器核心。适用于：理解 `select_initial()` 和 `transform()` 的沙箱类型选择逻辑。
- `codex-rs/sandboxing/src/policy_transforms.rs` — 权限策略转换层。适用于：理解 `effective_permission_profile()` 如何合并 base profile 和 additional permissions。
- `codex-rs/core/src/config/permissions.rs` — 权限 profile 编译引擎。适用于：理解 TOML 配置如何编译为运行时 `FileSystemSandboxPolicy`。
- `codex-rs/config/src/permissions_toml.rs` — TOML 权限配置解析与 profile 继承。适用于：理解 `extends` 链继承和合并语义。

## 智慧（社区）

- [OpenAI Codex GitHub Discussions](https://github.com/openai/codex/discussions) — Codex 社区讨论区，适用于：安全配置、沙箱策略的实践经验交流。
- [r/rust](https://reddit.com/r/rust) — Rust 社区，适用于：Landlock、Seatbelt 等底层沙箱技术的一般性讨论。

## 空白

- 目前缺乏系统性的 Codex 安全架构深度解析文章或第三方教程。本课程的目标之一就是填补这一空白。
- 平台沙箱（Seatbelt/Seccomp）与 Codex 权限模型的交互细节在第三方文档中尚不存在，需直接从源码分析。

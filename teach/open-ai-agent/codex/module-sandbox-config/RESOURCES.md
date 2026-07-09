# Sandbox、权限与配置系统资源

## 知识

- [Codex 源码：`docs/config.md`](../../../../open-ai-agent/codex/docs/config.md)
  本地配置文档入口，指向基础、进阶和完整配置参考。适用于确认用户可见配置项的官方说明边界。
- [Codex 源码：`docs/sandbox.md`](../../../../open-ai-agent/codex/docs/sandbox.md)
  本地 sandbox 与 approvals 文档入口。适用于把源码概念映射到用户文档术语。
- [Codex 源码：`codex-rs/config/src/config_toml.rs`](../../../../open-ai-agent/codex/codex-rs/config/src/config_toml.rs)
  `ConfigToml` schema 定义，适用于查找 `sandbox_mode`、`sandbox_workspace_write`、`default_permissions` 与 `[permissions]` 的 TOML 入口。
- [Codex 源码：`codex-rs/config/src/permissions_toml.rs`](../../../../open-ai-agent/codex/codex-rs/config/src/permissions_toml.rs)
  用户自定义 permission profile 的 TOML 结构和继承解析。适用于理解 profile 的文件系统、网络和 workspace roots 写法。
- [Codex 源码：`codex-rs/core/src/config/mod.rs`](../../../../open-ai-agent/codex/codex-rs/core/src/config/mod.rs)
  运行态 `Config` 与 `Permissions` 组装入口。适用于追踪配置层、requirements、trust 与 profile 选择如何汇合。
- [Codex 源码：`codex-rs/core/src/config/permissions.rs`](../../../../open-ai-agent/codex/codex-rs/core/src/config/permissions.rs)
  权限 profile 编译器。适用于从 TOML profile 跳到 `FileSystemSandboxPolicy` 与 `NetworkSandboxPolicy`。
- [Codex 源码：`codex-rs/sandboxing/src/manager.rs`](../../../../open-ai-agent/codex/codex-rs/sandboxing/src/manager.rs)
  sandbox 执行前的统一分派层。适用于理解平台选择、附加权限、managed network 和最终 `SandboxExecRequest`。
- [Codex 源码：`codex-rs/linux-sandbox/README.md`](../../../../open-ai-agent/codex/codex-rs/linux-sandbox/README.md)
  Linux sandbox 行为说明。适用于确认 bubblewrap、legacy Landlock、网络隔离和 glob deny 的实现策略。
- [Codex 源码：`codex-rs/execpolicy/README.md`](../../../../open-ai-agent/codex/codex-rs/execpolicy/README.md)
  execpolicy 规则语言概览。适用于区分“命令前缀策略”与“文件/网络 sandbox 权限”。

## 智慧（社区）

- Codex 仓库 issue / PR 讨论
  适用于验证 sandbox 行为变更是否符合维护者语境，尤其是平台差异和安全边界问题。
- Rust crate 单元测试与集成测试
  适用于用真实测试案例校验理解，例如 `manager_tests.rs`、`permissions_tests.rs`、Linux/Windows sandbox tests。

## 空白

- 本主题未额外检索在线官方文档全文；当前产物以仓库源码和本地文档入口为准。
- Windows sandbox 的底层 ACL、WFP、防火墙与 elevated IPC 细节需要后续 L2/L3 专题拆分。

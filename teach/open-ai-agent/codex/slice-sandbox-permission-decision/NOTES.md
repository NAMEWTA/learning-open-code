# 教学笔记：Sandbox 权限决策链路

## 课程设计决策

- 采用垂直切片方式，追踪一条完整的工具调用→沙箱创建链路，而非按模块拆解
- 第 1 节课（flow-map）侧重全局视图和时序理解，第 2 节课（main-path）侧重代码级追踪
- 参考文档提供决策树、数据结构和异常路径的速查表，便于后续查阅

## 源文件引用

课程覆盖以下核心源文件：
- `codex-rs/execpolicy/src/decision.rs` — Decision 枚举
- `codex-rs/execpolicy/src/policy.rs` — Policy::check() 匹配逻辑
- `codex-rs/core/src/config/permissions.rs` — 权限编译和内置 profile
- `codex-rs/config/src/permissions_toml.rs` — TOML 解析和 extends 继承
- `codex-rs/sandboxing/src/manager.rs` — select_initial + transform
- `codex-rs/sandboxing/src/policy_transforms.rs` — effective_permission_profile
- `codex-rs/protocol/src/permissions.rs` — FileSystemSandboxPolicy 和决策树实现
- `codex-rs/protocol/src/config_types.rs` — SandboxMode, WindowsSandboxLevel 等配置类型
- `docs/sandbox.md` — 沙箱概念文档入口

## 待补充

- 目前参考文档中异常路径仅列出对照表，可在了解具体平台沙箱实现后补充详细分析
- 如用户有特定平台（Windows/Linux）的沙箱调试需求，可增加平台专项短期课程

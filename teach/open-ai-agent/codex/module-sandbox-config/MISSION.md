# 使命：Sandbox、权限与配置系统

## 为什么
本主题帮助学习者快速建立 Codex 配置、权限 profile 与平台 sandbox 的因果链路。完成后，学习者应能在阅读或改动执行权限相关代码时，判断某个 TOML 配置最终会怎样影响命令执行边界。

## 成功的样子
- 能说清 `sandbox_mode`、`default_permissions`、`[permissions]` 与 `approval_policy` 各自负责什么。
- 能沿着“配置加载 → 权限编译 → sandbox transform → 平台执行”找到关键源码入口。
- 能识别内置 profile、用户自定义 profile、requirements 约束与运行时附加权限之间的关系。

## 约束条件
- L1 主题只做模块级导览，不展开所有平台 sandbox 的系统调用细节。
- lesson 必须是 15 分钟短课；完整清单和源码阅读顺序放入 reference。
- 只基于当前 `open-ai-agent/codex/` 源码快照，不修改源项目。

## 不在范围内
- 不讲模型 provider、MCP、hooks、登录认证等非权限主线配置。
- 不做 macOS Seatbelt、Linux bubblewrap/seccomp、Windows restricted token 的逐行实现课。
- 不覆盖 `execpolicy` 规则语言的完整语法，只说明它在权限系统旁边的位置。

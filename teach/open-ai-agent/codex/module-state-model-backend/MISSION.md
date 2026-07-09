# 使命：状态、模型提供商与后端通信

## 为什么
用户需要理解 Codex 如何连接到 OpenAI API、管理认证令牌、持久化会话状态到 SQLite、以及通过特性 rollout 控制功能发布。这 10 个 crate 构成了 Codex 与外部世界交互的底层基础——没有它们，CLI 无法登录、模型无法调用、会话无法恢复、云端配置无法拉取。

## 成功的样子
- 能画出从 `codex login` 到令牌持久化再到底层 API 调用的数据流图。
- 能区分 `codex-state`（SQLite 状态持久化）、`codex-thread-store`（Thread CRUD 存储接口）、`codex-rollout`（会话文件发现与索引）三者的职责边界。
- 能说出 `ModelProvider` trait 的核心交互方法（info、auth、account_state、api_provider、api_auth、api_auth_for_scope、models_manager 等 8 个），以及 `ModelProviderInfo` 如何从 `config.toml` 合并到内置默认 provider。
- 能按推荐顺序进入各个 crate 的源码阅读，不被 30+ 源文件淹没。

## 约束条件
- 本主题是 L1 模块导览，短课控制在 15 分钟内完成。
- 只写入 `teach/open-ai-agent/codex/module-state-model-backend/`，不修改源项目和其他主题目录。
- 课程必须链接 L0 总览，并把长清单分流到 reference。

## 不在范围内
- 不讲 Bazel/CI/发布流水线（属于 L1-module-build-release）。
- 不讲 CLI/TUI 用户交互细节或 app-server JSON-RPC 协议（已有独立主题）。
- 不深入 rollout-trace reducer 的时序归约细节。

# 状态、模型提供商与后端通信 资源

## 知识

- [codex-rs/state/Cargo.toml](../../../../open-ai-agent/codex/codex-rs/state/Cargo.toml)
  SQLite 状态 crate 依赖清单（sqlx、libsqlite3-sys、uuid）。适用于确认持久化层的依赖边界。
- [codex-rs/state/src/lib.rs](../../../../open-ai-agent/codex/codex-rs/state/src/lib.rs)
  StateRuntime、LogEntry、ThreadMetadata、GoalStore 等 public API 导出面。适用于判断 state crate 对外承诺的接口。
- [codex-rs/state/src/log_db.rs](../../../../open-ai-agent/codex/codex-rs/state/src/log_db.rs)
  核心 SQLite 查询和 schema 操作。适用于理解 rollout metadata 如何写入和查询。
- [codex-rs/state/src/runtime/](../../../../open-ai-agent/codex/codex-rs/state/src/runtime/)
  threads.rs、goals.rs、memories.rs、logs.rs——StateRuntime 的子模块实现。适用于理解不同数据域的读写接口。
- [codex-rs/thread-store/Cargo.toml](../../../../open-ai-agent/codex/codex-rs/thread-store/Cargo.toml)
  Thread 存储 crate 依赖清单（codex-state、codex-rollout、codex-protocol）。适用于确认存储层依赖链。
- [codex-rs/thread-store/src/store.rs](../../../../open-ai-agent/codex/codex-rs/thread-store/src/store.rs)
  ThreadStore trait 定义——create/resume/append/flush/shutdown/read/list/search/archive/delete。适用于理解存储抽象的全套操作。
- [codex-rs/thread-store/src/local/](../../../../open-ai-agent/codex/codex-rs/thread-store/src/local/)
  LocalThreadStore 实现——基于本地文件系统的 create/read/list/search/archive/delete。适用于追踪 Thread CRUD 的具体实现。
- [codex-rs/rollout/Cargo.toml](../../../../open-ai-agent/codex/codex-rs/rollout/Cargo.toml)
  Rollout 持久化 crate 依赖清单。适用于确认 rollout 层依赖边界。
- [codex-rs/rollout/src/lib.rs](../../../../open-ai-agent/codex/codex-rs/rollout/src/lib.rs)
  RolloutRecorder、ThreadsPage、RolloutConfig、search 等 public API 导出面。适用于确认 rollout 层的公共接口。
- [codex-rs/rollout/src/recorder.rs](../../../../open-ai-agent/codex/codex-rs/rollout/src/recorder.rs)
  RolloutRecorder 实现——将 rollout item 追加到文件。适用于理解 session 持久化的写入路径。
- [codex-rs/rollout/src/list.rs](../../../../open-ai-agent/codex/codex-rs/rollout/src/list.rs)
  Thread 列表读取、游标分页、路径查找。适用于理解如何发现和列出已有 session。
- [codex-rs/rollout/src/search.rs](../../../../open-ai-agent/codex/codex-rs/rollout/src/search.rs)
  Rollout 文件全文搜索。适用于理解 session 内容检索机制。
- [codex-rs/rollout-trace/src/lib.rs](../../../../open-ai-agent/codex/codex-rs/rollout-trace/src/lib.rs)
  TraceWriter、RawTraceEvent、replay_bundle 等 trace 记录 public API。适用于理解 rollout trace bundle 的写入与回放。
- [codex-rs/model-provider/Cargo.toml](../../../../open-ai-agent/codex/codex-rs/model-provider/Cargo.toml)
  模型提供商 crate 依赖清单（codex-api、codex-login、codex-model-provider-info）。适用于确认 provider 层依赖。
- [codex-rs/model-provider/src/provider.rs](../../../../open-ai-agent/codex/codex-rs/model-provider/src/provider.rs)
  ModelProvider trait 定义和 ConfiguredModelProvider 实现。适用于理解 provider 抽象的核心方法和运行时行为。
- [codex-rs/model-provider/src/auth.rs](../../../../open-ai-agent/codex/codex-rs/model-provider/src/auth.rs)
  ProviderAuthScope、ResolvedProviderAuth、resolve_provider_auth——provider 认证解析逻辑。适用于理解认证如何从 AuthManager 流转到 HTTP 请求。
- [codex-rs/model-provider-info/src/lib.rs](../../../../open-ai-agent/codex/codex-rs/model-provider-info/src/lib.rs)
  ModelProviderInfo 定义——name、base_url、env_key、auth、wire_api、重试配置等。适用于理解 provider 的配置结构和验证逻辑。
- [codex-rs/backend-client/Cargo.toml](../../../../open-ai-agent/codex/codex-rs/backend-client/Cargo.toml)
  后端 API 客户端 crate 依赖清单（reqwest、codex-backend-openapi-models）。适用于确认 HTTP 客户端依赖。
- [codex-rs/backend-client/src/client.rs](../../../../open-ai-agent/codex/codex-rs/backend-client/src/client.rs)
  Client 实现——accounts、config、rate limits、task 等 API 调用。适用于理解后端 REST API 的调用封装。
- [codex-rs/login/Cargo.toml](../../../../open-ai-agent/codex/codex-rs/login/Cargo.toml)
  登录认证 crate 依赖清单（tiny_http、webbrowser、sha2、pkce）。适用于确认登录层的依赖。
- [codex-rs/login/src/lib.rs](../../../../open-ai-agent/codex/codex-rs/login/src/lib.rs)
  AuthManager、DeviceCode、LoginServer、TokenData 等 public API。适用于理解登录模块的对外接口。
- [codex-rs/login/src/device_code_auth.rs](../../../../open-ai-agent/codex/codex-rs/login/src/device_code_auth.rs)
  OAuth 设备码流程实现——request_device_code、complete_device_code_login。适用于理解 CLI 登录的核心流程。
- [codex-rs/login/src/auth/manager.rs](../../../../open-ai-agent/codex/codex-rs/login/src/auth/manager.rs)
  AuthManager 实现——令牌缓存、刷新、过期检测、多认证方式路由。适用于理解认证状态机的完整逻辑。
- [codex-rs/keyring-store/src/lib.rs](../../../../open-ai-agent/codex/codex-rs/keyring-store/src/lib.rs)
  KeyringStore trait 和 DefaultKeyringStore 实现——平台密钥链（macOS Keychain / Windows Credential Manager / Linux secret-service）。适用于理解令牌的安全存储。
- [codex-rs/cloud-config/src/lib.rs](../../../../open-ai-agent/codex/codex-rs/cloud-config/src/lib.rs)
  云端配置 crate public API——cloud_config_bundle_loader。适用于理解云端配置的拉取入口。
- [codex-rs/cloud-config/src/service.rs](../../../../open-ai-agent/codex/codex-rs/cloud-config/src/service.rs)
  CloudConfigService——配置拉取、缓存、刷新调度。适用于理解云端配置的完整生命周期。
- [codex-rs/cloud-config/src/cache.rs](../../../../open-ai-agent/codex/codex-rs/cloud-config/src/cache.rs)
  云端配置本地缓存实现。适用于理解配置的离线可用性设计。

## 智慧（社区）

- [Codex GitHub Issues](https://github.com/openai/codex/issues)
  用户反馈、认证问题、provider 配置问题和功能请求的聚集地。适用于验证学习结论是否与真实使用场景对齐。
- [Codex GitHub Discussions](https://github.com/openai/codex/discussions)
  社区讨论区，包含 provider 配置示例、第三方 provider 集成经验分享。

## 空白

- 当前主题仅基于仓库内 Rust 源码和 Cargo 依赖；OpenAI 后端 API 的 HTTP 协议细节、速率限制策略和令牌刷新机制的实际行为可能落后于源码注释，需要后续通过 API 文档或运行时抓包验证。
- keyring-store 的跨平台行为差异（尤其是 Linux secret-service 和 FreeBSD sync-secret-service）缺少官方文档覆盖，需参考 keyring crate 的源码和平台测试。

# 会话 resume/fork/archive 持久化链路 资源

## 知识

### 源码入口
- [ThreadStore trait 定义](https://github.com/anthropics/claude-code/blob/main/codex-rs/thread-store/src/store.rs) — 存储中立的所有线程持久化操作接口，含 create/resume/append/persist/archive/delete
- [Session rollout_reconstruction](https://github.com/anthropics/claude-code/blob/main/codex-rs/core/src/session/rollout_reconstruction.rs) — 从 JSONL rollout 反向扫描重建 Session 历史的核心算法
- [StateRuntime 初始化与 SQLite 管理](https://github.com/anthropics/claude-code/blob/main/codex-rs/state/src/runtime.rs) — 4 个 SQLite 数据库的打开、迁移、backfill 协调
- [thread_processor.rs - thread_fork / thread_archive](https://github.com/anthropics/claude-code/blob/main/codex-rs/app-server/src/request_processors/thread_processor.rs) — app-server 侧 fork 和 archive 的 RPC 处理器
- [thread_lifecycle.rs - 线程监听器与卸载](https://github.com/anthropics/claude-code/blob/main/codex-rs/app-server/src/request_processors/thread_lifecycle.rs) — 线程生命周期的监听器附加、热 resume、30 分钟空闲卸载
- [rollout crate - session_index.rs](https://github.com/anthropics/claude-code/blob/main/codex-rs/rollout/src/session_index.rs) — 会话名到 thread_id 的索引映射

### 官方文档
- [Codex AGENTS.md](https://github.com/anthropics/claude-code/blob/main/AGENTS.md) — Codex 项目自身的 AI 协作指南，含模块地图

### 测试目录
- `codex-rs/rollout/src/tests.rs` — rollout 持久化集成测试
- `codex-rs/rollout/src/recorder_tests.rs` — RolloutRecorder 单元测试

## 智慧（社区）

- [Claude Code Discord](https://discord.gg/anthropic) — Claude Code 用户社区，可讨论会话管理和持久化问题
- [Anthropic Developer Forum](https://community.anthropic.com/) — Anthropic 官方开发者论坛

## 空白

- rollout JSONL 格式的完整文档目前仅存在于 `codex_protocol` 的 Rust 类型定义中，尚无独立的设计文档
- ThreadStore trait 的不同实现（如 file-based vs SQLite-based）没有公开的对比文档
- backfill 的重试和失败恢复策略在代码中较分散，缺乏集中说明

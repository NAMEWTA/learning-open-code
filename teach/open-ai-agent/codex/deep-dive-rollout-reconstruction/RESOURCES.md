# Rollout JSONL 反向扫描重建 资源

## 知识

### 源码入口（核心）
- `codex-rs/core/src/session/rollout_reconstruction.rs` — 反向扫描算法主实现（460 行），包含 `reconstruct_history_from_rollout`、`ActiveReplaySegment`、`finalize_active_segment`、三条件提前终止逻辑
- `codex-rs/rollout/src/recorder.rs` — JSONL 写入端（1973 行），包含 `RolloutRecorder` 的 append-only 写入模型、`load_rollout_items` 正向读取、`RolloutWriterState` 缓冲与恢复机制
- `codex-rs/state/src/runtime/backfill.rs` — SQLite backfill 状态机（279 行），包含 `try_claim_backfill` 租约机制、`checkpoint_backfill` 增量水印

### 测试文件
- `codex-rs/core/src/session/rollout_reconstruction_tests.rs` — 反向扫描算法的单元测试，覆盖 turn 段边界、compaction 窗口、rollback 跳过等场景
- `codex-rs/rollout/src/recorder_tests.rs` — RolloutRecorder 的集成测试

### 协议定义
- `codex-rs/protocol/src/protocol.rs` — `RolloutItem` 枚举定义（ResponseItem、EventMsg、Compacted、TurnContext、WorldState、SessionMeta 等变体）

### 官方文档
- [Codex AGENTS.md](https://github.com/anthropics/codex/blob/main/AGENTS.md) — Codex 项目整体架构与模块职责说明
- [Codex README](https://github.com/anthropics/codex/blob/main/README.md) — 项目概览与快速开始

## 智慧（社区）

- [Anthropic Codex GitHub Discussions](https://github.com/anthropics/codex/discussions) — Codex 官方讨论区，可提问架构设计问题
- [Claude Code Discord](https://discord.gg/anthropic) — Anthropic 开发者社区，包含 Codex 用户交流频道

## 空白

- 暂无关于 JSONL vs WAL-based SQLite 在 append-only 场景下的业界基准测试对比资料
- 暂无 Codex 团队关于"为什么选择 JSONL 而非嵌入式数据库做热路径"的官方设计文档或博客
- Rust `enumerate().rev()` 在大 rollout（10 万+行）下的性能 profile 数据未公开

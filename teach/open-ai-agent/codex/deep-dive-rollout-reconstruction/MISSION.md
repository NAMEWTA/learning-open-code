# 使命：Rollout JSONL 反向扫描重建 Session 算法

## 为什么
理解 Codex 如何在进程重启后从 append-only JSONL 日志中精确重建完整会话状态，掌握反向扫描算法的设计权衡——这是理解 Codex 持久化架构"为什么不用数据库做热路径"的关键拼图。

## 成功的样子
- 能画出 `reconstruct_history_from_rollout` 的反向扫描流程图，解释三条件提前终止的触发时机
- 能对比 JSONL append-only 写入与 SQLite 查询两种策略在 resume 场景下的性能差异
- 能指出该算法在当前实现中的已知局限（legacy compaction 双循环、全量 eager load）及改进方向

## 约束条件
- 前置知识：已完成 L2 slice-session-resume-fork 课程，理解冷 Resume 的三种路径
- 单课 15 分钟，共 2 节课 + 1 份参考文档
- 仅覆盖 `codex-rs/core`、`codex-rs/rollout`、`codex-rs/state` 三个 crate

## 不在范围内
- SQLite backfill 的完整实现细节（属于 L3 state-model-backend 模块）
- Fork/Archive 路径的 RolloutItem 处理（已在 L2 覆盖）
- TUI/App-server 层的 resume 触发逻辑

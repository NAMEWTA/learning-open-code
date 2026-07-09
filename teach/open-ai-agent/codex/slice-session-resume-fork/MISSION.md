# 使命：会话 resume/fork/archive 的持久化链路

## 为什么
理解 Codex 如何将一次对话会话从内存中的 Thread 对象，持久化到磁盘上的 JSONL rollout 文件和 SQLite 数据库，并在后续重启时从持久化存储中完整恢复（resume）、分支复制（fork）和归档（archive）。掌握这条链路后，就能定位会话持久化中任何环节的问题——无论是 rollout 文件损坏导致无法恢复、fork 时历史截断不正确，还是 archive 操作半途失败的数据一致性问题。

## 成功的样子
- 能画出从用户启动到 session 发现/创建、rollout JSONL 写入、SQLite backfill 的完整持久化时序图
- 能说出 ThreadStore trait 的 5 个核心方法（create/resume/append/persist/archive）及其职责
- 能解释 Session::reconstruct_history_from_rollout() 的反向扫描算法和 RolloutReconstruction 输出
- 能分析 resume 时 session 不存在、fork 冲突、archive 失败回滚三条异常路径的代码位置和处理逻辑

## 约束条件
- 学习者已通过 L1-module-state-model-backend 了解 StateRuntime（SQLite 4 库）、ThreadStore trait、rollout JSONL 日志
- 学习者已通过 L1-module-core-runtime 了解 Session 生命周期和 turn 模型
- 单节课不超过 15 分钟阅读量

## 不在范围内
- ThreadStore 的具体 SQLite 实现细节（属于 L1-module-state-model-backend）
- rollout compression 的 zstd 压缩策略（属于 rollout crate 内部优化）
- app-server 的 WebSocket/JSON-RPC 传输层细节
- ephemeral session 的内存管理模式

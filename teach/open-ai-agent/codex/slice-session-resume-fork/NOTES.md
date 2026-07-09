# 教学笔记：会话 resume/fork/archive 的持久化链路

## 教学要点

- ThreadStore trait 是理解整个持久化链路的"钥匙"——先讲清楚 trait 的每个方法职责，再展开具体实现
- reconstruct_history_from_rollout() 是核心难点：反向扫描算法需要画图辅助理解
- archive 的子树归档（含 spawned descendants）是一个容易被忽略的细节

## 待办

- 后续可增加第 4 节课：rollout compression 对 resume 性能的影响

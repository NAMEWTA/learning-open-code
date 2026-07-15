# 教学笔记：定时任务调度

## 用户偏好

- 以架构理解为主，不要求逐行阅读源码
- 关注"为什么这么设计"而非"怎么写代码"

## 关键强调点

- cron 是 per-profile 隔离的（#4707），每个 profile 的 jobs.json 互不干扰
- scheduler_provider 的 Axis B 设计是有意的——触发和执行的分离
- deliver=origin 的回退链路是常见疑惑点：没有 origin 时依次尝试各平台 home channel
- [SILENT] 标记机制：agent 输出此标记则抑制投递，但仍保存到本地 output
- lifecycle_guard 是多层防线之一：创建时阻断 + 执行时 terminal_tool 阻断

## 待办

- 后续可拆课：0002-cron-scheduler-tick-deep-dive.html（tick 函数的锁机制、并行池、读写锁）
- 后续可拆课：0003-multi-platform-delivery.html（19+ 平台的投递适配和 mirror 机制）

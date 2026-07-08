# 使命：parallel 与 chain execution 全链路

## 为什么
在 pi-subagents 里，一次 `tasks` 并行调用和一条 `chain` 链式调用都会启动多个 child agent，但编排语义、输出传递和失败语义完全不同。要调试「并行没跑满」「链式 `{previous}` 断了」「dynamic fanout 没展开」，必须能从前台入口一路指到 `executeChain`、动态扇出和 workflow graph。

## 成功的样子
- 能区分 top-level parallel（`tasks`）与 chain 内 parallel step（`chain[].parallel`）的入口与聚合方式
- 能按顺序说出 `executeChain` 对 sequential、static parallel、dynamic fanout 三种 step 的分支
- 能解释 `prev` / `outputs` / `aggregateParallelOutputs` 如何在步骤间传递上下文
- 能读懂 `details.workflowGraph` 节点树与 integration 测试的断言含义

## 约束条件
- 以 foreground chain 为主路径，不展开 async chain 后台 runner
- 单节课 15 分钟内完成，长表与文件索引查 reference 速查页

## 不在范围内
- 单次 foreground `runSync` 细节（见 `slice-single-foreground-run`）
- async 生命周期与 wait/status（见 `slice-async-lifecycle-status-wait`）
- worktree、acceptance、intercom detach 的完整分支（本切片仅标注分叉点）

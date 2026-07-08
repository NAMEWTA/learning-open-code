# 使命：goal 续跑机制的设计权衡

## 为什么
L2 切片已经讲清「链路怎么走」，但要真正调试「为何空转续跑」或「为何该续却不续」，必须理解 worker + evaluator 这套设计为何长成现在这样——备选方案是什么、`progress_key` 为何用 SHA256、三次重读 checkpoint 防什么竞态。

## 成功的样子
- 能对比至少两种续跑架构（worker 内隐式环 vs 外部调度）并说明 deer-flow 的取舍
- 能逐步复述 `_prepare_goal_continuation_input` 的决策树与每道守卫的成本
- 能列出已知局限（LLM evaluator 不可复现、证据仅可见对话等）及合理改进方向

## 约束条件
- L4 深度剖析：基于 L2 `slice-goal-continuation` 已建立的链路认知
- 拆成两节短课 + 参考笔记页

## 不在范围内
- 修改 deer-flow 源码或调 evaluator prompt
- 前端 goal UI 与 TUI `/goal` 交互细节

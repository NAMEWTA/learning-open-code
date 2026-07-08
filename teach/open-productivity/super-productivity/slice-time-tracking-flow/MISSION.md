# 使命：开始追踪、空闲检测与时间记录全链路

## 为什么
用户需要能从一次“开始/停止追踪”的交互一路追到 Super Productivity 的任务耗时、work context 起止时间、idle 修正、focus/break 规则、metric 记录和 op-log 持久化。掌握这条链路后，可以定位时间丢失、重复计时、跨端同步缺口和 focus mode 联动异常。

## 成功的样子
- 能画出从任务行按钮到 `task.timeSpent`、`timeTracking`、`metric`、`SUP_OPS` 的状态流。
- 能判断某个动作是只更新本地 UI 状态，还是会生成可同步的 persistent operation。
- 能解释 idle dialog 为什么先扣回已误记时间，再按用户选择把时间记到任务或 break。
- 能列出后续 L3/L4 需要深挖的 reducer、effect、service 和持久化边界。

## 约束条件
- 本主题是 L2 垂直切片，只讲端到端主链路和关键分叉；逐函数证明留给 L3/L4。
- 只写入 `teach/open-productivity/super-productivity/slice-time-tracking-flow/`。
- 源码引用尽量使用完整相对路径，减少裸函数名导致的快照污染。

## 不在范围内
- 不展开 Android/iOS 原生 foreground service 的完整实现，只标出它们与本链路的交接点。
- 不讲整个 op-log sync 冲突解决体系，只讲时间追踪相关 action 如何进入本地 op-log。
- 不讲 UI 视觉细节和翻译文案。

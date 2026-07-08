# 使命：Focus session、break、metric 与当前任务追踪联动全链路

## 为什么
用户需要把「专注计时」和「任务时间追踪」当成两条会互相拉扯的状态线来读，而不是两个独立功能。Pomodoro 完成后的 break、Flowtime 手动结束、idle 弹窗、追踪按钮的 play/pause 都会同时影响 `focusMode.timer`、`task.currentTaskId` 和每日 `metric.focusSessions`。掌握这条 L2 链路后，排查「专注结束了但还在计时」「休息期间误启动下一 session」「focus session 没进指标」等问题时，不会只盯 UI 或只盯 reducer。

## 成功的样子
- 能画出 UI / effect → focus state → time-tracking → task / metric 的主路径，并指出双向同步的 effect 名称。
- 能区分 `focusMode.timer`（本地 UI 计时器）、`task.currentTaskId`（本地追踪指针）和 `metric.focusSessions`（可同步的日汇总）各自保存什么。
- 能判断 Pomodoro 自动 break、Flowtime 手动结束、追踪停止、idle 弹窗分别会 dispatch 哪些 action。
- 能说清 `completeFocusSession` 何时写 metric，以及 `isPauseTrackingDuringBreak` 如何改变 break 前后的 current task 行为。

## 约束条件
- 本主题是 L2 垂直切片，只讲主路径和关键分叉；tick 音效、Electron taskbar、Android 前台服务等平台细节留给 L3/L4。
- 只写入 `teach/open-productivity/super-productivity/slice-focus-mode-flow/`。
- 课程中必须保持三层分离：focus timer state、current task tracking、metric 日记录。
- 源码引用使用完整相对路径，便于快照追踪。

## 不在范围内
- 不展开 time-tracking 的 op-log flush、batch accumulator 与 work context 分钟取整（见 `slice-time-tracking-flow`）。
- 不覆盖 focus overlay 全部屏幕导航、准备动画与 Android native restore 细节。
- 不讲 metric 图表渲染、简单计数器统计与每日反思表单。

# 使命：项目完成、任务归档与工作上下文收尾全链路

## 为什么
用户需要能从 Super Productivity 的“Complete Project”菜单一路追到未完成任务处理、项目 done/archived 标志、任务移动或归档、history/worklog 输出和工作上下文切换。掌握这条链路后，可以判断项目收尾相关 bug 应该落在 dialog、service、task/archive、worklog、work-context 还是 op-log 边界。

## 成功的样子
- 能画出项目完成入口、未完成任务处理、确认、完成标志、导航和庆祝弹窗的顺序。
- 能判断“完成项目”“移动未完成任务到 Inbox”“标记任务完成”“任务归档”“删除项目”分别会改哪些状态。
- 能解释为什么项目完成不是单个 reducer action，而是 dialog、service、task/archive、worklog 和 work-context 的组合流程。
- 能指出后续 L3/L4 深挖目标，包括 completion info、archive flush、worklog 映射和 op-log archive 边界。

## 约束条件
- 本主题是 L2 垂直切片，只讲主链路和关键分叉；逐函数证明留给 L3/L4。
- 只写入 `teach/open-productivity/super-productivity/slice-project-completion-flow/`。
- 与 `module-task-domain`、`module-planning-time` 和 `slice-time-tracking-flow` 保持交叉链接。

## 不在范围内
- 不展开完整 op-log sync 冲突解决，只标出哪些 action 具备 persistent meta。
- 不讲 Plainspace sharing、项目复制、项目主题视觉实现的完整细节。
- 不把每日 Daily Summary 的任务归档机制误写成项目完成本身。

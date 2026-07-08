# 使命：任务计划到日程渲染的 Planner 与 Schedule 投影全链路

## 为什么
用户需要能从一次“把任务安排到某天或某个时间”的操作一路追到 Super Productivity 的任务字段、Planner state、Schedule 投影和最终 UI。掌握这条 L2 链路后，排查任务出现在错误日期、定时任务重复、重复任务投影重叠、日历块挤占时间等问题时，不会把持久状态和只读视图条目混成一层。

## 成功的样子
- 能判断一次拖拽、弹窗提交或新增任务会写入 `task.dueDay`、`task.dueWithTime`、`planner.days` 还是 `TODAY_TAG.taskIds`。
- 能区分 scheduled task、due-only task、repeat projection、calendar block 和 Schedule view entry 的数据边界。
- 能沿着 selectors 和 mapper 找到 Planner 列表、Schedule 周视图、Planner scheduled 区的首查文件。
- 能说清 `planner-shared.reducer.ts` 与 `task-shared-scheduling.reducer.ts` 分别维护哪类跨实体一致性。

## 约束条件
- 本主题是 L2 垂直切片，只讲主路径和关键分叉；逐函数证明、复杂拖拽边界和历史 bug 回归留给 L3/L4。
- 只写入 `teach/open-productivity/super-productivity/slice-planner-schedule-flow/`。
- 课程中必须保持四层分离：Planner state、Task due 字段、Schedule view entries、calendar integration。
- 源码引用使用完整相对路径，便于快照追踪。

## 不在范围内
- 不展开 op-log 冲突解决、LWW 回放和跨设备合并细节。
- 不覆盖完整 Calendar provider/plugin 写回协议，只标出 Schedule 读取与可移动事件交接点。
- 不讲每个 Planner/Schedule 组件的视觉样式和 i18n 文案。

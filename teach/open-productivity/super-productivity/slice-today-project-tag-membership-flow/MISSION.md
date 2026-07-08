# 使命：任务进入 Today、Project 与 Tag 视图的归属判定全链路

## 为什么
本主题用于帮助读码者在 super-productivity 中追查“任务为什么出现在这个视图，为什么没有出现在另一个视图”。掌握后，学习者能把一次任务 action 造成的字段变化，沿着 meta-reducer、selector、WorkContext 和 MenuTree 一路追到用户实际看到的列表。

## 成功的样子
- 能区分 Today 虚拟标签、普通 `tagIds`、`project.taskIds` 与 `dueDay/dueWithTime` 的职责。
- 能从一个任务对象判断它是否应出现在 Today、Project、Tag 主列表或导航菜单里。
- 能定位归属异常优先该读哪个源码文件，而不是在 UI 组件里盲搜。

## 约束条件
- 这是 L2 短课，lesson 必须在 15 分钟内完成。
- 只写入本主题目录，避免影响其他并行 worker 的输出。
- 课程使用简体中文，但源码标识符保持英文。

## 不在范围内
- 不展开完整新增任务 UI 表单流程；相关内容链接到 `slice-task-create-flow`。
- 不深入 op-log 冲突解决、issue provider 同步或 planner 全链路。
- 不把 Today 的排序列表当成普通标签成员关系讲解。

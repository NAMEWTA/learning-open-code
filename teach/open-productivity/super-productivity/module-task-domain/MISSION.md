# 使命：任务、项目、标签与工作上下文领域

## 为什么
用户希望能读懂 super-productivity 最核心的任务领域建模：任务如何归属到 Today、Project、Tag，状态如何经由 NgRx 与 meta-reducers 保持一致。掌握这部分后，后续分析时间追踪、同步、重复任务和提醒时能先判断“这是任务域规则，还是外部 feature 的附加行为”。

## 成功的样子
- 能用一句话解释任务域在整体架构中的职责和边界。
- 能从 UI 操作追踪到 Service、actions、reducers/selectors、meta-reducers 与 op-log capture。
- 能判断一个任务为什么出现在 Today、某个 Project 或某个 Tag 中，并指出相关源码入口。
- 能说出 `dueDay` / `dueWithTime` 互斥和 `TODAY_TAG` 虚拟标签这两个维护约束。

## 约束条件
- 本主题是 L1 模块总览，不做完整垂直切片。
- 每节 lesson 控制在 15 分钟内，长接口清单和表格放入 reference。
- 只写入 `teach/open-productivity/super-productivity/module-task-domain/`。

## 不在范围内
- 不展开完整同步协议、op-log 冲突解决和 SuperSync 服务端。
- 不深入每个任务 UI 组件、提醒弹窗、附件与短语法解析细节。
- 不覆盖 Planner、Schedule、Calendar、Issue Provider 的完整业务链路。

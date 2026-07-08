# 任务进入 Today、Project 与 Tag 视图的归属判定全链路资源

## 知识

- [源码：`src/app/features/work-context/store/work-context.selectors.ts`](../../../../open-productivity/super-productivity/src/app/features/work-context/store/work-context.selectors.ts)
  Today、Project、Tag active work context 的核心组装点。适用于：判断任务实际进入哪个工作视图。
- [源码：`src/app/features/tag/store/tag.reducer.ts`](../../../../open-productivity/super-productivity/src/app/features/tag/store/tag.reducer.ts)
  普通标签与 `TODAY_TAG` 的排序/成员计算差异。适用于：区分 `tag.taskIds` 与 `task.tagIds`。
- [源码：`src/app/root-store/meta/task-shared-meta-reducers/task-shared-crud.reducer.ts`](../../../../open-productivity/super-productivity/src/app/root-store/meta/task-shared-meta-reducers/task-shared-crud.reducer.ts)
  新增、更新、删除任务时 Project/Tag/Today 列表的维护。适用于：追查 action 写侧。
- [源码：`src/app/root-store/meta/task-shared-meta-reducers/task-shared-scheduling.reducer.ts`](../../../../open-productivity/super-productivity/src/app/root-store/meta/task-shared-meta-reducers/task-shared-scheduling.reducer.ts)
  `dueDay`、`dueWithTime` 与 Today 列表的互斥写入规则。适用于：排查 Today 归属。
- [源码：`src/app/root-store/meta/task-shared-meta-reducers/project-shared.reducer.ts`](../../../../open-productivity/super-productivity/src/app/root-store/meta/task-shared-meta-reducers/project-shared.reducer.ts)
  移动任务到其他 Project 和删除 Project 的跨状态维护。适用于：排查 Project 归属异常。
- [源码：`src/app/root-store/meta/task-shared-meta-reducers/tag-shared.reducer.ts`](../../../../open-productivity/super-productivity/src/app/root-store/meta/task-shared-meta-reducers/tag-shared.reducer.ts)
  删除 Tag、清理任务 `tagIds`、过滤陈旧 `taskIds`。适用于：排查 Tag 删除后的悬挂引用。
- [源码：`src/app/features/menu-tree/menu-tree.service.ts`](../../../../open-productivity/super-productivity/src/app/features/menu-tree/menu-tree.service.ts)
  Project/Tag 导航树水合、排序和缺失项追加。适用于：区分导航可见性和任务成员关系。
- [架构决策：`ARCHITECTURE-DECISIONS.md`](../../../../open-productivity/super-productivity/ARCHITECTURE-DECISIONS.md)
  `dueDay/dueWithTime` 互斥和 `TODAY_TAG` 虚拟标签模式的一手说明。适用于：解释设计原因。
- [L1：任务、项目、标签与工作上下文领域](../module-task-domain/reference/task-domain-overview.html)
  本主题的父级知识图谱。适用于：复习任务域入口和边界。
- [相关 L2：新增任务与短语法解析全链路](../slice-task-create-flow/reference/task-create-flow-reference.html)
  任务创建阶段如何写入归属字段。适用于：从输入解析回溯到本主题。

## 智慧（社区）

- 本地源码测试与评审：`src/app/features/work-context/store/work-context.selectors.spec.ts`、`src/app/features/tag/store/tag.reducer.spec.ts`、`src/app/features/menu-tree/store/menu-tree.selectors.spec.ts`
  这些测试比外部问答更贴近当前仓库行为。适用于：把课程中的判断点改写成回归测试。

## 空白

- 本次没有收录外部社区讨论。该主题依赖当前源码中的 NgRx selector 与 meta-reducer 不变量，外部资料容易落后于仓库实现。

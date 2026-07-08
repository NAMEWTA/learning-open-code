# 新增任务与短语法解析全链路资源

## 知识

- `src/app/features/tasks/add-task-bar/add-task-bar.component.ts`
  新增任务 UI 的核心入口。适用于追踪输入解析、提交、日期/提醒/重复配置组装。
- `src/app/features/tasks/add-task-bar/add-task-bar-parser.service.ts`
  UI 侧短语法解析到临时状态的适配层。适用于判断默认值、手动选择值和短语法值谁覆盖谁。
- `src/app/features/tasks/short-syntax.ts`
  短语法纯解析逻辑。适用于查 `+project`、`#tag`、`@due`、`!deadline`、估时、URL 附件规则。
- `src/app/features/tasks/task.service.ts`
  任务实体创建门面。适用于判断默认 project、Today 默认 dueDay、`TaskSharedActions.addTask` 派发。
- `src/app/root-store/meta/task-shared-meta-reducers/task-shared-crud.reducer.ts`
  新增主任务的跨实体写入位置。适用于查 task、project.taskIds、tag.taskIds、planner day 的一致性维护。
- `src/app/root-store/meta/task-shared-meta-reducers/short-syntax-shared.reducer.ts`
  非 UI 调用短语法后的原子更新边界。适用于查短语法如何一次性更新任务、项目、计划和标签。
- `src/app/op-log/capture/operation-log.effects.ts`
  persistent action 到 op-log operation 的写入链路。适用于判断哪些新增任务相关 action 会落入 `SUP_OPS`。
- `src/app/features/tasks/add-task-bar/add-task-bar-parser.service.spec.ts`
  UI 解析边界测试。适用于校验 deadline、URL 附件、默认值保留和移除短语法的行为。
- `src/app/features/tasks/store/short-syntax.effects.spec.ts`
  store effect 短语法测试。适用于校验 service/外部调用新增任务时的短语法后处理。

## 智慧（社区）

- Super Productivity 上游 Issues
  适用于验证任务新增、Today 归属、短语法解析、提醒和同步相关历史 bug 的真实使用场景。
- 本仓库相邻主题 `teach/open-productivity/super-productivity/module-task-domain/`
  适用于回看任务、项目、标签、工作上下文的 L1 模块总览。

## 空白

- 未纳入完整 Electron 主进程快捷键注册链路；本主题只追踪到 Angular 侧 `ShortcutService` 和 IPC 入口。
- 未纳入 op-log 远端 replay、冲突合并与 compaction 的完整深挖；这些应拆为 L3/L4 主题。

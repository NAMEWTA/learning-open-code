# 外部 Issue 拉取、映射与双向同步全链路 资源

## 知识

- 源码：`src/app/features/issue/store/poll-to-backlog.effects.ts`
  自动导入 backlog 的 effect 入口。适用于判断 provider 筛选条件、轮询模式和错误吞吐。
- 源码：`src/app/features/issue/issue.service.ts`
  issue 集成主编排服务。适用于追踪去重、provider 映射、创建任务、刷新已有 issue task。
- 源码：`src/app/features/issue/issue-service-interface.ts`
  provider 必须/可选能力接口。适用于确认哪些 provider 能拉新 issue、刷新任务、写回远端。
- 源码：`src/app/features/issue/providers/`
  内建 provider 实现。适用于比较 Jira、GitLab、OpenProject、Plainspace 等 provider 如何映射任务字段。
- 源码：`src/app/plugins/issue-provider/plugin-issue-provider-adapter.service.ts`
  plugin issue provider 适配到同一接口的桥。适用于理解 migrated/plugin provider 如何进入拉取与映射链路。
- 源码：`src/app/features/issue/two-way-sync/`
  双向同步 effect、adapter、决策函数与 sidecar。适用于定位本地任务更新如何写回 provider。
- 源码：`src/app/features/tasks/store/task.actions.ts`
  任务局部 action，尤其是 `addSubTask` 的持久化边界。适用于区分 task action 和 provider action。
- 源码：`src/app/root-store/meta/task-shared.actions.ts`
  `TaskSharedActions.addTask/updateTask/deleteTask/deleteTasks` 的 op-log 元数据。适用于判断哪些任务变化会持久化为操作。
- 测试：`src/app/features/issue/store/poll-to-backlog.effects.spec.ts`
  backlog 轮询条件与 transient error 后继续轮询的行为佐证。
- 测试：`src/app/features/issue/store/poll-issue-updates.effects.spec.ts`
  已有 issue task 更新轮询的上下文范围行为佐证。
- 测试：`src/app/features/issue/two-way-sync/compute-push-decisions.spec.ts`
  provider wins、no baseline、方向配置、互斥字段清理的决策佐证。
- 测试：`src/app/features/issue/two-way-sync/issue-two-way-sync.effects.spec.ts`
  push、delete、auto-create、sync bookkeeping 跳过等 effect 行为佐证。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/johannesjo/super-productivity/issues)
  适用于把同步异常、provider 行为差异和用户数据风险放回真实问题场景中验证。

## 空白

- 本主题未查 Jira、GitLab、OpenProject、CalDAV、Plainspace 的外部 API 文档；当前目标是解释 Super Productivity 内部链路和边界。
- 未覆盖完整 op-log 实现，后续可单独生成 L3/L4 主题补齐持久化与远端重放细节。

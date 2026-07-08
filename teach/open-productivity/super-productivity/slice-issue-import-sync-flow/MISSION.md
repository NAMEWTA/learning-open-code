# 使命：外部 Issue 拉取、映射与双向同步全链路

## 为什么
读者需要能在 Super Productivity 中定位外部 issue 集成的真实数据流：什么时候只是 provider 拉取或状态维护，什么时候才会创建、更新、删除本地任务，并在本地任务变化后写回远端。掌握这条链路后，可以更稳地排查重复导入、遗漏同步、误删远端 issue、op-log 负载过大等问题。

## 成功的样子
- 能从 provider 自动拉取入口追到 `IssueService.addTaskFromIssue` 与任务 action 落点。
- 能判断某个 action 是 provider 配置状态、任务状态、同步基线，还是远端写回副作用。
- 能解释双向同步为什么需要 baseline、为什么 provider changed 时跳过 push。
- 能根据故障现象快速跳到 effect、service、adapter、sidecar 或 reducer。

## 约束条件
- 本主题是 L2 垂直切片，第一节课必须在 15 分钟内完成。
- 源码路径在 SNAPSHOT 中使用源项目内相对路径，不带 `open-productivity/super-productivity/` 前缀。
- 只写入 `teach/open-productivity/super-productivity/slice-issue-import-sync-flow/`。

## 不在范围内
- 不展开每个 provider 的 HTTP API 细节。
- 不完整讲 op-log 系统实现，只讲 issue 同步链路触达的任务 action 边界。
- 不覆盖 issue provider 配置 UI 表单的全部字段。

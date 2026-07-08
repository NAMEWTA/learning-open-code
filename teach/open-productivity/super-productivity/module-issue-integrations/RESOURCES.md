# Issue Provider、日历集成与外部工作项资源

## 知识

- [L0 项目总览](../00-overview/reference/00-overview.html)
  用于复习 super-productivity 的整体功能、Angular renderer、NgRx、op-log、插件与 Electron 位置。
- [任务领域模块总览](../module-task-domain/reference/task-domain-overview.html)
  外部 issue 和 calendar event 最终都会映射为 `Task`，阅读本主题前需要先知道任务归属与 Today/Project/Tag 规则。
- [Operation Log 与同步模块参考](../module-op-log-sync/reference/op-log-sync-overview.html)
  判断 `IssueProviderActions`、任务更新、sidecar 和 provider 写回是否会进入持久化同步时使用。
- [`src/app/features/issue/issue.model.ts`](../../../../open-productivity/super-productivity/src/app/features/issue/issue.model.ts)
  issue provider key、配置实体、内置 provider、迁移到插件的 provider 和插件 key 的核心类型来源。
- [`src/app/features/issue/issue-service-interface.ts`](../../../../open-productivity/super-productivity/src/app/features/issue/issue-service-interface.ts)
  provider 必须实现的读、搜、导入、刷新、附件、subtask 与可选写回合同。
- [`src/app/features/issue/issue.service.ts`](../../../../open-productivity/super-productivity/src/app/features/issue/issue.service.ts)
  搜索、导入、刷新、外部 issue 到 `Task` 字段映射和 provider service map 的主入口。
- [`src/app/features/issue/store/poll-to-backlog.effects.ts`](../../../../open-productivity/super-productivity/src/app/features/issue/store/poll-to-backlog.effects.ts)
  自动拉取新 issue 到 backlog 的 effect，适合看 `isAutoAddToBacklog` 与 `pollingMode`。
- [`src/app/features/issue/store/poll-issue-updates.effects.ts`](../../../../open-productivity/super-productivity/src/app/features/issue/store/poll-issue-updates.effects.ts)
  已导入 issue task 的外部更新轮询入口，适合区分当前上下文轮询与 always 全局轮询。
- [`src/app/features/issue/two-way-sync/issue-two-way-sync.effects.ts`](../../../../open-productivity/super-productivity/src/app/features/issue/two-way-sync/issue-two-way-sync.effects.ts)
  本地任务字段推送回远端、自动创建远端 issue、删除远端 issue 的核心 effect。
- [`src/app/features/calendar-integration/`](../../../../open-productivity/super-productivity/src/app/features/calendar-integration/)
  iCal / 插件日历事件读取、banner、自动导入、隐藏事件和 time-block 写回的模块入口。
- [`electron/jira.ts`](../../../../open-productivity/super-productivity/electron/jira.ts)
  Electron 主进程侧 Jira 请求代理、自签名证书和附件图片 header 处理线索。

## 智慧（社区）

- [super-productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)
  适用于验证 issue provider、calendar、sync 相关 bug 的真实用户场景和维护者讨论。
- [super-productivity Discussions](https://github.com/super-productivity/super-productivity/discussions)
  适用于观察 provider 需求、插件化迁移和日历工作流的设计取舍。

## 空白

- 本主题暂不收录 Jira、GitLab、OpenProject、Redmine、CalDAV、Google Calendar 等第三方 API 官方文档；这些应在后续 L2 provider 切片中按具体 provider 补充。

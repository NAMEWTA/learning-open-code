# 使命：Issue Provider、日历集成与外部工作项

## 为什么
用户需要在 super-productivity 中快速判断外部 Jira、GitLab、CalDAV、Calendar、插件 provider 等工作项如何进入本地任务域，以及哪些变更由轮询、双向同步、日历导入或 Electron 辅助负责。掌握这个边界后，后续阅读单个 provider 或排查同步问题时不会把配置、导入、刷新和写回混在一起。

## 成功的样子
- 能说清 `IssueProvider` 配置实体、`IssueServiceInterface` provider 合同和 `IssueService.addTaskFromIssue()` 的分工。
- 能从 backlog 轮询、issue 更新轮询、two-way-sync、calendar/time-block 四条链路中选对阅读入口。
- 能解释为什么 GitHub、ClickUp、Gitea、Linear、Trello、Azure DevOps 现在属于插件形态，而不是当前内置 provider 实现。
- 能用参考文档定位某个 provider 的配置、API、映射、内容展示和特有 effects。

## 约束条件
- 本主题是 L1 模块总览，只建立边界和读法，不展开每个 provider 的完整 API 细节。
- lesson 必须是 15 分钟内可完成的短课，长 provider 清单和接口表放入 reference。
- 产出只写入 `teach/open-productivity/super-productivity/module-issue-integrations/`。

## 不在范围内
- 不逐行讲解 Jira、GitLab、CalDAV、OpenProject、Redmine 等具体 provider 的所有请求参数。
- 不覆盖插件开发教程；这里只说明插件 issue provider 如何接入现有模块。
- 不深挖 op-log 冲突、任务域实体不变量或 Electron 主进程整体架构，这些已有相邻主题承接。

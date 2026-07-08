# 教学笔记：日历 time block 同步

- 父模块 L1：`module-issue-integrations/lessons/0001-issue-integrations-module-tour.html` 已把 calendar/time-block 列为第四条链路；本切片展开读/写双向细节。
- 与 `slice-planner-schedule-flow` 交叉：后者讲 task/planner 如何投影到 Schedule；本切片聚焦 calendar 事件来源与写回。
- 与 `slice-issue-import-sync-flow` 交叉：日历 auto-import 最终也调用 `IssueService.addTaskFromIssue`，但触发入口与 sync window 门控不同。
- 首课强制含 mermaid `sequenceDiagram`；参考文档承载长表格与源码索引。

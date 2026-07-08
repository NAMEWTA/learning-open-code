# 教学笔记：外部 Issue 拉取、映射与双向同步全链路

- 用户要求交互与文档使用简体中文，源码标识符保留英文。
- 第一节 lesson 聚焦判断链路边界：provider 拉取、任务创建/更新、双向同步写回不能混成一步。
- reference 承载长清单、入口表、action/effect/service/reducer/provider 边界与故障排查。
- 后续 L3 候选：`IssueService.addTaskFromIssue`、`computePushDecisions`、plugin sync adapter、task shared meta-reducer、sidecar/op-log 边界。

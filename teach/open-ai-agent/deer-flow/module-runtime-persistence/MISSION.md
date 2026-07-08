# 使命：Runtime 与 persistence

## 为什么
学习者希望能读懂 DeerFlow 的长任务运行时，尤其是一次 agent run 如何从 HTTP 请求变成后台任务、SSE 事件、checkpoint 状态和数据库记录。掌握这条边界后，后续排查“消息没显示”“run 卡住”“重启后状态不对”“token 用量不准”等问题时，可以快速定位该看 runtime 还是 persistence。

## 成功的样子
- 能画出一次 run 从创建、流式执行、事件落库到最终状态更新的主线。
- 能区分 `RunStore`、`RunEventStore`、LangGraph checkpointer 和 LangGraph store 各自保存什么。
- 能从 Gateway 装配点找到 checkpointer、stream bridge、event store、SQLAlchemy repository 的实际注入位置。

## 约束条件
- 本主题是 L1 模块总览，不展开完整垂直切片和每个异常分支。
- 主课控制在 15 分钟内完成；长表格和源码索引放在 reference。
- 本轮只写入 `teach/open-ai-agent/deer-flow/module-runtime-persistence/`，不修改源码、项目索引或进度台账。

## 不在范围内
- 不逐行讲解 LangGraph checkpointer 内部实现。
- 不展开前端 `useStream`、artifact 展示和 subagent executor 的完整切片。
- 不讲数据库迁移脚本的逐行 DDL，只讲 schema bootstrap 与 runtime 的关系。

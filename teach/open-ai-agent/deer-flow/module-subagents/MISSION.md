# 使命：Subagent 系统

## 为什么
学习者需要能排查 deer-flow 长任务委托链路：当 lead agent 调用 `task` 后，开发者要知道后台 subagent 怎样启动、怎样产生可回看的 step、怎样最终进入前端 subtask card。掌握这条链路后，才能判断问题落在 task tool、executor、run event store 还是前端回填。

## 成功的样子
- 能用一张调用链解释 `task_tool` 如何把一次委托转换为后台 `SubagentExecutor` 任务。
- 能指出 `task_started`、`task_running`、终态事件分别怎样映射为 `subagent.start`、`subagent.step`、`subagent.end`。
- 能根据状态契约和测试线索判断 subtask card 显示异常时该先查哪个源码边界。

## 约束条件
- 本次是 L1 模块课，只覆盖模块职责、结构、关键入口和一条主调用链。
- lesson 控制在 15 分钟内完成；长状态契约、executor 细节和测试矩阵放入 reference。
- 仅写入 `teach/open-ai-agent/deer-flow/module-subagents/`，不修改源项目、不更新项目索引或进度文件。

## 不在范围内
- 不深入 LangGraph agent 推理细节。
- 不讲前端 workspace 的完整渲染体系，只说明 subtask card 如何消费 subagent step。
- 不讲 runtime/persistence 的完整 run 生命周期；相关内容已由前置模块覆盖。

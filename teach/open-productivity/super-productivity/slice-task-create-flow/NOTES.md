# 教学笔记：新增任务与短语法解析全链路

- 本轮作为 teach-goal L2 内容 worker 执行，只写入 `teach/open-productivity/super-productivity/slice-task-create-flow/`。
- 用户要求最终列出修改文件、审计结果、后续 L3/L4 线索。
- 课程设计采用“入口 -> 临时解析状态 -> TaskService -> TaskSharedActions -> meta-reducer -> op-log”的垂直路径。
- 后续可拆 L3：`AddTaskBarParserService` 的 deadline 覆盖规则、`shortSyntax` 的日期解析正则、`TaskSharedActions.applyShortSyntax` 原子更新。

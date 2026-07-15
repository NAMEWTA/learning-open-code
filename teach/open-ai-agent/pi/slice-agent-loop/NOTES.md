# 教学笔记：Agent 对话循环全链路

- 本课程是 L2 垂直切片，承接 L1-module-agent（概念层）和 L1-module-ai（API 层），向下游 L2-tool-execution 和 L2-session-management 传递。
- 学生在 L1-module-agent 已学过 steer/followUp 的队列概念，本文聚焦控制流层面的"何时轮询、何时消费"。
- 事件类型（AgentEvent）已在前置课程的 reference 文档中列出，本课程引用但不重复枚举。
- 工具执行失败路径是"合意难度"关键点——要求学生从异常路径反推正常流程，强化存储强度。

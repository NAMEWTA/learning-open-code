# 使命：工具执行全链路

## 为什么
在 Pi Agent 中，工具调用是 LLM 与真实世界交互的唯一通道。LLM 生成 tool_use 后，需要经过路由分发、权限鉴权、参数校验、实际执行、结果序列化五个环节才能回到 LLM。理解这条全链路后，你将能安全地自定义工具、为工具添加权限层、以及在工具失败时诊断根因。这是从"使用 Pi"到"理解 Pi 内核"的关键跨越。

## 成功的样子
- 能画出从 LLM 返回 tool_use 到 ToolResultMessage 回传的完整 6 阶段时序图
- 能说出 ToolName 联合类型的 7 个值，以及每个工具的 Operations 接口和可插拔设计
- 能解释 _refreshToolRegistry 的三层注册体系：baseTools → customTools → extensionTools
- 能定位工具执行失败的四种异常路径（tool not found / blocked / 参数校验 / execute 异常）
- 能独立阅读 bash/read/edit/write 四个工具中任意一个的完整 execute() 实现

## 约束条件
- 前置知识：L1-module-coding-agent（工具体系概念）+ L1-module-agent（Agent 工具调用流程）
- 聚焦于 coding-agent 包内的 tools/ 目录和 agent-session.ts 的工具管理部分
- 不深入 agent-loop.ts 的双层循环控制流（已在 slice-agent-loop 覆盖）

## 不在范围内
- Agent 对话循环的双层 while 结构（slice-agent-loop 覆盖）
- 扩展系统 Hook 生命周期完整列表（slice-extension-system 覆盖）
- find/grep/ls 工具的内部实现（结构与 read 类似，可类比学习）
- TUI 渲染层如何展示工具调用（slice-tui-render-cycle 覆盖）

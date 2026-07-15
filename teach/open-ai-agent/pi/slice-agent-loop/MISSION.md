# 使命：Agent 对话循环全链路

## 为什么
需要理解 Pi Agent 从接收用户输入到 LLM 响应、再到工具调用执行、最后回到 LLM 的完整闭环。掌握这条链路后才能安全地修改 Agent 行为——例如自定义工具执行策略、拦截 LLM 请求、或者注入中间件逻辑。

## 成功的样子
- 能画出从 prompt() 到 agent_end 的完整事件序列图
- 能解释外层循环（followUp）和内层循环（tool calls + steering）的分工与触发时机
- 能在脑海中复现一次"用户发消息 → LLM 返回 tool_call → 工具执行 → LLM 再次响应"的全过程
- 能定位工具调用失败（tool not found / 参数校验失败 / execute 异常）时的事件发放路径

## 约束条件
- 前置知识：L1-module-agent（Agent 类 API 与双层循环概念）+ L1-module-ai（LLM API 调用）
- 聚焦于 agent-loop.ts 和 agent.ts 的核心控制流，不展开 session/compaction/TUI

## 不在范围内
- 会话持久化（JSONL 存储、fork/merge）—— 属于 L2-session-management
- 上下文压缩算法 —— 属于 L3-micro compaction
- 具体工具（read/bash/edit/write）的内部实现 —— 属于 L2-tool-execution

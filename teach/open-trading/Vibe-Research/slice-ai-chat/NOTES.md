# 教学笔记：AI 对话全链路

## 用户偏好
- 批量生成模式，不生硬询问"你想学什么"，直接按默认计划推进。
- 课程使用简体中文，代码标识符保留英文。

## 教学注意事项
- L1-backend 已讲过 chat.py / cli_runtime.py / mcp_server.py 的模块职责，L2 应聚焦「串联」而非重复介绍。
- 三条通道的选择对用户来说是实际决策点：API 填 key 最简单但花钱、CLI 免 key 但只能本机、MCP 给 agent 用但不能自己聊天——这个权衡在 lesson 中要说清楚。
- cli_runtime.py 的三种投递方式（system-file/stdin/arg）是 CLI 通用的设计模式，值得单独一节讲透。

## 待办事项
- 后续可考虑增加 L3 微观 API 课程：逐行分析 _call_llm_stream 的 SSE 解析逻辑。
- 后续可考虑增加 L4 深度剖析：SSRF 防护的防 DNS rebinding 攻击细节。

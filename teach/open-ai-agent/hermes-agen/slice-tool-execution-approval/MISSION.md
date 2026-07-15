# 使命：工具执行与审批全链路

## 为什么
理解 Hermes Agent 从 LLM 发出 tool_call 到安全闸门判断、再到工具实际执行的完整链路，以便在需要定制审批策略、添加自定义工具或排查"工具被误拦截"问题时，能精准定位到对应的代码层进行修改或调试。

## 成功的样子
- 能画出 tool_call → registry → approval → execute → result 的完整调用时序图
- 能说出三层安全闸门（HARDLINE / DANGEROUS / Smart）的触发条件和裁决逻辑
- 能在遇到 HARDLINE 误拦截或 Smart 审批误判时，定位到对应的审批层代码

## 约束条件
- 以源码阅读为主，不修改 hermes-agen 源码
- 结合 L1 已有的 module-tools 和 module-agent-core 基础知识
- 单节短课，15 分钟内可完成

## 不在范围内
- 自定义工具的编写与注册（属 module-tools 进阶）
- TUI 终端后端的内部实现细节（属 module-tui）
- MCP 协议工具发现与动态刷新

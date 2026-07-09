# 教学笔记：分析决策全链路

- 用户已学完 L0 项目全景和 3 个 L1 模块总览（agents / graph / dataflows），具备读懂链路追踪的前置知识
- 3 节短课的设计：0001 画全景图（概念层）→ 0002 追主路径（代码层）→ 0003 讲异常路径（边界层），逐层深入
- 链路中的结构化输出 Schema（schemas.py）是一个值得未来深挖的子主题，特别是 Anthropic Provider 使用 tool-use 模式实现结构化输出的机制
- checkpoint / memory_log 的延迟反思机制在 L0 和 L1 中未详细展开，可在未来补一节"历史学习与反思闭环"

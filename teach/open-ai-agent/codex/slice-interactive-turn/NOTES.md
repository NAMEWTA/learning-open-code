# 教学笔记：交互 TUI 中一次用户 turn 的执行链路

## 学习者画像
- 已完成 L0 项目总览和 L1 全部 10 个模块导览
- 在 L1-module-tui 中了解了 App/ChatWidget/BottomPane 三层结构
- 在 L1-module-core-runtime 中了解了 ThreadManager/CodexThread/Op/EventMsg 四个核心对象

## 教学策略
- 先画链路地图（mermaid 时序图），让学习者对整个闭环有全局印象
- 再详解主成功路径，逐层说明数据如何从用户输入流转到模型响应再回到 UI
- 参考文档提供速查表，方便后续翻阅
- 异常路径放在 lesson 0002 末尾作为一个独立小节

## 注意事项
- 不要试图在 lesson 0002 中覆盖所有异常情况——只讲一条典型错误路径
- 使用中文描述概念，但在代码引用中保持 Rust 标识符原文
- 交叉链接回 L1-module-tui 和 L1-module-core-runtime 的课程，帮助学习者回溯

## 待办
- [ ] 后续可以新增 L3 课程，深入分析流式渲染的 chunking 策略（AdaptiveChunkingPolicy）和 commit_tick 动画机制
- [ ] 后续可以新增独立的异常处理专题（token 超限、网络重试、WebSocket 断线恢复）

# 使命：Pi Agent Harness 项目总览

## 为什么
Pi Agent Harness 是一个自扩展编码 Agent 的 monorepo 项目，由 Earendil Works 维护。学习它的整体架构、包依赖关系、技术选型与设计哲学，是深入理解现代 AI 编码 Agent 实现原理的第一步。掌握项目全景后，你才能有方向地深入各子包源码，最终具备阅读、调试和扩展 Pi 的能力。

## 成功的样子
- 能一句话说清 Pi 是什么、解决什么问题
- 能画出 5 个核心包（tui、ai、agent、coding-agent、orchestrator）的依赖关系图
- 能解释每个包的职责及其在系统中的定位
- 理解 Pi 的技术栈选型理由和核心设计决策

## 约束条件
- 具备 TypeScript/Node.js 编程基础
- 学习时间碎片化，每节课不超过 15 分钟
- 以源码阅读为主，不要求运行完整项目

## 不在范围内
- 各包内部源码逐文件分析（由后续模块级 goal 覆盖）
- 扩展系统、Hook 机制、Provider 注册等具体实现细节
- 发布流程、CI/CD 配置的详细解读

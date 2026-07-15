# 使命：pi-coding-agent 模块总览

## 为什么
pi-coding-agent 是 Pi Agent Harness 中代码量最大、职责最广的包。它既是用户直接使用的 CLI 入口，又是连接 pi-ai（LLM API）、pi-agent-core（Agent 运行时）和 pi-tui（终端 UI）三个底层包的聚合层。理解它的内部分层、工具体系和扩展机制，是后续深入各切面（会话管理、工具执行、Hook 系统等）的前提。掌握此模块后，你将能独立阅读 Pi 的主入口源码，并具备为 Pi 编写自定义扩展的基础。

## 成功的样子
- 能说出 pi-coding-agent 在 monorepo 架构中的位置及其依赖的三个底层包
- 能画出 cli/ → core/ → modes/ 的内部分层图，并解释每层的职责
- 能列出 pi-coding-agent 对外暴露的 7 个标准工具（read/bash/edit/write/find/grep/ls）
- 理解扩展系统（extensions）的基本概念：如何注册 Hook、自定义工具和 UI 组件
- 知道 ./rpc-entry 导出路径的作用及其与主入口的区别

## 约束条件
- 具备 TypeScript/Node.js 编程基础，已通过 L0 总览课程了解 Pi 整体架构
- 学习时间碎片化，每节课不超过 15 分钟
- 以源码阅读为主，不要求运行完整项目

## 不在范围内
- 各工具（read/bash/edit 等）的逐行实现细节（后续 slice 级 goal 覆盖）
- 扩展系统 Hook 生命周期的完整列表（slice-extension-system 覆盖）
- TUI 渲染引擎的实现原理（module-tui 覆盖）
- Agent 运行时的状态机实现（module-agent 覆盖）
- LLM Provider 的 API 调用细节（module-ai 覆盖）

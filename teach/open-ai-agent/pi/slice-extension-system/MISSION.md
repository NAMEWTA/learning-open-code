# 使命：扩展系统加载与执行全链路

## 为什么
Pi 的扩展系统是 coding-agent 模块中最复杂的子系统——它不只是"插件"，而是一种能让第三方代码深度注入 Agent 生命周期的运行时框架。理解从 package.json 声明到自定义工具/Hook/Provider 注入的完整链路，是编写 Pi 扩展的前提。掌握此链路后，你将能独立开发 Pi 扩展，并理解事件驱动架构在 CLI Agent 中的应用模式。

## 成功的样子
- 能画出扩展从启动发现到运行时事件分发的完整时序图
- 能说出 loader.ts 的三层扩展发现规则（项目本地 → 全局 → 显式路径）和 package.json 中 `pi.extensions` 字段的作用
- 能解释 ExtensionRuntime 的设计：为什么先创建 throwing stub 再 bindCore
- 能说出 ExtensionRunner.emit() 的通用事件分发逻辑和 5 种专用 emit（messageEnd/toolResult/toolCall/userBash/context）的特殊处理
- 知道扩展加载失败的两类异常路径：模块加载失败和 handler 执行异常

## 约束条件
- 已通过 L1-module-coding-agent 了解扩展系统的五种能力（Hook/Tool/SlashCommand/AutocompleteProvider/UI）
- 学习时间碎片化，本课不超过 15 分钟
- 以源码阅读为主，不要求运行完整项目

## 不在范围内
- 各事件类型的详细参数结构（参考 types.ts 源码）
- 具体扩展开发 API 教程（后续跟进课程覆盖）
- 扩展快捷键冲突检测机制详解
- CLI 入口中扩展配置解析的细节（slice-cli-entry 覆盖）

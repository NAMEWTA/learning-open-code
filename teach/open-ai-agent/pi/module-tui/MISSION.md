# 使命：pi-tui — 终端 UI 差异渲染库模块总览

## 为什么
pi-tui 是 Pi Agent Harness 最底层的终端 UI 基础包，实现了差异渲染（只更新变化区域）、Markdown 解析、东亚字符宽度感知布局和文本编辑器组件。掌握 pi-tui 的架构，你才能理解 Pi 的终端交互模式是如何做到流畅、无闪烁的——这是 pi-coding-agent 交互体验的基石。

## 成功的样子
- 能一句话说清 pi-tui 在 Pi monorepo 中的定位：最底层基础包，不依赖任何其他 pi 包
- 能列出 pi-tui 主入口导出的全部模块类别（TUI 核心、组件、键盘、工具函数、原生模块）
- 能画出内部分层：src/ 核心（TUI、Terminal、Keybindings）→ src/components/ UI 组件（13+ 个）→ native/ 平台原生模块
- 能解释差异渲染的核心原理（逐行对比 previousLines 与新渲染内容，只发送变化区域到终端），并手写简化伪代码

## 约束条件
- 具备 TypeScript/Node.js 编程基础，了解终端 ANSI 转义序列的基本概念
- 学习时间碎片化，每节课不超过 15 分钟
- 以源码阅读和架构理解为主，不要求实际编写 TUI 组件
- 不要求配置或运行 pi-tui 的完整开发环境

## 不在范围内
- 各 UI 组件的完整实现细节（如 Editor 的撤销栈、选区管理）
- 原生模块（native-modifiers、darwin-modifiers.node）的 C++ 实现
- Kitty 图像协议、iTerm2 图像协议的编码细节
- 键盘协议协商流程（Kitty keyboard protocol flags 握手）
- pi-coding-agent 如何集成 pi-tui 的具体代码

# 使命：pi-tui 嵌入使用指南

## 为什么
我想在自己的 Node.js CLI 工具中嵌入 pi-tui 的终端渲染能力，构建一个具备流畅交互体验的 TUI 应用。我需要知道它能否脱离 Pi 生态独立使用、渲染原理是什么、以及具体怎么集成——从安装到写出第一个自定义组件。

## 成功的样子
- 能独立安装 `@earendil-works/pi-tui` 并跑通最小可运行示例
- 能解释差分渲染三策略（首帧/全量/增量）的触发条件和 ANSI 生成逻辑
- 能编写自定义 Component，理解 render() 契约、缓存策略和 handleInput() 生命周期
- 能将 pi-tui 嵌入自己的项目，使用 Text、Input、Editor、Box、Overlay 等内置组件构建交互界面

## 约束条件
- 具备 TypeScript/Node.js 编程基础，了解终端 ANSI 转义序列基本概念
- 学习时间碎片化，每节课不超过 15 分钟
- 需要实际可运行的代码示例，不只是理论

## 不在范围内
- Pi monorepo 其他包（pi-agent-core、pi-coding-agent、pi-ai）的集成方式
- Native 模块（darwin-modifiers、win32-console-mode）的 C 源码实现
- Kitty/iTerm2 图像协议的编码细节
- Editor 组件的撤销栈、选区管理、自动补全等高级特性

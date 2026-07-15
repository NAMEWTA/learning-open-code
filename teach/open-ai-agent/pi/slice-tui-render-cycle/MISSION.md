# 使命：TUI 差异渲染循环全链路

## 为什么
理解 pi-tui 的差异渲染循环是掌握 Pi 终端交互体验的必经之路。L1 模块总览只解释了差异渲染的"是什么"，本切片让你真正看懂"怎么做的"——从组件树 render() 调用开始，经过逐行比对、ANSI 转义序列生成，到终端像素更新的完整数据流。掌握这条链路后，你将能够：诊断 TUI 闪烁问题、理解为什么某些场景会触发全量重绘、以及自定义 TUI 组件时如何避免溢出崩溃。

## 成功的样子
- 能画出从 requestRender() 到 terminal.write() 的完整调用链，包含每个决策分支（首帧/尺寸变化/差异渲染/全量重绘）
- 能解释 previousLines 逐行比对的算法细节，以及 firstChanged/lastChanged 的边界条件
- 能说明同步输出协议（\x1b[?2026h/l）的作用，以及为什么差异渲染必须在同步包裹内执行
- 能识别三种异常降级路径：窗口 resize 全量重绘、变化区域溢出视口全量重绘、行宽溢出崩溃保护

## 约束条件
- 已通过 L0 项目总览和 L1-module-tui 课程，了解 pi-tui 的模块职责和 Component 接口
- 了解终端 ANSI 转义序列的基本概念（光标移动 \x1b[nA/B、清行 \x1b[2K、清屏 \x1b[2J）
- 学习时间碎片化，每节课不超过 15 分钟
- 以源码阅读和数据流追踪为主

## 不在范围内
- Overlay 系统的焦点恢复策略（overlayFocusRestore 状态机）
- Kitty 图像协议的编码/解码细节（parseKittyImageHeader、deleteKittyImages）
- 终端颜色方案查询（OSC 11）和键盘协议协商（Kitty keyboard protocol flags）
- 具体 UI 组件的 render() 实现细节（Editor 的换行布局、Markdown 的 token 渲染）

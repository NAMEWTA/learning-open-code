# TUI 差异渲染循环 资源

## 知识

- [src/tui.ts — TUI 核心类](https://github.com/earendil-works/pi/blob/main/packages/tui/src/tui.ts)
  doRender() 方法（~370 行）是本切片的绝对核心。涵盖：requestRender 调度链、组件树渲染、previousLines 差异比对、ANSI 序列生成、同步输出包裹。适用于：理解每次终端刷新背后的完整决策树。

- [src/tui.ts — requestRender/scheduleRender](https://github.com/earendil-works/pi/blob/main/packages/tui/src/tui.ts#L712-L759)
  渲染请求的节流调度链路。16ms 最小间隔（MIN_RENDER_INTERVAL_MS）、force 参数触发全量重绘、process.nextTick 异步调度。适用于：理解高频渲染请求如何被合并。

- [src/tui.ts — compositeOverlays](https://github.com/earendil-works/pi/blob/main/packages/tui/src/tui.ts#L1032-L1091)
  Overlay 合成算法。将 overlay 组件的渲染结果按 focusOrder 排序后，逐层拼接到基础内容行上。适用于：理解弹窗/下拉菜单如何覆盖在主内容上。

- [src/tui.ts — compositeLineAt](https://github.com/earendil-works/pi/blob/main/packages/tui/src/tui.ts#L1176-L1224)
  单行 Overlay 拼接算法。使用 extractSegments 提取前后段、sliceWithWidth 截取 Overlay 内容、visibleWidth 防溢出校验。适用于：理解东亚字符宽度感知的列级精确拼接。

- [src/tui.ts — fullRender](https://github.com/earendil-works/pi/blob/main/packages/tui/src/tui.ts#L1284-L1325)
  全量重绘的闭包实现。包含清屏 \x1b[2J\x1b[H\x1b[3J、逐行输出、同步输出包裹。适用于：理解全量重绘与差异渲染的输出差异。

- [src/terminal.ts — Terminal 接口](https://github.com/earendil-works/pi/blob/main/packages/tui/src/terminal.ts#L52-L94)
  终端抽象接口定义：write()、columns/rows、光标控制、清屏操作。适用于：理解 TUI 如何与不同终端后端解耦。

- [src/utils.ts — visibleWidth/sliceByColumn](https://github.com/earendil-works/pi/blob/main/packages/tui/src/utils.ts)
  东亚字符宽度感知的工具函数。visibleWidth() 计算字符串在终端中的实际列宽，sliceByColumn() 按列宽截断字符串。适用于：理解差异渲染中行宽校验和截断的底层实现。

- [前导课程：L1-module-tui](../module-tui/lessons/0001-tui-module-tour.html)
  pi-tui 模块总览。涵盖 Component 接口、Container 树形挂载、差异渲染基本原理。本切片的前置知识。

- [前导课程：L0 项目总览](../00-overview/lessons/0001-project-map.html)
  Pi monorepo 整体架构与 5 个核心包职责。

## 智慧（社区）

- [Pi GitHub Issues](https://github.com/earendil-works/pi/issues)
  搜索 "render"、"flicker"、"redraw" 关键词可找到与差异渲染相关的 bug 报告和优化讨论。

- [ANSI 转义序列参考 — Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)
  CSI 序列的权威参考，涵盖光标移动、擦除、SGR 颜色等所有 pi-tui 使用的序列。

## 空白

- pi-tui 没有关于差异渲染算法的独立设计文档或注释，理解完全依赖源码阅读。
- 终端同步输出协议（\x1b[?2026h/l）的终端兼容性表缺失——不同终端模拟器对该协议的支持程度不一，但 pi-tui 未在代码中做终端类型检测。

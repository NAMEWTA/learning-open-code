# pi-tui 模块资源

## 知识

- [Pi GitHub 仓库 — packages/tui/](https://github.com/earendil-works/pi/tree/main/packages/tui)
  pi-tui 源码目录，包含 README.md、package.json、src/、native/ 全部源码。适用于：了解包结构、入口文件、原生模块预编译产物。

- [package.json — @earendil-works/pi-tui](https://github.com/earendil-works/pi/blob/main/packages/tui/package.json)
  包元数据、npm scripts、dependencies（marked、get-east-asian-width）、devDependencies（@xterm/headless、chalk）。适用于：确认外部依赖版本和原生模块文件清单。

- [src/index.ts](https://github.com/earendil-works/pi/blob/main/packages/tui/src/index.ts)
  主入口文件，重导出所有公共类型和函数。适用于：快速了解 pi-tui 的完整公共 API 全貌。

- [src/tui.ts](https://github.com/earendil-works/pi/blob/main/packages/tui/src/tui.ts)
  TUI 核心类实现，包含 Component 接口、Container 容器、TUI 类的差异渲染 doRender() 方法、Overlay 系统、焦点管理。适用于：理解差异渲染的完整流程和 Overlay 叠层机制。

- [src/components/editor.ts](https://github.com/earendil-works/pi/blob/main/packages/tui/src/components/editor.ts)
  多行文本编辑器组件，支持撤销/重做、剪贴板（KillRing）、自动补全、选区操作。适用于：理解 pi-tui 最复杂的 UI 组件。

- [src/components/markdown.ts](https://github.com/earendil-works/pi/blob/main/packages/tui/src/components/markdown.ts)
  基于 marked 库的 Markdown 渲染组件，处理流式输出的不完整 Markdown 标记。适用于：理解 Agent 输出如何在终端中以格式化文本呈现。

- [src/utils.ts](https://github.com/earendil-works/pi/blob/main/packages/tui/src/utils.ts)
  工具函数集合：visibleWidth()（感知东亚字符宽度）、truncateToWidth()、wrapTextWithAnsi()、sliceByColumn()。适用于：理解东亚字符宽度感知布局的实现。

- [marked 文档](https://marked.js.org/)
  pi-tui 的 Markdown 解析依赖 marked 18.x。适用于：理解 Markdown Token 结构和自定义 Tokenizer。

- [get-east-asian-width 文档](https://www.npmjs.com/package/get-east-asian-width)
  pi-tui 的东亚字符宽度计算依赖 get-east-asian-width 1.6.0。适用于：理解 CJK 字符在终端显示中占 2 列宽度的原理。

## 智慧（社区）

- [Pi GitHub Issues](https://github.com/earendil-works/pi/issues)
  Pi 项目的 issue 跟踪。适用于：搜索 pi-tui 相关的 bug 报告和功能讨论。

- [r/commandline](https://reddit.com/r/commandline)
  Reddit 上的命令行工具社区，讨论 TUI 框架、终端技术等话题。适用于：了解终端 UI 开发的最佳实践和社区讨论。

## 空白

- pi-tui 没有独立的官方文档站点，所有文档在 Pi monorepo 根目录的 README.md 中。
- marked 和 get-east-asian-width 是两个小型独立 npm 包，pi-tui 仅使用其核心 API，不涉及深度定制。
- 社区中没有 pi-tui 的专门学习资源或教程，学习完全依赖源码阅读。

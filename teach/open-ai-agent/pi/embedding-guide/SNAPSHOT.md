# 课程快照：pi-tui 嵌入使用指南

## 源项目信息
- **仓库路径**：`open-ai-agent/pi`
- **Git Commit**：`8479bd84743e8889f728acb21a62794102db0529`
- **短 Commit**：`8479bd8`
- **分支**：`main`
- **快照时间**：2026-07-15T12:00:00+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/tui/package.json` | 确认零 Pi 依赖和包元信息 | 🔴 核心 |
| `packages/tui/src/tui.ts` | TUI 主类、Component 接口、doRender 差分渲染算法、Overlay 系统 | 🔴 核心 |
| `packages/tui/src/terminal.ts` | Terminal 接口、ProcessTerminal 实现、raw mode 管理 | 🔴 核心 |
| `packages/tui/src/index.ts` | 公开 API 导出清单 | 🔴 核心 |
| `packages/tui/src/utils.ts` | visibleWidth、truncateToWidth、wrapTextWithAnsi 等工具函数 | 🟡 辅助 |
| `packages/tui/src/components/editor.ts` | Editor 组件实现（wordWrapLine 等） | 🟡 辅助 |
| `packages/tui/src/components/input.ts` | Input 组件实现 | 🟡 辅助 |
| `packages/tui/src/components/box.ts` | Box 容器组件实现 | 🟡 辅助 |
| `packages/tui/src/components/text.ts` | Text 组件实现 | 🟡 辅助 |
| `packages/tui/src/components/markdown.ts` | Markdown 组件实现 | 🟡 辅助 |
| `packages/tui/src/editor-component.ts` | EditorComponent 接口定义 | 🟡 辅助 |
| `packages/tui/README.md` | 官方入门文档和 API 说明 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | `lessons/0001-arch-and-principles.html` | 独立性确认、三层架构、Component 接口契约、差分渲染原理速览 |
| 02 | `lessons/0002-diff-render-engine.html` | 渲染调度管线、三策略触发条件、逐行比对算法、ANSI 序列与 CSI 2026 |
| 03 | `lessons/0003-embedding-practice.html` | 最小示例、内置组件、自定义 Component 编写、Overlay 弹窗实战 |

## 快照摘要
- 课程数：3
- 引用源文件数：12
- 学习记录数：0

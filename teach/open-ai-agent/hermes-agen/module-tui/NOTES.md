# 教学笔记：终端 UI 模块

## 模块特征

- ui-tui/ 是 Node.js/TypeScript 前端，tui_gateway/ 是 Python 后端，两者通过 JSON-RPC over stdio 通信
- 这是整个 Hermes 项目中唯一的前端模块，技术栈与其余 Python 代码完全不同
- 使用 React 19 + Ink 6 + nanostores，与 Web 前端的 React 开发模式一致但渲染目标是终端

## 教学重点

- 双进程架构是理解 TUI 的关键入口——先讲清楚 Node <-> Python 的分工和通信
- 斜杠命令的两级 dispatch（本地注册表 → Gateway fallback）是展示架构优势的好例子
- 会话历史与多行编辑是用户最常接触的交互功能，建议用交互演示辅助理解

## 后续可扩展课程

- 单个组件深度分析（markdown 渲染器、应用布局、流式输出）
- 斜杠命令系统完整剖析（7 个命令文件、register → dispatch → exec 全链）
- Gateway 端 RPC 方法全景（server.py 中的所有 handler）
- 性能优化专题（虚拟列表、高度缓存、调整大小合并）

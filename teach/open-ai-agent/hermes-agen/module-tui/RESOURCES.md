# 终端 UI 资源

## 知识

### 源码入口（核心 — Node/TypeScript 前端）

- [entry.tsx](open-ai-agent/hermes-agen/ui-tui/src/entry.tsx) -- TUI 主入口，TTY 检测、终端模式重置、GatewayClient 启动、Ink render 挂载
- [app.tsx](open-ai-agent/hermes-agen/ui-tui/src/app.tsx) -- 顶层 Ink 组件树，组合 appActions / appComposer / appStatus 等 props
- [gatewayClient.ts](open-ai-agent/hermes-agen/ui-tui/src/gatewayClient.ts) -- JSON-RPC 桥接层 (795行)，管理 Python 子进程生命周期、WebSocket 重连、请求超时
- [useMainApp.ts](open-ai-agent/hermes-agen/ui-tui/src/app/useMainApp.ts) -- 顶层组合 Hook (1146行)，连接所有子 Hooks，暴露完整的 transcript / composer / status 状态
- [createSlashHandler.ts](open-ai-agent/hermes-agen/ui-tui/src/app/createSlashHandler.ts) -- 斜杠命令处理器 (153行)，dispatch 分发与 Gateway fallback 回退
- [README.md](open-ai-agent/hermes-agen/ui-tui/README.md) -- ui-tui 官方自述，含架构说明、热键表、事件表面、文件地图

### 源码入口（核心 — Python Gateway 后端）

- [entry.py](open-ai-agent/hermes-agen/tui_gateway/entry.py) -- Gateway stdio 入口 (382行)，信号处理、MCP 后台发现、JSON-RPC 主循环
- [server.py](open-ai-agent/hermes-agen/tui_gateway/server.py) -- RPC handler 注册与会话管理 (534KB)，包含所有 `dispatch` 方法路由
- [transport.py](open-ai-agent/hermes-agen/tui_gateway/transport.py) -- 传输抽象层 (220行)，StdioTransport / TeeTransport，JSON 帧写入与管道断裂处理
- [render.py](open-ai-agent/hermes-agen/tui_gateway/render.py) -- Python 端富文本渲染桥 (50行)，可选 rich/ANSI 输出
- [slash_worker.py](open-ai-agent/hermes-agen/tui_gateway/slash_worker.py) -- 持久化斜杠命令子进程 (158行)，独立 HermesCLI 实例 + 孤儿进程看门狗

### 源码入口（app/ 子模块 — 关键 Hooks 与 Stores）

- [useComposerState.ts](open-ai-agent/hermes-agen/ui-tui/src/app/useComposerState.ts) -- 输入状态管理 (draft、多行缓冲、队列编辑、补全请求)
- [useInputHandlers.ts](open-ai-agent/hermes-agen/ui-tui/src/app/useInputHandlers.ts) -- 按键路由 (Enter 提交、Tab 补全、Ctrl+C 中断、Up/Down 历史导航)
- [useSubmission.ts](open-ai-agent/hermes-agen/ui-tui/src/app/useSubmission.ts) -- 消息提交、Shell 执行 (!cmd)、行内插值 ({!cmd})
- [turnController.ts](open-ai-agent/hermes-agen/ui-tui/src/app/turnController.ts) -- 有状态 Turn 生命周期驱动 (流式文本缓冲、工具/推理状态、中断处理)
- [createGatewayEventHandler.ts](open-ai-agent/hermes-agen/ui-tui/src/app/createGatewayEventHandler.ts) -- Gateway 事件 → 状态更新映射 (40+ 种事件类型)
- [useSessionLifecycle.ts](open-ai-agent/hermes-agen/ui-tui/src/app/useSessionLifecycle.ts) -- 会话创建/恢复/激活/关闭和可见历史重置
- [slash/registry.ts](open-ai-agent/hermes-agen/ui-tui/src/app/slash/registry.ts) -- 斜杠命令注册表，`findSlashCommand(name)` 大小写不敏感查找

### 源码入口（组件树核心）

- [appLayout.tsx](open-ai-agent/hermes-agen/ui-tui/src/components/appLayout.tsx) -- 顶层布局组合 (Transcript + Status Bar + Input + Completions)
- [textInput.tsx](open-ai-agent/hermes-agen/ui-tui/src/components/textInput.tsx) -- 自定义行编辑器（多行编辑、补全、粘贴处理）
- [streamingAssistant.tsx](open-ai-agent/hermes-agen/ui-tui/src/components/streamingAssistant.tsx) -- 实时流式助手行渲染

### 官方文档与外部资料

- [React 官方文档](https://react.dev) -- React 核心概念（Hooks、Context、组件生命周期），TUI 前端的技术基础
- [Ink 文档](https://github.com/vadimdemedes/ink) -- React for CLI，Hermes TUI 依赖的终端渲染框架
- [nanostores 文档](https://github.com/nanostores/nanostores) -- 轻量状态管理库，TUI 中所有 Store 的基础
- [JSON-RPC 2.0 规范](https://www.jsonrpc.org/specification) -- Gateway 通信协议规范
- [Hermes Agent GitHub](https://github.com/NousResearch/hermes-agent) -- 项目仓库

## 智慧（社区）

- [Nous Research Discord](https://discord.gg/nousresearch) -- Hermes Agent 开发者社区，TUI 相关讨论与 bug 反馈
- [Hermes Agent GitHub Issues](https://github.com/NousResearch/hermes-agent/issues) -- 问题追踪，可观察 TUI 相关的真实 bug 与功能请求

## 空白

- 暂无第三方教程或博客系统讲解 Hermes TUI 架构——目前知识来源主要是源码阅读和 ui-tui/README.md
- Ink 框架在大型 TUI 项目中的最佳实践参考资料较少，Hermes TUI 的架构设计本身是一个难得的参考案例
- 没有找到关于 ui-tui 组件树渲染性能优化的公开分析文档

# Pi Agent Harness · 架构教学 Wiki

> 📊 整体进度：15/15 goals · 100% · 已执行 5 轮
> 🕐 最后更新：2026-07-09

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ██████████ |
| L1 模块总览 | 6 | 6 | ██████████ |
| L2 垂直切片 | 8 | 8 | ██████████ |
| L3 微观 API | 0 | * | L3/L4 由 agent 发现驱动 |
| L4 深度剖析 | 0 | * | L3/L4 由 agent 发现驱动 |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/0001-project-map.html)**
  > 15 分钟建立全局地图，理解 Pi 的 monorepo 架构和 5 个核心包。
- **[📄 Pi Agent Harness 项目总览参考](00-overview/reference/00-overview.html)**
  > 技术栈：TypeScript + Node.js · 架构风格：分层 monorepo · 5 个顶层包

---

## 📦 L1 · 模块总览

### module-ai — pi-ai：多 Provider 统一 LLM API
- **[📘 模块导览短课](module-ai/lessons/0001-ai-module-tour.html)**
  > 12 分钟理解 35 个 Provider、6 个 exports 子路径、4 层内部分层和延迟加载机制。
- **[📄 模块总览参考](module-ai/reference/ai-overview.html)**
  > 职责：屏蔽 OpenAI/Anthropic/Google/Bedrock/Mistral 五个 SDK 的接口差异
- **关联垂直切片**：
  - [🔪 多 Provider LLM 统一调度全链路](slice-llm-provider-dispatch/lessons/0001-flow-map.html)

### module-agent — pi-agent-core：Agent 运行时
- **[📘 模块导览短课](module-agent/lessons/0001-agent-module-tour.html)**
  > 12 分钟理解传输抽象、状态管理、双层循环和消息队列。
- **[📄 模块总览参考](module-agent/reference/agent-overview.html)**
  > 职责：通用 Agent 运行时（传输抽象 + 状态管理 + 工具调用 + attachment 支持）
- **关联垂直切片**：
  - [🔪 Agent 对话循环全链路](slice-agent-loop/lessons/0001-flow-map.html)
  - [🔪 会话持久化全链路](slice-session-management/lessons/0001-flow-map.html)

### module-coding-agent — pi-coding-agent：交互式编程 CLI
- **[📘 模块导览短课](module-coding-agent/lessons/0001-coding-agent-module-tour.html)**
  > 12 分钟理解 CLI 入口、7 个标准工具、四层内部分层和扩展系统。
- **[📄 模块总览参考](module-coding-agent/reference/coding-agent-overview.html)**
  > 职责：聚合 pi-ai + pi-agent-core + pi-tui，提供交互式编程 CLI
- **关联垂直切片**：
  - [🔪 工具执行全链路](slice-tool-execution/lessons/0001-flow-map.html)
  - [🔪 Agent Hook 生命周期](slice-hook-system/lessons/0001-flow-map.html)
  - [🔪 扩展系统全链路](slice-extension-system/lessons/0001-flow-map.html)
  - [🔪 CLI 入口与模式选择](slice-cli-entry/lessons/0001-flow-map.html)

### module-tui — pi-tui：终端 UI 差异渲染库
- **[📘 模块导览短课](module-tui/lessons/0001-tui-module-tour.html)**
  > 12 分钟理解差异渲染原理、12 个 UI 组件和东亚字符宽度感知。
- **[📄 模块总览参考](module-tui/reference/tui-overview.html)**
  > 职责：终端差异渲染（differential rendering）+ Markdown 解析 + 文本编辑器
- **关联垂直切片**：
  - [🔪 TUI 差异渲染循环全链路](slice-tui-render-cycle/lessons/0001-flow-map.html)

### module-orchestrator — pi-orchestrator：实验性编排器
- **[📘 模块导览短课](module-orchestrator/lessons/0001-orchestrator-module-tour.html)**
  > 12 分钟理解 IPC 协议、5 状态实例机和多 Agent 编排。
- **[📄 模块总览参考](module-orchestrator/reference/orchestrator-overview.html)**
  > 职责：通过 Unix Socket IPC 将 pi-coding-agent 包装为可远程管理的多实例编排服务

### module-scripts-infra — 构建脚本与基础设施
- **[📘 模块导览短课](module-scripts-infra/lessons/0001-scripts-infra-module-tour.html)**
  > 12 分钟理解三层防线（pre-commit → CI → release）和供应链安全策略。
- **[📄 模块总览参考](module-scripts-infra/reference/scripts-infra-overview.html)**
  > 职责：质量门禁、锁文件生成、版本发布与 CI/CD 分层架构

---

## 🔪 L2 · 垂直切片

### slice-agent-loop — Agent 对话循环全链路
- **[📘 课程：链路地图](slice-agent-loop/lessons/0001-flow-map.html)**
  > 从 prompt() 到 LLM 响应再到工具调用的完整 7 步数据流。
  > 所属模块：[module-agent](module-agent/reference/agent-overview.html)

### slice-tool-execution — 工具执行全链路
- **[📘 课程：链路地图](slice-tool-execution/lessons/0001-flow-map.html)**
  > 从 LLM tool_use 到 bash/read/edit/write 执行的 6 阶段调用链。
  > 所属模块：[module-coding-agent](module-coding-agent/reference/coding-agent-overview.html)

### slice-session-management — 会话持久化全链路
- **[📘 课程：链路地图](slice-session-management/lessons/0001-flow-map.html)**
  > JSONL 存储/内存仓库/上下文压缩的四层架构与完整数据流。
  > 所属模块：[module-agent](module-agent/reference/agent-overview.html)

### slice-llm-provider-dispatch — 多 Provider LLM 调度全链路
- **[📘 课程：链路地图](slice-llm-provider-dispatch/lessons/0001-flow-map.html)**
  > 从 builtinModels 到 streamSimple 的 9 步完整路径。
  > 所属模块：[module-ai](module-ai/reference/ai-overview.html)

### slice-tui-render-cycle — TUI 差异渲染循环全链路
- **[📘 课程：链路地图](slice-tui-render-cycle/lessons/0001-flow-map.html)**
  > 从 requestRender 到终端像素的完整数据流（节流调度 → 组件树渲染 → 差异比对 → ANSI 输出）。
  > 所属模块：[module-tui](module-tui/reference/tui-overview.html)

### slice-hook-system — Agent Hook 生命周期全链路
- **[📘 课程：链路地图](slice-hook-system/lessons/0001-flow-map.html)**
  > 31 种事件、三层架构与 6 种 emit 执行策略的完整链路。
  > 所属模块：[module-coding-agent](module-coding-agent/reference/coding-agent-overview.html)
  > 关联切片：[🔪 扩展系统全链路](slice-extension-system/lessons/0001-flow-map.html)

### slice-extension-system — 扩展系统全链路
- **[📘 课程：链路地图](slice-extension-system/lessons/0001-flow-map.html)**
  > 从 package.json 声明到自定义工具/Hook/Provider 注入的六阶段全链路。
  > 所属模块：[module-coding-agent](module-coding-agent/reference/coding-agent-overview.html)

### slice-cli-entry — CLI 入口与模式选择全链路
- **[📘 课程：链路地图](slice-cli-entry/lessons/0001-flow-map.html)**
  > 从 pi 命令到 Agent 会话启动的 9 阶段管线与三种模式分发。
  > 所属模块：[module-coding-agent](module-coding-agent/reference/coding-agent-overview.html)

---

## 📊 源码覆盖统计

| 指标 | 数值 |
|------|------|
| 源码文件总数 | 800（含 294 测试文件） |
| L1 模块覆盖 | 6/6（100%） |
| 核心功能切片 | 8/8（100%） |
| 教学课程 | 15 节 |
| 参考文档 | 10 份 |
| 豁免文件 | node_modules、dist、*.wasm、*.node、models.generated.ts、test/fixtures |

---

## 🔜 后续可扩展的 L3/L4 主题

Agents 在生成过程中发现了以下可深入展开的主题，可作为 L3 微观 API 或 L4 深度剖析的候选：

| 候选主题 | 来源 goal | 层级建议 |
|----------|----------|---------|
| 35 个 Provider 的完整注册表与配置 | L1-module-ai | L3 |
| OAuth Token 刷新互斥锁机制 | L1-module-ai | L4 |
| agent-loop.ts 双层循环的完整状态机 | L2-agent-loop | L4 |
| JSONL 存储的 append-only 设计与版本校验 | L2-session-management | L4 |
| 上下文压缩的分支摘要算法 | L2-session-management | L4 |
| TUI 组件的 Component 接口与 Container 树形渲染 | L2-tui-render-cycle | L3 |
| IPC Unix Socket 的 JSONL 流协议 | L1-module-orchestrator | L4 |
| Radius 心跳退避算法（指数退避 + 25% 抖动） | L1-module-orchestrator | L4 |
| npm 供应链安全：shrinkwrap 生成与 check 流水线 | L1-module-scripts-infra | L3 |

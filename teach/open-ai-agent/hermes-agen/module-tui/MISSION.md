# 使命：终端 UI — React+Ink TUI 架构与交互系统

## 为什么
Hermes Agent 的核心竞争力之一是"真正的终端界面"——一个基于 React+Ink 的全功能 TUI，而非简单的 readline 循环。理解这套 TUI 的架构设计、React 组件树与 Python Gateway 的 JSON-RPC 通信机制，是深入定制 Hermes 交互体验、贡献前端代码或排查 TUI 相关 bug 的必要前提。

## 成功的样子
- 能画出 ui-tui/ (Node/React) 与 tui_gateway/ (Python) 之间的进程通信图，说清 JSON-RPC 请求/响应/事件三通道的流向
- 能独立追踪一条斜杠命令（如 /model）从前端输入到 Gateway 执行再返回结果的完整链路
- 能定位输入处理、补全系统、会话历史组件在源码中的位置，并解释其协同方式

## 约束条件
- 不深入 Agent 核心引擎的对话循环逻辑（属于 L1-agent-core 课程）
- 不覆盖 Web Dashboard（web/）或桌面应用（apps/desktop/）的 UI 实现
- 不涉及 MCP 工具发现或 Provider 层的实现细节（属于对应专项课程）
- 关注架构级理解，不要求掌握每个组件/命令的逐行实现

## 不在范围内
- 单个 React 组件（如 markdown 渲染器、状态栏）的细节实现
- Python Agent 端的模型推理、工具执行、会话持久化
- Ink 库本身的内部实现原理

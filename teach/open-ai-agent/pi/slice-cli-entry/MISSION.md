# 使命：CLI 入口与模式选择全链路

## 为什么
理解 Pi 从敲下 `pi` 命令到 Agent 会话启动的完整链路。这条路径串联了命令行参数解析（50+ 参数）、启动配置引导、Provider 认证、会话管理（新建/恢复/fork/continue）、模型选定（ScopedModel 与 thinking level）、以及三种运行模式（interactive/batch/RPC）的分发决策。掌握它你就能读懂 Pi 启动的每一行代码，并能自如地用 CLI 参数控制 Pi 行为。

## 成功的样子
- 能从 `cli.ts` 的 `#!/usr/bin/env node` 开始，逐层追溯到 `InteractiveMode.run()` / `runPrintMode()` / `runRpcMode()` 的分发点
- 能画出 main() 函数的 9 阶段启动管线图（解析→版本/导出速出→首次设置→会话管理→运行时工厂→模型→模式分发→运行）
- 能区分 `--session`（打开）、`--continue`（最近）、`--resume`（TUI 选择）、`--fork`（复制）四种会话恢复策略的差异
- 能说出 `resolveAppMode()` 的决策逻辑：RPC 通过 `--mode rpc` 强制，print 通过管道/`-p`/`--print` 触发，其余走 interactive
- 理解 `rpc-entry.ts` 与 `cli.ts` 的区别及其在 orchestrator 场景中的作用

## 约束条件
- 已通过 L1-module-coding-agent 了解 pi-coding-agent 的内部分层（cli/core/modes）和工具/扩展体系
- 单次学习时间不超过 15 分钟，本课聚焦入口全链路，不深入各模式内部实现
- TypeScript/Node.js 基础，能读懂 async/await 和 import 图

## 不在范围内
- InteractiveMode 的 TUI 组件树与事件循环机制（slice-tui-render-cycle 覆盖）
- Agent 对话循环的 token 消费与工具调用（slice-agent-loop 覆盖）
- 扩展系统的加载时序与 Hook 注册（slice-extension-system 覆盖）
- print-mode 中的流式输出与 JSON 格式细节（后续 print-mode 专题）
- RPC 模式的 JSON-RPC 协议细节（module-orchestrator 已覆盖基础）

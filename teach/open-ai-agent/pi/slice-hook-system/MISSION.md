# 使命：Agent Hook 生命周期全链路

## 为什么
Hook 系统是 Pi 扩展机制的核心——它允许第三方扩展在 Agent 生命周期的关键节点注入自定义逻辑。理解事件从注册到触发再到结果合并的完整链路，是编写 Pi 扩展的前提。无论是拦截工具调用、修改 LLM 上下文、还是监听会话状态变化，都需要穿透 Hook 系统的事件订阅、类型校验、执行时序与异常路径。

## 成功的样子
- 能绘制从 `pi.on("tool_call", handler)` 到 handler 执行完毕的完整时序图
- 能列举 ExtensionAPI 上 31 种 Hook 事件的分类（Session / Agent / Tool / Model / Input / Resource）
- 能解释 ExtensionRunner.emit() 的通用分发逻辑，以及 6 种专用 emit 方法的不同策略（链式修改 vs 短路返回 vs 合并结果）
- 能说明 runner.ts 中 session_before_* 事件的提前取消机制，以及 extension 异常时 ExtensionError 的上报流程

## 约束条件
- 聚焦 `packages/coding-agent/src/core/extensions/` 目录下的 types.ts、loader.ts、runner.ts 三个文件
- 以 TypeScript 类型定义和运行时代码为主，不涉及具体 UI 渲染
- 学习时间：约 15 分钟

## 不在范围内
- Extension 发现策略（package.json pi 字段、目录扫描）已在 L1-module-coding-agent 覆盖
- 自定义 Tool/TUI 组件的具体实现（slice-tool-execution、slice-tui-render-cycle 覆盖）
- pi-agent-core 的 EventBus 内部实现（module-agent 覆盖）
- Provider 注册与模型切换（slice-llm-provider-dispatch 覆盖）

# 教学笔记：CLI 入口与模式选择全链路

## 教学要点

- main.ts 有 855 行，是本仓库最长的单文件之一。教学时需聚焦 9 阶段管线，不要陷入每个 helper 函数的细节。
- `createRuntime` 是一个工厂闭包，在 main() 中定义但被 `createAgentSessionRuntime` 调用（支持 session reload 时重新创建）。这是理解"首次启动 vs 会话重载"的关键分界点。
- `process.emitWarning = (() => {})` 这行抑制了 Node 内部警告，防止污染 TUI 输出。这是一个值得提及的工程细节。
- `configureHttpDispatcher()` 被调用两次（cli.ts 一次、main.ts 启动初期一次），因为第一次是全局 undici 配置，第二次是设置加载后应用用户配置的 idle timeout。

## 常见混淆点

- `--session` vs `--session-id`：前者支持模糊匹配（prefix）和跨项目搜索，后者要求在本地精确匹配或新建。
- `resolveAppMode()` 中 print 模式优先级高于 interactive：一旦检测到管道输入或 `-p` 标志，即使 TTY 也走 print。
- `takeOverStdout()` / `restoreStdout()` 只在非 interactive 模式下使用，用于阻止 TUI 组件意外写屏。

## 交叉引用

- 前置课程：[L1-module-coding-agent](../module-coding-agent/lessons/0001-coding-agent-module-tour.html)
- 后续深入：[slice-agent-loop](../slice-agent-loop/lessons/0001-flow-map.html) — InteractiveMode 内部的对话循环
- 后续深入：[slice-tool-execution](../slice-tool-execution/lessons/0001-flow-map.html) — 工具注册与执行链路
- 后续深入：[slice-session-management](../slice-session-management/lessons/0001-flow-map.html) — SessionManager 的 JSONL 存储细节

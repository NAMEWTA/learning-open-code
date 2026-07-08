# Pi Agent Harness · 架构教学 Wiki

> 整体进度：16/16 goals · 100% · 最后更新：2026-07-07T16:24:57+08:00

## 进度面板

| 层级 | 完成 | 总数 |
|------|------|------|
| L0 项目总览 | 1 | 1 |
| L1 模块总览 | 5 | 5 |
| L2 垂直切片 | 6 | 6 |
| L4 深度剖析 | 4 | 4 |

## L0 · 项目总览

- [项目导览短课](teach/open-ai-agent/pi/00-overview/lessons/0001-project-map.html)
  - [项目总览参考](00-overview/reference/00-overview.html) · [源码覆盖清单](00-overview/reference/source-coverage.html)

## L1 · 模块总览
### module-agent — Agent 运行时模块
- [模块导览短课](teach/open-ai-agent/pi/module-agent/lessons/0001-agent-module-tour.html)
- [模块总览参考](module-agent/reference/agent-overview.html)
- [API 速查](module-agent/reference/agent-api.html)
### module-ai — LLM 供应商抽象模块
- [模块导览短课](teach/open-ai-agent/pi/module-ai/lessons/0001-ai-module-tour.html)
- [模块总览参考](module-ai/reference/ai-overview.html)
- [API 速查](module-ai/reference/ai-api.html)
### module-coding-agent — 编程 Agent CLI 模块
- [模块导览短课](teach/open-ai-agent/pi/module-coding-agent/lessons/0001-coding-agent-module-tour.html)
- [模块总览参考](module-coding-agent/reference/coding-agent-overview.html)
- [API 速查](module-coding-agent/reference/coding-agent-api.html)
### module-orchestrator — RPC 编排模块
- [模块导览短课](teach/open-ai-agent/pi/module-orchestrator/lessons/0001-orchestrator-module-tour.html)
- [模块总览参考](module-orchestrator/reference/orchestrator-overview.html)
- [API 速查](module-orchestrator/reference/orchestrator-api.html)
### module-tui — 终端 UI 模块
- [模块导览短课](teach/open-ai-agent/pi/module-tui/lessons/0001-tui-module-tour.html)
- [模块总览参考](module-tui/reference/tui-overview.html)
- [API 速查](module-tui/reference/tui-api.html)

## L2 · 垂直切片
- [Agent 会话全链路](teach/open-ai-agent/pi/slice-agent-session-flow/lessons/0001-flow-map.html)
- [CLI 启动全链路](teach/open-ai-agent/pi/slice-cli-startup-flow/lessons/0001-flow-map.html)
- [上下文压缩全链路](teach/open-ai-agent/pi/slice-context-compaction-flow/lessons/0001-flow-map.html)
- [OAuth 认证全链路](teach/open-ai-agent/pi/slice-oauth-auth-flow/lessons/0001-flow-map.html)
- [RPC 编排全链路](teach/open-ai-agent/pi/slice-rpc-orchestration/lessons/0001-flow-map.html)
- [TUI 渲染全链路](teach/open-ai-agent/pi/slice-tui-render-cycle/lessons/0001-flow-map.html)

## L4 · 深度剖析
- [Agent 双层循环深度剖析](teach/open-ai-agent/pi/deep-dive-agent-loop-double/lessons/0001-problem-frame.html)
- [AgentSession 架构深度剖析](teach/open-ai-agent/pi/deep-dive-agent-session-arch/lessons/0001-problem-frame.html)
- [供应商兼容层深度剖析](teach/open-ai-agent/pi/deep-dive-compat-unification/lessons/0001-problem-frame.html)
- [TUI 差分渲染深度剖析](teach/open-ai-agent/pi/deep-dive-diff-rendering/lessons/0001-problem-frame.html)

## 源码覆盖统计

| 指标 | 数值 |
|------|------|
| 当前纳入源码/配置/测试/文档文件 | 970 |
| 主题目录 | 16 |
| 审计状态 | 通过 `audit_topic.py --all` |

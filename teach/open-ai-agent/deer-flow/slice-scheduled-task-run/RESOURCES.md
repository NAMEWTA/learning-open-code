# scheduled task 创建与执行 资源

## 知识

- [deer-flow AGENTS.md — Scheduled-task note](open-ai-agent/deer-flow/AGENTS.md) — 工作区页面路径、调度器开关、`non_interactive` 背景 run 约定
- [Scheduled Tasks MVP 设计](open-ai-agent/deer-flow/docs/superpowers/specs/2026-07-01-scheduled-tasks-mvp-design.md) — 任务模型、状态机与 overlap 策略的产品设计
- [Scheduled Tasks MVP 实现计划](open-ai-agent/deer-flow/docs/superpowers/plans/2026-07-01-scheduled-tasks-mvp.md) — 分阶段落地清单，适合对照源码是否齐全
- [backend CONFIGURATION.md — scheduler](open-ai-agent/deer-flow/backend/docs/CONFIGURATION.md) — `scheduler.enabled`、`poll_interval_seconds` 等运行参数

## 智慧（社区）

- [deer-flow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `scheduled task` 可看到真实故障报告与修复讨论
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/) — 理解调度最终复用的 thread run / checkpoint 语义

## 空白

- 官方用户向「定时任务运维手册」尚未单独成文；排障主要依赖 AGENTS.md、设计 spec 与 `backend/tests/test_scheduled_task_*.py` 回归用例

# 聊天流式执行 资源

## 知识

- [LangGraph Platform Runs API](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html#tag/runs) — DeerFlow Gateway 的 `thread_runs` 路由对齐此协议，前端 `useStream` 依赖同一 SSE 格式
- [LangGraph JS SDK useStream](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/js_ts_sdk_ref/#usestream) — `frontend/src/core/threads/hooks.ts` 的流式状态机来源
- `open-ai-agent/deer-flow/backend/docs/STREAMING.md` — Gateway 与 DeerFlowClient 并行流式设计、stream_mode 语义
- `open-ai-agent/deer-flow/frontend/AGENTS.md` — 线程流数据流与 stop/reconnect 行为摘要

## 智慧（社区）

- [LangGraph GitHub Discussions](https://github.com/langchain-ai/langgraph/discussions) — 流式断连、checkpoint 与 SDK 兼容问题
- [DeerFlow Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `stream`、`isLoading`、`409` 可找到真实故障案例

## 空白

- 暂无针对 DeerFlow 定制 Gateway SSE 的中文社区教程；本仓库 `teach/` 切片与 L1 模块文档填补此缺口

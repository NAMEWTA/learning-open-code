# IM channel 入站执行 资源

## 知识

- `open-ai-agent/deer-flow/backend/AGENTS.md` — IM Channels System 章节：Message Flow 11 步总览与三种 run 模式
- `open-ai-agent/deer-flow/backend/docs/IM_CHANNEL_CONNECTIONS.md` — 用户绑定、`connection_id` / `owner_user_id` 语义
- [LangGraph Platform Runs API](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref.html#tag/runs) — `ChannelManager` 经 `langgraph_sdk` 调用的 `threads.create`、`runs.wait`、`runs.stream`、`runs.create` 协议
- `open-ai-agent/deer-flow/backend/app/channels/manager.py` — 调度核心：`_dispatch_loop`、`_handle_chat`、thread 映射与出站

## 智慧（社区）

- [DeerFlow Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `channel`、`THREAD_BUSY`、`bound identity` 可找到真实故障案例
- [LangGraph GitHub Discussions](https://github.com/langchain-ai/langgraph/discussions) — SDK `ConflictError`、长 run 超时相关问题

## 空白

- 暂无面向 DeerFlow IM channel 入站→run 的中文社区教程；本仓库 L1 `module-channels` 与 L2 本切片填补此缺口

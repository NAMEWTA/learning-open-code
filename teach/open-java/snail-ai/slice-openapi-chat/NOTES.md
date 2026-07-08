# 便签

- 用户要求生成 L2 垂直切片主题 `L2-slice-openapi-chat`，目标是 OpenAPI 流式对话。
- 本次只允许写入 `teach/open-java/snail-ai/slice-openapi-chat/**`，不得编辑源码、`index.md`、`_progress.*` 或其他主题目录。
- 现有 L1 风格是：短课建立地图，reference 承载长清单、源码索引和排查表。本主题沿用该结构。
- 源码观察：`OpenApiChatRequest.deepPlanEnabled`、`webSearchEnabled`、`timeout` 当前没有进入 `AgentChatCommand`；同步超时由 `OpenApiChatService.SYNC_CHAT_TIMEOUT_MS = 300_000L` 固定。
- 源码观察：OpenAPI 流式 bridge 只转发可解析为 `ChatStreamResponse` 的 JSON chunk；部分责任链本地错误以纯文本 `Error:` 或 `[ERROR]` 写入，流式 OpenAPI 侧可能只看到 `done` 或服务层 catch 后的 `error`。

# 便签

- 本主题是 Snail AI 的 L2 垂直切片，默认读者已经看过 `module-skill-mcp`、`module-agent-client`、`module-commons-grpc` 三个 L1。
- 用户明确限制本次只能写入 `teach/open-java/snail-ai/slice-mcp-skill-tools/**`，因此不更新 `teach/open-java/snail-ai/index.md`、`_progress.*` 或其他主题目录。
- 课程主线固定为“绑定 -> 描述符 -> gRPC dispatch -> resolver -> `ToolCallback`/`read_skill` -> 模型工具调用 -> cleanup”。
- 当前源码中 MCP 的 `authType` 与 `authConfig` 会保存并下发到 descriptor，但 Client resolver 没有消费它们；reference 需要把这个现状单独列为调试点。
- 当前源码中 SSE transport 保留在枚举和文档中，但 Server 测试连接与 Client resolver 都把 SSE 视为 MCP SDK 2.x deprecated，不会真正注册工具。

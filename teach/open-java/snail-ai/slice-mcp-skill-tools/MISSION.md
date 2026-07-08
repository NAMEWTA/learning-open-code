# 使命：L2 MCP 与 Skill 工具注入

## 为什么
学习者需要能把 Snail AI 中一次 Agent 对话的工具来源追完整：从 Agent 绑定 MCP/Skill，到 Server 下发描述符，再到 Client 把 MCP server 和 Skill 转成 Spring AI 可调用的工具。掌握这条链路后，遇到 MCP 工具缺失、`read_skill` 不可用、Skill 支撑文件没落盘或对话结束后资源未释放时，可以按源码边界定位问题。

## 成功的样子
- 能说清 Agent 创建/更新时 MCP 与 Skill 关联表如何写入，并在对话时如何被 Handler 读取。
- 能把 `McpHandler`、`SkillAgentChatHandler` 产出的描述符映射到 `ChatDispatchRequest` 字段。
- 能解释 `/chat/dispatch` 到 Client 后，`ToolRuntime` 按什么顺序解析 MCP、基础工具、RAG、Skill 和本地 `@Tool`。
- 能说明 `read_skill` 如何回调 Server 获取完整 Skill 内容与支撑文件，并把文件物化到临时目录。
- 能用 checklist 排查 transport、认证字段、support files、模型工具调用和 cleanup 的常见失败点。

## 约束条件
- 源项目根目录固定为 `open-java/snail-ai`，课程以当前 checkout 源码为准。
- 本主题是 L2 垂直切片，默认读者已看过 `module-skill-mcp`、`module-agent-client`、`module-commons-grpc` 三个 L1。
- lesson 控制为 15 分钟内完成，长表格、DTO 字段和调试清单放入 reference。
- 本次只写入 `teach/open-java/snail-ai/slice-mcp-skill-tools/**`，不修改 Snail AI 源码、项目索引、进度文件或其他主题目录。

## 不在范围内
- 不实现新的 MCP 认证注入、连接池或工具治理方案。
- 不展开 Spring AI 内部 tool calling 的完整源码，只讲 Snail AI 把 callbacks 交给 `ChatClient` 的边界。
- 不复述 Admin UI、Skill 上传编辑器或 gRPC 基础设施的 L1 全量内容。

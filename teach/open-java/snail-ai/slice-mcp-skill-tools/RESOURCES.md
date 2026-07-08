# MCP 与 Skill 工具注入资源

## 知识

- [Skill 与 MCP L1](../module-skill-mcp/lessons/0001-skill-mcp-module-tour.html)
  用于复习 Skill/MCP 从 Admin 配置到 Client 工具执行的模块边界。
- [Agent Client L1](../module-agent-client/lessons/0001-agent-client-module-tour.html)
  用于复习 Client gRPC handler、`ChatSessionRuntime`、`ToolRuntime` 和 `DefaultChatClientFactory`。
- [Commons 与 gRPC L1](../module-commons-grpc/lessons/0001-commons-grpc-module-tour.html)
  用于复习 `/chat/dispatch` 统一 gRPC 信封、URI 分发和 Client 回调 Server 的协议边界。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/agent/AgentService.java`
  Agent 创建/更新时保存 MCP 与 Skill 绑定关系的入口。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/McpHandler.java`
  Server 对话链中按 Agent 读取 MCP 绑定并生成 `McpServerDescriptor` 的核心源码。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/SkillAgentChatHandler.java`
  Server 对话链中按 Agent 读取 Skill 绑定并生成 `SkillDescriptor` 的核心源码。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/LlmCallHandler.java`
  把 MCP/Skill 描述符装入 `ChatDispatchRequest` 并通过 `/chat/dispatch` 下发 Client 的边界。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/runtime/tool/ToolRuntime.java`
  Client 一次对话解析工具集合的顺序与 cleanup 入口。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/resolver/ClientMcpToolResolver.java`
  Client 根据 MCP 描述符连接 Streamable HTTP 或 Stdio server，并转成 Spring AI `ToolCallback`。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/resolver/ClientSkillToolResolver.java`
  Client 追加 Skill 渐进式披露提示，并注册 `read_skill` 工具。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/tool/ReadSkillTool.java`
  `read_skill` 回调 Server、缓存 Skill 内容、异步物化支撑文件的核心源码。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/executor/client/DefaultChatClientFactory.java`
  将已解析工具注入 `defaultTools` 并启用 `ToolCallingAdvisor` 的源码边界。
- `open-java/snail-ai/docs/guide/mcp/transport.md`
  MCP transport 文档；用于和源码中的 SSE deprecated、Streamable HTTP、Stdio 实际行为对照。
- `open-java/snail-ai/docs/guide/mcp/auth.md`
  MCP auth 文档；用于识别文档声明和当前 runtime 未消费 `authConfig` 的差异。

## 智慧（社区）

- [Snail AI Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  项目真实协作入口；适用于追踪 MCP/Skill 工具注入契约的 issue、PR 和提交历史。
- [Snail AI GitHub 镜像](https://github.com/aizuda/snail-ai)
  README 给出的镜像入口；适用于检索公开讨论和对照社区反馈。
- 本地源码评审：`open-java/snail-ai`
  当前课程以工作区实际 checkout 为准；当文档、注释和实现不一致时，优先回到源码、DTO 和调用点核对。

## 空白

- 当前未发现覆盖“Agent 绑定 MCP/Skill -> `/chat/dispatch` -> Client resolver -> 模型 tool call -> cleanup”的端到端自动化测试；本主题判断主要来自源码阅读。
- 当前未发现 runtime 已应用 MCP `authConfig` 的实现；配置字段和文档存在，但 `ClientMcpToolResolver` 与 `McpToolService` 的连接构造未把认证信息注入 transport。
- 当前未发现 Skill 支撑文件物化完成后再允许模型访问文件的同步屏障；`ReadSkillTool` 返回 `skillContent` 后通过虚拟线程异步写文件。

# Skill 与 MCP 能力模块资源

## 知识

- [Skill/MCP 模块构建 API（L3）](./reference/skill-mcp-api.html)
  `snail-ai-feature-skill` 的 Maven 坐标、依赖声明与 slice-mcp-skill-tools 运行时边界对照。
- [`snail-ai-feature-skill/pom.xml`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-skill/pom.xml)
  本主题 L3 主源码：模块坐标、父 POM、直接依赖清单。
- [`SkillHandler.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-skill/src/main/java/com/aizuda/snail/ai/features/skill/handle/SkillHandler.java)
  Server 侧按 Agent 绑定读取 `SkillPO` 列表，供 `SkillAgentChatHandler` 生成描述符。
- [`SkillContentCallbackHandler.java`](../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-skill/src/main/java/com/aizuda/snail/ai/features/skill/handle/SkillContentCallbackHandler.java)
  Client `read_skill` 经 gRPC 回调 Server 获取 Skill 正文与支撑文件的 Handler。
- [MCP 与 Skill 工具注入切片（L2）](../slice-mcp-skill-tools/reference/mcp-skill-tools-flow-map.html)
  一次对话从绑定到 `ToolRuntime` 解析与 cleanup 的垂直切片；用于对照 feature-skill 在链路中的两段参与点。
- [L0 项目地图](../00-overview/lessons/0001-project-map.html)
  用于确认 Snail AI 的 Server、Agent Client、Persistence 和 Docs 顶层分层。
- [Agent 责任链模块导览](../module-agent-chain/lessons/0001-agent-chain-module-tour.html)
  用于衔接 `McpHandler`、`SkillAgentChatHandler` 与 `LlmCallHandler` 的 Server 端上下文装配边界。
- [Agent Client 执行层模块导览](../module-agent-client/lessons/0001-agent-client-module-tour.html)
  用于衔接 Client 端 `ToolRuntime`、`ClientSkillToolResolver`、`ClientMcpToolResolver` 和 `ChatClient` 工具注入边界。
- `open-java/snail-ai/docs/guide/skill/index.md`
  官方 Skill 概念、生命周期和包结构说明；阅读时需以当前源码的渐进式 `read_skill` 行为为准。
- `open-java/snail-ai/docs/guide/skill/create.md`
  Skill 在线创建、ZIP 上传、frontmatter、导出和删除流程说明。
- `open-java/snail-ai/docs/guide/skill/file-editor.md`
  Skill 在线文件编辑器说明，可对照 `SkillController` 的文件树、内容保存、重命名和删除接口。
- `open-java/snail-ai/docs/guide/mcp/index.md`
  官方 MCP 集成概览、API 清单和绑定关系说明；认证类型描述需要和当前枚举源码核对。
- `open-java/snail-ai/docs/guide/mcp/auth.md`
  MCP 认证配置说明；`SNAPSHOT.md` 已引用，阅读时需和 `McpAuthTypeEnum`、`McpServerPO`、Client resolver 的实际注入边界对照。
- `open-java/snail-ai/docs/guide/mcp/transport.md`
  MCP SSE、Streamable HTTP、Stdio 的配置说明；当前源码中 SSE 在 SDK 2.x 下被标记为废弃并跳过或报错。
- `open-java/snail-ai/docs/sql/snail_ai_schema.sql`
  Skill、Skill 文件、MCP Server、Agent 关联表结构的一手数据库定义。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/SkillController.java`
  Skill 管理和在线文件编辑 API 入口。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/McpServerController.java`
  MCP Server 管理、连接测试和列表 API 入口。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/McpHandler.java`
  Server 责任链中 MCP 配置转描述符的核心实现。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/SkillAgentChatHandler.java`
  Server 责任链中 Skill 配置转描述符的核心实现。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/runtime/tool/ToolRuntime.java`
  Client 工具集合统一解析入口，是本主题最重要的执行边界。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/resolver/ClientSkillToolResolver.java`
  Skill 描述符转 `read_skill` 工具和系统提示词追加的实现。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/resolver/ClientMcpToolResolver.java`
  MCP 描述符转 Spring AI `ToolCallback` 的实现。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/tool/ReadSkillTool.java`
  Client 运行时读取 Skill 完整内容、缓存并物化支撑文件的实现。

## 智慧（社区）

- [Snail AI Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  项目真实协作入口；适用于核对 Issue、提交源码疑问和观察 Skill/MCP 模块演进。
- 本地源码评审：`open-java/snail-ai`
  当前课程以工作区实际 checkout 为准；当官方文档、SQL 注释和 Java 源码不一致时，优先回到源码和测试验证。

## 空白

- 当前未发现覆盖 `ClientSkillToolResolver`、`ReadSkillTool`、`ClientMcpToolResolver`、`ToolRuntime`、`SkillService` 或 `McpServerService` 的直接单元测试。
- MCP 认证配置在当前 Client resolver 中尚未实际注入到 transport 构建流程，后续 L2/L3 学习需要结合运行环境验证。
- 官方 MCP 文档对认证类型的描述与 `McpAuthTypeEnum`、SQL 注释存在差异，本主题只按当前源码和枚举讲解。

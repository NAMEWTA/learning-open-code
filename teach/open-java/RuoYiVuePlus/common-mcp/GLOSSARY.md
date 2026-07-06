# ruoyi-common-mcp MCP 模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**MCP (Model Context Protocol)**：
Anthropic 提出并已演化为行业标准的开放协议，定义了 AI 应用与外部数据源 / 工具之间的通信规范。核心模型为 Client-Server 架构，提供 Tools（工具调用）、Resources（资源读取）、Prompts（提示模板）三大原语。本模块通过 Spring AI 的 Java 实现来使用该协议。
_Avoid_: 「MCP 是某个 AI 模型的功能」（它是独立于模型的通信协议）。

**Spring AI MCP**：
Spring AI 项目对 MCP 协议的 Java 实现（本项目使用 2.0.0 版本）。提供 `spring-ai-starter-mcp-server-webmvc`（服务端）和 `spring-ai-starter-mcp-client`（客户端）两个 Starter，将 MCP 的 SSE 传输、JSON-RPC 消息、Lifecycle 管理等底层细节封装为 Spring Boot 自动配置。
_Avoid_: 「Spring AI 的 MCP 功能已内置在 spring-boot-starter 中」（独立 Starter，需要显式依赖）。

**McpSyncClient**：
Spring AI MCP 提供的同步客户端接口（`io.modelcontextprotocol.client.McpSyncClient`）。一个 `McpSyncClient` 实例代表与一个 MCP Server 的已初始化连接，提供 `listTools()` / `callTool()` / `readResource()` / `getServerInfo()` 等方法。本模块的 `McpClientTemplate` 直接持有 `List<McpSyncClient>` 来管理多个连接。
_Avoid_: 「MCP 客户端 Bean」（它是由 Spring AI 的 Bootstrap 创建的，不是本模块创建的）。

**McpClientTemplate**：
本模块的核心模板类（`core/McpClientTemplate.java`），封装了对 `List<McpSyncClient>` 的遍历操作。提供 `listTools()` / `callTool()` / `readResource()` / `findClient()` 方法，支持按 Server 名称精确调用或广播到所有 Server。业务代码通过它间接使用 MCP，不必直接操作 `McpSyncClient` 列表。
_Avoid_: 「MCP 服务层」（它是一个模板/工具类，不涉及 MCP Server 端的业务逻辑）。

**McpToolCallResult**：
本模块定义的工具调用结果 Record（`core/McpToolCallResult.java`）。将 MCP SDK 的 `McpSchema.CallToolResult` 转换为带 `serverName` 标记的项目结果对象。核心字段：`serverName`（来源 Server 名称）、`error`（是否出错）、`content`（文本内容列表）、`structuredContent`（结构化数据）。
_Avoid_: 「工具返回值」（它是对 CallToolResult 的包装，附加了 serverName 上下文）。

**McpResourceReadResult**：
本模块定义的资源读取结果 Record（`core/McpResourceReadResult.java`）。将 MCP SDK 的 `McpSchema.ReadResourceResult` 转换为带 `serverName` 标记的项目结果对象。核心字段：`serverName`（来源 Server 名称）、`contents`（资源内容列表 `List<ResourceContents>`）。
_Avoid_: 「资源文件内容」（它是 ResourceContents 的集合，ResourceContents 可以是文本或二进制 Blob）。

**McpAutoConfiguration**：
本模块的 Spring Boot 自动配置类（`config/McpAutoConfiguration.java`）。用 `@AutoConfiguration` 声明 + `.imports` 文件注册，用 `@ConditionalOnBean(McpSyncClient.class)` 确保仅当用户配置了 MCP Server 连接后才创建 `McpClientTemplate` Bean，用 `@ConditionalOnMissingBean` 允许业务方覆盖。
_Avoid_: 「MCP 配置类」（它是 Spring Boot 自动配置类，不负责 MCP Server 连接参数的具体配置——那些在 application.yml 的 `spring.ai.mcp.client.connections` 下）。

**Tool 与 Resource（MCP 原语）**：
MCP 协议的两种核心交互原语。**Tool**（工具）允许 Client 调用 Server 暴露的函数（有参数、有返回），语义类似 RPC；**Resource**（资源）允许 Client 读取 Server 暴露的数据（如文件内容、数据库记录），语义类似 REST GET。Spring AI MCP 中分别对应 `McpSchema.Tool` 和 `McpSchema.Resource`。
_Avoid_: 「MCP 的 API 接口」（用原语（primitive）更准确，它们是协议层的概念，非 HTTP API）。

**CallToolRequest / CallToolResult**：
Spring AI MCP 定义的工具调用请求/响应类型（`io.modelcontextprotocol.spec.McpSchema`）。`CallToolRequest` 封装 `toolName` + `arguments`；`CallToolResult` 封装 `content`（文本片段）+ `isError`（是否出错）+ `structuredContent`。本模块的 `McpClientTemplate.callTool()` 底层就调用 `client.callTool(new CallToolRequest(name, args))`。
_Avoid_: 「HTTP 请求/响应」（底层走 MCP 协议的 JSON-RPC，非 HTTP 语义）。

**ReadResourceRequest / ReadResourceResult**：
Spring AI MCP 定义的资源读取请求/响应类型（`io.modelcontextprotocol.spec.McpSchema`）。`ReadResourceRequest` 封装 `uri`（资源地址）；`ReadResourceResult` 封装 `contents`（`List<ResourceContents>`，每个可能是 TextResourceContents 或 BlobResourceContents）。本模块的 `McpClientTemplate.readResource()` 底层就调用 `client.readResource(new ReadResourceRequest(uri))`。
_Avoid_: 「文件下载请求」（资源 URI 是由 MCP Server 定义的协议级标识符，不一定是文件系统路径）。

## 待收录
- 随着课程深入，可补充「SSE Transport」「Streamable HTTP」「Prompts 原语」等术语。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

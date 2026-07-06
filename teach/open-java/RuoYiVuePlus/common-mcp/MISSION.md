# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-mcp MCP 通信模块

## Why
学习者要能彻底读懂 `ruoyi-common-mcp` 这个公共模块：它只有 4 个 Java 类，是对 **Spring AI MCP**（Model Context Protocol）框架的一层「项目化封装」。理解它，等于理解 RuoYi-Vue-Plus 如何把 Anthropic 提出的 MCP 协议（已演化为 AI 行业标准）通过 Spring AI 的官方 Starter 接入企业级 Java 项目——用 Spring Boot 自动配置实现零代码接入、用一个模板类封装 `McpSyncClient` 的常用操作、用 Record 结果模型统一多 Server 返回格式。达到能给同事讲清「什么是 MCP 协议、本项目怎么用它」「为什么 4 个类就能让 Java 应用获得 AI 工具调用能力」「如何通过 McpClientTemplate 调用外部 MCP Server 的工具和资源」，并能在此基础上对接公司自己的 MCP Server 或排查工具调用失败的完整链路。重点是**读懂 MCP 协议的 Client/Server 模型与 Spring AI 如何桥接到 Java**，不是从零实现 MCP 传输层。

## Success looks like
- 能用一句话说清 MCP 协议是什么，以及 `ruoyi-common-mcp` 与 Spring AI MCP 的关系。
- 能画出 MCP Client-Server 通信模型图，说出 `McpSyncClient` 在其中的角色。
- 能解释 `McpAutoConfiguration` 如何通过 `@AutoConfiguration` + `@ConditionalOnBean(McpSyncClient.class)` + `AutoConfiguration.imports` 实现「只有当项目中配置了 MCP Server 连接时才自动创建模板 Bean」。
- 能讲清 `McpClientTemplate` 的 6 个核心方法（`listTools`、`callTool` 两个重载、`readResource` 两个重载、`findClient`）各自做什么，以及为什么业务代码不直接操作 `List<McpSyncClient>`。
- 能区分 `McpToolCallResult` 和 `McpResourceReadResult` 两个 Record 的结构差异，并说出它们如何对齐 MCP 协议中的 `CallToolResult` 和 `ReadResourceResult`。
- 能通过 `McpClientTemplate.callTool(serverName, toolName, arguments)` 调用指定 Server 的工具，并正确解析返回的 `McpToolCallResult.content()` 和 `structuredContent()`。
- 能通过 `McpClientTemplate.readResource(serverName, uri)` 读取指定 Server 的资源，并正确解析 `McpResourceReadResult.contents()`。
- 能读懂 pom.xml 中的 `spring-ai-starter-mcp-server-webmvc` + `spring-ai-starter-mcp-client` 两个依赖各自的作用。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java + MCP 协议，讲解聚焦后端 Java 调用 MCP Server，但会在适当的练习中联系「AI 应用 / LLM Agent 如何通过 MCP 获取外部能力」。
- 目标是「读懂」而非「能改造 Spring AI」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述调用链路」为主。
- 全部讲解基于仓库真实代码与 Spring AI MCP 2.0.0 源码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- MCP 协议的底层传输实现（SSE / stdio / Streamable HTTP）——只讲协议概念与 Java 调用，不讲 Go/Python 的 MCP SDK 实现。
- Spring AI MCP Server 端的实现细节——本模块侧重 Client 端的使用封装。`spring-ai-starter-mcp-server-webmvc` 依赖仅提及，不深入 Server 端注解与注册机制。
- LLM / ChatModel / Function Calling 的完整链路——仅在解释「MCP 工具对大模型意味着什么」时点到。
- 具体 MCP Server 的部署（如文件系统 Server、数据库 Server、天气 API Server）——只用假想场景演示调用方式。

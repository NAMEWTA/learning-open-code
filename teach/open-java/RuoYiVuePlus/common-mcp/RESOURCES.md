# ruoyi-common-mcp MCP 模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（含 Spring AI MCP 2.0.0 源码）。以下外部资源用于补充 MCP 协议规范与 Spring AI 官方说明。

## Knowledge

- [官方规范: _MCP 协议规范 (Model Context Protocol)_ — Anthropic (modelcontextprotocol.io)](https://modelcontextprotocol.io/)
  理解 MCP 协议的权威来源。涵盖协议架构、Lifecycle、Tools/Resources/Prompts 三大原语、传输层（SSE/stdio/Streamable HTTP）。本模块一切 Java 调用的协议层语义来自此规范。
- [代码: _ruoyi-common-mcp 模块四件套_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-mcp/src/main/java/org/dromara/common/mcp/)
  `McpAutoConfiguration` / `McpClientTemplate` / `McpToolCallResult` / `McpResourceReadResult`。任何关于「这个模块做了什么」的问题，最终答案在这四个文件里。
- [官方文档: _Spring AI MCP 文档_ — Spring (spring.io)](https://docs.spring.io/spring-ai/reference/api/mcp.html)
  Spring AI 对 MCP 协议的 Java 实现文档。理解 `McpSyncClient` 接口、配置项、Bootstrap 流程时查阅。本模块的 `McpClientTemplate` 直接封装的就是 `McpSyncClient`。
- [代码: _Spring AI MCP 2.0.0 源码_ — spring-ai-mcp](https://github.com/spring-projects/spring-ai)
  `McpSyncClient` 接口定义、`McpSchema`（Tool/Resource/CallToolRequest/ReadResourceRequest）、`McpClient` 抽象实现。理解 `McpClientTemplate` 里 `client.listTools()` / `client.callTool()` / `client.readResource()` 的返回结构时对照查阅。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li (plus-doc)](https://plus-doc.dromara.org/)
  本项目设计说明，含自动配置规范、common 模块设计范式。理解 `McpAutoConfiguration` 的设计约定时查阅。
- [官方规范: _MCP Specification (Markdown)_ — GitHub (modelcontextprotocol/specification)](https://github.com/modelcontextprotocol/specification)
  MCP 协议的 GitHub 仓库，含详细的技术规范、变更日志、示例。理解协议细节时查阅。

## Wisdom (Communities)

- [社区: _Spring AI GitHub Issues_](https://github.com/spring-projects/spring-ai/issues)
  遇到 Spring AI MCP 集成问题（如 `McpSyncClient` 初始化失败、连接管理行为）时，Issues 区是最及时的官方回应来源。
- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  了解 RuoYi 维护者如何为本模块选型 Spring AI MCP、以及社区实际使用中遇到的问题。

## Gaps
- 暂无显著缺口。MCP 协议规范仍在活跃演进中（当前版本仍较新），建议关注 modelcontextprotocol.io 的更新。Spring AI MCP 2.0.0 对应 MCP 协议某一稳定版本，如有大版本升级，需重新对照。

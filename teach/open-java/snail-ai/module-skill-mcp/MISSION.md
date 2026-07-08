# 使命：Skill 与 MCP 能力模块

## 为什么
学习者需要看清 Snail AI 中可配置能力如何从 Admin 页面进入 Agent 对话执行边界。掌握这个主题后，学习者能判断一个工具不可用、Skill 内容没被读取、MCP 连接失败或临时禁用能力时，应该查 Admin 配置、Server 责任链、gRPC DTO，还是 Agent Client 的 resolver。

## 成功的样子
- 能把 Skill、MCP Server 从创建、绑定、对话分发到 Client 工具解析说成一条完整链路。
- 能定位 Admin 控制器、服务、PO/VO/DTO、枚举、Server Handler、Client resolver 的具体源码文件。
- 能判断 `read_skill`、MCP ToolCallback、base tools、RAG/custom tools 的执行边界和资源清理时机。
- 能读出 `snail-ai-feature-skill` 的 Maven 坐标、直接依赖各自职责，并说明 MCP/Skill 运行时哪些阶段落在本 jar、哪些落在 `feature-agent`、`feature-model` 与 Agent Client。

## 约束条件
- 本主题是 L1 模块总览，lesson 必须保持 15 分钟内完成。
- 长清单、源码索引、时序图和易错点放入 `reference/skill-mcp-overview.html`。
- 只读源项目，不修改 `open-java/snail-ai` 源码。

## 不在范围内
- 不展开 Spring AI MCP SDK 的底层协议实现。
- 不实现或调试真实 MCP Server。
- 不深挖 RAG、Memory、模型适配器和完整 SSE 回写细节。

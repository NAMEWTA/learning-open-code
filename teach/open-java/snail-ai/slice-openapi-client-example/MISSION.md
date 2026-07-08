# 使命：L2-slice-openapi-client-example（OpenAPI Client 示例）

## 为什么
用户需要从示例工程和 SDK 客户端侧看懂一次 OpenAPI chat 调用如何发出去、如何回流，以及它和 Server OpenAPI 入口之间的边界。掌握后可以快速定位认证头错误、URL/context path 拼错、SSE 没有事件、同步响应为空、示例工程和源码文档不一致这几类集成问题。

## 成功的样子
- 能画出 `示例 /demo 接口 -> OpenApiChatClient 动态代理 -> OpenApiHttpInvokeHandler -> Server OpenAPI Controller -> OpenAPI Chat 服务` 的调用链。
- 能说明 `Snail-Ai-App-Id`、`Snail-Ai-Token`、`snail-ai.openapi.prefix`、`web-port` 分别在哪里读取和使用。
- 能区分 SDK 的 `chatStream`、`chatSync`、`SnailAiOpenApi.ChatBuilder#stream`、`SnailAiOpenApi.ChatBuilder#execute` 四种调用表面。
- 能解释 `text`、`thinking`、`done`、`error` 四类 SSE event 在 SDK 侧如何被解析，以及同步响应只返回哪些字段。
- 能把示例工程的 `/demo/**` 边界和 Server 的 `/snail-ai/openapi/v1/**` 边界对应起来。

## 约束条件
- 教学内容只基于当前 `open-java/snail-ai` 源码、相关文档和已有 `slice-openapi-chat` 主题。
- 本次只写入 `teach/open-java/snail-ai/slice-openapi-client-example/`，不修改源码、项目索引、进度文件或其他主题目录。
- 第一节课控制在 15 分钟内完成；长表格、源码索引、错误边界和调试清单放入 reference。

## 不在范围内
- 不修复示例工程、SDK 或文档中的不一致。
- 不展开 Agent 责任链、gRPC Client 执行、模型 provider、RAG、MCP 和 Skill 的内部实现。
- 不教授 Admin 登录态、嵌入式 Chat UI Token 或浏览器前端工程。

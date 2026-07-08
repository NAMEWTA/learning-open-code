# 便签

- 用户要求生成 L2 垂直切片主题 `L2-slice-openapi-client-example`，目标是 OpenAPI Client 示例。
- 本次只允许写入 `teach/open-java/snail-ai/slice-openapi-client-example/**`，不得编辑源码、`index.md`、`_progress.*` 或其他主题目录；因此没有按 teach skill 的默认规则更新项目索引。
- `snail-ai-agent-example` 当前是独立 Spring Boot 示例应用：它的 `pom.xml` 使用 Spring Boot parent，依赖 `snail-ai-openapi-starter`，没有出现在根 `open-java/snail-ai/pom.xml` 的 reactor `modules` 中。
- 示例工程同时包含 Agent Client 能力和 OpenAPI Client 示例：启动类使用 `@EnableSnailAiAgent`，`OpenApiDemoController` 注入 SDK 类型化客户端并暴露 `/demo/**`。
- SDK 自动配置的 canonical prefix 是 `snail-ai.openapi`；示例配置文件中写作 `snail-ai.open-api`，排查绑定问题时应同时检查配置键、metadata 和 Spring Boot relaxed binding。
- 当前源码中的 `SnailAiOpenApi.ChatBuilder#stream()` 返回 `Flux<OpenApiChatStreamEvent>`，不是文档里的 `listener(...)` 回调式 API。
- `OpenApiChatRequest.conversationId` 在源码上标注 `@NotBlank`；示例工程流式入口把它作为可选 query 参数，按源码推导，不传可能被 Server 参数校验拒绝。
- OpenAPI 流式 SDK 只按 SSE 的 `event:` 和 `data:` 行解析；如果认证或参数校验在进入流前返回普通 JSON envelope，SDK 可能只完成 Flux 而不产生业务事件，需要看 HTTP body、Server 日志或直接 curl。

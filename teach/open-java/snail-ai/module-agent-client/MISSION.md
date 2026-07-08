# 使命：Agent Client 执行层模块

## 为什么
学习者已经理解 Server 端 Agent 责任链的上下文装配边界，现在需要看清 Agent Client 如何接收 gRPC 分发、构建 Spring AI ChatClient，并在本地运行 Advisor、Interceptor 与 Tool。这个主题帮助学习者判断自定义工具、模型调用、客户端日志和流式回传问题应该落在哪一层排查。

## 成功的样子
- 能把 Server 端 `LlmCallHandler` 之后的 Client 执行路径说成 5 个阶段。
- 能定位启动配置、gRPC 分发、ChatClient 构建、Advisor、Tool resolver、模型工厂各自所在源码。
- 能判断新增自定义 `@Tool`、`SnailAiInterceptor` 或模型配置校验时应改哪个扩展点。
- 能按子模块查阅 `reference/agent-client-api.html`：Chat starter、Executor core、OpenAPI client、Common 工具的方法签名与启用注解。

## 约束条件
- 本主题是 L1 模块总览，lesson 必须保持 15 分钟内完成。
- 长接口清单、源码索引和注意事项放入 `reference/agent-client-overview.html`；L3 微观 API 放入 `reference/agent-client-api.html`。
- 只读源项目，不修改 `open-java/snail-ai` 源码。

## 不在范围内
- 不展开完整流式 chunk 切片和 SSE 回写细节。
- 不深挖 Server 端 Handler 责任链，已由 `module-agent-chain` 承接。
- 不讲具体模型适配器内部实现，后续由模型模块主题承接。

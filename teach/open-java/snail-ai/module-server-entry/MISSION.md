# 使命：Server API 入口模块

## 为什么
学习者希望在 Snail AI 源码中快速判断一个 HTTP 请求从哪个入口进入、使用哪套认证、如何变成业务服务调用，以及什么时候返回普通 JSON 或 SSE 流。掌握这层边界后，后续排查 Admin、OpenAPI、Agent 对话和 RAG 接口问题时，可以先定位入口再深入业务链路。

## 成功的样子
- 能区分 Admin API 的 `Snail-Ai-Auth` 与 OpenAPI 的 `Snail-Ai-App-Id` / `Snail-Ai-Token`，并找到对应拦截器。
- 能根据 URL 路径定位到 Admin 或 OpenAPI Controller，再判断它委托给哪个服务层。
- 能识别流式接口的响应边界，说明 `Flux`、`ServerSentEvent` 与同步收集器分别出现在哪里。
- 能使用 `reference/server-entry-overview.html` 把握入口边界，并用 `reference/server-entry-api.html` 按业务域查端点、VO 字段与流式事件类型。

## L3 补充交付（API 速查）
- `reference/server-entry-api.html` 覆盖 Admin 13 个 Controller 与 OpenAPI 5 个 Controller 的全部 REST 端点。
- 按用户/认证、智能体、对话、RAG、记忆 VO、Skill、MCP、模型、应用、资源、OpenAPI 分节，含请求/响应 VO 字段与三种 Admin 流式 + OpenAPI SSE 事件类型。
- 记忆域注明当前无 `MemoryController`，记忆通过智能体配置字段启用。

## 约束条件
- 本主题是 L1 模块课，每节 lesson 控制在 15 分钟内完成。
- 只讲入口层的控制器、认证拦截、路径边界和响应边界。
- 以当前工作区源码和项目文档为准，不依赖尚未完成的同级主题。

## 不在范围内
- 不展开 Agent 责任链内部 Handler 算法。
- 不展开 RAG 检索、模型适配、gRPC Client 执行细节。
- 不讲管理后台前端页面实现。

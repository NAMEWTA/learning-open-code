# Server API 入口模块资源

## 知识

- [源码：Admin Controller 集合](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/)  
  管理后台 REST/SSE 入口集合。适用于：按业务域定位 Admin 请求入口和 `@LoginRequired` 使用方式。
- [源码：Admin 认证拦截器](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/interceptor/AuthenticationInterceptor.java)  
  `Snail-Ai-Auth`、JWT 校验、角色校验、`UserSessionUtils` 写入与清理。适用于：理解管理端认证边界。
- [源码：OpenAPI Controller 集合](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/controller/)  
  外部集成接口入口集合。适用于：查询智能体、用户、会话、流式/同步对话和嵌入式 Token 的入口。
- [源码：OpenAPI App 鉴权](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/interceptor/OpenApiAuthInterceptor.java)  
  `Snail-Ai-App-Id`、`Snail-Ai-Token`、应用状态、Token 比较和 OpenAPI 会话写入。适用于：区分外部应用凭证与 Admin 登录态。
- [源码：OpenAPI MVC 配置](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/config/OpenApiWebMvcConfiguration.java)  
  将 OpenAPI 拦截器注册到 `/openapi/**`。适用于：理解 servlet context path 与控制器路径的组合。
- [源码：OpenAPI 流式输出收集器](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/stream/CollectingChatStreamWriter.java)  
  同步对话把流式回调收集为完整文本的边界。适用于：比较 `chat` 与 `chatSync`。
- [文档：OpenAPI 概述](../../../../open-java/snail-ai/docs/api/openapi/index.md)  
  面向第三方系统的接口前缀、认证方式、接口范围和 Admin/OpenAPI 差异。适用于：快速核对外部调用口径。
- [文档：OpenAPI 认证方式](../../../../open-java/snail-ai/docs/api/openapi/auth.md)  
  明确 `Snail-Ai-App-Id` / `Snail-Ai-Token` 与 `Snail-Ai-Auth` 的适用场景。适用于：排查认证头混用。
- [配置：应用默认端口与 context path](../../../../open-java/snail-ai/snail-ai-starter/src/main/resources/application.yml)  
  `server.port: 8900` 与 `server.servlet.context-path: /snail-ai`。适用于：把源码路径常量还原为外部 URL。
- [源码：Admin VO/DTO 集合](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/vo/)  
  全部请求/响应 VO，含 agent、rag、knowledge、memory、skill、mcp、model、app 子包。适用于：核对 API 参考中的字段定义。
- [源码：Admin 流式 DTO](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/dto/)  
  `ChatStreamEvent`、`AgentCreateStreamEvent`、`RagQaStreamEvent`。适用于：理解 Admin 三种流式事件的 type 与载荷。
- [源码：Admin 流式适配器](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/stream/)  
  `AgentCreateStreamHttpAdapter`、`RagQaStreamHttpAdapter`、`AdminStreamMediaTypes`。适用于：确认 NDJSON 编码边界。
- [源码：Admin 异常与响应包装](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/handler/)  
  `RestExceptionHandler`、`GlobalRestfulResponseBodyAdvice`。适用于：理解非流式自动包 Result 与流式错误格式。
- [源码：OpenAPI 公共 DTO](../../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/openapi/dto/)  
  `OpenApiChatRequest`、`OpenApiChatStreamEvent`、`OpenApiAgentVO` 等。适用于：OpenAPI 对外契约核对。
- [源码：OpenAPI 路径常量](../../../../open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/constants/OpenApiPathConstants.java)  
  `/openapi/v1` 下全部路径常量。适用于：还原外部 URL。
- [参考：L3 API 速查](./reference/server-entry-api.html)  
  按业务域列出的完整 REST 端点、VO 字段与流式事件表。适用于：接口联调与源码追踪起点。

## 智慧（社区）

- [Snail AI Gitee Issues](https://gitee.com/aizuda/snail-ai/issues)  
  官方源码仓库的问题讨论区。适用于：验证接口文档与实际源码不一致、反馈认证或 OpenAPI 调用问题。

## 空白

- 当前工作区未发现 `snail-ai-server-admin` 或 `snail-ai-server-openapi` 下针对 Controller、拦截器、OpenAPI Chat 的专属 `src/test` 用例；后续如果要做行为校验，需要补充集成测试或 MockMvc/WebFlux 测试资源。

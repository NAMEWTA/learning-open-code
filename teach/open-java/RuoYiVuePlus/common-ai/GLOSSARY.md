# ruoyi-common-ai AI 模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**Snail AI Agent**：
aizuda 社区出品的开源 AI Agent 框架。提供三个 Spring Boot Starter：chat-starter（聊天网关）、executor-starter（执行器调度）、openapi-starter（OpenAPI 客户端）。`ruoyi-common-ai` 的全部 AI 能力来自它。
_Avoid_: 「AI 大模型」（Snail AI Agent 是框架层，模型是底层能力提供方）。

**SnailAiConfig**：
RuoYi 对 Snail AI Agent 的自动配置类（`org.dromara.common.ai.config.SnailAiConfig`）。用 `@AutoConfiguration` + `@ConditionalOnProperty(prefix="snail-ai", name="enabled")` + `@EnableSnailAiAgent` + `@EnableSnailAiOpenApi` 四个注解实现「配置开关控制、三合一自动激活」。
_Avoid_: 「AI 配置类」（太泛，这个类的职责是激活 Snail AI 框架的两个核心能力）。

**@EnableSnailAiAgent**：
Snail AI Agent 框架的启用注解，来自 `snail-ai-agent-chat-starter`。激活后自动注册聊天网关控制器、聊天服务等核心 Bean。被 [[glossary:SnailAiConfig]] 引用。
_Avoid_: 「启用 Agent」（不加框架名，容易和 Spring AI 等其它 Agent 框架混淆）。

**@EnableSnailAiOpenApi**：
Snail AI Agent 框架的 OpenAPI 启用注解，来自 `snail-ai-openapi-starter`。激活后自动注册 OpenAPI 客户端相关 Bean，使应用能调用外部 AI 模型的 OpenAPI 接口。被 [[glossary:SnailAiConfig]] 引用。

**SnailAiChatGatewayController**：
Snail AI Agent 框架自带的聊天网关控制器（`com.aizuda.snail.ai.agent.chat.starter.SnailAiChatGatewayController`），映射到 `/api/snail/chat/**` 路径。由 Snail AI 前端 SDK 直接消费，其响应格式为框架自定义的 `Result` 对象。[[glossary:SnailAiChatExceptionHandler]] 通过 `assignableTypes` 精确绑定到此控制器。
_Avoid_: 「聊天控制器」（省略了 "Gateway"，它不只是聊天，是聊天能力的网关入口）。

**SnailAiChatExceptionHandler**：
AI 模块的定点异常处理器（`org.dromara.common.ai.handler.SnailAiChatExceptionHandler`）。用 `@RestControllerAdvice(assignableTypes = SnailAiChatGatewayController.class)` 精确绑定到 Snail AI 聊天网关，用 `@Order(HIGHEST_PRECEDENCE)` 确保优先级最高。覆盖 8 种异常类型，全部返回 Snail AI SDK 的 `Result<Void>` 格式，而非 RuoYi 通用的 `R` 格式——这是「响应格式边界隔离」的关键设计。
_Avoid_: 「全局异常处理器」（它不是全局的，只作用于 Snail AI Chat 接口）。

**Result (Snail AI)**：
Snail AI Agent 框架的通用响应对象（`com.aizuda.snail.ai.common.model.Result`），字段为 `status (int)` / `message (String)` / `data (T)`。与 RuoYi 的 `R`（`code` / `msg` / `data`）字段名不同，前端 SDK 按 `Result` 格式解析。[[glossary:SnailAiChatExceptionHandler]] 必须返回 `Result` 而非 `R`，否则前端无法正确读取错误信息。
_Avoid_: 「RuoYi 的 R」（两者字段名不同，互相不兼容）。

**BaseSnailAiException**：
Snail AI Agent 框架的业务异常基类（`com.aizuda.snail.ai.common.execption.BaseSnailAiException`）。所有 Snail AI 业务层异常都继承自它。在 [[glossary:SnailAiChatExceptionHandler]] 中作为兜底捕获，返回「AI 服务请求失败」。

**SnailAiAuthenticationException**：
Snail AI Agent 框架的认证异常（继承自 [[glossary:BaseSnailAiException]]）。在 [[glossary:SnailAiChatExceptionHandler]] 中第一个被捕获，返回专用状态码 `5001` 和「认证失败，请重新登录」提示。优先级高于 `BaseSnailAiException`。

**装配套件范式（Kit Assembly Pattern）**：
RuoYi `ruoyi-common-*` 模块包装第三方库的标准设计模式：①依赖成熟开源库（不重复造轮子）；②用一个自动配置类实现「依赖即生效、开关控制」；③用异常处理器将第三方异常转成项目统一或 SDK 约定的响应格式。`ruoyi-common-sms` 和 `ruoyi-common-ai` 都遵循此范式，但 AI 模块多了一层「响应格式边界隔离」——因为 Snail AI 有独立的前端 SDK，必须保持其 `Result` 格式不被 RuoYi 的 `R` 覆盖。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

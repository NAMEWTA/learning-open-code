# 0002-chat-ui-embed-architecture

## 日期
2026-07-06

## 类型
学习记录

## 标题
chat.ui.embed 嵌入模式的三层架构理解

## 内容

通过第 5-7 课，理解了 Snail AI Chat 的 iframe 嵌入模式的完整架构：

### 三个关键问题的答案

1. **chat.ui.embed 配置来源**：这是 Snail AI SDK（`snail-ai-agent-chat-starter` v1.0.0）内置的配置项。RuoYi 只在 `application-dev.yml` 中填写值，不包含任何消费这些配置的 Java 类。SDK 通过 `@ConfigurationProperties(prefix = "snail-ai.chat.ui.embed")` 绑定配置，再由 `SnailAiChatGatewayController` 注入到 Chat HTML 前端页面。

2. **UI 嵌入 + 免登入机制**：
   - Vue 端通过 `<iframe>` 嵌入 Snail AI Chat 页面
   - 免登入依赖两个 URL 参数：`openId`（Snail AI 用户标识，通过 `registerCurrentSnailUser()` 获取）和 `trustedCredential`（RuoYi JWT token）
   - `/snail-chat/**` 和 `/api/snail/chat/**` 被配置在 `security.excludes` 中，绕过 Sa-Token 拦截器
   - SDK 的 Controller 内部自行验证 `trustedCredential` 的有效性

3. **API 转发到 SDK Controller 的机制**：
   - `@EnableSnailAiAgent` 注解通过 `@Import` 导入 SDK 配置类，将 `SnailAiChatGatewayController` 注册为 Spring Bean
   - Controller 处理 `/snail-chat/**`（Chat HTML 页面）和 `/api/snail/chat/**`（Chat REST API + SSE Stream）
   - `SnailAiChatExceptionHandler` 通过 `@RestControllerAdvice(assignableTypes = SnailAiChatGatewayController.class)` 限定只处理 SDK Controller 的异常
   - 异常返回 Snail AI 的 `Result` 格式（`{status, message}`），而非 RuoYi 的 `R` 格式（`{code, msg}`）

### 关键洞察

**assignableTypes 的精妙之处**：`SnailAiChatExceptionHandler` 类上没有 `@ConditionalOnProperty`，所以当 `snail-ai.enabled=false` 时它仍会被加载。但因为 `SnailAiChatGatewayController` 不在容器中，`assignableTypes` 匹配不到任何 Controller，异常处理器成为空挂——零副作用。这是一种「被动安全」设计。

### 相关课程
- 0005-chat-ui-embed-config
- 0006-iframe-embed-and-auto-login
- 0007-api-forwarding-to-sdk-controller

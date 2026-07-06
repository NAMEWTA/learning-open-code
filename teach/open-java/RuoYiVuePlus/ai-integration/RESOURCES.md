# ruoyi-ai 模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充框架原理。

## Knowledge

- [代码: `ruoyi-ai/pom.xml` — 模块依赖声明](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-ai/pom.xml)
  整个模块只依赖 5 个内部模块（core、api、common-ai、satoken、web），不含任何第三方 AI 库。理解模块在依赖树中的位置时直接看这里。
- [代码: `SnailAiController.java` — 唯一的控制器](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-ai/src/main/java/org/dromara/ai/controller/SnailAiController.java)
  73 行代码完成用户注册桥接。理解「RuoYi 用户 → Snail AI 用户」的身份映射时查阅。
- [代码: `SnailAiConfig.java` — 自动配置入口](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-ai/src/main/java/org/dromara/common/ai/config/SnailAiConfig.java)
  16 行的 `@AutoConfiguration`，通过 `@EnableSnailAiAgent` + `@EnableSnailAiOpenApi` 两个注解激活整个 AI 能力。理解条件装配时查阅。
- [代码: `SnailAiChatExceptionHandler.java` — AI Chat 专属异常处理器](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-ai/src/main/java/org/dromara/common/ai/handler/SnailAiChatExceptionHandler.java)
  125 行，返回 Snail AI SDK 的 `Result` 而非 RuoYi 的 `R`。理解「双响应格式」设计时查阅。
- [代码: `application-dev.yml` 中的 snail-ai 配置段](RuoYi-Vue-Plus/ruoyi-admin/src/main/resources/application-dev.yml)
  完整的 snail-ai 配置树：Server gRPC 连接、Client 配置、Chat 嵌入模式、OpenAPI Client、HTTP 超时。理解配置全貌时查阅。
- [代码: React 端 `fetchAgentChat()` — SSE 流式对话实现](plus-ui-react/src/api/ai/agent/index.ts)
  `ReadableStream` + `TextDecoder` + SSE event 解析的完整实现。理解前端流式对话数据流时查阅。
- [代码: React 端 `AiChatPage` — AI Chat 完整页面](plus-ui-react/src/pages/ai/chat/index.tsx)
  使用 `@ant-design/x` 的 `Bubble`、`Conversations`、`Sender`、`Prompts` 组件构建的完整对话界面。理解 React 端原生集成模式时查阅。
- [代码: Vue 端 `AiChatPage` — iframe 嵌入模式](plus-ui-vue/src/views/ai/chat/index.vue)
  通过 `registerCurrentSnailUser()` 获取 openId，拼接 `/snail-chat/?openId=...&trustedCredential=...` URL 嵌入 iframe。理解 Vue 端嵌入模式时查阅。
- [代码: Vue 端 Snail AI 监控页](plus-ui-vue/src/views/monitor/snailai/index.vue)
  通过 `VITE_APP_SNAILAI_ADMIN` 环境变量配置的 iframe 嵌入 Snail AI 管理后台。理解运维集成时查阅。
- [官方文档: Snail AI — aizuda（爱组搭）](https://snail.ai)
  Snail AI 是爱组搭开源的 AI 智能体平台，RuoYi-Vue-Plus 集成了它的 Java SDK Starter。理解 SDK 能力边界时查阅。
- [经典: Spring Boot 条件装配 `@ConditionalOnProperty`](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/autoconfigure/condition/ConditionalOnProperty.html)
  `ruoyi-ai` 整个模块的可拔插特性依赖此注解。理解「配置驱动的模块开关」时查阅。
- [官方: `@ant-design/x` — Ant Design AI 组件库](https://x.ant.design/)
  React 端 AI Chat 页使用的 Ant Design 官方 AI 组件。理解前端组件选择动机时查阅。

## Wisdom (Communities)

- [社区: Dromara 开源社区 / RuoYi-Vue-Plus Issues](https://gitee.com/dromara/RuoYi-Vue-Plus)
  AI 模块的集成讨论、配置问题、Snail AI 版本升级在 Issues 中常有涉及。
- [社区: 爱组搭 / Snail AI 开源社区](https://gitee.com/aizuda/snail-ai)
  Snail AI Server 端的官方仓库，包含完整的 AI Agent 调度、模型管理、知识库等功能。理解「服务端提供什么」时查阅。

## Gaps
- Snail AI SDK 的内部实现（`com.aizuda.snail.ai.openapi.client.core.api.OpenApiUserClient`）为闭源或未纳入本仓库——我们仅能通过调用方式推断其契约。但对理解集成模式不是阻碍。
- gRPC 通信细节不在本模块代码中可见——Snail AI Starter 封装了通信层。对理解模块设计格局无实质影响。

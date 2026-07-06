# ruoyi-ai 模块 Glossary

本术语表收录 ruoyi-ai 模块讲解中真正理解的核心概念。术语应按理解顺序阅读——后面的定义依赖前面的术语。

## Terms

**Snail AI**：
爱组搭（aizuda）开源的 AI 智能体平台，提供 Agent 调度、模型管理、知识库、对话管理等功能。RuoYi-Vue-Plus 通过其 Java SDK Starter 集成。
_Avoid_: 蜗牛 AI（直译）、SnailAI

**Snail AI SDK**：
Snail AI 的 Java 客户端 SDK（`com.aizuda.snail.ai.*`），以 Spring Boot Starter 形式提供。封装了 gRPC 通信、Agent 管理、Chat 网关控制器、OpenAPI 客户端等能力。
_Avoid_: Snail AI 依赖、AI 库

**@EnableSnailAiAgent**：
Snail AI SDK 提供的激活注解，通过 `@Import` 导入 Agent 相关配置，注册 `SnailAiChatGatewayController`（AI Chat REST 端点）、智能体管理等全套功能。
_Avoid_: 开启 AI Agent、Agent 开关

**@EnableSnailAiOpenApi**：
Snail AI SDK 提供的激活注解，通过 `@Import` 导入 OpenAPI Client 配置，创建 `OpenApiUserClient` Bean 用于调用 Snail AI Server 的用户管理 API。
_Avoid_: OpenAPI 开关

**条件装配**（Conditional Configuration）：
Spring Boot 的 `@ConditionalOnProperty` 机制——仅在指定配置属性满足条件时才加载 Bean。ruoyi-ai 使用两层条件装配实现可拔插：总开关（`snail-ai.enabled`）控制整个 AI 能力，子开关（`snail-ai.open-api.enabled`）控制用户注册端点。
_Avoid_: 条件加载、可选模块

**可拔插**（Pluggable）：
ruoyi-ai 模块的核心设计哲学——通过条件装配实现 AI 能力的动态开关。`snail-ai.enabled=false` 时，整个 AI 模块零开销（不加载 Bean、不建立连接、不注册路由）。
_Avoid_: 可插拔、热插拔

**OpenApiUserClient**：
Snail AI SDK 提供的用户管理客户端接口，通过 gRPC 调用 Snail AI Server 的 OpenAPI。核心方法是 `register(OpenApiUserRegisterRequest)`，根据 `externalId` 幂等创建/获取 Snail AI 用户。
_Avoid_: 用户客户端、AI 用户 API

**身份桥接**（Identity Bridging）：
RuoYi 用户体系（userId: Long）与 Snail AI 用户体系（openId: String）之间的映射过程。由 `SnailAiController.registerCurrentUser()` 实现——将 RuoYi userId 作为 `externalId` 注册到 Snail AI，获得 `openId`。
_Avoid_: 用户同步、身份映射

**双响应格式**（Dual Response Format）：
ruoyi-ai 模块中同时存在两种 HTTP 响应格式：RuoYi 统一格式 `R{code, msg, data}`（用于 `/snail-ai/**` 端点）和 Snail AI SDK 格式 `Result{status, message, data}`（用于 `/api/snail/chat/**` 端点）。两者不兼容，需要独立的异常处理器。
_Avoid_: 两套返回格式、响应格式不一致

**SnailAiChatGatewayController**：
Snail AI SDK 提供的 AI Chat REST 控制器，处理 `/api/snail/chat/**` 路径的请求。由 `@EnableSnailAiAgent` 注解激活后自动注册。它的消费者是 Snail AI 前端 SDK，期望 `Result` 格式响应。
_Avoid_: Chat 网关、AI 聊天控制器

**SSE**（Server-Sent Events）：
服务器向客户端推送事件流的 HTTP 协议。React 端通过 `fetch()` + `ReadableStream` + `TextDecoder` 消费 `/snail-ai/agent/{id}/chat/stream` 的 SSE 流，实现 AI 对话的「逐字输出」效果。事件类型：`thinking`（思考过程）、`message`（对话内容）、`done`（流结束）、`error`（异常）。
_Avoid_: 服务器推送事件、事件流

**trustedCredential**：
Vue 端 iframe 嵌入模式中通过 URL 参数传递给 Snail AI 内嵌页面的认证凭证，实际值为 RuoYi 的 Sa-Token 登录 token。Snail AI 页面使用此 token 代表当前用户调用 RuoYi API。
_Avoid_: 信任凭证、认证令牌

**嵌入模式**（Embed Mode）：
Snail AI 内建前端的 iframe 嵌入配置（`chat.ui.embed.*`）。通过 `show-header: false`、`show-sidebar-user: false`、`compact-input: true` 等设置，让 Snail AI UI 在 RuoYi 页面中看起来像原生功能。
_Avoid_: iframe 模式、内嵌模式

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。
- 若某术语在更广领域中用法模糊，注明本 workspace 内的约定用法。

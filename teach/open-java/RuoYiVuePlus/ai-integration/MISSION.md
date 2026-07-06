# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-ai 模块——可拔插 AI 智能体集成

## Why
`ruoyi-ai` 是 RuoYi-Vue-Plus 中**最特殊的功能模块**——它只有 2 个文件、控制器仅 73 行代码，但它引入了一个完整的 AI 智能体平台（Snail AI），通过条件装配实现了「可拔插 AI 能力」。学习者需要理解：为什么一个 AI 模块的核心是 **SDK 集成而非业务代码**？`@ConditionalOnProperty` 如何让 AI 成为可开关的功能？为什么 AI Chat 接口需要**独立的异常处理体系**返回 SDK 原生格式而非 RuoYi 的 `R` 格式？React 端的 SSE 流式对话和 Vue 端的 iframe 嵌入为何走向两条完全不同的技术路线？目标是**读懂集成格局与可拔插设计哲学**，不是学 AI 算法。

## Success looks like
- 能用一句话讲清 `ruoyi-ai` 模块的本质：「它不实现 AI 能力，它是 Snail AI SDK 的 Spring Boot 适配器——通过自动配置、条件装配和双异常处理体系将外部 AI 平台嵌入 RuoYi」
- 能画出 ruoyi-ai 的三层物理架构：`ruoyi-modules/ruoyi-ai`（业务模块 · 控制器）→ `ruoyi-common/ruoyi-common-ai`（通用配置 · 自动装配 + 异常处理）→ 两个前端（React 原生组件 + Vue iframe 嵌入），并讲清每一层的职责边界
- 能解释 `SnailAiConfig` 的 `@ConditionalOnProperty(prefix = "snail-ai", name = "enabled", havingValue = "true")` 和 `SnailAiController` 的 `@ConditionalOnProperty(prefix = "snail-ai.open-api", name = "enabled", havingValue = "true")` 两层条件装配的差异与目的
- 能讲清 `snail-ai.enabled=false` 时整个 AI 模块如何做到**零侵入**——没有任何 AI 相关 Bean 被加载、没有任何 AI 路由被注册
- 能讲清 `registerCurrentUser()` 的用户身份桥接链路：`LoginHelper.getUserId()` → `OpenApiUserRegisterRequest` → `OpenApiUserClient.register()` → `OpenApiUserVO`，以及为什么需要这个桥接
- 能解释 `SnailAiChatExceptionHandler` 的 `@RestControllerAdvice(assignableTypes = SnailAiChatGatewayController.class)` 为什么限定控制器类型，以及为什么它返回 `Result<Void>` 而非 `R<*>`——双响应格式（SDK Result vs RuoYi R）的设计动机
- 能讲清 React 端 SSE 流式对话的完整数据流：`fetch()` → `ReadableStream` → `TextDecoder` → SSE event 解析（event: thinking/message/done/error）→ `normalizeStreamChunk()` JSON 解析 → React state 增量渲染
- 能解释 Vue 端为什么选择 iframe 嵌入模式而非 React 的原生组件模式，以及 `trustedCredential` 的免登机制

## Constraints
- 学习者已有 `2026-06-30-teach-ruoyi-api` 的模块依赖知识，理解 `ruoyi-api` 作为契约层的角色
- 学习者已有 `2026-06-30-teach-ruoyi-auth` 的登录链路知识，理解 `LoginHelper`、`LoginUser`、Sa-Token 认证体系
- 目标是「读懂集成格局与可拔插设计哲学」，课程以追踪真实代码结构、解释设计动机为主
- 全部讲解基于仓库真实代码，引用具体文件路径与类名
- 交互语言：简体中文
- 每节课短小（几分钟内可完成），有一个具体胜利
- 不要求学习者具备 AI/LLM 背景知识——模块本身不涉及 AI 算法

## Out of scope
- Snail AI 平台本身的架构与实现（Server 端 gRPC、Agent 调度、模型调用）——本模块只是 Snail AI 的客户端/适配器
- LLM/大语言模型的工作原理、Prompt Engineering、RAG 等技术
- gRPC 协议原理与实现细节——配置中涉及 gRPC 端口，但不深入协议层
- `ruoyi-common-ai` 中 `@EnableSnailAiAgent` 和 `@EnableSnailAiOpenApi` 注解背后的 Snail AI Starter 自动配置原理
- Snail Job（`snail-job`）分布式任务调度模块——它是独立功能模块，仅在配置文件中与 snail-ai 并列
- 前端 `@ant-design/x` 组件库的使用教程——仅在讲解 SSE 数据流时涉及

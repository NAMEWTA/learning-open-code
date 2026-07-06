# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-ai AI 公共模块

## Why
学习者要能彻底读懂 `ruoyi-common-ai` 这个公共模块：它本身只有 2 个 Java 类，是对开源 AI Agent 框架 **Snail AI Agent**（aizuda 出品，含 chat-starter / executor-starter / openapi-starter 三个 starter）的一层「项目化适配」。理解它，等于理解 RuoYi-Vue-Plus 如何把一个第三方 AI 框架「收编」进自己的技术栈——用 Spring Boot 自动配置实现 `snail-ai.enabled=true` 即用，用定点异常处理器保持 Snail AI SDK 前端消费的 Result 响应格式不被 RuoYi 通用 R 格式覆盖。达到能给同事讲清「这个 AI 模块为什么只有两个类」「SnailAiChatExceptionHandler 为什么不能用通用的 R 格式返回」「与 ruoyi-common-sms 的适配范式有何异同」，并能在自己的 RuoYi 项目里启用 AI 聊天功能、排查 AI 调用失败问题的程度。重点是**读懂设计动机与 API 约定边界**，不是 AI 算法原理。

## Success looks like
- 能用一句话说清 `ruoyi-common-ai` 与 Snail AI Agent 框架的关系，并说出模块仅有的两个类各自承担什么职责。
- 能解释 `SnailAiConfig` 如何用一个 `@AutoConfiguration` + 两个 `@Enable*` 注解 + `@ConditionalOnProperty` 实现「三合一自动激活」，以及为什么比手动逐模块 `@Import` 更安全。
- 能讲清 `SnailAiChatExceptionHandler` 用 `@RestControllerAdvice(assignableTypes = SnailAiChatGatewayController.class)` 定点拦截（而非全局拦截）后，为什么要返回 Snail AI SDK 的 `Result(status/message/data)` 而非 RuoYi 通用的 `R(code/msg/data)`——以及 `@Order(HIGHEST_PRECEDENCE)` 在优先级上的意义。
- 能识别 `SnailAiChatExceptionHandler` 覆盖的 8 种异常类型（认证异常、业务异常、模型调用异常、参数校验异常、非法参数/状态、通用兜底），并说出每种异常返回的用户提示语设计逻辑。
- 能对比 `ruoyi-common-ai` 与 `ruoyi-common-sms` 的「装配套件」范式异同：两者都遵循「自动配置 + 异常处理」的收编模式，但 AI 模块多了一层「响应格式边界隔离」（Result vs R），并且无需自定义缓存实现（因为 Snail AI 不依赖项目 Redis）。
- 能说出 pom.xml 中三个 Snail AI starter（chat-starter / executor-starter / openapi-starter）各自的大致用途，以及 `ruoyi-common-core` 作为公共依赖的角色。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会在「SnailAiChatGatewayController」一节联系到前端 SDK 调用入口（点到为止）。
- 目标是「读懂」而非「能改造框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- Snail AI Agent 框架各 starter 的内部实现细节（聊天引擎、执行器调度、OpenAPI 调用链）——只讲项目如何启用与配置，不讲框架内部。
- AI 模型（LLM）的选型、训练、调优、Prompt 工程——本模块只负责框架接入，不涉及 AI 业务设计。
- `ruoyi-common-sms` 的完整实现——仅在「装配套件范式对比」时点到关键差异。
- AI 聊天业务的具体前端实现与 SSE 流式传输细节。

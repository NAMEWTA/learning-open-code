# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-social 社交登录模块

## Why
学习者要能彻底读懂 `ruoyi-common-social` 这个公共模块：它基于开源 OAuth 聚合框架 **JustAuth**，提供社交登录能力，并扩展了 Gitea、MaxKey、TopIAM 三个自定义提供者。理解它，等于理解 RuoYi-Vue-Plus 如何包装一个第三方 OAuth 框架——用 Redis 缓存授权状态替代默认内存缓存、用 Spring Boot 自动配置实现零配置接入、通过 `SocialUtils` 工厂方法统一 27 个平台（含 3 个自研）的调用入口，并在此基础上扩展企业微信、钉钉等中国特色社交登录。重点是**读懂 JustAuth 标准流程与 RuoYi 的定制化扩展**，不是从零实现 OAuth 协议。

## Success looks like
- 能用一张全景图讲清模块的 13 个文件各自承担什么职责，并说出 `SocialUtils`、`AuthRedisStateCache`、`SocialAutoConfiguration` 三者的协作关系。
- 能讲清 JustAuth 标准 OAuth 登录的四个阶段（构建授权地址 → 用户授权回调 → 拿 code 换 token → 拿 token 换用户信息），以及 RuoYi 的 `SocialUtils.loginAuth()` 和 `getAuthRequest()` 在这条链上各自做了什么。
- 能讲清 `AuthRedisStateCache` 为什么要实现 `AuthStateCache` 接口，以及它用 `RedisUtils` + `SOCIAL_AUTH_CODE_KEY` 前缀替换 JustAuth 默认内存缓存的意义（集群下 state 校验不丢、3 分钟过期）。
- 能讲清自定义 OAuth 提供者的标准范式：一个 `AuthSource` 枚举（定义 authorization/accessToken/userInfo 三个端点 URL）+ 一个 `AuthDefaultRequest` 子类（实现 `getAccessToken()` 和 `getUserInfo()` 两个方法），并能对照 Gitea / MaxKey / TopIAM 三个实例说出它们的差异。
- 能讲清企业微信 `AbstractAuthWeChatEnterpriseRequest` 和钉钉 `AuthDingTalkV2Request` 与标准 OAuth2 流程的关键差异在哪里（corpId/corpSecret 验证方式、user_ticket 敏感信息获取、JSON 请求体格式）。
- 能完整追踪一次社交登录全链路：前端点击 "Gitee 登录" → `AuthController` → `SocialUtils.loginAuth()` → `getAuthRequest()` switch 匹配 → JustAuth `AuthRequest.login()` → `AuthRedisStateCache` 存取 state → 返回 `AuthUser` → 业务层注册/登录，并说出每一环的关键类和 Redis key。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端 OAuth 流程，但会在第 5 课联系前端登录入口（点到为止）。
- 目标是「读懂」而非「能改造框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路 / 画架构图」为主。
- 全部讲解基于仓库真实代码与 JustAuth 源码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- JustAuth 框架所有内置平台（GitHub/QQ/微信等）的 OAuth 细节——只讲 RuoYi 怎么统一调用，不讲每个平台 API 的差异细节。
- 前端社交登录页面（Vue 组件）的完整实现——仅在追踪全链路时点到前端入口 URL。
- 业务层 `AuthController` / `LoginHelper` / `SocialLoginBody` 的完整实现——已在 `2026-06-30-teach-ruoyi-auth` 课程覆盖，本课只接社交登录策略一环。
- OAuth 2.0 / OIDC 协议本身的 RFC 规范——默认学习者已有基础概念。

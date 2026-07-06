> **服务工作流：** `../T-teach/T-teach.md`
> **产物文件名：** `mission.md`
> **父目录规则：** 本模板产物写入 `YYYY-MM-DD-<kebab-name>/` change 目录内

# Mission: Admin 启动模块与认证入口

## Why

ruoyi-admin 是整个 RuoYi-Vue-Plus 系统的启动入口和认证网关。它承载了 Spring Boot 应用的启动引导、5 种认证策略的统一调度、登录事件的发布与监听、以及全局配置的集中管理。学习这个模块，你将掌握一个真实生产级 Java 后台系统如何用策略模式优雅地组织多种认证方式、如何用 Spring 事件机制解耦登录副作用（在线状态记录、日志写入、IP 归属地解析）、以及如何通过 Sa-Token 实现与客户端无关的会话管理。这些能力可以直接迁移到你自己的后台项目中，让你不再从零摸索认证架构。

## Success looks like

- 从 `DromaraApplication.main()` 出发，能完整追踪一次密码登录请求的执行链路：控制器接收 JSON 请求体 -> 策略工厂按 grantType 路由到 PasswordAuthStrategy -> 验证码校验 -> BCrypt 密码比对 -> 登录失败计数与锁定 -> 构建 LoginUser 上下文 -> Sa-Token 签发 token -> 发布 UserLoginSuccessEvent -> 监听器记录在线信息和登录日志。
- 能在 `IAuthStrategy` 框架下新增第六种认证方式（例如 LDAP 登录），只需新增一个 `@Service("ldapAuthStrategy")` 实现类，无需修改 AuthController 或任何已有策略代码。
- 能解释 `UserActionListener`（Sa-Token 钩子）与 `UserLoginSuccessListener`（Spring 事件监听器）的分工关系，以及事件记录（`record`）如何在 Java 17+ 中替代传统 POJO。
- 能独立配置验证码开关、密码最大重试次数与锁定时间、多客户端（client_id）的独立超时策略，并解释这些配置如何通过 `application.yml` 映射到运行时的行为。
- 能通过断点调试定位认证失败原因：验证码过期、用户不存在、账号停用、密码错误、客户端授权类型不匹配、第三方平台未绑定等异常分支。

## Constraints

- 要求具备 Spring Boot 基础：理解 `@Service`、`@RestController`、`@EventListener`、`application.yml` 配置绑定。
- 要求了解 Sa-Token 的基本概念：登录态、token、会话。
- 要求对 Redis 有基本认知：知道 Redis 用于缓存验证码、在线用户信息和登录错误计数。
- 不要求预先掌握 JustAuth（第三方登录库）或 SMS4J（短信发送库），这些会在课程中随用随讲。

## Out of scope

- 前端登录页面（Vue/React）的实现与交互细节。
- 其他业务模块（system 系统管理、generator 代码生成、workflow 工作流）的内部实现。
- ruoyi-admin 中与认证无关的配置项（Elasticsearch、MQTT、MCP 协议等）。
- Spring Boot 基础知识的系统讲解（只会在必要时简要回顾）。
- 生产部署、容器化、CI/CD 等运维话题。

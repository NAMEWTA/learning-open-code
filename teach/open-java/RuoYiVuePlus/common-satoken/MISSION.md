# Mission: 掌握 ruoyi-common-satoken 认证模块

## Why

所有后端系统的第一道防线就是认证——你是谁、你有什么权限、你该访问什么。RuoYi-Vue-Plus 没有直接手写 Filter/Interceptor 来实现这套机制，而是集成了 Sa-Token 轻量认证框架，并在此基础上做了 JWT 化、Redis 持久化、Caffeine 加速、异常统一处理等工程化加固。学完这套模块，你不仅能理解整个平台的登录、Token 签发、权限校验、踢人下线的完整链路，还能掌握"如何为一个开源框架做生产级适配"的通用方法论——这比会用一个框架更重要。

## Success looks like

- 能画出 Sa-Token + JWT + Redis + Caffeine 在 RuoYi-Vue-Plus 中的协作架构图
- 能解释 SaTokenConfig 中四个 Bean 的注册原因及其在框架中的角色
- 能说清楚 PlusSaTokenDao 的两级缓存策略：何时读 Caffeine、何时回源 Redis
- 能追踪一个登录请求从 Controller 到 Token 写入 Redis 的完整调用链
- 能区分 NotLoginException 的五种子类型并写出对应的前端处理逻辑
- 能独立添加一个新的权限码并在 SaPermissionImpl 中实现校验
- 能解释 JWT 模式与 Redis 模式的切换原理及各自的适用场景
- 能对比 ruoyi-common-satoken 与 ruoyi-common-sms 在 DAO 设计上的异同

## Constraints

- 学习者已了解 Java 8+、Spring Boot 自动配置、Redis 基础操作
- 以仓库源码为第一信任源，外部文档仅作辅助理解
- 教学语言为简体中文，代码中的注释和日志保持原文
- 所有代码引用须来自模块实际源码，不得虚构 API

## Out of scope

- Sa-Token 框架本身的完整使用手册（如注解鉴权、OAuth2 集成等）
- 前端如何存储和发送 Token（localStorage/Cookie 策略）
- 第三方登录（微信、企业微信等）的对接细节
- Spring Security 与 Sa-Token 的对比选型

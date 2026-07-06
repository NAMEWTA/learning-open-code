# ruoyi-common-satoken Resources

> 第一信任源：`RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-satoken/src/main/java/org/dromara/common/satoken/` 下的全部源码。以下外部资源用于补充框架背景知识，当与源码行为不一致时，以源码为准。

## Knowledge

- [类型: 官方文档 — Sa-Token 核心文档](https://sa-token.cc/doc.html)  
  Sa-Token 官方站点，涵盖登录认证、权限鉴权、踢人下线、Token 持久化、JWT 集成等全部功能说明。重点阅读「集成 JWT」和「集成 Redis」两个章节。

- [类型: 官方文档 — Sa-Token JWT 集成指南](https://sa-token.cc/doc.html#/plugin/jwt)  
  说明 Sa-Token 如何切换到 JWT 模式、Simple 模式与 Mixin 模式的区别、JWT 密钥配置等。本模块使用的正是 `StpLogicJwtForSimple`。

- [类型: 官方文档 — Sa-Token Dao 持久化](https://sa-token.cc/doc.html#/plugin/dao-extend)  
  解释 `SaTokenDao` 接口的设计意图：将 Token/Session 数据从内存迁移到 Redis/MongoDB 等外部存储，实现分布式会话共享。

- [类型: 代码 — PlusSaTokenDao 源码](https://gitee.com/dromara/RuoYi-Vue-Plus/blob/main/ruoyi-common/ruoyi-common-satoken/src/main/java/org/dromara/common/satoken/core/dao/PlusSaTokenDao.java)  
  RuoYi 自定义的 SaTokenDao 实现，Caffeine + Redis 两级缓存的核心代码。

- [类型: 代码 — SaTokenConfig 自动配置](https://gitee.com/dromara/RuoYi-Vue-Plus/blob/main/ruoyi-common/ruoyi-common-satoken/src/main/java/org/dromara/common/satoken/config/SaTokenConfig.java)  
  四个 Bean 注册的入口，理解模块装配逻辑的第一站。

- [类型: 代码 — LoginHelper 工具类](https://gitee.com/dromara/RuoYi-Vue-Plus/blob/main/ruoyi-common/ruoyi-common-satoken/src/main/java/org/dromara/common/satoken/utils/LoginHelper.java)  
  业务层最常用的登录工具，封装了登录、登出、用户信息获取、超管判断等方法。

- [类型: 官方文档 — Caffeine Cache](https://github.com/ben-manes/caffeine/wiki)  
  Caffeine 本地缓存库的官方 Wiki，了解其过期策略、容量控制、统计信息等核心特性。

## Wisdom (Communities)

- [类型: 社区 — RuoYi-Vue-Plus Gitee Issues](https://gitee.com/dromara/RuoYi-Vue-Plus/issues)  
  搜索 "satoken" 或 "登录" 相关的 Issue，可看到真实用户遇到的认证问题和作者回复。

## Gaps

- Sa-Token 与 Spring Security 的深度对比（架构理念、性能、生态）——当前缺乏系统性的横向评测资料。
- Caffeine 在 SaTokenDao 中仅做了简单的固定参数配置（5秒过期、最大1000条），未涉及更精细的调优策略（如基于访问频率的动态过期、异步刷新等），相关最佳实践资料缺失。

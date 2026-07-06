# Mission: 全面读懂 RuoYi-Vue-Plus 的 ruoyi-common-redis 缓存服务模块

## Why
学习者要能在脑中完整重建 `ruoyi-common-redis` 这个公共模块「提供了什么能力、每个类各管什么、为什么这样设计」的全景，理解它如何用 **Redisson** 把 Redis 包装成一套开箱即用的缓存 / 分布式 / 限流 / 防重 / 发号能力，并能在自己的业务代码里正确选用。重点是**读懂模块设计与各组件职责**，不是从零实现一个缓存框架。讲解全部基于本仓库真实代码（已逐文件核对）。

## Success looks like
- 能用一张图讲清模块的 5 大区域（配置 config / 处理器 handler / 注解切面 aspectj / 缓存管理 manager / 工具类 utils）各自的职责与依赖关系，并说出每块的关键类。
- 能解释「为什么选 Redisson 而不是 RedisTemplate」，以及 `RedisConfig` 里 `CompositeCodec`（key 用 String、value 用 JSON）+ `setNameMapper(KeyPrefixHandler)` + 单机/集群双模式这三处定制各解决了什么问题。
- 能讲清 `@RateLimiter` 限流的完整链路：注解 → `RateLimiterAspect` 切面 → SpEL 解析 key → `RedisUtils.rateLimiter` → Redisson `RRateLimiter` 令牌桶，并说清 DEFAULT / IP / CLUSTER 三种 `LimitType` 的差异。
- 能讲清 `@RepeatSubmit` 防重提交的链路与「为什么用 `setIfAbsent` + 成功保留键 / 失败删键」这套幂等设计，以及它和 `@RateLimiter` 在意图上的区别。
- 能讲清二级缓存的设计：`CacheConfig` → `PlusSpringCacheManager` → `CaffeineCacheDecorator`（Caffeine 一级本地 + Redis 二级分布式），并能解释 `cacheName#ttl#maxIdle#maxSize#local` 这种「在缓存名里塞参数」的约定为什么存在。
- 能说清四个工具类各自的定位：`RedisUtils`（通用读写 / 限流 / 发布订阅 / 原子值）、`CacheUtils`（操作 Spring Cache 命名空间）、`QueueUtils`（分布式队列）、`SequenceUtils`（分布式发号器），并能在「该用哪个」的场景题里选对。
- 能说清 `RedisExceptionHandler` 为什么单独处理 Lock4j 锁失败异常，以及这个模块与 `ruoyi-common-json`、`ruoyi-common-satoken`、Lock4j 的依赖边界。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解以追踪真实代码 + 解释设计动机为主。
- 目标是「读懂并能正确选用」而非「能改框架」——练习以「读代码答问题 / 选型判断 / 复述链路」为主，不要求大量动手编码。
- 全部讲解基于仓库真实代码，引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- Redisson / Caffeine / Lock4j 各自的完整 API 与底层实现细节——仅讲本模块用到的部分。
- 分布式锁 Lock4j 的注解用法本身（`@Lock4j` 不在本模块内，仅在异常处理处交叉点到）。
- 业务模块里具体怎么用这些缓存（如登录、验证码、租户）——仅在举例时引用，不展开业务。
- Redis 自身的数据结构原理、运维部署、持久化等基础设施话题。

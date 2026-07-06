# ruoyi-common-redis 缓存服务模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-redis/`）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _Redisson Wiki_ — Redisson（GitHub）](https://github.com/redisson/redisson/wiki)
  本模块的基石。模块没有直接用 Spring 的 `RedisTemplate`，而是全程用 Redisson 的 `RedissonClient`。理解 `RBucket` / `RMap` / `RMapCache` / `RRateLimiter` / `RIdGenerator` / `RTopic` / `RBlockingQueue` / `Codec` / `NameMapper` 时查阅。
- [官方文档: _RuoYi-Vue-Plus 官方文档 · 缓存监控 / 缓存使用_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目对缓存、限流、防重、发号器的设计说明与使用示例。理解「为什么这样封装」「业务里怎么调」时查阅。
- [官方文档: _Spring Framework · Cache Abstraction_ — Spring（docs.spring.io）](https://docs.spring.io/spring-framework/reference/integration/cache.html)
  理解 `CacheManager` / `Cache` / `@Cacheable` / `@CacheEvict` 抽象，以及 `PlusSpringCacheManager` 为什么要实现 `CacheManager` 接口、`CaffeineCacheDecorator` 为什么实现 `Cache` 接口时查阅。
- [官方文档: _Caffeine Wiki_ — ben-manes（GitHub）](https://github.com/ben-manes/caffeine/wiki)
  本地一级缓存库。理解 `expireAfterWrite` / `maximumSize` / `Cache.get(key, mappingFunction)` 时查阅，对应 `CacheConfig.caffeine()` 与 `CaffeineCacheDecorator`。
- [代码: _config / handler / aspectj / manager / utils 五大目录_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-redis/src/main/java/org/dromara/common/redis/)
  模块第一现场。任何「这个能力到底怎么实现」的问题，最终答案在这里。
- [官方文档: _Lock4j_ — baomidou（GitHub）](https://github.com/baomidou/lock4j)
  分布式锁框架，本模块仅在 `RedisExceptionHandler` 统一处理它的 `LockFailureException`。理解锁失败为什么要降级成「请稍后再试」时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么这样设计」「某版本行为变化」（如 Jackson 3.x 序列化校验器变更、fory 序列化方案取舍）时，Issues 和讨论区是最贴近维护者意图的反馈源。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + 上述官方文档支撑。

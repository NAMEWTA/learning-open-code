# ruoyi-common-redis 缓存服务模块 Glossary

记录学习者在 8 节课程中**真正理解**的核心术语。覆盖 Redisson 封装、序列化、注解切面、二级缓存、工具类五大块。

## Terms

**Redisson**：
本模块的基石库。它把 Redis 的能力包装成 Java 程序员熟悉的分布式对象（Map、Set、Queue、AtomicLong、限流器、发号器等），让「用 Redis」像「用 Java 集合」一样自然。整个模块通过 `RedissonClient` 操作 Redis，不使用 Spring 的 `RedisTemplate`。

**Codec（编解码器）**：
Redisson 决定「对象如何序列化进 Redis」的组件。本模块用 `CompositeCodec`，对 key 用 `StringCodec`（便于在 redis-cli 中阅读），对 value 用 JSON（便于存储复杂对象并还原类型）。
_Avoid_: 「序列化器」（泛称，本项目特指 Redisson 的 Codec 体系）。

**NameMapper（key 名映射器）**：
Redisson 提供的 key 名转换扩展点。本模块的 [[KeyPrefixHandler]] 实现它，<code>map()</code> 存时自动加前缀、<code>unmap()</code> 取时自动去前缀，对业务代码透明。

**KeyPrefixHandler**：
实现 Redisson <code>NameMapper</code> 接口的 key 前缀处理器。前缀为空时什么都不做；非空时构造成 <code>prefix:</code> 格式，用 <code>startsWith</code> 防重复添加。解决了多项目/环境共用 Redis 的 key 冲突问题。

**令牌桶（RRateLimiter）**：
<code>@RateLimiter</code> 限流的底层机制。Redisson 的 <code>RRateLimiter</code> 在 Redis 中用 Lua 脚本原子维护一个按速率补充令牌的桶——<code>tryAcquire</code> 扣一个令牌，耗尽则获取失败（返回 -1），切面据此抛限流异常。
_Avoid_: 「计数器限流」（本模块用的是令牌桶而非固定窗口计数）。

**LimitType（限流类型）**：
定义限流 key 的维度。DEFAULT 全局限流（所有请求共享一个桶）、IP 按来源 IP 各自限流、CLUSTER 按后端实例各自控单机（RateType=PER_CLIENT）。
_Avoid_: 「限流模式」（类型只决定 key 维度和 RateType，不改变令牌桶本身）。

**SpEL 动态 key**：
Spring 表达式语言，<code>@RateLimiter</code> 用它把方法参数动态拼进限流 key。切面用 <code>MethodBasedEvaluationContext</code> 喂参数、<code>SpelExpressionParser</code> 解析表达式，支持 <code>#参数</code> 和 <code>#{模板}</code> 两种格式。

**幂等（防重提交语境）**：
保证「同一次操作即使被提交多次，效果也只发生一次」的性质。<code>@RepeatSubmit</code> 通过 <code>setObjectIfAbsent</code>（不存在才写入）抢占一个带过期时间的 key 来实现：成功保留键直到过期、失败立即删键（允许重试）。
_Avoid_: 「防抖」（前端概念，二者目标相近但实现层与语义不同）。

**setObjectIfAbsent（原子占位）**：
<code>RedisUtils.setObjectIfAbsent</code>，底层是 Redis SETNX + 过期的原子操作。不存在则写入并返回 true（抢到），已存在返回 false（被占了）。是 <code>@RepeatSubmit</code> 防重提交的核心 API。

**二级缓存**：
本模块的缓存加速结构：一级是 JVM 内的 Caffeine 本地缓存（30s 过期 / 1000 条），二级是 Redis 分布式缓存。读优先命中本地、写时先失效本地再写 Redis，适合字典/配置等「读多写少、能忍几十秒陈旧」的数据。
_Avoid_: 「多级缓存」（本模块固定两级，不宜泛化）。

**PlusSpringCacheManager**：
自定义 Spring CacheManager，在 Redisson 原版上增加两个能力：① 缓存名支持 <code>cacheName#ttl#maxIdle#maxSize#local</code> 格式（不改注解就能声明缓存策略）；② 接入 Caffeine 本地缓存。根据是否有 TTL/SIZE 自动选 RMap 还是 RMapCache。

**CaffeineCacheDecorator**：
实现 Spring <code>Cache</code> 接口的装饰器。对 <code>get</code> 用 <code>caffeine.get(key, loader)</code> 实现「先本地后回源」；对 <code>put</code> 先 <code>invalidate</code> 清本地再写 Redis（防旧本地值残留）。key 用 <code>cacheName:key</code> 格式防止不同缓存命名空间冲突。

**RBucket / RMap / RMapCache**：
Redisson 的三种核心分布式对象。RBucket 是单个对象容器；RMap 是 Hash 结构（不过期）；RMapCache 是带 TTL/maxIdle/maxSize 的 Map。<code>RedisUtils</code> 的对象/Map 操作底层分别对应 RBucket 和 RMap。

**RAtomicLong（分布式原子值）**：
Redisson 的分布式 Long 型计数器，底层是 Redis INCR（原子递增）。<code>RedisUtils</code> 用它提供 <code>setAtomicValue</code> / <code>incrAtomicValue</code> / <code>decrAtomicValue</code>，并发安全。

**RTopic（发布订阅）**：
Redisson 的 Pub/Sub 封装。<code>RedisUtils</code> 用它提供 <code>publish</code> / <code>subscribe</code> / <code>unsubscribe</code>，用于跨实例事件通知（如「字典更新了，各位清缓存」）。注意消息不持久化。

**RBlockingQueue（分布式阻塞队列）**：
<code>QueueUtils</code> 的底层对象，基于 Redis List（LPUSH + BRPOP）。适合轻量临时任务；重量级/需要持久化/重试/死信的场景请用 MQ。

**RIdGenerator（分布式发号器）**：
<code>SequenceUtils</code> 的底层对象。Redisson 提供的分布式唯一 ID 生成器，基于 Lua 原子递增，支持初始值/步长/过期。本模块按时间分片 key（如 P20260630），每天/每分钟一个新 key，老 key 自动过期避免堆积，生成如 <code>P20260630000001</code> 的业务单号。

**RBatch（批处理）**：
Redisson 的批量命令接口。把多个异步操作打包成一次网络往返发给 Redis。<code>RedisUtils.deleteObject(Collection)</code> 和 <code>delMultiCacheMapValue</code> 都用它减少网络开销。

**Lock4j 锁降级**：
本模块不实现分布式锁，只通过 <code>RedisExceptionHandler</code> 兜底 Lock4j 框架的 <code>LockFailureException</code>——将锁竞争失败从"系统异常"降级为"业务处理中，请稍后再试"。锁由 Lock4j 管，异常归 redis 模块兜。

**TransactionAwareCacheDecorator**：
Spring 提供的事务感知缓存装饰器。<code>PlusSpringCacheManager</code> 在 <code>transactionAware=true</code> 时自动包这层，保证缓存写入在 Spring 事务提交后才执行（事务回滚则缓存不写）。

**自动装配（AutoConfiguration.imports）**：
Spring Boot 3.x 的自动装配入口文件（<code>META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports</code>）。其列出 <code>RedisConfig / CacheConfig / RateLimiterConfig / IdempotentConfig</code> 四个 <code>@AutoConfiguration</code> 类，使得引入该模块即可自动装配全部能力。

**反序列化类型校验器（BasicPolymorphicTypeValidator）**：
Jackson 3.x 的安全机制。当 JSON 带类型信息（<code>activateDefaultTyping</code>）时，攻击者可从不可信数据触发反序列化漏洞。本模块当前默认全放行（注释提示建议收紧为 <code>allowIfBaseType("org.dromara")</code> 白名单）。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

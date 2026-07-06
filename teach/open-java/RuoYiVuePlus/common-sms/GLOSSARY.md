# ruoyi-common-sms 短信模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**sms4j**：
Dromara 社区出品的开源短信聚合框架（本项目使用 3.3.5 版本）。提供多厂商统一的 API，封装了阿里云、腾讯云、华为云等厂商的 SDK。`ruoyi-common-sms` 的全部发送能力来自它。
_Avoid_: 「短信 SDK」（指单个厂商 SDK，sms4j 是聚合层）。

**SmsDao**：
sms4j 定义的缓存接口（`org.dromara.sms4j.api.dao.SmsDao`），声明 `set` / `get` / `remove` / `clean` 方法。短信拦截计数和重试状态的存取都通过它。sms4j 自带一个基于 `ConcurrentHashMap` 的默认实现 `SmsDaoDefaultImpl`。
_Avoid_: 「短信数据库」（它存的是运行时临时状态，不是业务数据表）。

**PlusSmsDao**：
RuoYi 对 [[glossary:SmsDao]] 的自定义实现（`ruoyi-common-sms/core/dao/PlusSmsDao.java`）。将所有存取转发给 `RedisUtils`，key 加 `global:` 前缀，使短信拦截计数使用项目统一的 Redis 缓存，替代 sms4j 默认的单机内存实现。是实现集群下防刷拦截的基础。
_Avoid_: 「短信 DAO 层」（它是一个缓存适配器，不是 ORM）。

**GLOBAL_REDIS_KEY**：
RuoYi 框架级 Redis key 前缀，值为 `"global:"`，定义在 `org.dromara.common.core.constant.GlobalConstants`。所有系统级缓存 key（验证码、限流、防重提交等）都挂在这个命名空间下，与多租户和业务 key 隔离。

**SmsBlend**：
sms4j 的发送器接口，每个厂商的实现类都实现它。`SmsFactory.getSmsBlend("配置ID")` 返回的就是它。核心方法是 `sendMessage(phones, templateId, params)`，返回 `SmsResponse`。

**SmsFactory**：
sms4j 的工厂入口，唯一静态方法是 `getSmsBlend(configId)`。按配置 ID 去 yml 的 `blends` 段找到对应厂商的 `SmsBlend` 实例。

**SmsResponse**：
sms4j 发送返回对象。核心字段：`success (boolean)` — 发送是否成功；`data (Object)` — 厂商返回的原始响应；`configId (String)` — 用的是哪个配置。

**SmsBlendException**：
sms4j 统一包装的短信运行时异常（`RuntimeException`），携带 `code`（厂商错误码）、`message`、`requestId`。被 [[glossary:SmsExceptionHandler]] 全局兜底。

**SmsExceptionHandler**：
`@RestControllerAdvice` 标注的全局异常处理器（`ruoyi-common-sms/handler/SmsExceptionHandler.java`）。精确匹配 `SmsBlendException`，对内 `log.error` 记 URI+堆栈，对外返回统一 `R.fail("短信发送失败，请稍后再试...")`。体现「内外有别」的响应纪律。

**自动配置垫片（Auto Configuration Adapter）**：
RuoYi `ruoyi-common-*` 模块包装第三方库的标准范式：用一个 `XxxAutoConfiguration` + `.imports` 文件 + 若干 `@Bean` 实现「依赖即生效、零配置接入」。[[glossary:SmsAutoConfiguration]] 是本范式在短信模块的体现。

**SmsAutoConfiguration**：
短信模块的 Spring Boot 自动配置类（`config/SmsAutoConfiguration.java`）。用 `@AutoConfiguration(after=DataRedisAutoConfiguration)` 声明加载时序（Redis 先就绪），用 `@Primary` 让 [[glossary:PlusSmsDao]] 压过 sms4j 默认实现，用 `@Bean` 注册 [[glossary:SmsExceptionHandler]]。通过 `AutoConfiguration.imports` 文件被 Spring Boot 发现。

**CAPTCHA_CODE_KEY**：
验证码在 Redis 中的 key 前缀，值为 `GLOBAL_REDIS_KEY + "captcha_codes:"`，即 `global:captcha_codes:`。短信验证码的完整 key 为 `global:captcha_codes:{手机号}`，由 [[glossary:SmsAuthStrategy]] 和 `CaptchaController` 共享使用，5 分钟过期。

**SmsAuthStrategy**：
Ruoyi 短信登录策略（`web/service/impl/SmsAuthStrategy.java`），Bean 名为 `smsAuthStrategy`。负责校验短信验证码、按手机号查用户、调用 `LoginHelper.login()` 签发 token。`validateSmsCode()` 方法用与发码端相同的 key 从 Redis 取验证码比对。

**@RateLimiter**：
RuoYi 自有的限流注解（`ruoyi-common-redis`），基于 Redis + Lua 脚本实现。在 `smsCode()` 上以 `@RateLimiter(key="#phoneNumber", time=60, count=1)` 注解，实现该手机号 60 秒内最多调用 1 次。

**config1 / config2**（配置 ID）：
yml 中 `sms.blends` 下的自定义标识，代码中用 `SmsFactory.getSmsBlend("config1")` 按 ID 找对应厂商配置。命名自由，可同时配置多个厂商或多个同厂商账号，是实现多厂商共存和租户隔离的机制。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

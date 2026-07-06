# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-sms 短信模块

## Why
学习者要能彻底读懂 `ruoyi-common-sms` 这个公共模块：它本身只有三个类，是对开源短信聚合框架 **sms4j** 的一层「项目化适配」。理解它，等于理解 RuoYi-Vue-Plus 如何把一个第三方 starter「收编」进自己的技术栈——用框架自带的 Redis 统一缓存、用全局异常处理器兜底、用 Spring Boot 自动配置无侵入接入。达到能给同事讲清「这个模块为什么只有三个类却不可或缺」「短信验证码登录从发码到校验怎么走通」，并能在此基础上自己接入一个新短信厂商或排查发送失败问题的程度。重点是**读懂设计动机与真实调用链**，不是从零造短信轮子。

## Success looks like
- 能用一句话说清 `ruoyi-common-sms` 与 sms4j 的关系，并说出模块仅有的三个类各自承担什么职责。
- 能解释 `PlusSmsDao` 为什么要用 `RedisUtils` 替换 sms4j 默认的内存缓存 `SmsDaoDefaultImpl`，以及它对「短信拦截/防刷在集群下生效」意味着什么。
- 能讲清 `SmsAutoConfiguration` 如何通过 `AutoConfiguration.imports` + `@AutoConfiguration(after=...)` + `@Primary` 实现「不写一行 `@Import` 也能自动接管」的无侵入装配。
- 能讲清 `SmsExceptionHandler` 用 `@RestControllerAdvice` 捕获 `SmsBlendException` 后，如何把它转成统一的 `R` 失败响应，以及为什么要单独为短信建一个异常处理器。
- 能完整追踪「发送短信验证码 → 存 Redis → 短信登录校验」这条真实业务链：`CaptchaController.smsCode()` → `SmsFactory.getSmsBlend()` → `SmsAuthStrategy.validateSmsCode()`，并说出每一环的关键类与 Redis key。
- 能读懂 `application-dev.yml` 中 `sms:` 配置段（多厂商 blends、`config1/config2`、`restricted/minute-max/account-max` 拦截参数），并能照葫芦画瓢加一个新厂商配置。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会在「短信验证码登录」一节联系到前端调用入口（点到为止）。
- 目标是「读懂」而非「能改造框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路」为主。
- 全部讲解基于仓库真实代码与 sms4j 3.3.5 源码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- sms4j 框架各厂商 SDK 的内部实现细节（阿里/腾讯/华为各自的签名算法）——只讲项目如何调用，不讲厂商 SDK 内部。
- 邮箱验证码（`ruoyi-common-mail` / `MailBuilder`）的完整实现——仅在与短信验证码对照时点到。
- 短信登录之外的其它登录策略（password/social/xcx）的完整链路——已在 `2026-06-30-teach-ruoyi-auth` 课程覆盖，本课只接其短信策略一环。
- 工作流/系统消息中调用短信通知的业务编排细节。

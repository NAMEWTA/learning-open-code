# ruoyi-common-sms 短信模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（含 sms4j 3.3.5 sources jar）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _sms4j 官方文档_ — Dromara（sms4j.com）](https://sms4j.com/)
  本模块封装的短信聚合框架权威说明。理解 `SmsBlend` / `SmsFactory` / 多厂商 `blends` 配置 / 拦截重试 / `SmsDao` 接口时查阅。本模块的一切都建立在它之上。
- [代码: _ruoyi-common-sms 模块三件套_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-sms/src/main/java/org/dromara/common/sms/)
  `SmsAutoConfiguration` / `PlusSmsDao` / `SmsExceptionHandler`。任何关于「这个模块做了什么」的问题，最终答案在这三个文件里。
- [代码: _sms4j 3.3.5 源码_](file:///Users/wta/.m2/repository/org/dromara/sms4j/)
  `SmsDao` 接口、`SmsDaoDefaultImpl`（默认内存实现）、`SmsBlendException`、`SmsResponse`。理解「项目为什么要替换默认实现」时对照查阅 sources jar。
- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `AutoConfiguration.imports` / `after` 排序 / `@Primary` 覆盖默认 Bean 的机制时查阅。第 3 课的核心原理来源。
- [代码: _短信真实使用现场_](RuoYi-Vue-Plus/ruoyi-admin/src/main/java/org/dromara/web/controller/CaptchaController.java)
  发送短信验证码的入口；配合 `web/service/impl/SmsAuthStrategy.java`（短信登录校验）构成完整业务闭环。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明，含验证码、登录、Redis 等章节。理解模块在整体架构中的位置时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么这样封装」「sms4j 某版本行为变化」时，Issues 与讨论区最贴近维护者意图。sms4j 与 RuoYi-Vue-Plus 同属 Dromara 社区，问题常能交叉解答。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + sms4j 源码 + 上述官方文档支撑。

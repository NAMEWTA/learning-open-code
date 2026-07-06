# ruoyi-common-mail 邮件模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（含 Hutool 6.x 源码）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-mail 模块三件套_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-mail/src/main/java/org/dromara/common/mail/)
  `MailConfig.java` / `MailProperties.java` / `MailBuilder.java`。任何关于「这个模块做了什么」的问题，最终答案在这三个文件里。
- [官方文档: _Hutool 邮件工具 JakartaMail_ — Hutool（hutool.cn）](https://doc.hutool.cn/pages/JakartaMail/)
  Hutool 封装的 Jakarta Mail 发送工具说明。理解 `JakartaMail.create()` / `setUseGlobalSession()` / `addImage()` 等方法时查阅。MailBuilder 的 `send()` 方法最终就是调它的 `mail.send()`。
- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `AutoConfiguration.imports` / `@EnableConfigurationProperties` / `@ConditionalOnProperty` 机制时查阅。第 2 课的自动配置原理来源。
- [代码: _邮件真实使用现场 - 演示案例_](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-demo/src/main/java/org/dromara/demo/controller/MailSendController.java)
  `MailSendController` 提供三个演示接口：纯文本发送、带附件发送、多附件发送。是学习 MailBuilder 流式 API 最简洁的参考。
- [代码: _邮件真实使用现场 - 验证码_](RuoYi-Vue-Plus/ruoyi-admin/src/main/java/org/dromara/web/controller/CaptchaController.java)
  `CaptchaController.smsCode()` 方法中同时处理短信和邮箱验证码发送，展示了 MailBuilder 在真实登录场景中的使用方式（约第 112 行）。
- [代码: _邮件真实使用现场 - 工作流通知_](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-workflow/src/main/java/org/dromara/workflow/service/impl/FlwCommonServiceImpl.java)
  工作流模块中按消息类型（EMAIL_MESSAGE / SMS_MESSAGE）分发的处理，展示了邮件与短信在业务层的对称用法（约第 160 行）。
- [配置: _邮件 yml 配置段_](RuoYi-Vue-Plus/ruoyi-admin/src/main/resources/application-dev.yml)
  `mail:` 前缀下的 10 个配置项（enabled / host / port / auth / from / user / pass / starttlsEnable / sslEnable / timeout 等），是 MailProperties 绑定的数据源。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明，理解模块在整体架构中的位置时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「邮件发送失败」「SMTP 配置问题」「mail.enabled 开关行为」时，Issues 与讨论区最贴近维护者意图。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + Hutool 文档 + Spring Boot 自动配置文档支撑。

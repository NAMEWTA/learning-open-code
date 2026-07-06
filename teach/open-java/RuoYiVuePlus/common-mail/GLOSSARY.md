# ruoyi-common-mail 邮件模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**Jakarta Mail**：
Jakarta EE 的邮件 API 标准（`jakarta.mail-api` + Eclipse Angus 实现 `jakarta.mail`），是 Java EE 时代 `javax.mail` 的品牌迁移版本。本模块通过 Hutool 间接使用它，不直接调用 Jakarta Mail API。
_Avoid_: 「JavaMail」（那是 javax 时代的老名字）。

**MailAccount**：
Hutool 的邮件账户配置对象（`cn.hutool.extra.mail.MailAccount`），封装了 SMTP 服务器地址、端口、用户名密码、SSL/TLS 开关、超时等所有连接参数。`MailProperties.toMailAccount()` 方法的输出就是它，`MailConfig` 将它注册为 Spring 容器的单例 Bean。
_Avoid_: 「邮件账号表」（它是运行时配置对象，不是数据库表）。

**MailProperties**：
邮件配置属性类（`ruoyi-common-mail/config/properties/MailProperties.java`），用 `@ConfigurationProperties(prefix = "mail")` 绑定 yml 中 `mail:` 段的 10 个属性。核心方法是 `toMailAccount()` — 把平面属性转成 Hutool 的 `MailAccount` 对象。
_Avoid_: 「邮件属性文件」（它是由 Spring Boot 自动填充的 POJO，不是手动读取的 .properties 文件）。

**MailConfig**：
邮件模块的 Spring Boot 自动配置类（`ruoyi-common-mail/config/MailConfig.java`）。用 `@AutoConfiguration` + `AutoConfiguration.imports` 声明自动加载，用 `@EnableConfigurationProperties(MailProperties.class)` 激活配置绑定，用 `@ConditionalOnProperty(value = "mail.enabled", havingValue = "true")` 控制是否创建 `MailAccount` Bean。是整个模块的「总开关」。
_Avoid_: 「邮件配置」（太泛，容易与 `MailProperties` 混淆）。

**MailBuilder**：
流式邮件构建器（`ruoyi-common-mail/core/MailBuilder.java`），是模块对外暴露的唯一 API 入口。私有构造器 + 静态工厂 `of()` 创建实例，提供链式方法设置收件人/to/cc/bcc、主题、正文（text/html）、图片、附件，最终调用 `send()` 触发发送。是 Builder 模式 + Fluent API 的典型实现。
_Avoid_: 「邮件工具类」（它是有状态的 Builder 实例，不是静态工具方法集合）。

**JakartaMail**：
Hutool 对 Jakarta Mail 的封装类（`cn.hutool.extra.mail.JakartaMail`）。MailBuilder 的 `send()` 方法内部通过 `JakartaMail.create(account)` 创建它，设置各项参数后调用 `mail.send()` 真正发出邮件。返回 `message-id` 字符串。
_Avoid_: 「邮件发送器」（太泛，且容易与 MailBuilder 混淆 — JakartaMail 是底层，MailBuilder 是高层封装）。

**@ConditionalOnProperty**：
Spring Boot 条件装配注解。`MailConfig` 用它声明「只有当 `mail.enabled=true` 时才创建 `MailAccount` Bean」。开关关闭时，容器中没有 `MailAccount` 实例，`MailBuilder.of()` 仍可创建构建器，但 `send()` 时会因 `SpringUtils.getBean(MailAccount.class)` 找不到 Bean 而抛出 `NoSuchBeanDefinitionException`。这是邮件模块与短信模块「无异常处理器」的根本原因 — 邮件不发时直接抛异常，由业务方自行处理。
_Avoid_: 「条件注解」（太泛，且容易与 `@ConditionalOnClass`/`@ConditionalOnMissingBean` 等其他条件注解混淆）。

**useGlobalSession**：
`MailBuilder` 的内部布尔标志（默认 `true`）。控制 `JakartaMail` 是否复用 JVM 级的全局 `Session` 对象。当调用 `account()` / `from()` / `user()` / `pass()` 任一覆盖方法时，自动置为 `false` — 因为此时使用的是克隆后的临时账户，不应污染全局会话。是 Builder 内部「何时克隆账户」的决策依据。
_Avoid_: 「全局会话」（太泛，不特指 Jakarta Mail 的 Session 复用语义）。

**Builder 模式（Fluent API）**：
创建型设计模式。`MailBuilder` 的每个设值方法都返回 `this`（`return this;`），使得调用者可以用 `.to().subject().text().send()` 的链式语法组合参数，最终调用 `send()` 作为终止操作。与此相对的是 setter 风格（需要多行分别调用）和构造函数风格（参数过多时易错）。
_Avoid_: 「链式调用」（只描述了语法现象，没点出 Builder 模式的设计意图 — 分离构建过程与最终产出）。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录 — 术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语 — 一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

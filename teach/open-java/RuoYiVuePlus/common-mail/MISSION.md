# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-mail 邮件模块

## Why
学习者要能彻底读懂 `ruoyi-common-mail` 这个公共模块：它只有 **3 个 Java 类 + 1 个配置清单 + 1 个 pom**，是对 Jakarta Mail + Hutool 邮件工具的「项目化封装」。核心产物是 `MailBuilder` — 一个流式邮件构建器，让业务代码用一行链式调用就能发送邮件（含附件、内嵌图片、抄送密送等进阶用法）。理解它，等于理解 RuoYi-Vue-Plus 如何用「自动配置 + Builder 模式」对底层 Java Mail 做零摩擦封装，以及它与兄弟模块 `ruoyi-common-sms`（短信）在架构上的同构与差异。达到能给同事讲清「MailBuilder.send() 内部发生了什么」「如何从 yml 配置到邮件发出追踪完整路径」，并能基于 MailBuilder 写出生产级邮件发送代码的程度。重点是**读懂设计动机、真实调用链与 Builder 模式的实现技巧**，不是从零学 Jakarta Mail 协议本身。

## Success looks like
- 能用一句话说清 `ruoyi-common-mail` 三层架构：`MailProperties`（映射配置）→ `MailConfig`（装配 Bean）→ `MailBuilder`（流式发送）。
- 能画出 `MailBuilder.of().to("xx@xx.com").subject("测试").text("hello").send()` 的完整执行路径，包括：私有构造器 → 静态工厂 → 链式设值 → `validate()` 校验 → `resolveMailAccount()` 账户解析 → `JakartaMail.create()` → `mail.send()`。
- 能讲清 `MailProperties.toMailAccount()` 方法如何把 yml 的 10 个 `mail.*` 属性转成 Hutool 的 `MailAccount` 对象，以及 `@ConfigurationProperties(prefix = "mail")` 的绑定机制。
- 能解释 `MailConfig` 里的 `@ConditionalOnProperty(value = "mail.enabled", havingValue = "true")` 的作用：为什么邮件模块需要开关、开关关闭时 `MailAccount` Bean 不存在会导致什么。
- 能解释 `resolveMailAccount()` 的「账户克隆 + 字段覆盖」策略：当调用者临时覆盖 from/user/pass 时，为什么必须克隆一份而不是直接改全局 Bean，及其对 `useGlobalSession` 的影响。
- 能对比 `ruoyi-common-mail` 与 `ruoyi-common-sms` 的模块结构，说出两者的**相同**（都是 3 类模块 + AutoConfiguration.imports + pom）与**不同**（mail 多了一层 Builder 模式封装、没有异常处理器、使用条件开关而非 @Primary、底层依赖 Hutool 而非 sms4j）。
- 能写出一个包含 HTML 正文 + 附件 + 抄送的邮件发送代码，并对每个链式调用方法说明其源码位置。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端代码阅读与设计分析。
- 目标是「读懂」而非「改造邮件协议」— 课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 写代码」为主。
- 全部讲解基于仓库真实代码与 Hutool Jakarta Mail 封装（已逐行核对），引用具体文件路径与行号。
- 交互语言：简体中文。

## Out of scope
- Jakarta Mail（jakarta.mail-api / org.eclipse.angus）底层 SMTP 协议细节（EHLO、AUTH LOGIN、DATA 等命令）— 只讲项目如何调用，不讲协议报文。
- Spring Boot 自带的 `spring-boot-starter-mail` / `JavaMailSender` 用法对比 — 在第 1 课鸟瞰中点到为止，不做深度比较。
- Hutool 框架内部 `MailAccount` / `JakartaMail` 的全部 API — 只讲本项目用到的核心方法。
- 工作流中的邮件通知业务编排细节 — 在第 3 课实战中展示一个使用场景，不铺开讲工作流引擎本身。
- 邮件模板引擎（如 Thymeleaf / Freemarker 渲染 HTML 邮件）— 本模块不涉及，属于业务层自行组装的内容。

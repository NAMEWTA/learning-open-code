# ruoyi-common-social 社交登录模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-social/`）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _JustAuth 官方文档_ — Dromara（justauth.cn）](https://www.justauth.cn/)
  本模块封装的 OAuth 聚合框架权威说明。理解 `AuthRequest` / `AuthSource` / `AuthStateCache` / `AuthToken` / `AuthUser` / `AuthCallback` / `AuthConfig` 时查阅。本模块的一切第三方登录能力都建立在它之上。
- [代码: _ruoyi-common-social 模块全部源码_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-social/src/main/java/)
  模块第一现场。13 个 Java 文件分布在 5 个包下。任何关于「这个模块做了什么」的问题，最终答案在这里。
- [代码: _SocialUtils.java —— 27 个平台的统一调度中心_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-social/src/main/java/org/dromara/common/social/utils/SocialUtils.java)
  模块的「大脑」——`getAuthRequest()` 的 `switch` 语句是理解「JustAuth 的 AuthRequest 怎么被实例化」的最佳起点。
- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `AutoConfiguration.imports` / `@EnableConfigurationProperties` 机制时查阅。
- [代码: _JustAuth AuthDefaultRequest 源码_](https://github.com/justauth/JustAuth/blob/master/src/main/java/me/zhyd/oauth/request/AuthDefaultRequest.java)
  理解自定义提供者（Gitea/MaxKey/TopIAM）如何通过继承 `AuthDefaultRequest` 接入框架时查阅。关键方法：`login()` / `authorize()` / `getAccessToken()` / `getUserInfo()`。
- [代码: _JustAuth AuthStateCache 接口_](https://github.com/justauth/JustAuth/blob/master/src/main/java/me/zhyd/oauth/cache/AuthStateCache.java)
  理解 `AuthRedisStateCache` 要实现的四个方法（`cache` / `get` / `containsKey`）以及 JustAuth 为什么设计这个缓存抽象时查阅。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明，含登录策略、社交登录配置等章节。理解模块在整体架构中的位置时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么这样封装」「某平台 OAuth 行为变化」时，Issues 与讨论区最贴近维护者意图。JustAuth 与 RuoYi-Vue-Plus 同属 Dromara 社区，问题常能交叉解答。
- [社区: _JustAuth GitHub Issues_](https://github.com/justauth/JustAuth/issues)
  遇到特定平台 OAuth 对接问题（如企业微信 corpId 验证、钉钉 V2 接口变更）时，JustAuth 的 Issues 是平台细节的第一手资料。

## Gaps
- JustAuth 部分内置平台的 OAuth 文档（如 Coding、StackOverflow）较为简略或已过时，实际以仓库源码为准。
- MaxKey / TopIAM 作为国内较新的 IAM 产品，社区文档仍在完善中，本项目是参考实现之一。

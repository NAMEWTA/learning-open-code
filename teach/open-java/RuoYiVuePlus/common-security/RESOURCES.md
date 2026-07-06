# ruoyi-common-security 安全模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（含 Sa-Token 源码）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-security 模块三件套_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-security/src/main/java/org/dromara/common/security/)
  `config/SecurityConfig.java` / `config/properties/SecurityProperties.java` / `handler/AllUrlHandler.java`。任何关于「这个模块做了什么」的问题，最终答案在这三个文件里。
- [代码: _ruoyi-common-satoken 基础能力模块_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-satoken/src/main/java/org/dromara/common/satoken/)
  `LoginHelper`、`StpUtil` 等 Sa-Token 基础封装在此。理解本模块中 `LoginHelper.CLIENT_KEY` / `LoginHelper.CLIENT_ACCESS_PATH_KEY` / `LoginHelper.CLIENT_IP_WHITELIST_KEY` 的来源与含义时查阅。
- [官方文档: _Sa-Token 官方文档_](https://sa-token.cc/)
  本模块底层依赖的认证授权框架权威说明。理解 `SaServletFilter` / `SaInterceptor` / `SaRouter` / `StpUtil` 的核心 API 时查阅。
- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `@EnableConfigurationProperties` / `FilterRegistrationBean` / `InitializingBean` / `WebMvcConfigurer` 的机制时查阅。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明，含安全配置、权限注解、客户端管理等章节。理解模块在整体架构中的位置时查阅。
- [代码: _安全配置实际使用现场 — yml 配置_](RuoYi-Vue-Plus/ruoyi-admin/src/main/resources/application-dev.yml)
  查找 `security.excludes` 配置段，了解项目中实际排除了哪些路径。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么这样配置过滤」「SSE 场景鉴权失败」等问题时，Issues 与讨论区最贴近维护者意图。Sa-Token 与 RuoYi-Vue-Plus 同属 Dromara 社区，问题常能交叉解答。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + Sa-Token 官方文档 + Spring Boot 官方文档支撑。

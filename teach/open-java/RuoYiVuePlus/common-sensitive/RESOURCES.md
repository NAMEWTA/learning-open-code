# ruoyi-common-sensitive 数据脱敏模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（含 hutool DesensitizedUtil 源码）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-sensitive 模块五件套_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-sensitive/src/main/java/org/dromara/common/sensitive/)
  `@Sensitive` 注解 / `SensitiveStrategy` 策略枚举 / `SensitiveJsonFieldProcessor` 处理器 / `SensitiveConfig` 自动配置 / `SensitiveService` 服务接口。任何关于「这个模块做了什么」的问题，最终答案在这五个文件里。
- [代码: _DesensitizedUtils 自定义脱敏工具_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-core/src/main/java/org/dromara/common/core/utils/DesensitizedUtils.java)
  继承 hutool `DesensitizedUtil`，提供 `mask()` 灵活脱敏和 `maskHighSecurity()` 高安全脱敏方法。`SensitiveStrategy.STRING_MASK` 和 `MASK_HIGH_SECURITY` 的底层实现。
- [代码: _JsonFieldProcessor 接口_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-json/src/main/java/org/dromara/common/json/enhance/JsonFieldProcessor.java)
  JSON 增强框架的核心扩展点接口，定义 `collect → prepare → process` 三阶段生命周期。`SensitiveJsonFieldProcessor` 作为其实现类，在 `process` 阶段执行脱敏。
- [代码: _JsonFieldContext 记录类_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-json/src/main/java/org/dromara/common/json/enhance/JsonFieldContext.java)
  响应字段上下文，通过 `getAnnotation()` 方法让处理器获取字段上的注解元数据——脱敏处理器通过它拿到 `@Sensitive` 注解。
- [官方文档: _hutool DesensitizedUtil_ — Hutool（hutool.cn）](https://doc.hutool.cn/pages/DesensitizedUtil/)
  本模块 11 种内置脱敏策略的底层实现来源。理解 `idCardNum` / `mobilePhone` / `email` / `bankCard` 等脱敏规则时查阅。
- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `@Bean` 注册 `SensitiveJsonFieldProcessor` 为 Spring Bean 的机制时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「脱敏不生效」「如何新增自定义策略」时，Issues 与讨论区最贴近维护者意图。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + hutool 文档 + 上述接口源码支撑。

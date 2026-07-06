# ruoyi-common-translation 翻译模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-translation 模块全部 11 个 Java 文件_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-translation/src/main/java/org/dromara/common/translation/)
  本模块的完整源码。任何关于「某个注解/接口/实现做了什么」的问题，最终答案在这些文件里。
  目录结构：`annotation/`（2 个注解）、`core/`（SPI 接口 + 5 个实现）、`core/handler/`（JSON 管线处理器）、`config/`（自动装配）、`constant/`（类型常量）。
- [代码: _ruoyi-common-json 的 JsonFieldProcessor 扩展点_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-json/src/main/java/org/dromara/common/json/enhance/)
  翻译处理器接入的 JSON 增强管线。理解 `collect → prepare → process` 三阶段生命周期时，对照 `JsonFieldProcessor.java` 接口的三个 default 方法。理解字段上下文与注解读取时，对照 `JsonFieldContext.java` 的 `getAnnotation()` 方法。
- [代码: _翻译模块的实际使用现场_](RuoYi-Vue-Plus/)
  在 RuoYi 业务模块中搜索 `@Translation(type` 可见所有使用该注解的 VO 字段。典型场景：用户列表返回 `createDept`（部门名称）、`createBy`（创建人用户名）、`avatar`（OSS URL）等字段均带翻译注解。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明，含翻译模块的功能定位与使用示例。
- [Spring 文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `AutoConfiguration.imports` 机制时查阅。`TranslationConfig` 通过此机制实现「依赖即生效」。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「翻译模块如何扩展自定义类型」「批量翻译的性能考量」等问题时，Issues 与讨论区最贴近维护者意图。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + ruoyi-common-json 扩展点源码 + 上述文档支撑。
- 外部无可直接参考的「Java 注解驱动翻译引擎」独立文档——本模块是 RuoYi 原创设计，理解它的最佳资源就是其自身源码。

# ruoyi-common-json 序列化模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-json/`）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _Jackson Core / Databind / Annotations_ — FasterXML（GitHub Wiki）](https://github.com/FasterXML/jackson-docs/wiki)
  本模块使用的 `tools.jackson`（即 FasterXML Jackson 3.x 的包重命名版）。理解 `JsonMapper`、`SimpleModule`、`JsonGenerator`、`ValueDeserializer`、`JsonSerializer`、`BeanPropertyDefinition`、`AnnotatedMember` 时查阅。注意本仓库用 `tools.jackson` 而非 `com.fasterxml.jackson`——这是 RuoYi 为避开包冲突做的 re-shade。
- [官方文档: _Jackson · ObjectMapper / JsonMapper_ — FasterXML](https://github.com/FasterXML/jackson-docs/wiki/JacksonFeatures)
  理解 `JsonMapper`（Jackson 3.x 替代 `ObjectMapper` 的不可变构建器）的配置方式、`SerializationConfig`、`ClassIntrospector` 等内部 API 时查阅。
- [官方文档: _Hutool · 日期工具 DateUtil_ — Hutool（hutool.cn）](https://doc.hutool.cn/pages/DateUtil/)
  两个自定义反序列化器（`CustomDateDeserializer`、`CustomLocalDateTimeDeserializer`）都委托给 `DateUtil.parse()`。理解它如何支持「yyyy-MM-dd HH:mm:ss」「yyyy/MM/dd」「时间戳」等多种格式自动识别时查阅。
- [官方文档: _Bean Validation 2.0 / Jakarta Validation_ — Jakarta EE](https://jakarta.ee/specifications/bean-validation/)
  `@JsonPattern` 是标准的 `@Constraint` 注解，`JsonPatternValidator` 实现 `ConstraintValidator`。理解 `initialize` 与 `isValid` 的生命周期、`groups` 与 `payload` 的作用时查阅。
- [官方文档: _Spring Boot · Jackson Auto-configuration_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/json.html)
  理解 `JacksonAutoConfiguration`、`JsonMapperBuilderCustomizer` 在自动装配链中的位置，以及 `@AutoConfiguration(before = JacksonAutoConfiguration.class)` 为什么排在它前面时查阅。
- [代码: _config / enhance / handler / utils / validate 五个目录_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-json/src/main/java/org/dromara/common/json/)
  模块第一现场。任何「这个能力到底怎么实现」的问题，最终答案在这里。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么用 tools.jackson 而非 com.fasterxml.jackson」「JsonValueEnhancer 设计动机」「字段增强与 Jackson 原生过滤器的区别」时，Issues 和讨论区是最贴近维护者意图的反馈源。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + 上述官方文档支撑。

# ruoyi-common-doc 接口文档模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（含 springdoc-openapi sources jar）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _SpringDoc 官方文档_ — springdoc.org](https://springdoc.org/)
  本模块封装的核心框架权威说明。理解 `GlobalOperationCustomizer` / `GlobalOpenApiCustomizer` / `JavadocProvider` / `OpenAPI` 等核心接口时查阅。本模块的一切定制都建立在这些扩展点上。
- [代码: _ruoyi-common-doc 模块全部文件_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-doc/src/main/java/org/dromara/common/doc/)
  8 个 Java 文件的完整源码。`SpringDocConfig` / `SpringDocProperties` / `JavadocOperationCustomizer` / `ClassTagOperationCustomizer` / `JavadocResolver` / `AbstractMetadataJavadocResolver` / `SaTokenAnnotationMetadataJavadocResolver` / `SaTokenSecurityMetadata`。任何关于「这个模块做了什么」的问题，最终答案在这 8 个文件里。
- [代码: _自动配置清单_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-doc/src/main/resources/META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports)
  声明 `org.dromara.common.doc.config.SpringDocConfig` 为自动配置类。理解「依赖即生效」机制时对照查阅。
- [官方文档: _OpenAPI 3.0 规范_ — Swagger（swagger.io）](https://swagger.io/specification/)
  理解 `OpenAPI` / `Info` / `Paths` / `Operation` / `Tag` / `SecurityRequirement` 等模型对象时查阅。本模块所有生成内容都是 OpenAPI 模型。
- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `AutoConfiguration.imports` / `before` / `after` 排序 / `@EnableConfigurationProperties` 等机制时查阅。
- [代码: _therapi-runtime-javadoc_](https://github.com/dnault/therapi-runtime-javadoc)
  使 JavaDoc 在运行时可通过 `JavadocProvider` 读取的 Maven 插件。理解为什么能读到 Controller 方法的 JavaDoc 时查阅。
- [代码: _SaToken 权限注解_](https://sa-token.cc/)
  `@SaCheckPermission` / `@SaCheckRole` / `@SaIgnore` 等注解的属性定义。理解 `SaTokenAnnotationMetadataJavadocResolver` 反射读取的属性名时查阅。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明，含接口文档章节。理解模块在整体架构中的位置时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么这样定制 SpringDoc」「自定义注解怎么加文档描述」时，Issues 与讨论区最贴近维护者意图。
- [社区: _SpringDoc GitHub Issues_](https://github.com/springdoc/springdoc-openapi/issues)
  SpringDoc 自身的扩展点机制、版本兼容性问题，GitHub Issues 是最佳参考。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + SpringDoc 源码 + 上述官方文档支撑。

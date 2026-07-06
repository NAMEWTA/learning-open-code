# ruoyi-common-doc 接口文档模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**SpringDoc / springdoc-openapi**：
基于 OpenAPI 3.0 规范的 Spring Boot 自动集成库。自动扫描 Controller 生成 `/v3/api-docs` JSON 端点，配合 Swagger UI 提供可视化 API 文档。本模块通过实现其扩展接口（`GlobalOperationCustomizer` / `GlobalOpenApiCustomizer`）进行项目级定制。
_Avoid_: 「Swagger」（Swagger 是旧版规范 2.0，SpringDoc 实现的是 OpenAPI 3.0）。

**OpenAPI**：
OpenAPI 3.0 规范的 Java 模型根对象（`io.swagger.v3.oas.models.OpenAPI`）。包含 `info`（文档信息）、`tags`（标签分组）、`paths`（API 路径）、`components`（组件/安全方案）。SpringDoc 自动生成它，本模块的定制器对它做增强。
_Avoid_: 「API 文档 JSON」（虽然它最终序列化为 JSON，但在代码里它是一个对象图）。

**GlobalOperationCustomizer**：
SpringDoc 提供的全局操作定制器接口。`customize(Operation, HandlerMethod)` 方法在每个 API 操作生成后被回调，可修改操作的 `summary`、`description`、`tags` 等属性。`JavadocOperationCustomizer` 和 `ClassTagOperationCustomizer` 都实现了它。
_Avoid_: 「操作拦截器」（它不是拦截器，不控制请求处理，只在文档生成阶段生效）。

**GlobalOpenApiCustomizer**：
SpringDoc 提供的全局文档定制器接口。`customise(OpenAPI)` 方法在完整 OpenAPI 对象构建后被回调，可修改顶层 tags、paths、components。`ClassTagOperationCustomizer` 和 `SpringDocConfig.openApiCustomizer()` 都实现了它。
_Avoid_: 「文档过滤器」（它不只过滤，还能增加和修改内容）。

**JavadocProvider**：
SpringDoc 提供的 JavaDoc 运行时读取器。从 `therapi-runtime-javadoc` 编译期生成的 JSON 中读取类和方法级 JavaDoc。核心方法：`getClassJavadoc(Class)` / `getMethodJavadocDescription(Method)` / `getFirstSentence(String)`。
_Avoid_: 「JavaDoc 工具类」（它是 SpringDoc 框架内的特定抽象，不是通用工具）。

**JavadocResolver**：
本模块自建的扩展点接口（`core/resolver/JavadocResolver.java`）。继承 `Comparable` 和 `Ordered`，定义 `supports(HandlerMethod)` 判断是否处理、`resolve(HandlerMethod, Operation)` 执行解析、`getOrder()` 排序。允许为不同权限框架（SaToken、Spring Security 等）注册独立的文档增强解析器，而不修改核心定制器代码。
_Avoid_: 「权限解析器」（它是一个通用扩展点，不限于权限）。

**SaTokenSecurityMetadata**：
本模块自建的权限元数据模型（`core/model/SaTokenSecurityMetadata.java`）。用 `List<AuthInfo> permissions` 存权限校验信息、`List<AuthInfo> roles` 存角色校验信息、`boolean ignore` 存是否跳过校验。核心方法 `toMarkdownString()` 将权限规则转为可嵌入 API 描述的 Markdown 文本。
_Avoid_: 「权限配置」（它是文档生成模型，不是运行时鉴权数据）。

**SpringDocProperties**：
本模块的配置属性类（`config/properties/SpringDocProperties.java`）。通过 `@ConfigurationProperties(prefix="springdoc")` 将 yml 中 `springdoc.*` 段直接映射为类型安全的 Java 对象（含 `info` / `externalDocs` / `tags` / `paths` / `components`）。其中的 `InfoProperties` 内部类是为了让 Spring Boot 生成配置提示而单独声明的文档信息结构。
_Avoid_: 「文档配置」、「Swagger 配置」（它是属性映射 POJO，不是配置逻辑类）。

**AutoConfiguration.imports**：
Spring Boot 3.x 的自动配置发现文件（`META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`）。每行一个自动配置类的全限定名。Spring Boot 启动时扫描所有 jar 中的这个文件，加载其中声明的配置类。本模块用它声明 `SpringDocConfig`，实现「依赖即生效」。
_Avoid_: 「spring.factories」（那是 Spring Boot 2.x 的旧机制，本模块用新格式）。

**therapi-runtime-javadoc**：
开源 Maven 插件 + 运行时库，可在运行时通过 JSON 文件读取编译期保留的 JavaDoc 注释。SpringDoc 的 `JavadocProvider` 依赖它。本模块能读到 Controller 方法的原始 JavaDoc 中文描述，最终靠的就是这个库。
_Avoid_: 「Javadoc 解析器」（它是底层数据源，不做解析逻辑）。

**PlusPaths**：
`SpringDocConfig` 内部定义的 `Paths` 子类（`static class PlusPaths extends Paths`）。不添加任何字段或逻辑，纯粹作为**标记类**使用。`openApiCustomizer()` 用 `if (oldPaths instanceof PlusPaths) return;` 判断是否已处理过路径，防止多次回调时重复添加 context-path 前缀。
_Avoid_: 「路径工具类」（它是标记类，不是工具）。

**HandlerMethod**：
Spring MVC 的处理器方法封装（`org.springframework.web.method.HandlerMethod`）。包含 Controller 的 Bean 实例（`getBean()`）、具体方法（`getMethod()`）、方法参数等信息。SpringDoc 的定制器回调它，本模块通过它获取 JavaDoc、注解信息。
_Avoid_: 「Controller 方法」（HandlerMethod 是对 Controller 方法的元数据包装，不是方法本身）。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

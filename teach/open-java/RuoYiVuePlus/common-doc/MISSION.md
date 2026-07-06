# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-doc 接口文档模块

## Why
学习者要能彻底读懂 `ruoyi-common-doc` 这个公共模块：它只有 8 个 Java 文件，是对 SpringDoc（springdoc-openapi）的一层「项目化定制」——用 JavaDoc 运行时解析增强 API 描述、用 SaToken 注解解析自动生成权限文档、用自定义路径拼接修正上下文路径重复问题。理解它，等于理解 RuoYi-Vue-Plus 如何把 OpenAPI 文档从「能用」打磨成「好用」，达到能给同事讲清「这个模块为什么能自动从 JavaDoc 生成中文 API 描述」「Swagger UI 上的权限说明是怎么来的」「路径前缀为什么不会重复」，并能在此基础上排查文档生成异常或为自定义注解扩展文档描述。重点是**读懂设计动机与扩展点机制**，不是从零学 OpenAPI 规范。

## Success looks like
- 能用一句话说清 `ruoyi-common-doc` 与 SpringDoc 的关系，并说出模块 8 个文件分成哪几层、各层承担什么职责。
- 能解释 `SpringDocConfig` 里的 5 个 `@Bean` 各自注册了什么，以及 `@AutoConfiguration(before=SpringDocConfiguration)` 这个时序声明的意义。
- 能讲清 `SpringDocProperties` 如何用 `@ConfigurationProperties(prefix="springdoc")` 直接映射 SpringDoc 的 yml 配置段，以及 `InfoProperties` 为什么要复制一个内部类出来。
- 能讲清 `JavadocOperationCustomizer` 的完整流程：拿到 `JavadocProvider` → 取方法 JavaDoc → 首句作 `summary`、全文作 `description` → 然后遍历 `JavadocResolver` 列表追加扩展描述（权限说明）。
- 能讲清 `ClassTagOperationCustomizer` 同时实现两个定制器接口（`GlobalOperationCustomizer` + `GlobalOpenApiCustomizer`）的设计意图，以及 JavaDoc 第一行替换 Controller 类名作 tag 的完整逻辑。
- 能讲清 `JavadocResolver` 接口 + `AbstractMetadataJavadocResolver` 抽象类的扩展点设计：`supports()` 判断是否处理、`resolve()` 执行解析、`compareTo()` 按 order 排序——新增一个权限框架的文档解析器只需要继承抽象类。
- 能讲清 `SaTokenAnnotationMetadataJavadocResolver` 如何用**字符串类名 + ClassLoaderUtil** 加载 SaToken 注解（避免硬依赖），以及 `SaTokenSecurityMetadata` 如何把 `@SaCheckPermission` / `@SaCheckRole` / `@SaIgnore` 转成 Markdown 权限说明。
- 能讲清 `openApiCustomizer()` 中 `PlusPaths` 内部类的设计——为什么不能直接加前缀而要用一个标记类防止 `GlobalOpenApiCustomizer` 被多次回调导致路径重复。
- 能读懂 `AutoConfiguration.imports` 文件的作用，并能把本模块的自动装配模式迁移到自定义的 common 模块。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会在第 5 课联系到 Swagger UI 前端呈现（点到为止）。
- 目标是「读懂」而非「能改框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路」为主。
- 全部讲解基于仓库真实代码与 SpringDoc 源码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- OpenAPI 3.0 规范的完整语法（paths、components、security schemes 的字段细节）——只在用到时解释。
- Swagger UI / Knife4j 的前端渲染实现——只讲模块生成了什么数据，不讲 UI 怎么画。
- SaToken 框架本身的鉴权逻辑（`@SaCheckPermission` 的拦截器如何工作）——只在注解解析时引用其属性名。
- 其他 ruoyi-common-* 模块的完整实现——仅在与本模块的依赖边界处点到。
- `therapi-runtime-javadoc` 插件的 Maven 配置与编译期行为——只讲运行时如何读取 JavaDoc。

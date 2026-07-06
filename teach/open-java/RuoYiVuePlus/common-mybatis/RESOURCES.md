# ruoyi-common-mybatis 持久层模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-mybatis/`）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _MyBatis-Plus 官方文档_ — baomidou（baomidou.com）](https://baomidou.com/pages/24112f/)
  本模块的基石。理解 `BaseMapper`、`LambdaQueryWrapper`、`MetaObjectHandler`、`PaginationInnerInterceptor`、`OptimisticLockerInnerInterceptor`、`IdentifierGenerator`、`PostInitTableInfoHandler` 时查阅。`BaseMapperPlus` 继承了 `BaseMapper<T>`，`InjectionMetaObjectHandler` 实现了 `MetaObjectHandler`，`MybatisPlusConfig` 注册了分页和乐观锁插件。

- [官方文档: _MyBatis-Plus-Join (MPJ) 文档_ — yulichang（GitHub）](https://github.com/yulichang/mybatis-plus-join)
  联表查询框架。理解 `MPJLambdaWrapper`、`JoinWrappers`、`selectAs`、`leftJoin` 时查阅。`LambdaJoinQueryBuilder` 底层封装的就是 `MPJLambdaWrapper`，`QueryBuilder.lambdaJoin()` 通过 `JoinWrappers.lambda()` 创建。

- [官方文档: _dynamic-datasource 多数据源_ — baomidou（GitHub）](https://github.com/baomidou/dynamic-datasource-spring-boot-starter)
  多数据源框架。理解 `DynamicRoutingDataSource`、`DynamicDataSourceContextHolder`、`@DS` 注解时查阅。`DataBaseHelper` 通过 `SpringUtils.getBean(DynamicRoutingDataSource.class)` 获取数据源路由对象，再通过 `determineDataSource()` 解析当前数据源。

- [官方文档: _JSqlParser_ — JSqlParser（GitHub）](https://github.com/JSQLParser/JSqlParser)
  SQL 解析器。理解 `PlusDataPermissionInterceptor` 如何用 `CCJSqlParserUtil.parseExpression()` 解析数据权限 SQL 片段，以及 `processSelect/processUpdate/processDelete` 如何向原始 SQL 注入 WHERE 条件时查阅。

- [官方文档: _Spring Expression Language (SpEL)_ — Spring（docs.spring.io）](https://docs.spring.io/spring-framework/reference/core/expressions.html)
  SpEL 表达式引擎。理解 `DataScopeType` 枚举中的 `#{#deptName}`、`#{#user.deptId}`、`#{@sdss.xxx}` 模板如何被 `PlusDataPermissionHandler` 解析时查阅。涉及 `SpelExpressionParser`、`TemplateParserContext`、`StandardEvaluationContext`、`BeanFactoryResolver`。

- [代码: _annotation / aspect / config / core / enums / handler / helper / interceptor / utils 九大目录_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-mybatis/src/main/java/org/dromara/common/mybatis/)
  模块第一现场。任何「这个能力到底怎么实现」的问题，最终答案在这里。34 个 Java 文件按职责清晰分包。

- [代码: _ruoyi-common-core 工具模块_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-core/)
  本模块依赖的基础工具模块。理解 `MapstructUtils`（Entity-VO 转换）、`SpringUtils`（getBean）、`SqlUtil`（SQL 转义）、`StringUtils` 时查阅。

- [官方文档: _RuoYi-Vue-Plus 官方文档 · 数据权限_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目对数据权限、多数据源、代码生成的设计说明。理解「为什么这样设计」「业务里怎么配」时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「某版本行为变化」「数据权限死循环排查」「多数据源切换失败」等问题时，Issues 和讨论区是最贴近维护者意图的反馈源。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + MyBatis-Plus / MPJ / dynamic-datasource 官方文档支撑。

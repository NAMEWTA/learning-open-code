# ruoyi-common-elasticsearch 搜索引擎模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（含 Easy-Es 3.0.2 sources jar）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _Easy-Es 官方文档_ — Dromara（easy-es.cn）](https://www.easy-es.cn/)
  本模块封装的核心框架权威说明。理解 `BaseEsMapper` / `LambdaEsQueryWrapper` / `@EsMapperScan` / `@IndexName` 时查阅。Easy-Es 在 API 设计上深度对标 MyBatis-Plus，有 MP 经验的开发者上手极快。

- [代码: _ruoyi-common-elasticsearch 模块_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-elasticsearch/src/main/java/org/dromara/common/elasticsearch/config/)
  `EasyEsConfiguration` + `ActuatorEnvironmentPostProcessor`。任何关于「这个模块做了什么」的问题，最终答案在这两个文件里。

- [代码: _DEMO 演示代码_](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-demo/src/main/java/org/dromara/demo/)
  `Document.java`（ES 实体）+ `DocumentMapper.java`（Mapper 接口）+ `EsCrudController.java`（REST 控制器）。这是模块的**真实使用现场**，展示了 Easy-Es 从实体定义到 CRUD 的完整模式。

- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `AutoConfiguration.imports` / `@ConditionalOnProperty` 机制时查阅。第 2 课的核心原理来源。

- [官方文档: _Spring Boot EnvironmentPostProcessor_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/api/java/org/springframework/boot/EnvironmentPostProcessor.html)
  理解 `EnvironmentPostProcessor` 接口、`Ordered` 排序、`ConfigurableEnvironment` 时查阅。第 3 课讲 `ActuatorEnvironmentPostProcessor` 的原理基础。

- [官方文档: _Elasticsearch 7.x REST API_ — Elastic](https://www.elastic.co/guide/en/elasticsearch/client/java-rest/7.17/index.html)
  Easy-Es 底层使用的是 Elasticsearch 7.17.28 的 REST 客户端。理解底层通信模型时查阅。

- [配置: _easy-es 配置段_](RuoYi-Vue-Plus/ruoyi-admin/src/main/resources/application.yml#L288-L332)
  `easy-es.enable` / `address` / `global-config` 等全部 Easy-Es 配置项的实际使用示例。理解「配置如何驱动模块行为」的第一手资料。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / Easy-Es Gitee Issues_](https://gitee.com/dromara/easy-es)
  Easy-Es 与 RuoYi-Vue-Plus 同属 Dromara 社区。遇到版本兼容、API 行为等问题时，Issues 区最贴近维护者意图。

- [社区: _RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  项目自身的问题讨论区。关于「为什么 easy-es 默认关闭」「配置变更建议」等设计决策，可在此找到讨论记录。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + Easy-Es 官方文档 + 上述 Spring 文档支撑。

# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-elasticsearch 搜索引擎模块

## Why
学习者要能彻底读懂 `ruoyi-common-elasticsearch` 这个公共模块：它只有 2 个 Java 类，是对 Dromara 开源 Easy-Es 框架（Elasticsearch ORM 包装器）的一层「项目化适配」。理解它，等于理解 RuoYi-Vue-Plus 如何把 Elasticsearch 能力无侵入接入——通过 `@EsMapperScan` 扫描 Mapper、通过 `EnvironmentPostProcessor` 同步健康检查开关、通过 `@ConditionalOnProperty` 实现可插拔。达到能给同事讲清「这个模块只有 2 个类为什么能撑起整个 ES 引擎」「从配置到 CRUD 的完整链路怎么走」，并能基于它自己新建 ES 索引和业务查询的程度。重点是**读懂设计动机与真实依赖链**，不是从零学 Elasticsearch。

## Success looks like
- 能用一句话说清 `ruoyi-common-elasticsearch` 与 Easy-Es 的关系，并说出模块仅有的两个类各自承担什么职责。
- 能解释 `EasyEsConfiguration` 如何通过 `@AutoConfiguration` + `@ConditionalOnProperty` + `@EsMapperScan` 实现「easy-es.enable=true 即自动装配所有 EsMapper」的无侵入接入。
- 能讲清 `@EsMapperScan("org.dromara.**.esmapper")` 的包约定规则，理解为什么 `DocumentMapper` 放在 `org.dromara.demo.esmapper` 包下就能被自动发现。
- 能解释 `ActuatorEnvironmentPostProcessor` 如何通过 `EnvironmentPostProcessor` + `Ordered.HIGHEST_PRECEDENCE` 在 Spring 启动最早阶段同步 `easy-es.enable` 到 `management.health.elasticsearch.enabled`，避免关闭 ES 后健康检查报错。
- 能完整追踪「开启 ES → 配置连接 → 定义实体 → 编写 Mapper → CRUD 查询」这条链路：`application.yml` 中 `easy-es.enable=true` → `EasyEsConfiguration` 激活 → `DocumentMapper` 被扫描 → `EsCrudController` 注入 `DocumentMapper` → `LambdaEsQueryWrapper` 构建查询。
- 能模仿 `DocumentMapper` + `Document` + `EsCrudController` 的模式，为自己业务新建一个 ES 索引和查询接口。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会在第 3 课联系到 ES REST API 调用入口。
- 目标是「读懂」而非「精通 Elasticsearch」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 写简单查询」为主。
- 全部讲解基于仓库真实代码与 Easy-Es 3.0.2 版本（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- Elasticsearch 集群搭建、索引分片策略、聚合分析、分词器配置等 DBA/运维话题。
- Easy-Es 框架的全部 API（如嵌套查询、聚合、高亮、分页）——只讲项目 DEMO 中用到的核心 CRUD 方法。
- MyBatis-Plus 的使用方式——仅在与 Easy-Es API 风格对比时点到。
- Elasticsearch 与 MySQL 的数据同步方案（canal/logstash）。
- 本模块不包含的 Easy-Es 高级功能（如自动建索引注解 `@IndexName`、`@Settings` 等，DEMO 中未使用）。

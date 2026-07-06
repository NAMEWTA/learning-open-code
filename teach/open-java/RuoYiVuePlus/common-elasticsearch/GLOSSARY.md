# ruoyi-common-elasticsearch 搜索引擎模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**Easy-Es**：
Dromara 社区出品的开源 Elasticsearch ORM 框架（本项目使用 3.0.2 版本）。API 设计深度对标 MyBatis-Plus，提供 `BaseEsMapper` / `LambdaEsQueryWrapper` / `@EsMapperScan` 等开发者熟悉的编程模型，底层使用 Elasticsearch 7.17.28 REST 客户端。`ruoyi-common-elasticsearch` 的全部 ES 能力来自它。
_Avoid_: 「Easy-ES」（正确拼写为 Easy-Es，注意大小写）。

**BaseEsMapper**：
Easy-Es 的核心 Mapper 接口（`org.dromara.easyes.core.kernel.BaseEsMapper<T>`），对标 MyBatis-Plus 的 `BaseMapper`。继承它即可获得 `insert` / `selectOne` / `selectList` / `updateById` / `deleteById` 等开箱即用的 CRUD 方法。如 `DocumentMapper extends BaseEsMapper<Document>`。
_Avoid_: 「BaseMapper」（那是 MyBatis-Plus 的接口，虽然 API 相似但处理的是 ES 索引而非数据库表）。

**EsMapperScan**：
Easy-Es 的 Mapper 扫描注解（`org.dromara.easyes.spring.annotation.EsMapperScan`），对标 MyBatis-Plus 的 `@MapperScan`。本模块使用 `@EsMapperScan("org.dromara.**.esmapper")` 自动扫描并注册指定包路径下所有 `BaseEsMapper` 子接口为 Spring Bean。是实现「只需放对包名即可被自动发现」的关键。
_Avoid_: 「@MapperScan」（那是 MyBatis 的注解，用于扫描 MyBatis Mapper）。

**LambdaEsQueryWrapper**：
Easy-Es 的 Lambda 查询条件构造器（`org.dromara.easyes.core.conditions.select.LambdaEsQueryWrapper<T>`），对标 MyBatis-Plus 的 `LambdaQueryWrapper`。通过 `wrapper.eq(Entity::getField, value)` 的 Lambda 方式构建 ES 查询条件，编译期安全、避免字符串硬编码。DEMO 中的精确查询和模糊搜索均使用它。
_Avoid_: 「QueryWrapper」（那是 Easy-Es 的非 Lambda 版本，本项目中只用 Lambda 版）。

**EnvironmentPostProcessor**：
Spring Boot 的环境后处理器接口（`org.springframework.boot.EnvironmentPostProcessor`）。在 Spring Application 准备 `Environment` 之后、ApplicationContext 刷新之前调用，允许在容器启动的最早阶段修改或补充环境属性。`ActuatorEnvironmentPostProcessor` 利用它同步 ES 开关到健康检查配置。
_Avoid_: 「BeanFactoryPostProcessor」（那是容器后处理器，执行时机比 EnvironmentPostProcessor 晚很多）。

**Ordered.HIGHEST_PRECEDENCE**：
Spring `Ordered` 接口定义的最高优先级常量（值为 `Integer.MIN_VALUE`）。`ActuatorEnvironmentPostProcessor` 返回此值，确保它在所有其他 `EnvironmentPostProcessor` 之前执行，避免健康检查组件在开关同步之前就读取到错误的配置。

**AutoConfiguration**：
Spring Boot 自动配置类注解（`org.springframework.boot.autoconfigure.AutoConfiguration`），是 `@Configuration` 的增强替代（Spring Boot 2.7+）。配合 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` 文件，实现「添加依赖即自动加载配置类」的无侵入装配。`EasyEsConfiguration` 通过它被 Spring Boot 发现和加载。
_Avoid_: 「@Configuration」（AutoConfiguration 是它的特殊化版本，专用于自动配置场景）。

**ConditionalOnProperty**：
Spring Boot 条件装配注解（`org.springframework.boot.autoconfigure.condition.ConditionalOnProperty`）。通过 `value = "easy-es.enable", havingValue = "true"` 控制配置类仅在 `application.yml` 中 `easy-es.enable=true` 时才生效。是实现「可插拔模块」的核心机制——默认关闭，需要时一行配置即可开启。
_Avoid_: 「@Conditional」（那是 Spring 底层的条件注解，ConditionalOnProperty 是其在属性匹配场景的便捷封装）。

**Elasticsearch Health Indicator**：
Spring Boot Actuator 提供的内置健康检查端点之一。当 `management.health.elasticsearch.enabled=true` 时，Actuator 会在 `/actuator/health` 中报告 ES 集群的连接状态。`ActuatorEnvironmentPostProcessor` 将它与 `easy-es.enable` 同步，确保关闭 Easy-Es 时健康检查也不会去尝试连接一个不存在的 ES 服务。
_Avoid_: 直接叫「健康检查」（不够精确，Actuator 有十几个内置健康指示器，这是 ES 专门的那个）。

**可插拔模块（Pluggable Module）**：
RuoYi `ruoyi-common-*` 模块的标准设计模式：通过 `@ConditionalOnProperty` 绑定一个 `*.enable` 开关，默认关闭、一行配置即可开启；通过 `@AutoConfiguration` + `.imports` 文件实现依赖即自动发现。`ruoyi-common-elasticsearch` 是本模式的典型代表——`easy-es.enable=false` 时整个模块零开销。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

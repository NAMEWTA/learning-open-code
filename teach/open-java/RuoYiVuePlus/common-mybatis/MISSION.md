# Mission: 全面读懂 RuoYi-Vue-Plus 的 ruoyi-common-mybatis 持久层模块

## Why
学习者要能在脑中完整重建 `ruoyi-common-mybatis` 这个核心公共模块「提供了什么能力、每个类各管什么、为什么这样设计」的全景。它是整个项目最核心的持久层模块（34 个 Java 文件），将 MyBatis-Plus 的能力从「能用」拔高到「企业级生产就绪」，提供了**数据权限/数据范围、增强查询构建器（Lambda 表达式 + JOIN）、多数据源、SQL 日志、自动填充**五大核心能力。理解它，就等于理解 RuoYi-Vue-Plus 的数据层骨架——所有业务模块的 CRUD 都建立在这个模块之上。重点是**读懂模块设计与各组件的职责**，不是从零实现一个 ORM 框架。讲解全部基于本仓库真实代码（已逐文件核对）。

## Success looks like
- 能用一张图讲清模块的四大支柱（BaseMapperPlus / 数据权限体系 / 增强查询构建器 / 多数据源与SQL日志）及其依赖关系，并说出每块的关键类。
- 能讲清 `BaseEntity` 的 5 个字段（createDept / createBy / createTime / updateBy / updateTime）如何通过 `@TableField(fill = ...)` 配合 `InjectionMetaObjectHandler` 实现 INSERT 和 INSERT_UPDATE 时自动填充，以及 `BaseMapperPlus<T,V>` 如何通过泛型双参数 + `MapstructUtils.convert` 实现 Entity 到 VO 的零模板转换。
- 能完整追踪数据权限链路：`@DataPermission` 注解 -> `DataPermissionPointcut` 切点匹配 -> `DataPermissionAdvice` 设 ThreadLocal -> `PlusDataPermissionInterceptor.beforeQuery/beforePrepare` -> `PlusDataPermissionHandler.getSqlSegment` -> SpEL 解析 `DataScopeType` 模板 -> JSqlParser 拼接 WHERE 条件，并说清 6 种 `DataScopeType`（ALL/CUSTOM/DEPT/DEPT_AND_CHILD/SELF/DEPT_AND_CHILD_OR_SELF）的 SQL 模板差异。
- 能解释 `DataPermissionHelper` 如何通过 `ThreadLocal` + `SaStorage` 实现注解 -> 切面 -> 拦截器三层之间的上下文传递，以及 `DataPermissionIgnoreContext` 如何用栈机制支持嵌套忽略数据权限。
- 能讲清 `QueryBuilder.lambda()` / `QueryBuilder.lambdaJoin()` 两个入口分别创建 `LambdaQueryBuilder`（基于 `AggregateLambdaQueryWrapper`）和 `LambdaJoinQueryBuilder`（基于 `MPJLambdaWrapper`），以及它们支持的标准 CRUD 条件、聚合函数（SUM/MAX/MIN/AVG/COUNT）、子查询（eqSub/inSub/existsSub）、FIND_IN_SET 等高级能力。
- 能说清 `PageQuery` 的 `build()` 方法如何将前端传的 `pageNum/pageSize/orderByColumn/isAsc` 转成 MyBatis-Plus 的 `Page<T>` 对象，以及排序字符串的解析规则（支持逗号分隔多字段 + 各自升降序）。
- 能讲清多数据源（dynamic-datasource 集成）与 `DataBaseHelper` 如何通过 `DynamicRoutingDataSource` 获取当前数据库类型，并用缓存 + `DatabaseMetaData` 实现 `findInSet` 的多数据库方言（MySQL/Oracle/PostgreSQL/SQL Server）兼容。
- 能讲清 `SqlLogInterceptor` 如何拦截 `StatementHandler.query/update/batch` 方法，解析 `BoundSql` 参数占位符还原完整 SQL，并按 8000 字符分片输出（支持日志系统或控制台两种输出模式），以及为什么用 `ReentrantLock` 保护控制台输出。
- 能结合实际业务场景推导「超级管理员查看全部」「部门经理看本部门及以下」「普通员工只看自己」三条数据权限策略如何通过配置角色的 `dataScope` 字段值（1/4/5）和 `@DataPermission` 注解自动生效。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解以追踪真实代码 + 解释设计动机为主。
- 目标是「读懂并能正确选用」而非「能改框架」——练习以「读代码答问题 / 选型判断 / 复述链路」为主。
- 全部讲解基于仓库真实代码，引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- MyBatis-Plus 框架本身的完整 API 与底层实现——仅讲本模块用到并扩展的部分。
- MyBatis-Plus-Join（MPJ）的完整联表能力——仅讲本模块 `LambdaJoinQueryBuilder` 封装的部分。
- dynamic-datasource 框架的完整配置与多数据源切换策略——仅讲 `DataBaseHelper` 的数据库类型识别。
- 业务模块里具体怎么用这些能力（如 SysUserMapper、SysDeptService 等业务类的具体查询逻辑）——仅在举例时引用，不展开业务。
- JSqlParser 的 SQL 解析引擎细节——仅在数据权限 WHERE 条件拼接处点到。
- SpEL 表达式的完整语法——仅讲 `DataScopeType` 模板中用的 `#{#deptName}` 和 `#{@sdss.xxx}` 格式。
- MySQL/Oracle/PostgreSQL/SQL Server 各自的 SQL 方言差异——仅讲 `DataBaseHelper.findInSet` 的适配逻辑。

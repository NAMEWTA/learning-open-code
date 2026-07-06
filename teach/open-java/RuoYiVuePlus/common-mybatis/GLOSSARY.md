# ruoyi-common-mybatis 持久层模块 Glossary

记录学习者在 8 节课程中**真正理解**的核心术语。覆盖 Entity 基类、数据权限、查询构建器、多数据源、SQL 日志五大块。

## Terms

**BaseMapperPlus**：
项目自定义的 Mapper 顶接口，继承 MyBatis-Plus 的 `BaseMapper<T>` 并引入第二个泛型 `<V>`（VO 类型）。提供 `selectVoById/selectVoList/selectVoPage` 等 Entity 到 VO 自动转换方法，以及 `insertBatch/updateBatchById` 等便捷批处理方法。底层用 `MapstructUtils.convert` 做转换、`Db.saveBatch` 做批处理。入口文件：`core/mapper/BaseMapperPlus.java`。
_Avoid_: 「BaseMapper」（MyBatis-Plus 原生接口，仅单泛型 `<T>`，无 VO 转换能力）。

**BaseEntity**：
所有业务实体的基类（JPA 风格），继承 `Serializable`，定义 5 个公共审计字段：`createDept`（创建部门）、`createBy`（创建者）、`createTime`（创建时间）标记 `FieldFill.INSERT`；`updateBy`（更新者）、`updateTime`（更新时间）标记 `FieldFill.INSERT_UPDATE`。`@TableField(fill = ...)` 注解触发了 `InjectionMetaObjectHandler` 的自动填充。入口文件：`core/domain/BaseEntity.java`。

**InjectionMetaObjectHandler**：
实现 MyBatis-Plus `MetaObjectHandler` 接口的自动填充处理器。`insertFill` 对 `BaseEntity` 实例自动填 `createTime/updateTime/createBy/updateBy/createDept`；`updateFill` 填 `updateTime/updateBy`。用户 ID 通过 `LoginHelper.getLoginUser()` 获取，获取不到时填默认值 -1（代表无用户/系统操作）。入口文件：`handler/InjectionMetaObjectHandler.java`。

**@DataPermission**：
数据权限注解，标记在 Mapper 方法或类上（`@Target({METHOD, TYPE})`），包含 `@DataColumn` 数组和 `joinStr`（拼接 AND/OR）。注解本身不执行 SQL 拼接——它只标记「这个方法/类需要数据权限过滤」，真正的拼接由 `PlusDataPermissionHandler` 完成。入口文件：`annotation/DataPermission.java`。

**@DataColumn**：
数据权限字段映射注解，定义 SpEL 模板中的占位符 key（如 `deptName`、`userName`）与数据库列名 value（如 `dept_id`、`user_id`）的对应关系。一个 `@DataPermission` 可包含多个 `@DataColumn`，如同时标注部门列和用户列。入口文件：`annotation/DataColumn.java`。

**DataScopeType**：
数据权限范围枚举，含 6 种类型：`ALL`（全部数据，code=1，无 SQL 条件）、`CUSTOM`（自定义，code=2）、`DEPT`（本部门，code=3）、`DEPT_AND_CHILD`（部门及以下，code=4）、`SELF`（仅自己，code=5）、`DEPT_AND_CHILD_OR_SELF`（部门及以下或自己，code=6）。每种类型绑定了 SpEL 模板 SQL（`sqlTemplate`）和兜底 SQL（`elseSql`，通常为 `1 = 0` 即无数据）。入口文件：`enums/DataScopeType.java`。

**数据权限三层架构**：
`@DataPermission` 控制的是「要不要过滤」和「用什么 SQL 模板」，分三层协作：① 切面层：`DataPermissionPointcut` + `DataPermissionAdvice` 拦截 Mapper 调用，将注解存入 `ThreadLocal`；② 拦截器层：`PlusDataPermissionInterceptor` 在 MyBatis 执行 SQL 前（`beforeQuery`/`beforePrepare`）检查注解，调用处理器拼接 WHERE 条件；③ 处理器层：`PlusDataPermissionHandler` 解析 SpEL 模板、获取当前用户角色、生成 SQL 片段并通过 JSqlParser 注入原始 SQL。

**DataPermissionHelper**：
数据权限上下文工具类，无构造器（`@NoArgsConstructor(access = PRIVATE)`），桥接三层通信：用 `ThreadLocal<DataPermission>` 传递 `@DataPermission` 注解对象（`setPermission/getPermission/removePermission`）；用 `SaStorage` 传递 SpEL 变量（`getVariable/setVariable`）和权限访问控制（`getAccess/setAccess`）；提供 `ignore(Runnable/Supplier)` 在子查询中暂时关闭数据权限（防止 SpEL 模板内的 SQL 又触发数据权限，造成死循环）。入口文件：`helper/DataPermissionHelper.java`。

**DataPermissionAccess**：
Java `record` 类型，封装当前请求的权限和角色约束 `(Set<String> perms, Set<String> roleKeys)`。`PlusDataPermissionHandler.resolveAccess()` 从 HandlerMethod 上提取 `@SaCheckPermission` 和 `@SaCheckRole` 注解值，用于筛选参与数据权限计算的角色（`scopeRoles` 方法）。入口文件：`core/domain/DataPermissionAccess.java`。

**DataPermissionIgnoreContext**：
数据权限忽略状态管理器，用 `ThreadLocal<Deque<Boolean>>` 实现状态栈。`enable()` 压栈当前忽略状态并设置忽略；`disable()` 弹栈恢复之前状态。支持嵌套忽略：A 方法忽略中调 B 方法也忽略，B 退出后恢复 A 的状态。入口文件：`helper/DataPermissionIgnoreContext.java`。

**LambdaQueryBuilder**：
Lambda 查询构建器，包装 `AggregateLambdaQueryWrapper<T>`（继承 `LambdaQueryWrapper<T>`），提供 `eq/ne/gt/ge/lt/le/like/between/in/notIn/orderBy/groupBy/having` 等标准 CRUD 条件，以及 `selectSum/selectMax/selectMin/selectAvg/selectCount/selectSub` 等聚合查询。特殊能力：`eqSub/inSub/existsSub` 子查询条件、`findInSet` 数据库方言兼容、`eqIfPresent/likeIfText` 智能判空。通过 `QueryBuilder.lambda(SysUser.class)` 创建。入口文件：`core/query/LambdaQueryBuilder.java`。

**LambdaJoinQueryBuilder**：
MPJ 联表查询构建器，包装 `MPJLambdaWrapper<T>`，在 `LambdaQueryBuilder` 的基础上增加联表能力：`leftJoin`、`selectAs`（字段映射到别名对象）、`selectAll(entityClass, alias)`。条件方法需显式传表别名（如 `eq("u", SysUser::getUserId, value)`），支持 `betweenParams` 从 Map 读取参数。终端方法：`list(Class<R>)` / `page(P, Class<R>)` / `count()`。通过 `QueryBuilder.lambdaJoin(SysUser.class)` 创建。入口文件：`core/query/LambdaJoinQueryBuilder.java`。

**LambdaCrudChainWrapper**：
Mapper 级链式 CRUD 包装器，继承 `AbstractLambdaWrapper` 并实现 `Query`、`Update`、`LambdaQueryCondition` 接口。由 `BaseMapperPlus.lambda()` 创建，同时具备查询和更新能力。终端方法：`list()/voList()/one()/voOne()/page()/voPage()/delete()/update()` 等。聚合查询、子查询能力与 `LambdaQueryBuilder` 等价。入口文件：`core/mapper/LambdaCrudChainWrapper.java`。

**PageQuery**：
前端分页请求的通用封装，字段：`pageSize`（分页大小）、`pageNum`（当前页码）、`orderByColumn`（排序字段，支持逗号分隔多字段）、`isAsc`（升/降序，支持各自指定）。`build()` 方法生成 MyBatis-Plus `Page<T>` 对象：自动处理驼峰转下划线、兼容 `ascending/descending` 前端命名、校验排序参数合法性。默认 `pageSize = Integer.MAX_VALUE`（查全部）。入口文件：`core/page/PageQuery.java`。

**DataBaseHelper**：
数据库助手工具类，核心能力：① `getDataBaseType()` 获取当前数据源对应的数据库类型（通过 `DynamicRoutingDataSource.determineDataSource()` + `DatabaseMetaData.getDatabaseProductName()` 识别，结果缓存到 `ConcurrentHashMap`）；② `findInSet(var1, var2)` 生成兼容 4 种数据库的 FIND_IN_SET SQL 片段——MySQL 用 `find_in_set`、Oracle 用 `instr`、PostgreSQL 用 `strpos`、SQL Server 用 `charindex`。入口文件：`helper/DataBaseHelper.java`。

**SqlLogInterceptor**：
完整 SQL 日志拦截器，实现 MyBatis 原生 `Interceptor` 接口（`@Intercepts` 标记拦截 `StatementHandler.query/update/batch/queryCursor`）。核心流程：拦截 SQL 执行 → 解析 `BoundSql` 中的 `?` 占位符 → 根据 `ParameterMapping` 还原实际参数值（处理 Date/LocalDateTime/Enum 等类型） → 拼出可执行完整 SQL → 输出日志（含耗时、Mapper ID、错误信息）。超长 SQL 按 8000 字符分片输出，控制台模式用 `ReentrantLock` 防多线程穿插。通过 `mybatis-plus.sql-log.enabled=true` 开启。入口文件：`interceptor/SqlLogInterceptor.java`。

**PlusDataPermissionInterceptor**：
数据权限 MyBatis 拦截器，继承 `BaseMultiTableInnerInterceptor`，实现 `InnerInterceptor`。SQL 执行前拦截：`beforeQuery` 处理 SELECT（`parserSingle`）、`beforePrepare` 处理 UPDATE/DELETE（`parserMulti`）。先检查 `InterceptorIgnoreHelper` 是否忽略、再检查是否有有效注解，然后委托 `PlusDataPermissionHandler.getSqlSegment` 生成过滤条件，最后通过 JSqlParser 的 `processSelect/processUpdate/processDelete` 将条件注入原始 SQL 的 WHERE 子句。入口文件：`interceptor/PlusDataPermissionInterceptor.java`。

**MybatisPlusConfig**：
模块总配置类，`@MapperScan("${mybatis-plus.mapperPackage}")` 扫描 Mapper 包，`@EnableTransactionManagement` 开启事务。注册 8 个 Bean：`MybatisPlusInterceptor`（内含数据权限 + 分页 + 乐观锁三个内部拦截器）、`DataPermissionPointcutAdvisor`（数据权限切面）、`SqlLogInterceptor`（条件装配）、`MetaObjectHandler`（自动填充）、`IdentifierGenerator`（雪花 ID，用网卡 MAC 防集群重复）、`MybatisExceptionHandler`（异常兜底）、`PostInitTableInfoHandler`（逻辑删除开关）。入口文件：`config/MybatisPlusConfig.java`。

**PlusPostInitTableInfoHandler**：
表信息初始化后处理器，实现 `PostInitTableInfoHandler`。在 MyBatis-Plus 初始化每个 `TableInfo` 后回调，读取配置 `mybatis-plus.enableLogicDelete`（默认 true），若为 false 则通过反射将 `TableInfo.withLogicDelete` 设为 false，实现「全局关闭逻辑删除」的开关。入口文件：`handler/PlusPostInitTableInfoHandler.java`。

**雪花 ID（IdentifierGenerator）**：
MyBatis-Plus 的主键生成策略。`MybatisPlusConfig.idGenerator()` 使用 `DefaultIdentifierGenerator(NetUtil.getLocalhost())`——用网卡 MAC 地址作为 workerId，防止集群环境下各节点的雪花 ID 冲突。`IdGeneratorUtil` 是对其的工具封装，提供 `nextId()/nextLongId()/nextUUID()/nextIdWithPrefix()` 等方法。入口文件：`utils/IdGeneratorUtil.java`。

**MybatisExceptionHandler**：
MyBatis 异常全局处理器，`@RestControllerAdvice`。捕获两类异常：`DuplicateKeyException`（主键/唯一索引冲突，返回 409 冲突提示）和 `MyBatisSystemException`（递归查找根因：若为 `NotLoginException` 返回 401、若为 `CannotFindDataSourceException` 返回数据源未找到提示、否则返回 500）。入口文件：`handler/MybatisExceptionHandler.java`。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

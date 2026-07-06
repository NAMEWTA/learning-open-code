# RuoYi-Vue-Plus 数据权限 术语表

本术语表覆盖 RuoYi-Vue-Plus 数据权限(Data Scope)体系的核心概念。术语仅在学习者**真正理解**后收录。

## Terms

**数据权限 (Data Scope)**：
根据当前登录用户的角色类型，在 SQL 执行前自动往 WHERE 子句中追加过滤条件的机制。不同角色看到同一 SQL 的不同结果集。
_Avoid_: 数据范围、数据隔离（后者通常指多租户 TenantLine）

**DataScopeType**：
六种预定义的数据过滤模式枚举，每种通过一条 SpEL 模板定义其生成的 SQL 片段。code 为 1-6。
_Avoid_: 数据权限类型、scope type

**SpEL 模板**：
使用 Spring 表达式语言写的 SQL 条件模板，例如 `#{#deptName} IN ( #{@sdss.getDeptAndChild(#user.deptId)} )`。模板里的 `#变量` 由 Handler 注入，`@bean` 引用 Spring Bean 方法。

**@DataPermission**：
容器注解，包含一组 `@DataColumn` 和一个可选的 `joinStr`。放在 Mapper 方法上，声明该方法需要数据权限过滤。

**@DataColumn**：
声明 SpEL 模板中占位符变量名（key）与数据库列名（value）的映射关系。例如 `key="deptName"` → `value="dept_id"`。

**ThreadLocal 注解传递**：
运行时流程：AOP 切面在 Mapper 方法调用前将 `@DataPermission` 注解对象存入 ThreadLocal，MyBatis 拦截器在 SQL 执行前从 ThreadLocal 取出。方法执行完清理。这解决了"MyBatis 拦截器无法直接拿到 Java 方法注解"的问题。

**PlusDataPermissionHandler**：
数据权限的大脑类。负责 `getSqlSegment`（入口）和 `buildDataFilter`（核心），从当前用户角色和注解信息生成 SQL WHERE 片段。

**PlusDataPermissionInterceptor**：
MyBatis 的 InnerInterceptor 实现。在 `beforeQuery`（SELECT）和 `beforePrepare`（UPDATE/DELETE）中拦截 SQL，委托 Handler 改写 WHERE。

**joinStr**：
多角色条件之间的拼接符。SELECT 默认 OR（任一角色满足即可），UPDATE/DELETE 默认 AND（必须满足全部角色条件）。可用注解属性显式指定。

**NullSafe**：
SpEL 求值的安全兜底机制。当 `#user.deptId` 或 `@sdss.xxx` 返回 null 时，返回 "-1" 而非 null，避免 SQL 语法错误（如 `IN ()` 或 `= null`）。

**sdss**：
Spring Bean 名称 `"sdss"`，对应 `SysDataScopeServiceImpl`。提供 `getRoleCustom(roleId)`（查 sys_role_dept 返回部门 ID 串）和 `getDeptAndChild(deptId)`（查部门及子部门返回 ID 串）。在 SpEL 模板中通过 `@sdss` 引用。

**DataPermissionHelper**：
静态工具类。提供 `getPermission/setPermission/removePermission`（操作 ThreadLocal 注解）、`getVariable/setVariable`（操作 SpEL 扩展变量）、`getContext()`（Sa-Token Storage 上下文 Map）、`ignore(Runnable/Supplier)`（临时关闭权限）。

**DataPermissionIgnoreContext**：
`ignore()` 的底层实现。内部用 ThreadLocal 栈管理忽略状态，通过反射操作 MyBatis-Plus 的 `IGNORE_STRATEGY_LOCAL` 实现忽略 dataPermission 插件。支持嵌套并恢复进入前状态。

**DataPermissionAccess**：
记录当前 HTTP 请求接口的权限约束（从 `@SaCheckPermission` 和 `@SaCheckRole` 注解提取的权限码集合和角色标识集合）。用于 `scopeRoles` 方法中筛选真正拥有当前接口权限的角色子集。

**scopeRoles**：
根据接口权限约束筛选参与数据权限计算的角色的方法。无约束时使用用户全部角色；有约束时从 `LoginUser.dataScopeRoleMap` 反查出该接口真正关联的角色。

**dataScopeRoleMap**：
`LoginUser` 中的一个 Map：`权限码 → [角色ID列表]`。登录时由 `SysPermissionServiceImpl.getDataScopeRoleMap()` 构建，供接口约束筛选时反查使用。

**AOP 切面 (DataPermissionAdvice + DataPermissionPointcut)**：
Spring AOP 的两个切面组件。Pointcut 通过 `StaticMethodMatcherPointcut` 匹配带 `@DataPermission` 的方法（兼容 MyBatis JDK 动态代理）；Advice 在方法执行前把注解塞进 ThreadLocal、执行后清理。

**deptTree 接口**：
`GET /system/role/deptTree/{roleId}`，一次返回 `{ depts: 部门树, checkedKeys: 已选部门ID }`。用于前端"分配权限"弹窗回填部门树勾选。不同于部门管理用的 `/system/dept/list`。

**父子联动 (deptCheckStrictly)**：
部门树交互选项。开启时（checkStrictly=false）：选子节点自动选父节点，选父节点自动选所有子节点。提交时需收集半选态父节点（Vue 用 `getHalfCheckedKeys`，React 手写 `collectAncestorKeys`）。

**接口约束**：
通过 Controller 上的 `@SaCheckPermission` 注解限制「哪些角色能参与当前接口的数据权限计算」。避免用户多角色时，接口 A 被角色 B（全部数据）越权。

**超管短路**：
`LoginHelper.isSuperAdmin()` 返回 true 时，`getSqlSegment` 直接返回原 where，不添加任何过滤条件。用户 ID 与 `SystemConstants.SUPER_ADMIN_USER_ID` 比对。

**elseSql**：
DataScopeType 的兜底 SQL。当 SpEL 模板的变量没有匹配上注解的 key 时生效。通常设为 `" 1 = 0 "`（查不到任何数据——安全兜底）。

**TemplateParserContext**：
SpEL 解析器使用的模板上下文，定义 `#{` 为表达式前缀、`}` 为后缀。与 Spring 默认的 `#{}` 一致但显式指定了分隔符。

**SpEL (Spring Expression Language)**：
Spring 框架内置的表达式语言。核心组件：`ExpressionParser`（解析字符串为 Expression AST）、`EvaluationContext`（提供变量、函数、类型转换器、BeanResolver）、`PropertyAccessor`（读写 Java 对象属性）。支持字面量、变量引用（`#var`）、Bean 引用（`@bean`）、方法调用、运算符、集合、模板字符串。

**BeanResolver (BeanFactoryResolver)**：
SpEL 中解析 `@beanName` 引用的接口实现。内部持有 `BeanFactory` 引用，`resolve(context, "beanName")` 调用 `beanFactory.getBean("beanName")`，从 Spring 容器获取 Bean 实例返回给 SpEL。在数据权限体系中用于解析 `@sdss`。

**NullSafeStandardEvaluationContext**：
`PlusDataPermissionHandler` 的内部类，继承 `StandardEvaluationContext`，覆写 `lookupVariable()`。当 SpEL 变量不存在或值为 null 时返回默认值 `"-1"` 而非 null，防止 SQL 语法错误。

**NullSafePropertyAccessor**：
`PlusDataPermissionHandler` 的内部类，实现 `PropertyAccessor` 接口，使用装饰器模式包装原始 `ReflectivePropertyAccessor`。当对象属性读取为 null 时返回默认值 `"-1"` 而非 null。与 NullSafeStandardEvaluationContext 形成两层 NullSafe 防护。

**computeIfAbsent**：
Java `Map` 方法。语法：`map.computeIfAbsent(key, mappingFunction)`。若 key 不存在则用 mappingFunction 计算新 value 并放入 Map，始终返回 key 关联的 value（原有或新创建）。在 `getDataScopeRoleMap` 中用于将 role→perms 映射反转为 perm→roleIds 映射。

**LoginHelper.login()**：
Sa-Token 登录封装方法。按 `loginUser.getLoginId()`（格式 `userType:userId`）调用 `StpUtil.login()`，将 userId/username/deptId 等关键信息存入 Sa-Token 的 extra 扩展数据，并将完整 `LoginUser` 对象存入 Token 专属 SaSession（Redis 存储）。

**buildLoginUser**：
`SysLoginService.java:126-147` 方法。从 `SysUserVo` 构建 `LoginUser` 对象。步骤：①同步设置基础身份（userId/deptId/username/nickname/userType/deptName/deptCategory）；②用 `ThreadUtils.virtualInvokeAll` 创建 4 个虚拟线程并行加载菜单权限、角色权限、角色列表+dataScopeRoleMap、岗位列表。

**SaLoginParameter**：
Sa-Token 的登录参数对象。包含设备类型（deviceType）、超时时间（timeout）、活跃超时（activeTimeout）及扩展 Map（extra）。在登录策略中由客户端配置构建，传递给 `LoginHelper.login()`。

## Rules
- 仅在**真正理解**后才收录术语——术语表是压缩知识的记录。
- 定义说清术语**是什么**，不说它做什么或怎么做。
- 术语表自身术语互相引用——一旦入库，后续定义优先使用已入库术语。
- 理解加深时在原文上修订，不留过时条目。

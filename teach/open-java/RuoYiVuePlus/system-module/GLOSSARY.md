# GLOSSARY — ruoyi-system 术语表

## 架构术语

| 术语 | 定义 | 首次出现 |
|------|------|----------|
| **BO (Business Object)** | 业务对象，即前端传给后端的入参 DTO，放在 `domain/bo/` 下 | 第1课 |
| **VO (View Object)** | 视图对象，即后端返回给前端的出参 DTO，放在 `domain/vo/` 下 | 第1课 |
| **BaseEntity** | 所有实体的公共父类，包含 createBy/createTime/updateBy/updateTime 四个审计字段 | 第2课 |
| **@TableLogic** | MyBatis-Plus 逻辑删除注解，标记后 delete 操作自动转为 update del_flag='1' | 第2课 |
| **BaseController** | Controller 基类，提供 toAjax() 等通用方法 | 第8课 |
| **QueryBuilder** | ruoyi 封装的流式查询条件构建器，支持 IfPresent/IfText/IfNotEmpty 等语义化方法 | 第9课 |

## 权限术语

| 术语 | 定义 | 首次出现 |
|------|------|----------|
| **RBAC** | Role-Based Access Control，基于角色的访问控制。User → Role → Menu 的三层模型 | 第3课 |
| **role_key** | 角色权限字符串，如 `super_admin`，用于 @SaCheckRole 校验 | 第3课 |
| **perms** | 菜单权限字符串，如 `system:user:list`，用于 @SaCheckPermission 校验 | 第3课 |
| **menu_type** | 菜单类型：M=目录（侧边栏分组）、C=菜单（实际页面）、F=按钮（操作权限） | 第5课 |
| **@SaCheckPermission** | Sa-Token 权限校验注解，检查用户是否拥有指定权限字符串 | 第8课 |
| **@SaCheckRole** | Sa-Token 角色校验注解，检查用户是否拥有指定角色 | 第8课 |
| **Data Scope** | 数据权限范围，控制用户能看到哪些数据行。6种级别：全部/自定义/本部门/部门及以下/仅本人/部门及以下或本人 | 第4课 |
| **super_admin** | 超级管理员角色标识，拥有所有权限，userId=1，dataScope 检查自动跳过 | 第3课 |

## 数据模型术语

| 术语 | 定义 | 首次出现 |
|------|------|----------|
| **ancestors** | 祖级列表字段，如 `"0,100,200"`，存储从根到父的所有部门ID，用逗号分隔。用于快速查询子孙节点 | 第6课 |
| **FIND_IN_SET** | MySQL 函数，在逗号分隔字符串中查找值，ruoyi 用于通过 ancestors 查询子节点 | 第6课 |
| **is_frame** | 是否外链菜单，Y 表示以 http(s):// 开头的外部链接 | 第5课 |
| **is_cache** | 是否缓存页面，Y 表示页面切换时保持组件状态不销毁 | 第5课 |
| **menuCheckStrictly** | 菜单树父子是否联动选择，true=不联动，false=联动 | 第2课 |
| **deptCheckStrictly** | 部门树父子是否联动选择 | 第2课 |
| **del_flag** | 逻辑删除标记：0=正常，1=已删除 | 第2课 |

## 缓存术语

| 术语 | 定义 | 首次出现 |
|------|------|----------|
| **@Cacheable** | Spring Cache 注解，方法结果自动缓存，下次调用直接返回缓存值 | 第7课 |
| **@CacheEvict** | Spring Cache 注解，方法执行后清除缓存。allEntries=true 清空整个缓存区 | 第7课 |
| **@Caching** | Spring Cache 组合注解，同时声明多个缓存操作 | 第7课 |
| **AopProxy** | Spring AOP 代理对象。同类内部方法调用不走代理，需通过 SpringUtils.getAopProxy(this) 获取代理 | 第7课 |
| **CacheNames** | ruoyi 定义的缓存名称常量类，集中管理所有缓存名 | 第7课 |

## Controller 横切术语

| 术语 | 定义 | 首次出现 |
|------|------|----------|
| **@Log** | 操作日志注解，自动记录操作人、时间、参数、结果到 sys_oper_log 表 | 第8课 |
| **@RepeatSubmit** | 防重复提交注解，基于 Redis 实现，默认 5000ms 内相同请求不允许重复 | 第8课 |
| **@ApiEncrypt** | 接口加密注解，标记后请求体自动解密、响应体自动加密 | 第8课 |
| **DataPermissionHelper.ignore()** | 临时忽略数据权限过滤（如查看个人中心时不应受数据权限限制） | 第8课 |
| **MapstructUtils.convert()** | ruoyi 封装的 MapStruct 转换工具，用于 BO ↔ Entity 互转 | 第9课 |

## 事件术语

| 术语 | 定义 | 首次出现 |
|------|------|----------|
| **OnlineUserCleanEvent** | 在线用户清理事件，角色/权限变更时发布，强制相关用户重新登录 | 第9课 |
| **OssConfigChangeEvent** | OSS 配置变更事件，OSS 配置修改后刷新缓存 | 第1课 |

## 数据权限术语

| 术语 | 定义 | 首次出现 |
|------|------|----------|
| **data_scope=1** | 全部数据权限 — 不注入任何过滤条件 | 第4课 |
| **data_scope=2** | 自定义数据权限 — 从 sys_role_dept 表读取角色关联的部门列表 | 第4课 |
| **data_scope=3** | 本部门数据权限 — 只能看自己部门的数据 | 第4课 |
| **data_scope=4** | 本部门及以下数据权限 — 自己部门 + 所有子部门 | 第4课 |
| **data_scope=5** | 仅本人数据权限 — 只能看自己的数据 | 第4课 |
| **@DataScope** | 数据权限注解，标记在 Mapper 方法上，自动注入数据范围 SQL 条件 | 第10课 |

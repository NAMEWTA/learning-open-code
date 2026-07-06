# Mission: 掌握 RuoYi-Vue-Plus 数据权限(Data Scope)全链路

## Why
你正在使用 RuoYi-Vue-Plus(含 plus-ui-vue / plus-ui-react 双前端 + RuoYi-Vue-Plus 后端)做开发。数据权限是这套框架最核心也最容易"用错却查不出"的能力之一:同一个查询,不同角色看到的数据行不同。学会它之后,你能放心地给任意业务表加"按部门/按本人"的数据隔离,看懂别人写的权限配置,并在权限"不生效"或"越权"时快速定位根因——而不是把它当黑盒。

## Success looks like
- 能在角色管理界面(Vue 或 React)给一个角色配置数据范围(全部/本部门/本部门及以下/仅本人/自定义/部门及以下或本人),并准确预判某用户登录后某个列表能查到哪些数据行。
- 能在自己写的 Mapper 方法上正确添加 `@DataPermission` + `@DataColumn`,让查询/更新/删除自动按当前登录用户的角色过滤,且会处理多表 join 的列别名场景。
- 能不看提示,口述从「Mapper 方法被调用」到「最终 SQL 多出 WHERE 片段」的完整链路:AOP 切面入 ThreadLocal → MyBatis 拦截器 → Handler → DataScopeType 的 SpEL 模板渲染 → 拼回原 SQL。
- 能说清前端「分配权限」弹窗里 dataScope 与 deptIds 两个字段如何产生、如何提交到 `PUT /system/role/permission`,以及后端如何用它们驱动 SQL。
- 能新增一种自定义数据范围规则(改 DataScopeType 模板 + sdss 服务),能用 `DataPermissionHelper.ignore` 临时关闭权限,能按清单排查"权限不生效/越权/SQL 报错"三类典型故障。

## Constraints
- 学习偏好:结合本仓库**真实代码**讲解,每个结论都要能落到 `file_path:line` 的具体证据,不要泛泛的概念课。
- 交互语言:简体中文。
- 三个项目都要覆盖:RuoYi-Vue-Plus(后端,核心)、plus-ui-vue、plus-ui-react。
- 课程需短小、可复习;配套速查参考文档(reference/)便于日后翻阅。

## Out of scope
- 租户隔离(多租户 TenantLine)、菜单/按钮权限(Sa-Token 的 @SaCheckPermission 本身)不作为主线深入——仅在与数据权限交叉处(接口约束 DataPermissionAccess)点到为止。
- 不深入 MyBatis-Plus / JSqlParser 的内部解析器实现细节,只讲到"它把 WHERE 表达式交给 Handler 改写"这一层。
- 不讲数据库建表 SQL 与初始化数据。

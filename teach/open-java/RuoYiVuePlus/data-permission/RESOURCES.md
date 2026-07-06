# RuoYi-Vue-Plus 数据权限 Resources

围绕"读懂并能扩展 RuoYi-Vue-Plus 数据权限"策展。本主题最高信任度的资源是**本仓库源码本身**,辅以官方文档与所依赖框架的一手文档。

## Knowledge

### 一手资源:本仓库源码(最高信任度)

- **后端核心引擎** — `RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-mybatis/src/main/java/org/dromara/common/mybatis/`
  数据权限的全部底层逻辑都在这里。何时取用:理解原理、扩展规则、排错。关键文件:
  - `annotation/DataPermission.java`、`annotation/DataColumn.java` — 注解定义
  - `enums/DataScopeType.java` — 6 种数据范围 + SpEL 模板(整套体系的"配置中心")
  - `handler/PlusDataPermissionHandler.java` — 大脑:生成 WHERE 片段
  - `interceptor/PlusDataPermissionInterceptor.java` — MyBatis 拦截器
  - `aspect/DataPermissionAdvice.java`、`DataPermissionPointcut.java` — AOP 切面(注解入 ThreadLocal)
  - `helper/DataPermissionHelper.java`、`helper/DataPermissionIgnoreContext.java` — 上下文与忽略机制
  - `config/MybatisPlusConfig.java` — 拦截器与切面的装配点

- **后端 SpEL 服务与角色配置** — `RuoYi-Vue-Plus/ruoyi-modules/ruoyi-system/.../service/impl/`
  `SysDataScopeServiceImpl.java`(bean 名 `sdss`,模板里 `@sdss.xxx` 调它)、`SysRoleServiceImpl.java`(维护 sys_role_dept)、`SysPermissionServiceImpl.java`(构建 dataScopeRoleMap)。何时取用:理解"自定义部门/部门及以下"的 id 串怎么来,角色配置怎么落库。

- **后端使用示例** — `SysUserMapper.java`(双列 + join 别名)、`SysDeptMapper.java`、`ruoyi-demo/.../TestDemoMapper.java`(含 `joinStr="AND"` 示例)。何时取用:照着写自己的注解。

- **Vue 前端配置界面** — `plus-ui-vue/src/views/system/role/index.vue` + `src/api/system/role/`。何时取用:理解"分配权限"弹窗如何选 dataScope、勾部门树、提交 deptIds。

- **React 前端配置界面** — `plus-ui-react/src/pages/system/role/components/useRolePermission.tsx` + `RolePermissionModal.tsx` + `src/api/system/role/`。何时取用:对比 React(antd Tree 手写祖先补全)与 Vue(el-tree 内置 API)的差异。

### 官方文档

- [类型: _官方文档_ — RuoYi-Vue-Plus 官方文档(dromara)](https://plus-doc.dromara.org/)
  覆盖整体架构、数据权限使用说明。何时取用:确认官方推荐用法、对照版本差异。注意以仓库实际代码为准,文档可能滞后。

### 依赖框架一手文档(理解底层时取用)

- [类型: _官方文档_ — MyBatis-Plus 数据权限插件](https://baomidou.com/plugins/data-permission/)
  RuoYi 的 `PlusDataPermissionInterceptor` 继承自 MP 的 `BaseMultiTableInnerInterceptor`。何时取用:理解 InnerInterceptor 拦截链、beforeQuery/beforePrepare 时机。
- [类型: _官方文档_ — Spring Framework SpEL(Spring 表达式语言)](https://docs.spring.io/spring-framework/reference/core/expressions.html)
  DataScopeType 的模板 `#{#deptName} IN (...)` 就是 SpEL。何时取用:看懂模板里 `#变量`、`@bean`、`#{}` 的含义。
- [类型: _官方文档_ — Sa-Token](https://sa-token.cc/)
  登录态、`@SaCheckPermission`(与 DataPermissionAccess 接口约束相关)。何时取用:理解 LoginHelper / 当前用户从哪来。

## Wisdom (Communities)

- [类型: _社区_ — RuoYi-Vue-Plus Gitee 仓库 Issues / 讨论](https://gitee.com/dromara/RuoYi-Vue-Plus)
  框架作者与大量实践者在此。何时取用:遇到"权限不生效"等共性问题时搜 issue,或提问。
- [类型: _社区_ — Dromara 开源社区](https://dromara.org/)
  RuoYi-Vue-Plus 所属的开源组织,有 QQ/微信群与多个相关项目。何时取用:深度交流框架设计与最佳实践。

## Gaps
- 暂无明显缺口。本主题以源码为唯一权威,文档与社区为辅,足以支撑全部 Success 项。

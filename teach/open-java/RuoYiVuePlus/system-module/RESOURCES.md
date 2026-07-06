# Resources — ruoyi-system 学习资源策展

## 一手资料（Primary Sources）

### 源码必读
| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `SysPermissionServiceImpl.java` | 权限聚合：角色权限 + 菜单权限 | 理解权限模型入口 |
| `SysMenuServiceImpl.java` | 菜单树构建 + 前端路由生成 | 理解动态路由机制 |
| `SysDataScopeServiceImpl.java` | 数据权限计算：自定义范围 + 部门及子部门 | 理解数据权限 |
| `SysRoleServiceImpl.java` | 角色 CRUD + 权限分配 + 在线用户清理 | 理解角色管理 |
| `SysUserServiceImpl.java` | 用户 CRUD + 角色/岗位关联 + 校验 | 理解用户管理 |
| `SysDeptServiceImpl.java` | 部门树管理 + 祖级路径维护 | 理解树形数据管理 |
| `SysUserController.java` | 用户管理 REST API 全貌 | 理解 Controller 规范 |
| `SysMenuController.java` | 菜单管理 + 动态路由 API | 理解前端路由获取 |
| `SysRoleController.java` | 角色管理 + 用户授权 API | 理解角色分配流程 |

### 数据库设计
| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `SysUserMapper.xml` | 用户分页查询、导出查询、已分配/未分配查询 | 理解复杂 SQL |
| `SysMenuMapper.xml` | 菜单权限查询、按角色查菜单、按用户查菜单树 | 理解菜单 SQL |
| `SysRoleMapper.xml` | 角色分页查询、按用户查角色 | 理解角色 SQL |

### 核心领域对象
| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `SysUser.java` | 用户实体完整字段 | 理解用户数据模型 |
| `SysRole.java` | 角色实体 + dataScope 字段 | 理解角色与数据权限关系 |
| `SysMenu.java` | 菜单实体 + 路由计算方法 | 理解菜单如何转为前端路由 |
| `SysDept.java` | 部门实体 + ancestors 字段 | 理解部门树无限级实现 |

## 依赖框架文档（Secondary Sources）

| 资源 | 覆盖内容 | 链接 |
|------|----------|------|
| MyBatis-Plus 官方文档 | LambdaQueryWrapper、分页、逻辑删除 | https://baomidou.com/ |
| Sa-Token 官方文档 | 权限认证、角色校验、Token 管理 | https://sa-token.cc/ |
| Hutool 工具库 | TreeUtil、StrUtil、CollUtil | https://hutool.cn/ |

## 推荐社区

- **RuoYi-Vue-Plus 官方 Gitee**：https://gitee.com/dromara/RuoYi-Vue-Plus — 提交 Issue、查看文档
- **Dromara 社区**：https://dromara.org/ — 开源社区，RuoYi-Vue-Plus 所属组织

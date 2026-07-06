# Mission — ruoyi-system 模块深度学习

## Why（为什么学）

ruoyi-system 是 RuoYi-Vue-Plus 微服务体系中**最核心的业务模块**，承载了整个后台管理系统的用户、角色、菜单、部门、权限、数据字典、系统配置、操作日志等全部系统管理功能。理解 ruoyi-system 的设计与实现，就等于掌握了 RuoYi-Vue-Plus 的"中枢神经"，能够：

- 理解企业级 RBAC 权限模型的完整落地实现
- 掌握 MyBatis-Plus 在复杂业务场景中的最佳实践
- 学会数据权限（Data Scope）从数据库到 SQL 拦截的完整链路
- 理解前后端分离架构中动态路由的生成机制
- 获得可直接复用的系统管理模块设计和代码

## Success（成功标准）

完成本课程后，学习者应能：

1. **独立画出 ruoyi-system 的完整架构图**，包括分层结构、核心领域模型、服务依赖关系
2. **口述 RBAC 权限模型的完整链路**：从用户登录 → 角色查询 → 菜单权限 → 数据权限 → SQL 拦截
3. **独立实现一个类似的功能模块**，遵循 ruoyi-system 的代码规范和分层模式
4. **理解并修改数据权限范围逻辑**，包括 5 种数据范围的计算和 SQL 注入
5. **理解前端动态路由的生成逻辑**：SysMenu → buildMenus → RouterVo 的完整转换过程
6. **掌握缓存策略**：哪些数据被缓存、缓存 key 设计、缓存失效时机

## Constraints（约束）

- 需要具备 Spring Boot 基础
- 需要了解 MyBatis-Plus 基本用法
- 需要了解 Sa-Token 基本概念
- 本课程聚焦 ruoyi-system 模块本身，不深入讲解 common 模块的内部实现

## Out of scope（非目标）

- 不讲解前端 UI 实现（plus-ui-vue / plus-ui-react）
- 不深入讲解微服务网关、服务注册与发现
- 不讲解 MQTT、WebSocket 等通信模块
- 不深入讲解 OSS、SMS 等外部服务集成的内部实现（仅讲解 system 模块如何使用它们）

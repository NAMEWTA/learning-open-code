# Mission: 全面读懂 RuoYi-Vue-Plus 的 ruoyi-demo 演示示例模块

## Why（为什么学）

ruoyi-demo 是 RuoYi-Vue-Plus 微服务体系中**最特殊的一站式学习入口**。它不是业务模块，而是用 20 个 Controller 将框架所有通用功能——缓存、分布式锁、限流、消息队列、ES 搜索、MCP 协议、数据脱敏、数据库加密、国际化、Excel 导入导出、批量操作、WebSocket 推送、邮件、短信、MQTT、Sa-Token 权限等——做成可运行、可调试、可直接参考的活文档。学完这个模块，你能：

- 一次性掌握 RuoYi-Vue-Plus 框架 90% 的通用能力，无需逐模块翻文档
- 获得所有通用功能的**现成代码模板**，在自己的业务中直接复用
- 理解每个通用功能在真实 Controller-Service-Mapper 调用链中的**正确使用方式**（注解参数、配置开关、注意事项）
- 建立对「框架层面提供了什么、业务模块如何使用」的**全局认知地图**
- 通过对比不同功能的实现模式，内化框架的**设计惯例**（如 `@ConditionalOnProperty` 条件装配、`R<T>` 统一响应、`BaseController` 继承体系）

## Success（成功标准）

完成本课程后，学习者应能：

1. **画出 ruoyi-demo 的完整功能地图**，将 20 个 Controller 按功能类别（缓存与并发控制、数据安全、消息通信、数据导入导出、权限认证、外部集成）归类，并说出每个类的核心能力。
2. **独立为新业务模块接入并正确使用任一通用功能**，例如：为新 Controller 添加 `@RateLimiter` 限流、为新实体配置 `@Sensitive` 脱敏注解、为新表实现 Excel 导入导出、为新方法添加 `@Lock4j` 分布式锁，并说明配置开关的启用条件。
3. **对比说出相似功能的差异与选型原则**，例如：`@Cacheable` vs `RedisUtils` 直接操作缓存、`@Lock4j` 注解 vs `LockTemplate` 编程式锁、Redis Pub/Sub vs PriorityQueue vs MQTT vs WebSocket 四种消息通信方式的适用场景。
4. **口述 MCP（Model Context Protocol）在 ruoyi-demo 中的完整双角色实现**：McpDemoServerTool 如何通过 `@McpTool` / `@McpResource` 暴露工具与资源，McpDemoClientService 如何通过 `McpClientTemplate` 调用远程 MCP Server，以及 `spring.ai.mcp.client.enabled` 开关的作用。
5. **解释 Sa-Token 权限模型在 ruoyi-demo 中的 16 个测试场景**，包括：基础登录/角色/权限、AND/OR 组合模式、通配符匹配、角色+权限混合校验、`orRole` 兜底、`@SaIgnore` 覆盖、临时权限、多端登录指定。

## Constraints（约束）

- 需要已学完或正在学习 `ruoyi-common-*` 系列公共模块，理解各 common 模块提供的基础能力
- 需要具备 Spring Boot 基础（依赖注入、AOP、Filter/Interceptor 概念）
- 需要了解 MyBatis-Plus 基本用法（LambdaQueryWrapper、分页、逻辑删除）
- 需要了解 Sa-Token 基本概念（登录态、角色、权限）
- 本课程聚焦 ruoyi-demo 模块的演示代码，每个功能的**底层实现原理**应回到对应的 ruoyi-common-* 模块学习
- 全部讲解基于仓库真实代码，引用具体文件路径与类名
- 交互语言：简体中文

## Out of scope（非目标）

- 各 common 模块的内部实现细节——demo 只展示「怎么用」，不解释「怎么实现」（这是对应 common 模块课程的目标）
- MCP 协议标准规范本身——仅讲解 ruoyi-demo 中 `@McpTool` / `@McpResource` / `McpClientTemplate` 的使用方式
- SnailJob 任务调度——ruoyi-demo 不包含 job 调度演示，该内容在 ruoyi-job 模块课程中
- 前端 UI 如何调用这些 API——本课程是纯后端 Controller 演示
- 微服务网关、服务注册与发现、配置中心等基础设施
- 各外部服务（Elasticsearch、MQTT Broker、SMS 平台、邮件服务器）的安装与运维

# RuoYi-Vue-Plus 教学索引

RuoYi-Vue-Plus 是一个基于 Spring Boot 3.x、Vue 3、React 18 的企业级全栈快速开发平台，涵盖 RBAC 权限、动态路由、数据权限、工作流、代码生成、分布式任务调度、AI 集成等能力。

## 教学主题

### 后端核心模块

| 主题 | 路径 | 描述 |
|------|------|------|
| 认证与授权系统 | `./authentication/` | 全栈登录认证链路：密码/SMS/社交登录、Sa-Token、JWT、API加密、前后端权限集成 |
| API合约层 | `./api-contracts/` | ruoyi-api 模块的依赖倒置合约设计：SPI接口、LoginUser继承体系、工作流事件解耦 |
| 系统核心业务模块 | `./system-module/` | ruoyi-system 模块全景：RBAC权限模型、菜单路由、部门树、缓存策略、Controller/Service设计规范 |
| 数据权限完整链路 | `./data-permission/` | 从注解到SQL注入的完整数据权限链路：DataScopeType六种类型、SpEL模板、前后端配置 |
| Admin启动模块 | `./admin-module/` | Spring Boot启动入口：五重认证策略工厂、Spring Event登录事件、全局配置管理 |
| Demo演示模块 | `./demo-module/` | 一站式学习入口：20个Controller覆盖CRUD、缓存、并发控制、数据脱敏、消息通信等框架能力 |
| 代码生成器 | `./code-generator/` | AnyLine元数据引擎+FreeMarker模板：从数据库表到全栈代码（Vue/React+Java+SQL）的完整生成管线 |

### 中间件与基础设施

| 主题 | 路径 | 描述 |
|------|------|------|
| 分布式任务调度 | `./task-scheduling/` | SnailJob框架集成：注解/继承两种执行器、广播/静态分片/Map/MapReduce/DAG六种任务模式 |
| 工作流引擎 | `./workflow-engine/` | Warm-Flow引擎集成：从发起审批到任务处理的完整链路、事件驱动解耦、前后端审批组件 |
| 监控中心 | `./monitoring/` | Spring Boot Admin监控：自注册模式、Spring Security安全防护、自定义状态变更通知 |
| AI集成模块 | `./ai-integration/` | 可插拔AI Agent集成：SDK适配器模式、双条件自动装配、SSE流式对话、React/Vue双前端对比 |

### 独立服务器

| 主题 | 路径 | 描述 |
|------|------|------|
| Snail AI Server | `./snail-ai-server/` | Snail AI平台的独立运行时：启动委托模式、gRPC通信、双层安全防护、Docker化部署 |
| Snail Job Server | `./snail-job-server/` | SnailJob调度服务器：跨包启动设计、双端口通信模型、Netty客户端通信、远程日志 |

### 前端架构

| 主题 | 路径 | 描述 |
|------|------|------|
| Vue前端完整架构 | `./vue-frontend/` | Vue 3 + TypeScript + Element Plus + Vite：路由/状态管理/Axios封装/布局系统/三层权限/Composable |
| React前端企业开发 | `./react-frontend/` | React 18 + UmiJS + Zustand + Ant Design：JSX到ProTable CRUD的15步渐进式学习路径 |

### 架构与工程规范

| 主题 | 路径 | 描述 |
|------|------|------|
| 设计模式与工程规范 | `./design-patterns/` | 以RuoYi-Vue-Plus为"设计模式博物馆"：17种GoF模式+18种前端架构模式+工程标准全景 |

### 通用模块体系

| 主题 | 路径 | 描述 |
|------|------|------|
| 通用模块宏概述 | `./common-modules/` | 24个ruoyi-common-*模块的六层架构全景：基础→持久化→安全→数据→集成→新兴技术 |
| common-core | `./common-core/` | 响应体/异常体系、常量枚举设计模式、工具类与校验注解 |
| common-web | `./common-web/` | Filter链/请求包装、全局异常处理与响应增强 |
| common-mybatis | `./common-mybatis/` | BaseMapperPlus/Entity基类、数据权限三层架构、QueryBuilder与多数据源 |
| common-redis | `./common-redis/` | Redisson封装/序列化、限流/防重复提交、二级缓存与工具类 |
| common-satoken | `./common-satoken/` | SaTokenConfig/JWT集成、权限验证与LoginHelper |
| common-security | `./common-security/` | 三道安全防线：URL扫描与客户端认证 |
| common-encrypt | `./common-encrypt/` | 双通道架构：API加密/解密通道、数据库字段加密 |
| common-sensitive | `./common-sensitive/` | 17种脱敏策略：响应增强与JsonValueEnhancer集成 |
| common-excel | `./common-excel/` | 注解驱动四层架构：导出管线、导入与下拉处理 |
| common-json | `./common-json/` | Jackson配置/序列化器、JSON增强三阶段框架、JsonUtils与校验 |
| common-translation | `./common-translation/` | @Translation注解+5种内置翻译器、三阶段管线与自定义翻译器 |
| common-log | `./common-log/` | @Log注解/AOP切面、事件驱动异步消费 |
| common-job | `./common-job/` | SnailJob集成/自动装配、各类型任务示例 |
| common-mail | `./common-mail/` | MailBuilder条件装配、发送管线与实践 |
| common-oss | `./common-oss/` | 工厂模式/客户端抽象、异步上传下载系统、配置热重载与URL构建 |
| common-sms | `./common-sms/` | sms4j集成/PlusSmsDao、发送-验证完整链路 |
| common-social | `./common-social/` | OAuth2.0+26平台支持、JustAuth扩展/自定义Provider |
| common-mqtt | `./common-mqtt/` | MQTT协议/Mica客户端、虚拟线程定制与监听器 |
| common-push | `./common-push/` | SSE/WebSocket双通道、Redis集群分发与前端消费 |
| common-doc | `./common-doc/` | SpringDoc定制/自动配置、JavaDoc解析/权限文档生成 |
| common-elasticsearch | `./common-elasticsearch/` | EasyEs自动装配、环境后处理器与CRUD |
| common-ai | `./common-ai/` | AI自动配置、异常处理与响应隔离 |
| common-mcp | `./common-mcp/` | MCP协议/Spring AI集成、McpClientTemplate工具调用 |
| common-bom | `./common-bom/` | BOM机制与版本仲裁/flatten插件 |

---

> **课程总数：** 240+ 节课，覆盖 RuoYi-Vue-Plus 全栈生态系统的所有核心模块。
> **语言：** 简体中文
> **前置知识：** Java 基础、Spring Boot 基础知识、MyBatis-Plus 基础知识、Vue 3 或 React 基础知识

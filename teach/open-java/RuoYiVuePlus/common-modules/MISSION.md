# 教学使命：RuoYi-Vue-Plus ruoyi-common 全模块深度学习

## Why — 为什么学

`ruoyi-common` 是 RuoYi-Vue-Plus 项目的基础设施层，包含 24 个独立模块，覆盖核心工具、数据持久化、安全认证、消息通信、文件存储、加密脱敏、国际化翻译等企业级开发的全链路基础能力。掌握这些模块意味着：

- 能独立搭建企业级后端项目的基础设施
- 理解 Spring Boot 生态下模块化分层的最佳实践
- 能复用这些模块到任何 Java 项目中
- 能从前端（plus-ui-vue）到后端全链路追踪功能实现

## Success — 成功标准

完成全部课程后，学习者应能：

1. **说出**每个 common 模块的职责、核心类和被哪些模块调用
2. **配置**任一模块在项目中的启用/禁用和参数调优
3. **追踪**一个前端请求如何经过各个 common 模块到达数据库并返回
4. **复现**模块的核心设计模式（如加密器的 SPI 扩展、翻译器的自定义实现）
5. **评估**何时应使用某模块、何时不应使用，以及替代方案

## Constraints — 约束

- 每节课必须在 5-10 分钟内可完成
- 每节课包含至少一个可运行验证的知识点
- 课程覆盖全部 24 个 common 模块
- 对于已有教学内容的模块（redis/sms/push/mqtt/job/ai），本课程做补充和深化

## Out of Scope — 不在此范围

- ruoyi-admin（管理后台应用层）的详细讲解
- ruoyi-modules（业务模块：system/gen/job 等）的业务逻辑详解
- ruoyi-api（远程调用接口）的详细讲解（已有独立课程）
- Spring Boot / MyBatis / Vue 基础语法教学
- 各模块的原始源码级逐行讲解（聚焦架构和使用层面）

## 课程体系

### 第1层：基石模块（必须先学）
| 编号 | 模块 | Java文件 | 核心主题 |
|------|------|----------|----------|
| 01 | ruoyi-common-core | 65 | 异常体系、基类、工具类、注解、枚举、全局配置 |
| 02 | ruoyi-common-web | 17 | 全局过滤器、拦截器、CORS、响应包装、参数校验 |
| 03 | ruoyi-common-mybatis | 34 | 数据权限、多数据源、乐观锁、自动填充、分页 |

### 第2层：安全与认证
| 编号 | 模块 | Java文件 | 核心主题 |
|------|------|----------|----------|
| 04 | ruoyi-common-security | 3 | Sa-Token 拦截器配置、客户端校验、IP白名单、Actuator Basic Auth |
| 05 | ruoyi-common-satoken | 5 | Sa-Token 集成、多账号认证、权限路由 |
| 06 | ruoyi-common-encrypt | 25 | API 加解密、数据库字段加解密、多算法支持 |
| 07 | ruoyi-common-sensitive | 5 | 数据脱敏注解、JSON 序列化脱敏、自定义策略 |

### 第3层：数据处理
| 编号 | 模块 | Java文件 | 核心主题 |
|------|------|----------|----------|
| 08 | ruoyi-common-excel | 21 | 动态 Excel 导入导出、模板渲染、大数据分批 |
| 09 | ruoyi-common-json | 13 | Jackson 序列化配置、类型引用、JSON 工具链 |
| 10 | ruoyi-common-translation | 11 | 翻译器框架、字典翻译、枚举翻译、自定义翻译器 |
| 11 | ruoyi-common-log | 7 | 操作日志注解、日志切面、登录日志、异步记录 |

### 第4层：通信与集成
| 编号 | 模块 | Java文件 | 核心主题 |
|------|------|----------|----------|
| 12 | ruoyi-common-redis | 18 | Redis 多客户端、发布订阅、分布式锁、限流 |
| 13 | ruoyi-common-mqtt | 3 | MQTT 消息协议、Topic 订阅、IoT 通信 |
| 14 | ruoyi-common-mail | 3 | 邮件发送、模板邮件、附件发送 |
| 15 | ruoyi-common-sms | 3 | 短信发送、多厂商适配、验证码场景 |

### 第5层：文件与搜索
| 编号 | 模块 | Java文件 | 核心主题 |
|------|------|----------|----------|
| 16 | ruoyi-common-oss | 18 | 对象存储抽象、S3/MinIO/本地/七牛等多适配器 |
| 17 | ruoyi-common-elasticsearch | 2 | ES 集成、索引操作、搜索查询 |
| 18 | ruoyi-common-doc | 8 | Knife4j/SpringDoc API 文档生成 |

### 第6层：新兴能力
| 编号 | 模块 | Java文件 | 核心主题 |
|------|------|----------|----------|
| 19 | ruoyi-common-ai | 2 | AI 模型集成、多厂商适配、流式对话 |
| 20 | ruoyi-common-mcp | 4 | MCP 协议集成、工具注册、SSE/STDIO 传输 |
| 21 | ruoyi-common-push | 17 | 消息推送、WebSocket、多平台推送 |

### 第7层：社交与调度
| 编号 | 模块 | Java文件 | 核心主题 |
|------|------|----------|----------|
| 22 | ruoyi-common-social | 13 | 第三方登录、OAuth2.0、JustAuth 集成 |
| 23 | ruoyi-common-job | 1 | 定时任务抽象、SnailJob 集成 |
| 24 | ruoyi-common-bom | 0 | 依赖版本管理、BOM 设计模式 |

## 学习方法

1. **按层次顺序学习**：每层内部模块有依赖关系，必须按编号顺序
2. **结合前端理解**：每节课都会标注对应的前端代码路径
3. **动手验证**：每节课结尾有验证点，建议在本地启动项目验证
4. **追溯调用链**：使用 IDE 的 Find Usages 功能追踪实际调用

## 前端对照 (plus-ui-vue)

前端项目使用 Vue 3 + TypeScript + Element Plus，主要与 common 模块的交互点：

- `utils/request.ts` → common-web（请求拦截、响应处理）
- `store/modules/user.ts` → common-satoken（登录态管理）
- `directive/permission.ts` → common-security（前端权限指令）
- `utils/auth.ts` → common-satoken（Token 存取）
- `components/` → common-encrypt/sensitive（前端加解密、脱敏展示）
- `api/` → 各业务 API 通过 common-web 过滤器链路

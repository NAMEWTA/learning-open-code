# ruoyi-demo 演示示例模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-modules/ruoyi-demo/`）。以下外部资源用于补充各子功能的框架文档与官方说明。

## 源码索引（Primary Sources — 仓库内）

| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `controller/TestDemoController.java` | 单表 CRUD 完整模板：分页查询、Excel 导入导出、`@RepeatSubmit` 防重、`@Log` 操作日志、`@SaCheckPermission` 权限校验、`ValidatorUtils` 校验工具、参数校验分组（Add/Edit/Query） | 学习标准 CRUD 开发规范时 |
| `controller/TestTreeController.java` | 树表 CRUD：树形数据查询、导出、`BaseController` 继承体系 | 学习树形数据管理时 |
| `controller/TestBatchController.java` | 批量操作：`insertBatch` 高性能批量插入、`insertOrUpdateBatch`、批量删除、`rewriteBatchedStatements` 配置说明 | 学习批量数据处理优化时 |
| `controller/RedisCacheController.java` | Spring Cache 三件套：`@Cacheable`（查询缓存）、`@CachePut`（更新缓存）、`@CacheEvict`（删除缓存），cacheNames 命名规则（`demo:cache#60s#10m#20#1` 格式），`RedisUtils` 手动缓存操作与过期设置 | 学习声明式缓存与手动缓存时 |
| `controller/RedisLockController.java` | 分布式锁两种方式：`@Lock4j` 注解声明式、`LockTemplate` 编程式（超时时间、获取锁超时、`RedissonLockExecutor`、释放锁） | 学习分布式锁的注解与编程两种用法时 |
| `controller/RedisRateLimiterController.java` | 分布式限流三种模式：全局限流、IP 限流、集群实例限流，`key` 表达式支持 SpEL 获取参数 | 学习接口限流保护时 |
| `controller/RedisPubSubController.java` | Redis 发布订阅：`RedisUtils.publish()` 发布、`RedisUtils.subscribe()` 订阅 | 学习轻量级消息通知时 |
| `controller/queue/PriorityQueueController.java` + `PriorityDemo.java` | 优先队列：`QueueUtils.addPriorityQueueObject`、`getPriorityQueueObject`、`removePriorityQueueObject`、`destroyPriorityQueue`，集群消费一次、需事务补偿 | 学习 Redis 优先队列（轻量级 MQ 替代）时 |
| `controller/TestEncryptController.java` + `domain/TestDemoEncrypt.java` + `mapper/TestDemoEncryptMapper.java` | 数据库字段加解密：`mybatis-encryptor.enable` 配置开关、`TestDemoEncrypt` 实体、加密写入 + 解密读取的完整对比 | 学习数据库字段透明加解密时 |
| `controller/TestSensitiveController.java` | 数据脱敏五种策略：`@Sensitive` + `SensitiveStrategy.ID_CARD/PHONE/ADDRESS/EMAIL/BANK_CARD`，`roleKey` 和 `perms` 条件脱敏（基于角色/权限判断是否脱敏），管理员默认不过滤 | 学习数据脱敏的注解配置与条件策略时 |
| `controller/TestI18nController.java` | 国际化三种方式：`MessageUtils.message(code)` 代码获取、`@NotBlank(message="{not.null}")` Validator 校验国际化、Bean 校验国际化、`messages.properties` key 体系 | 学习国际化消息与校验错误信息多语言时 |
| `controller/TestExcelController.java` + `service/IExportExcelService.java` + `service/impl/ExportExcelServiceImpl.java` | Excel 五种导出模式：单列表多数据模板填充、多列表多数据模板填充、下拉框导出、自定义导出、多 Sheet 导出；导入带监听器校验 | 学习 Excel 复杂导入导出场景时 |
| `controller/EsCrudController.java` + `domain/Document.java` + `esmapper/DocumentMapper.java` | Elasticsearch CRUD：`LambdaEsQueryWrapper` 精确查询与模糊搜索、`DocumentMapper` 继承 `BaseEsMapper`、`@ConditionalOnProperty(value="easy-es.enable")` 条件装配 | 学习 Easy-ES 操作 Elasticsearch 时 |
| `controller/MqttController.java` | MQTT 五种场景：发布消息、QoS0/QoS1 订阅、`${productKey}` 占位符主题、JSON 反序列化自定义（`MqttJsonDeserializer`）、方法参数映射规则（topic/byte[]/MqttPublishMessage/自定义类型） | 学习 mica-mqtt 客户端注解式开发时 |
| `mcp/McpDemoServerTool.java` + `mcp/McpDemoClientService.java` + `controller/McpDemoController.java` | MCP 完整双角色：Server 端 `@McpTool` / `@McpResource` 暴露工具与资源，Client 端 `McpClientTemplate` 调用远程工具/读取资源，`McpDemoController` 手动触发入口，`spring.ai.mcp.client.enabled` 开关 | 学习 MCP Server/Client 在 Spring AI 中的集成时 |
| `controller/WebSocketController.java` | WebSocket 推送：`MessageService` 发送点对点消息、`publishAll` 广播，`PushPayloadDTO` 消息体构造，`PushTypeEnum` / `PushSourceEnum` | 学习 WebSocket 实时消息推送时 |
| `controller/SaTokenTestController.java` | Sa-Token 权限 16 个场景：仅登录、单一角色/权限、SaIgnore、多角色/权限 AND/OR、通配符、角色+权限混合、orRole 兜底、SaIgnore 覆盖、临时权限、多端登录指定 | 学习 Sa-Token 权限体系完整用法时 |
| `controller/SmsController.java` | 短信发送：`SmsFactory.getSmsBlend("config1")` 多配置源、阿里云/腾讯云发送、黑名单管理 | 学习 SMS4J 多平台短信集成时 |
| `controller/MailSendController.java` | 邮件发送：`MailBuilder` 链式 API、简单邮件、单附件、多附件、附件路径安全提醒 | 学习邮件发送集成时 |
| `controller/Swagger3DemoController.java` | Swagger3 文件上传示例：`@RequestPart` 注解、`consumes = MULTIPART_FORM_DATA_VALUE` | 学习 Swagger 文档文件上传 API 写法时 |

## 依赖框架与库（Secondary Sources — 外部文档）

| 资源 | 覆盖内容 | 链接 |
|------|----------|------|
| Lock4j 官方文档 | `@Lock4j` 注解参数、`LockTemplate` 编程式 API、`RedissonLockExecutor` 配置、锁过期与获取超时、自定义锁执行器 | https://baomidou.com/reference/lock4j/ |
| Easy-ES 官方文档 | `LambdaEsQueryWrapper` API、`BaseEsMapper` CRUD 方法、索引自动创建、高亮查询、聚合、`@ConditionalOnProperty` 开关控制 | https://www.easy-es.cn/ |
| mica-mqtt 官方文档 | `@MqttClientSubscribe` 注解详解、QoS 等级、`MqttClientTemplate`、自定义序列化、变量替换 `${}`、Spring Boot 集成 | https://mica-mqtt.dreamlu.net/ |
| SMS4J 官方文档 | `SmsFactory` 多配置源、阿里云/腾讯云/华为云等平台配置、黑名单、短信拦截、结果回调 | https://sms4j.com/ |
| Spring AI MCP 官方文档 | `@McpTool` / `@McpResource` 注解、`McpSyncClient` API、MCP Server/Client 配置、工具注册与发现 | https://docs.spring.io/spring-ai/reference/api/mcp.html |
| Sa-Token 官方文档 | `@SaCheckLogin`/`@SaCheckRole`/`@SaCheckPermission`/`@SaIgnore` 注解详解、AND/OR 模式、通配符匹配、`orRole` 参数、临时权限、多账号体系 | https://sa-token.cc/ |
| Spring Cache 官方文档 | `@Cacheable`/`@CachePut`/`@CacheEvict` 注解详解、SpEL key 表达式、`condition` 条件缓存、`CacheManager` 配置、TTL 设置 | https://docs.spring.io/spring-framework/reference/integration/cache.html |
| RuoYi-Vue-Plus 官方文档 | 框架整体设计说明、各 common 模块功能概述、配置文件参考、常见问题 | https://plus-doc.dromara.org/ |
| Redisson 官方文档 | 分布式锁底层实现（看门狗机制、可重入锁、公平锁）、Redis 数据结构操作、集群模式配置 | https://redisson.org/docs/ |
| MyBatis-Plus 官方文档 | `BaseMapper` CRUD、`LambdaQueryWrapper`、分页插件、逻辑删除、`rewriteBatchedStatements` 批处理优化 | https://baomidou.com/ |

## 社区

- **RuoYi-Vue-Plus 官方 Gitee**：https://gitee.com/dromara/RuoYi-Vue-Plus — 提交 Issue、查看 Wiki 文档、Release 说明
- **Dromara 开源社区**：https://dromara.org/ — RuoYi-Vue-Plus 所属组织，包含 Lock4j、Easy-ES、mica-mqtt 等子项目
- **Dromara 社区微信群 / QQ 群**：通过 Gitee 主页获取加群方式，与维护者和用户交流实际问题

## 资源缺口

- ruoyi-demo 模块的 20 个 Controller 本身代码注释详尽，大部分功能均可通过代码 + 上述官方文档覆盖所有 Success 项。
- **MCP（Model Context Protocol）的 Spring AI 集成文档**目前仍处于较新阶段，部分细节可能需要查看 Spring AI 源码或 GitHub Issues 补充。
- `QueueUtils` 优先队列的内部实现（Redis Sorted Set）建议配合 `ruoyi-common-redis` 模块课程交叉学习。

# 演示示例模块 - 术语表

## 框架核心概念

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| ruoyi-demo (演示示例模块) | RuoYi-Vue-Plus 微服务体系中用 20 个 Controller 将框架所有通用功能做成可运行、可调试的活文档模块 | 学习框架通用能力的入口，获取各功能的现成代码模板 |
| BaseController (基础控制器) | 框架提供的控制器基类，封装了 startPage()、toAjax()、success() 等通用响应方法 | 所有业务 Controller 继承此类，复用分页和统一响应能力 |
| R&lt;T&gt; (统一响应包装) | 框架统一的 JSON 响应格式，包含 code、msg、data 三个字段 | 所有 Controller 方法的返回值，保证前端解析一致性 |
| BaseEntity (基础实体) | 框架提供的实体基类，统一包含 createTime、updateTime、createBy、updateBy 等审计字段 | 所有数据库实体继承此类，无需重复定义审计字段 |
| @ConditionalOnProperty (条件装配) | Spring Boot 条件注解，根据配置文件中指定属性的值决定是否加载某个 Bean | Easy-ES、mybatis-encryptor 等功能通过此注解实现配置开关控制 |

## MyBatis-Plus 相关

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| MyBatis-Plus | MyBatis 的增强工具包，提供 BaseMapper、分页插件、逻辑删除、乐观锁等开箱即用能力 | 整个框架的 ORM 层基础 |
| @TableName (表名映射) | 将 Java 实体类映射到数据库表名的注解 | 实体类声明时指定对应的数据库表，如 `@TableName("test_demo")` |
| @TableId (主键映射) | 标记实体类中主键字段的注解 | 标识数据库主键列，支持多种主键生成策略 |
| @TableLogic (逻辑删除) | MyBatis-Plus 逻辑删除注解，删除操作只更新标记字段而非物理删除数据 | 业务删除场景，保留数据可追溯，配合 delFlag 字段使用 |
| @Version (乐观锁) | MyBatis-Plus 乐观锁注解，更新时自动检查版本号一致性 | 并发更新场景，防止多人同时修改同一条数据导致覆盖 |
| @OrderBy (默认排序) | MyBatis-Plus 排序注解，指定查询时的默认排序字段和方向 | 实体默认排序，省去每次查询都写 ORDER BY |
| LambdaQueryWrapper | MyBatis-Plus 提供的 Lambda 表达式查询构造器，避免硬编码字段名 | 构建类型安全的查询条件，如 `.eq(Entity::getField, value)` |
| PageQuery / PageResult | 框架对 MyBatis-Plus 分页的封装，PageQuery 接收分页参数，PageResult 包装分页结果 | 所有分页查询接口统一使用，自动读取 pageNum 和 pageSize |
| rewriteBatchedStatements | JDBC 连接参数，将多条 INSERT 合并为一条批量 SQL | 配合 insertBatch 使用，在 JDBC URL 中添加此参数可提升 10-50 倍批量写入性能 |
| insertBatch (批量插入) | MyBatis-Plus 批量插入方法，一次提交多条记录 | 大批量数据导入场景，如 1000 条数据秒级写入 |
| insertOrUpdateBatch (批量新增或更新) | MyBatis-Plus 批量新增或更新方法，有 ID 则更新，无 ID 则插入 | 数据同步/导入场景，不确定数据是否存在时使用 |

## Sa-Token 权限相关

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Sa-Token | 轻量级 Java 权限认证框架，提供登录认证、角色权限、Token 会话等功能 | 整个框架的权限认证基础设施 |
| @SaCheckPermission (权限校验) | Sa-Token 注解，声明方法需要的权限字符串，当前用户必须拥有该权限才能访问 | 每个 Controller 方法上声明所需权限，如 `@SaCheckPermission("demo:demo:list")` |
| @SaCheckRole (角色校验) | Sa-Token 注解，声明方法需要的角色标识 | 需要特定角色才能访问的接口 |
| @SaIgnore (忽略鉴权) | Sa-Token 注解，标记方法跳过权限校验 | 公开接口或特殊场景下绕过鉴权 |
| 权限字符串命名惯例 | `模块:实体:操作` 格式，如 `demo:demo:list`、`demo:demo:add` | 统一项目中所有权限标识的命名规范 |

## Redis 缓存与并发控制

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| @Cacheable (查询缓存) | Spring Cache 注解，方法执行前先查缓存，命中则直接返回缓存值，不执行方法体 | 查询接口加速，如分页列表、单条详情 |
| @CachePut (更新缓存) | Spring Cache 注解，方法始终执行，并将返回值写入缓存 | 新增/修改数据后同步刷新缓存 |
| @CacheEvict (删除缓存) | Spring Cache 注解，方法执行后清除指定缓存 | 删除数据后同步清除对应缓存 |
| cacheNames (缓存名称) | RuoYi-Vue-Plus 增强格式 `名称#TTL#maxSize#maxIdleTime#淘汰策略`，用 # 分隔 | 声明缓存时指定名称和过期策略，如 `"demo:cache#60s#10m#20#1"` |
| CacheNames (缓存常量) | 预定义的缓存名称常量类，包含 DEMO_CACHE 等常量 | 避免硬编码缓存名称字符串 |
| RedisUtils (Redis 工具类) | 框架封装的 Redis 操作工具，支持 String、Hash、List、Set、Sorted Set 等所有数据结构 | 手动操作缓存的场景，如 `RedisUtils.setCacheObject(key, value)` |
| @Lock4j (分布式锁注解) | Lock4j 框架提供的声明式分布式锁注解，方法执行期间同一 key 只能一个线程进入 | 防止并发操作同一数据，如扣减库存、修改同一订单 |
| LockTemplate (编程式锁) | Lock4j 编程式锁模板，提供 lock()/releaseLock() 手动控制锁生命周期 | 需要自定义超时、降级、重试等复杂逻辑的场景 |
| RedissonLockExecutor (Redisson 锁执行器) | Lock4j 基于 Redisson 的分布式锁执行器，底层使用看门狗机制自动续期 | 指定分布式锁的底层实现方案 |
| Redisson | Redis 的 Java 客户端，提供分布式锁、分布式集合等高级功能，底层看门狗机制自动续期 | 分布式锁的底层实现 |
| @RateLimiter (限流注解) | 框架提供的分布式限流注解，限制单位时间内的请求次数 | 防止接口被恶意刷请求或流量过载 |
| LimitType (限流类型) | 限流计数维度枚举：DEFAULT（全局）、IP（按请求 IP）、CLUSTER（按服务实例） | 根据场景选择限流粒度 |
| @RepeatSubmit (防重提交) | 防重复提交注解，同一用户短时间内不能提交相同请求 | 防止用户快速双击按钮导致重复提交表单 |
| SpEL (Spring 表达式语言) | Spring Expression Language，在注解中通过 `#变量` 或 `#{表达式}` 动态获取方法参数值 | @RateLimiter 的 key 属性支持 SpEL 获取参数做差异化限流 |

## 数据安全

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| @Sensitive (数据脱敏) | 数据脱敏注解，在 Jackson 序列化返回 JSON 时自动对敏感字段进行部分遮盖 | 手机号、身份证、银行卡号等敏感信息返回前端时的保护 |
| SensitiveStrategy (脱敏策略) | 脱敏策略枚举，包含 ID_CARD、PHONE、ADDRESS、EMAIL、BANK_CARD 五种内置策略 | 为不同敏感字段选择合适的脱敏规则 |
| roleKey (角色条件脱敏) | @Sensitive 的参数，拥有指定角色时不脱敏 | 管理员角色查看明文，普通用户看脱敏数据 |
| perms (权限条件脱敏) | @Sensitive 的参数，拥有指定权限时不脱敏 | 有特定权限的用户查看明文，其他用户看脱敏数据 |
| Jackson 序列化 | Java 对象转 JSON 字符串的过程，脱敏在此阶段通过自定义序列化器实现 | 数据脱敏的生效时机，返回 JSON 给前端时触发 |
| @EncryptField (字段加密) | 数据库字段加解密注解，在 MyBatis 读写时对字段透明加解密 | 敏感数据存储到数据库时自动加密，读取时自动解密 |
| AlgorithmType (加密算法类型) | 加密算法枚举：AES（对称）、RSA（非对称）、SM2（国密非对称）、SM4（国密对称） | 根据安全级别和合规要求选择合适的加密算法 |
| AES (高级加密标准) | 对称加密算法，加密和解密使用同一密码，性能好 | 通用字段加密场景 |
| RSA (非对称加密算法) | 非对称加密算法，公钥加密、私钥解密 | 高安全场景，加密和解密使用不同密钥 |
| SM2 / SM4 (国密算法) | 中国国家密码标准算法，SM2 为非对称、SM4 为对称 | 信创/国产化合规要求的场景 |
| mybatis-encryptor.enable (加密开关) | 配置文件中的布尔值，控制数据库字段加解密功能是否启用 | 需设置为 true 后 @EncryptField 才生效 |
| MyBatis 拦截器 | MyBatis 的插件机制，可在 SQL 执行前后插入自定义逻辑 | @EncryptField 通过拦截器在读写数据库时进行加解密，对业务代码透明 |

## 国际化

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| i18n (国际化) | Internationalization 的缩写，软件支持多语言的能力 | 校验错误信息、业务提示根据用户语言环境自动切换 |
| MessageUtils (消息工具) | 框架提供的国际化消息获取工具，`MessageUtils.message(code)` 根据当前语言返回对应文本 | 代码中主动获取国际化文本，如业务提示、邮件内容 |
| messages.properties (消息资源文件) | 国际化消息的 key-value 配置文件，默认中文 | 定义所有可国际化的文本 key，扩展语言只需添加对应语言文件 |
| Accept-Language (请求头) | HTTP 请求头，标识用户偏好的语言 | 框架根据此请求头自动切换国际化资源文件 |
| ValidatorUtils (校验工具) | 框架封装的 Bean 校验工具，支持分组校验和手动触发校验 | 在 Service 层或非 Controller 环境手动触发参数校验 |
| @Validated (参数校验) | Spring 参数校验注解，开启方法级参数校验，支持分组 | Controller 方法参数或类级别声明校验规则 |
| QueryGroup / AddGroup / EditGroup (校验分组) | 参数校验分组接口，区分查询、新增、编辑三种场景的校验规则 | 同一个 BO 在不同操作下应用不同的校验规则，互不干扰 |

## 消息通信

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Redis Pub/Sub (发布订阅) | Redis 内置的发布订阅机制，发布者发送消息到频道，订阅者接收 | 集群内缓存失效通知、配置刷新广播等允许丢失的轻量级通知 |
| WebSocket (全双工通信协议) | 基于 TCP 的全双工通信协议，服务端可随时向客户端推送消息 | 站内信、实时通知、在线用户踢出等需即时送达的场景 |
| MessageService (消息推送服务) | 框架封装的 WebSocket 消息推送服务，支持点对点和全服广播 | 后端主动向前端推送消息的统一入口 |
| PushPayloadDTO (推送消息体) | WebSocket 推送消息的数据传输对象，包含消息类型、来源、内容和扩展参数 | 构造推送给前端的消息，统一消息格式 |
| PushTypeEnum (推送类型枚举) | 消息类型枚举：MESSAGE / NOTICE / WARNING 等 | 区分不同类别的推送消息 |
| PushSourceEnum (推送来源枚举) | 消息来源枚举：BACKEND（后端推送）/ FRONTEND（前端触发） | 标识消息的发起方 |
| publishAll (全服广播) | MessageService 方法，向所有在线用户广播消息 | 系统公告、全服通知等需要所有在线用户接收的场景 |
| publishMessage (点对点推送) | MessageService 方法，向指定用户（一个或多个）推送消息 | 个人消息通知、订单状态更新等定向推送场景 |
| MQTT (消息队列遥测传输) | ISO 标准的轻量级物联网消息协议，支持 QoS 分级、主题通配符和离线消息 | IoT 设备通信、车联网、智能家居等需可靠送达和设备管理的场景 |
| mica-mqtt | 开源的 Java MQTT 客户端框架，提供注解式 MQTT 订阅和 Spring Boot 自动配置 | ruoyi-demo 中 MQTT 功能的底层实现 |
| @MqttClientSubscribe (MQTT 订阅注解) | mica-mqtt 注解，声明一个方法为 MQTT 消息处理器，支持 QoS 和通配符 | 订阅 MQTT 主题并处理接收到的消息 |
| MqttQoS (MQTT 服务质量) | MQTT 服务质量等级：QoS0（最多一次）、QoS1（至少一次）、QoS2（精确一次） | 根据消息可靠性要求选择合适的 QoS 级别 |
| MqttClientTemplate (MQTT 客户端模板) | mica-mqtt 提供的 MQTT 客户端操作模板 | 发布 MQTT 消息到指定主题 |
| MqttJsonDeserializer (MQTT JSON 反序列化器) | mica-mqtt 自定义 JSON 反序列化器，将 MQTT payload 自动转为 Java 对象 | 接收 JSON 格式的 MQTT 消息时自动反序列化 |
| MqttPublishMessage (MQTT 发布消息) | mica-mqtt 的原始消息对象，包含 MQTT5 协议的所有属性 | 需要访问 MQTT5 高级特性（如属性、原因码）时的参数类型 |
| 优先级队列 (Priority Queue) | 基于 Redis Sorted Set 实现的轻量级消息队列，按 orderNum 排序出队 | 订单按优先级处理、延迟任务调度等不需要重量级 MQ 的场景 |
| QueueUtils (队列工具类) | 框架封装的优先级队列操作工具，提供 add/get/remove/destroy 方法 | 操作 Redis Sorted Set 实现的优先级队列 |
| Redis Sorted Set (有序集合) | Redis 数据结构，每个元素关联一个分数，按分数排序 | 优先级队列的底层存储结构 |
| Ack (消息确认机制) | Acknowledgment，消息消费后向 Broker 确认的机制，确保消息不丢失 | MQTT QoS1/2 和 RabbitMQ/RocketMQ 中有此机制；Redis Pub/Sub 和优先级队列没有 |

## Excel 操作

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| ExcelBuilder (Excel 构建器) | 框架封装的 Excel 读写工具，链式 API 一行代码完成导入导出 | Controller 中导入导出 Excel 的统一入口 |
| ExcelResult (导入结果) | Excel 导入的结果对象，包含解析后的数据列表和导入分析报告 | 获取导入成功/失败的行数和错误详情 |
| MapstructUtils (对象转换工具) | 框架封装的 MapStruct 对象转换工具 | Excel 导入时将 ImportVo 转为 Entity，导出时将 Entity 转为 ExportVo |
| MULTIPART_FORM_DATA (多部件表单数据) | HTTP Content-Type 的一种，用于文件上传 | Excel 导入接口的 consumes 声明，确保 Swagger3 正确生成文档 |

## MCP 协议

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| MCP (Model Context Protocol) | 模型上下文协议，用于 AI 模型与外部工具/资源之间的标准化通信 | ruoyi-demo 中演示 Spring AI 集成 MCP Server 和 Client 的方式 |
| @McpTool (MCP 工具注解) | Spring AI 注解，将一个方法暴露为 MCP Server 的工具端点 | MCP Server 端暴露可被 AI 调用的工具函数 |
| @McpResource (MCP 资源注解) | Spring AI 注解，将一个方法暴露为 MCP Server 的资源读取端点 | MCP Server 端暴露可被 AI 读取的数据资源 |
| McpClientTemplate (MCP 客户端模板) | Spring AI 提供的 MCP 客户端调用模板 | MCP Client 端通过此模板调用远程 MCP Server 的工具和资源 |
| spring.ai.mcp.client.enabled (MCP 客户端开关) | 配置文件中的布尔值，控制 MCP Client 功能是否启用 | 通过此开关控制 MCP 客户端的加载 |

## 外部集成

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Easy-ES | MyBatis-Plus 风格的 Elasticsearch ORM 框架，提供 LambdaEsQueryWrapper 等 API | ruoyi-demo 中 EsCrudController 操作 Elasticsearch 的底层框架 |
| BaseEsMapper (ES 基础映射器) | Easy-ES 提供的 Elasticsearch 基础 CRUD 映射器 | DocumentMapper 继承此类获得 ES 的增删改查能力 |
| Elasticsearch (ES) | 分布式搜索和分析引擎 | 全文搜索、日志分析等需要高性能搜索的场景 |
| SMS4J (短信聚合框架) | Java 短信发送聚合框架，统一阿里云、腾讯云等多平台 API | SmsController 演示多平台短信发送 |
| SmsFactory (短信工厂) | SMS4J 的短信实例工厂，`getSmsBlend("config1")` 获取指定配置的短信发送实例 | 多短信渠道管理和切换 |
| MailBuilder (邮件构建器) | 框架封装的邮件发送链式 API | 发送简单邮件、带附件邮件等场景 |
| SnailJob (任务调度框架) | 分布式任务调度框架 | ruoyi-job 模块中使用，ruoyi-demo 不包含（非本模块范围） |

## Lombok

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| @RequiredArgsConstructor (构造器注入) | Lombok 注解，自动生成包含所有 final 字段的构造函数，替代 @Autowired 字段注入 | Controller 和 Service 中声明 final 字段即可实现依赖注入 |
| @Data (数据注解) | Lombok 注解，自动生成 getter/setter/toString/equals/hashCode | 实体类和 DTO 上简化样板代码 |

## 架构设计概念

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| AOP (面向切面编程) | Aspect-Oriented Programming，在不修改原代码的情况下横向插入逻辑 | @Cacheable、@Lock4j、@Log 等注解通过 AOP 实现横切关注点 |
| 声明式编程 (Declarative) | 通过注解声明意图，框架自动处理实现细节的编程风格 | @Lock4j、@Cacheable、@RateLimiter 等一个注解搞定复杂功能 |
| 编程式 (Programmatic) | 手动调用 API 控制流程的编程风格 | LockTemplate、RedisUtils 等需要精细控制的场景 |
| 逻辑删除 (Logical Delete) | 标记删除而非物理删除的软删除策略 | 所有业务表的删除操作，保留数据可追溯 |
| 乐观锁 (Optimistic Lock) | 通过版本号实现并发控制，更新时检查版本号是否一致 | 多人同时编辑同一数据时防止覆盖 |
| 看门狗机制 (Watchdog) | Redisson 分布式锁的自动续期机制，防止业务未执行完锁已过期 | @Lock4j 底层 RedissonLockExecutor 实现长业务场景的锁续期 |

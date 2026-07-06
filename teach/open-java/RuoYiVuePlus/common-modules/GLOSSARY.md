# GLOSSARY · ruoyi-common 术语表

## A
- **AOP 切面** — Aspect-Oriented Programming。通过 @Aspect + @Around 在方法执行前后插入逻辑（如 @Log 注解的操作日志记录）。
- **自动填充（MetaObjectHandler）** — MyBatis-Plus 机制，在 INSERT/UPDATE 时自动为 createTime、updateBy 等审计字段赋值。

## B
- **BaseEntity** — ruoyi-common-mybatis 中的实体基类，定义 createDept/createBy/createTime/updateBy/updateTime 五个审计字段。
- **BaseMapperPlus** — 增强的 MyBatis Mapper 接口，提供实体到 VO 自动转换、批量操作、链式 CRUD。
- **BigNumberSerializer** — 当 Long 值超出 JS 安全范围（±9007199254740991）时自动以字符串形式序列化，防精度丢失。
- **BOM** — Bill of Materials。Maven POM 类型项目，统一管理所有模块的版本号。

## C
- **Caffeine** — 高性能 Java 本地缓存库。在 PlusSaTokenDao 中作为一级缓存（5秒过期）。
- **CIDR** — Classless Inter-Domain Routing。IP 地址段表示法，NetUtils 支持 CIDR 格式的 IP 匹配。
- **CORS** — Cross-Origin Resource Sharing。跨域资源共享，common-web 通过 CorsFilter 全局配置。

## D
- **数据权限** — 行级安全机制。同一张表，不同用户根据角色看到不同的数据行。通过 @DataPermission 注解 + JSqlParser SQL 注入实现。
- **脱敏（Sensitive）** — JSON 序列化时自动将敏感字段（手机号/身份证等）部分字符替换为 *。
- **DictService** — 字典查询服务 SPI 接口，定义在 common-core，实现在 ruoyi-system。

## E
- **Easy-Es** — 国产 Elasticsearch ORM 框架，API 风格类似 MyBatis-Plus。
- **ExcelBuilder** — common-excel 的统一入口类，链式调用完成导出/导入/模板操作。

## F
- **Fesod Sheet** — Apache 基金会的 Excel 读写引擎（EasyExcel 替代方案），common-excel 的底层依赖。
- **快速失败（Fail Fast）** — ValidatorConfig 的校验策略，遇到第一个校验失败立即停止。

## G
- **全局异常处理器（GlobalExceptionHandler）** — common-web 中的 @RestControllerAdvice，统一处理 16 种异常类型。

## H
- **Hutool** — 国产 Java 工具库，贯穿整个项目（加密、日期、JSON、HTTP、树形构建等）。

## I
- **i18n（国际化）** — BaseException 支持通过 code 键查找对应语言的错误消息。I18nLocaleResolver 从 content-language 请求头解析语言。
- **ip2region** — 离线 IP 地址定位库，common-core 的 AddressUtils 使用它解析 IP。

## J
- **JSqlParser** — SQL 解析器，PlusDataPermissionInterceptor 使用它解析和修改 SQL AST 注入数据权限条件。
- **JWT（JSON Web Token）** — Sa-Token 使用 JWT 简单模式，Token 自包含用户信息，无需每次查 Redis。
- **JustAuth** — 第三方登录开源 SDK，common-social 基于它支持 26 个平台。

## K
- **Knife4j** — Swagger UI 的增强版，common-doc 的 API 文档展示工具。

## L
- **LambdaCrudChainWrapper** — 链式 CRUD 包装器，提供 eq/like/between/voPage 等流式 API。
- **LoginHelper** — common-satoken 中的静态工具类，获取当前登录用户信息。
- **逻辑删除** — 通过标记字段（del_flag=1）实现软删除，而非物理删除。common-mybatis 全局配置。

## M
- **MapStruct-Plus** — 编译期 Java Bean 转换工具，MapstructUtils 是其静态包装器。
- **MCP（Model Context Protocol）** — AI 模型上下文协议，common-mcp 封装了 MCP Client 的工具调用。Spring AI 负责连接管理，本模块做应用层封装。
- **MQTT** — 物联网消息协议，common-mqtt 负责 Topic 订阅和消息收发。

## O
- **OAuth2.0** — 第三方授权协议。common-social 使用授权码模式（Authorization Code Grant）。
- **OSS（Object Storage Service）** — 对象存储。common-oss 基于 AWS S3 SDK 统一抽象，适配所有 S3 兼容存储。

## P
- **PageQuery** — 分页查询入参对象（pageSize/pageNum/orderByColumn/isAsc），60+ 文件使用它。
- **PlusWebInvokeTimeInterceptor** — 请求耗时日志拦截器，记录参数（自动脱敏）和执行时间。

## R
- **R&lt;T&gt;** — 统一 API 响应体 {code, msg, data}。55 个文件引用。前端 request.ts 根据 code 值决定 Promise 状态。
- **RepeatedlyRequestWrapper** — 请求体缓存包装器，使 InputStream 可多次读取。
- **ResponseEnhancementAdvice** — 响应体增强 Advice，在 Jackson 序列化前执行翻译和脱敏。

## S
- **Sa-Token** — 国产权限认证框架。common-satoken 基于它实现 Token 管理、权限校验、多账号体系。
- **S3 TransferManager** — AWS SDK 的大文件传输管理器，支持自动分片上传。
- **SpEL（Spring Expression Language）** — 数据权限的 SQL 模板使用 SpEL 表达式注入动态值（用户ID/部门ID等）。
- **SpringDoc** — Spring Boot 的 OpenAPI 3.0 实现，common-doc 生成 API 文档。
- **SSE（Server-Sent Events）** — 服务端推送事件，GlobalExceptionHandler 对 SSE 异常做了特殊静默处理。
- **雪花 ID（Snowflake ID）** — Twitter 开源的分布式 ID 生成算法。common-mybatis 的 IdGeneratorUtil 提供此能力。

## T
- **ThreadLocal** — 线程本地变量。数据权限注解、请求计时器等通过 ThreadLocal 在线程内传递上下文，请求结束后清理。
- **TranslationInterface** — 翻译器接口。实现它并标注 @TranslationType 即可注册新的翻译类型。

## V
- **虚拟线程（Virtual Thread）** — Java 21+ 特性。ThreadPoolConfig 和 ThreadUtils 支持虚拟线程。SpringUtils.isVirtual() 检测是否支持。

## W
- **WebSocket** — 全双工通信协议，common-push 用于实时消息推送。

## X
- **XSS（Cross-Site Scripting）** — 跨站脚本攻击。common-web 的 XssFilter + common-core 的 @Xss 注解提供双层防护。

# ruoyi-common-satoken Glossary

收录 Sa-Token 认证模块中的核心术语，聚焦 RuoYi-Vue-Plus 工程语境下的含义，而非框架通用定义。

## Terms

**Sa-Token**：
一个 Java 轻量级权限认证框架，提供登录认证、权限鉴权、Token 管理、踢人下线、账号封禁、多账号体系等开箱即用的功能。在 RuoYi-Vue-Plus 中作为认证骨干，替代了传统的 Spring Security + OAuth2 方案。
_Avoid_: "SA-TOKEN"、"sa-token"（官方约定驼峰拼写）。

**[[glossary:JWT]]**：
JSON Web Token，一种自包含的 Token 格式，将用户信息编码在 Token 自身中，服务端无需查库即可验证。RuoYi-Vue-Plus 通过 `sa-token-jwt` 插件将 Sa-Token 切换到 JWT 模式，Token 本身携带基础用户数据，详细登录信息仍存储在 Redis 的 Token Session 中。

**[[glossary:StpLogic]]**：
Sa-Token 的「认证逻辑」核心类，掌管登录、退出、Token 创建、会话管理等所有认证操作的底层实现。本模块注入的是 `StpLogicJwtForSimple`——JWT 简单模式的实现，Token 不再是一个随机字符串而是真正的 JWT。

**[[glossary:StpInterface]]**：
Sa-Token 的权限扩展接口，定义了两个方法：`getPermissionList(loginId, loginType)` 和 `getRoleList(loginId, loginType)`。框架在每次权限校验时自动回调此接口获取当前用户的权限码和角色列表。

**[[glossary:SaTokenDao]]**：
Sa-Token 的数据持久层接口，定义了 Token、Session 等数据的存储、读取、更新、删除、过期等操作。默认实现基于内存，RuoYi-Vue-Plus 通过 `PlusSaTokenDao` 将其替换为 Redis + Caffeine 两级缓存方案，支持分布式部署。

**[[glossary:StpLogicJwtForSimple]]**：
`sa-token-jwt` 插件提供的 JWT 简单模式 StpLogic 实现。与 Mixin 模式不同，Simple 模式将 JWT 生成完全交给 Sa-Token，使用者无需额外适配代码。Token 变为一段 Base64 编码的 JWT 字符串，可被任何语言解析。

**Caffeine**：
一个高性能的 Java 本地缓存库，接近理论极限的读写速度。在 `PlusSaTokenDao` 中用于缓存 Token/Session 数据，避免每次鉴权都穿透到 Redis，大幅降低 Redis 的 QPS 压力。

**Token Session**：
Sa-Token 中与 Token 绑定的会话对象，存储该 Token 的专属数据（如登录用户信息、临时状态等）。区别于 `Account Session`（按账号维度），Token Session 按 Token 维度隔离——同一账号多设备登录时各自独立。在 `LoginHelper.login()` 中，用户的部门信息和 LoginUser 对象均写入 Token Session。

**NotLoginException**：
Sa-Token 在用户未登录或登录状态异常时抛出的异常。包含多种子类型：`TOKEN_TIMEOUT`（过期）、`BE_REPLACED`（被顶下线）、`KICK_OUT`（被踢下线）、`TOKEN_FREEZE`（被冻结）等。`SaTokenExceptionHandler` 针对不同类型返回不同的中文提示。

**NotPermissionException**：
Sa-Token 在用户缺少指定权限码时抛出的异常，通常由 `@SaCheckPermission` 注解或 `StpUtil.checkPermission()` 调用触发。`SaPermissionImpl.getPermissionList()` 返回的列表中不包含目标权限码时抛出。

**[[glossary:LoginUser]]**：
RuoYi-Vue-Plus 定义的登录用户信息对象，包含 userId、userName、deptId、deptName、角色列表、权限列表等完整的用户画像。登录成功后通过 `LoginHelper` 写入 Token Session，权限校验时从其中提取权限码。

**[[glossary:自动配置]]**：
Spring Boot 的 AutoConfiguration 机制，通过 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` 文件声明配置类。`SaTokenConfig` 作为自动配置入口，使得引入 `ruoyi-common-satoken` 依赖即可自动装配认证体系，无需手动 `@ComponentScan`。

**Token 前缀**：
附加在 Token 字符串前面的标识，通常为 `"Bearer "`。HTTP 请求头 `Authorization: Bearer xxxxx` 中的 Bearer 就是 Token 前缀。`common-satoken.yml` 中配置 `token-prefix: "Bearer"`，Sa-Token 在读取时自动剥离。

**[[glossary:踢人下线]]**：
管理员主动使指定账号的 Token 失效，强制其退出登录。Sa-Token 提供 `StpUtil.kickout(loginId)` API，底层将该账号的 Token 标记为无效。与"顶人下线"不同，踢人是管理员行为，顶人是同一账号新登录自动踢掉旧会话。

## Rules

1. 仅在用户真正理解术语的核心含义后才收录——不追求术语数量，追求精确。
2. 有自己的观点——选择信息密度最高的称法作为术语名，其余标注 Avoid。例如统一用 Sa-Token 而非 SA-TOKEN。
3. 定义中引用其他术语时，使用 `[[glossary:术语名]]` 建立交叉引用。
4. 理解加深时直接修订原文，不留"待补充"或过时条目——术语表应反映当前认知水平。

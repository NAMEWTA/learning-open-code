# ruoyi-common-social 社交登录模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**JustAuth**：
Dromara 社区出品的开源 OAuth 聚合框架。封装了 GitHub、QQ、微信、微博、钉钉等 20+ 平台的 OAuth 登录流程，提供统一的 `AuthRequest` / `AuthSource` / `AuthToken` / `AuthUser` 抽象。`ruoyi-common-social` 的全部社交登录能力来自它。
_Avoid_: 「OAuth SDK」（JustAuth 是聚合层，不是单个平台的 SDK）。

**AuthRequest**：
JustAuth 定义的标准授权请求接口（`me.zhyd.oauth.request.AuthRequest`）。核心方法：`authorize(state)` — 生成授权地址、`login(callback)` — 执行完整登录回调。每个平台的实现类（如 `AuthGithubRequest`）都实现此接口。
_Avoid_: 「HttpRequest」（AuthRequest 是 OAuth 流程抽象，不是 HTTP 请求）。

**AuthDefaultRequest**：
JustAuth 提供的 `AuthRequest` 抽象基类，封装了 OAuth 标准流程的通用逻辑。所有平台实现（包括 RuoYi 自定义的 Gitea/MaxKey/TopIAM）都继承它，只需覆写 `getAccessToken()` 和 `getUserInfo()` 两个方法即可接入新平台。
_Avoid_: 「默认请求」（它是框架提供的模板基类，不是缺省实现）。

**AuthSource**：
JustAuth 定义的 OAuth 平台标识接口（`me.zhyd.oauth.config.AuthSource`）。声明三个关键方法：`authorize()` — 授权端点 URL、`accessToken()` — 令牌端点 URL、`userInfo()` — 用户信息端点 URL。RuoYi 的自定义提供者（Gitea/MaxKey/TopIAM）都通过枚举实现此接口。
_Avoid_: 「来源」（通用词汇，此处特指 OAuth 平台的端点配置）。

**AuthStateCache**：
JustAuth 定义的授权状态缓存接口。声明 `cache(key, value)` / `cache(key, value, timeout)` / `get(key)` / `containsKey(key)` 四个方法。OAuth 流程中用于临时存储 `state` 参数，防止 CSRF 攻击。JustAuth 默认提供基于 `ConcurrentHashMap` 的内存实现。
_Avoid_: 「状态缓存」（泛称，特指 OAuth state 参数的临时存储）。

**AuthRedisStateCache**：
RuoYi 对 [[glossary:AuthStateCache]] 的自定义实现。将所有存取转发给 `RedisUtils`，key 加 `SOCIAL_AUTH_CODE_KEY`（即 `social_auth_code:`）前缀，默认 3 分钟过期。替代 JustAuth 默认的单机内存缓存，使 state 校验在集群下不丢失。是 [[glossary:SocialAutoConfiguration]] 注册的唯一 Bean。
_Avoid_: 「Redis 状态缓存」（过于泛化，特指 OAuth state 的 Redis 实现）。

**SOCIAL_AUTH_CODE_KEY**：
RuoYi 框架级 Redis key 前缀，值为 `"social_auth_code:"`，定义在 `org.dromara.common.core.constant.GlobalConstants`。`AuthRedisStateCache` 的所有存取 key 都以此为前缀，与验证码 key（`captcha_codes:`）和业务 key 隔离。

**SocialAutoConfiguration**：
社交登录模块的 Spring Boot 自动配置类。用 `@AutoConfiguration` 声明、`@EnableConfigurationProperties(SocialProperties.class)` 激活配置绑定、`@Bean` 注册 `AuthRedisStateCache`。通过 `AutoConfiguration.imports` 文件被 Spring Boot 发现，实现「依赖即生效」。
_Avoid_: 「社交自动配置」（泛称，特指本模块的配置类）。

**SocialProperties**：
社交登录配置属性顶层容器（`@ConfigurationProperties(prefix = "justauth")`）。内部只有一行：`Map<String, SocialLoginConfigProperties> type`。key 为平台标识（如 `gitee`、`github`），value 为该平台的 OAuth 凭证集合。
_Avoid_: 「社交属性」（过于泛化，特指 yml 中 `justauth.type` 的映射结构）。

**SocialLoginConfigProperties**：
单个社交平台的 OAuth 凭证容器。核心字段：`clientId` / `clientSecret` / `redirectUri`。扩展字段覆盖全平台特殊需求：`agentId`（企业微信）、`alipayPublicKey`（支付宝）、`serverUrl`（Gitea/MaxKey/TopIAM 私服地址）、`tenantId`（微软 AAD）、`scopes`（授权范围列表）。
_Avoid_: 「登录配置」（泛称，特指 JustAuth 单平台凭证对象）。

**SocialUtils**：
模块的静态工具类，社交登录的「统一调度中心」。核心方法：`getAuthRequest(source, socialProperties)` — 通过 `switch` 语句按平台标识匹配并实例化 `AuthRequest`；`loginAuth(source, code, state, socialProperties)` — 构建 `AuthCallback` 并调用 `authRequest.login()`。覆盖了 JustAuth 内置 24 个平台 + RuoYi 自定义 3 个平台。
_Avoid_: 「社交工具类」（泛称，特指 AuthRequest 的工厂 + 登录入口）。

**AuthCallback**：
JustAuth 定义的回调参数对象。包含三个字段：`code`（授权码，OAuth 服务器回调时附在 URL 上）、`state`（状态值，用于 CSRF 校验）、`auth_code`（部分平台使用）。`SocialUtils.loginAuth()` 接收分散的 code/state 并组装成此对象。
_Avoid_: 「回调」（泛称，特指 OAuth 回调参数对象）。

**AuthToken**：
JustAuth 定义的用户令牌对象。包含 `accessToken`、`refreshToken`、`expireIn`、`tokenType`、`scope` 等标准 OAuth 字段。是 `getAccessToken()` 方法的返回值，后续用于调用 `getUserInfo()` 获取用户信息。
_Avoid_: 「token」（泛称，特指 OAuth 访问令牌对象）。

**AuthUser**：
JustAuth 定义的用户信息对象。包含 `uuid`（平台唯一标识）、`username`、`nickname`、`avatar`、`email`、`rawUserInfo`（平台原始响应）等字段。是 `getUserInfo()` 方法的返回值，也是整个 OAuth 登录流程的最终产物。
_Avoid_: 「用户」（泛称，特指从 OAuth 平台获取的用户信息对象）。

**AuthSource 枚举（自定义模式）**：
RuoYi 添加自定义 OAuth 提供者的标准范式：创建一个 `enum` 实现 `AuthSource` 接口，定义 `authorize()` / `accessToken()` / `userInfo()` 三个端点 URL。Gitea 的自定义 `AuthGiteaSource.GITEA`、MaxKey 的 `AuthMaxKeySource.MAXKEY`、TopIAM 的 `AuthTopIamSource.TOPIAM` 都是此模式的实例。
_Avoid_: 「OAuth 配置」（泛称，特指 JustAuth AuthSource 接口的实现模式）。

**自定义提供者扩展范式（3 件套）**：
RuoYi 为私服 OAuth 系统建立的标准接入模版：① 一个 `AuthSource` 枚举（定义端点 URL）→ ② 一个 `AuthDefaultRequest` 子类（实现 `getAccessToken()` 和 `getUserInfo()`）→ ③ 在 `SocialUtils.getAuthRequest()` 的 `switch` 中添加一个分支。Gitea/MaxKey/TopIAM 三个自定义提供者都精确遵循此范式。
_Avoid_: 「自定义 OAuth」（过于宽泛，根据上下文选用具体名称）。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

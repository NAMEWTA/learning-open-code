# RuoYi-Vue-Plus 全栈登录鉴权 Glossary

覆盖 Sa-Token 认证内核、客户端体系、登录方式、传输安全、前端鉴权对接五大块。术语按课程推进收录，定义只说「是什么」。

## Terms

**grantType（授权类型）**：
登录请求里标明「用哪种方式认证」的字段，取值如 `password` / `sms` / `email` / `social` / `xcx`。后端用它拼出 [[授权策略]] 的 Bean 名来选择校验逻辑。
_Avoid_: 「登录类型」（易与后端 `LoginType` 枚举混淆，后者仅用于失败计数提示）。

**授权策略（AuthStrategy）**：
实现 `IAuthStrategy` 接口、负责某一种 [[grantType]] 身份校验的 Spring Bean，Bean 名约定为 `<grantType>AuthStrategy`。五种登录方式的差异全部收敛在各自策略里，主干（入口/分发/签发）不变。
_Avoid_: 「登录服务」（`SysLoginService` 是策略共用工具类，非策略本身）。

**sys_client（客户端）**：
一张配置表，每行代表一个接入端（PC/APP/小程序等），记录该端允许的 grantType、设备类型、token 超时、访问路径与 IP 白名单。登录时按 `clientId` 取出，决定「这个端能用哪些登录方式、token 怎么配、能访问哪些路径」。

**LoginUser**：
后端登录态上下文对象，封装当前会话的身份（userId/username/userType）、部门、角色、岗位与权限集合。登录时由 `buildLoginUser()` 组装，存入 [[Token-Session]]。可被继承扩展（如 `XcxLoginUser` 加 openid）。

**loginId**：
Sa-Token 用来唯一标识登录主体的值。本项目设计为 `userType:userId`（如 `sys_user:1`），靠前缀支持多用户体系与权限隔离。

**Sa-Token**：
本项目的认证授权框架，负责签发/校验 token、维护登录态会话、提供注解鉴权与权限接口。
_Avoid_: 「Spring Security」（本项目未用它做认证内核）。

**JWT 简单模式（StpLogicJwtForSimple）**：
Sa-Token 的一种工作模式：token 本身是自带 loginId 与扩展信息、可离线验签的 JWT，但完整会话数据仍存 Redis。兼得「JWT 身份自携带」与「服务端可主动失效（踢人/改权限即时生效）」。

**Token-Session**：
Sa-Token 为「每个 token」维护的会话存储，存放完整 [[LoginUser]] 等重对象，经 `PlusSaTokenDao` 落 Redis（带 Caffeine 本地缓存）。
_Avoid_: 与「Account-Session（按账号）」混用——本项目登录态读写走 Token-Session。

**StpInterface**：
Sa-Token 的权限数据回调接口。本项目实现类 `SaPermissionImpl` 提供 `getPermissionList`（菜单权限码）与 `getRoleList`（角色），优先从当前 [[LoginUser]] 内存取，跨用户才查 PermissionService。

**SaInterceptor（统一拦截器）**：
注册在 `SecurityConfig` 的路由拦截器，对受保护请求依次做：登录校验、客户端一致性校验、客户端访问路径/IP 白名单校验。白名单由 `excludes` 与 `@SaIgnore` 控制。

**权限码（permission）**：
形如 `system:user:list` 的字符串，标识一个细粒度操作权限。后端用 `@SaCheckPermission` 校验，前端用它控制按钮显隐。`*:*:*` 表示全部放行。

**ApiEncrypt（接口加解密）**：
对请求/响应体在传输中做 [[AES+RSA 混合加密]] 的机制。`@ApiEncrypt` 注解标记的接口强制加密（无加密头则 403），由 `CryptoFilter` 在 Filter 层解密，与密码 BCrypt、token JWT 三者正交。

**AES+RSA 混合加密**：
用一次性 AES 密钥加密数据体（快），再用 RSA 公钥加密该 AES 密钥（安全传钥）的组合方案，思路同 TLS。前端 `crypto.ts` 加密、后端 `CryptoFilter` 解密。

**动态路由**：
前端登录后按当前用户角色权限，从后端菜单数据生成并注册的路由表，而非写死。Vue 在 `permission.ts` 守卫中 `generateRoutes()+addRoute`，React 在 `permissionStore.reloadMenus()`。刷新页面会重建。

**纵深防御（前端权限 vs 后端校验）**：
本项目的安全约定：前端 `v-hasPermi`/`hasPermi` 仅控制按钮显隐（体验，可被绕过），后端 `@SaCheckPermission` 才是真正的安全边界。两者并存，缺一不可。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：多个词指向同一概念时选最佳者，其余标 _Avoid_。
- 定义内部优先使用术语表自身术语（`[[名称]]` 交叉引用）。
- 理解加深时在原文上修订，不留过时条目。

> 说明：本表当前为「课程已系统讲解 + 配速查」的术语全集。学习者在自测/复述中确认掌握后，可在本表标注个人掌握度；尚未亲自复述确认的条目仅作课程索引。

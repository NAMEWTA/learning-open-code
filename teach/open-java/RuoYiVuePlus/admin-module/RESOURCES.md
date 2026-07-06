> **服务工作流：** `../T-teach/T-teach.md`
> **产物文件名：** `resources.md`
> **父目录规则：** 本模板产物写入 `YYYY-MM-DD-<kebab-name>/` change 目录内

# Admin 启动模块与认证入口 Resources

## Knowledge

- [官方文档: Sa-Token 认证授权框架](https://sa-token.cc/doc.html)
  - **覆盖内容**：登录认证、token 签发与校验、会话管理、踢人下线、权限注解、多客户端配置。RuoYi-Vue-Plus 的整个认证层构建在 Sa-Token 之上，`StpUtil.login()`、`@SaIgnore`、`SaLoginParameter` 等核心 API 均源于此。
  - **何时取用**：学习第 2 节（认证策略分发）和第 4 节（事件监听）之前必读；在调试 token 过期、并发登录、多客户端隔离等行为时作为速查参考。

- [官方文档: Spring Boot 核心特性 — Application Events and Listeners](https://docs.spring.io/spring-boot/reference/features/spring-application.html#features.spring-application.application-events-and-listeners)
  - **覆盖内容**：Spring 内置事件机制、`@EventListener` 注解、`ApplicationEventPublisher`、事件驱动的解耦模式。对应 ruoyi-admin 中 `UserLoginSuccessEvent` 的发布与 `UserLoginSuccessListener` 的消费。
  - **何时取用**：学习第 4 节（事件监听）之前阅读，理解为什么登录成功后不直接在 `AuthController` 里写日志和更新在线状态。

- [官方文档: JustAuth — 第三方登录开源组件](https://justauth.wiki/)
  - **覆盖内容**：OAuth 授权流程、`AuthRequest` 构建、`AuthUser` 数据结构、支持平台列表（GitHub、Gitee、微信、QQ 等）。对应 ruoyi-admin 中 `SocialAuthStrategy` 和 `XcxAuthStrategy` 的实现。
  - **何时取用**：学习第 3 节（第三方登录与小程序登录）之前阅读，理解 `SocialUtils.loginAuth()` 背后 JustAuth 做了什么。

- [教程文章: Strategy Pattern with Spring Boot — Baeldung](https://www.baeldung.com/spring-boot-strategy-pattern)
  - **覆盖内容**：如何在 Spring 容器中用 `@Service` 注解 + 命名约定实现策略模式，通过 bean 名称动态选择实现类。直接对应 ruoyi-admin 中 `IAuthStrategy` 的 `SpringUtils.getBean(grantType + "AuthStrategy")` 设计。
  - **何时取用**：学习第 2 节（认证策略分发）时作为补充阅读，理解 `passwordAuthStrategy`、`smsAuthStrategy` 等 bean 如何被自动发现和路由。

- [官方文档: Redis — 数据类型与 TTL](https://redis.io/docs/latest/develop/data-types/)
  - **覆盖内容**：Redis String 类型的 `SETEX`/`TTL` 操作、自动过期机制。对应 ruoyi-admin 中验证码缓存（`RedisUtils.setCacheObject(key, code, Duration)`）、登录错误计数、在线用户 token 的存储策略。
  - **何时取用**：学习第 1 节（密码登录全链路）中验证码校验部分时参考，理解为什么验证码能自动过期、为什么错误次数能在锁定时长后清零。

- [官方文档: Hutool — BCrypt 加密工具](https://doc.hutool.cn/pages/Bcrypt/)
  - **覆盖内容**：BCrypt 哈希算法的原理、`BCrypt.hashpw()` 和 `BCrypt.checkpw()` 的用法、加盐机制。对应 ruoyi-admin 中 `PasswordAuthStrategy` 的密码比对和 `SysRegisterService` 的注册密码加密。
  - **何时取用**：学习第 1 节（密码登录全链路）密码校验部分时参考，理解为什么密码不以明文存储、BCrypt 如何做到每次哈希结果不同但仍可校验。

- [官方文档: MyBatis-Plus — Lambda 查询与 VO 映射](https://baomidou.com/guides/data-interface/)
  - **覆盖内容**：Lambda 表达式构建类型安全查询、`voOne()` / `selectVoById()` 直接返回 VO 对象。对应 ruoyi-admin 中各策略中 `userMapper.lambda().eq(SysUser::getUserName, username).voOne()` 的写法。
  - **何时取用**：学习第 1-3 节中用户加载逻辑时参考，理解 MyBatis-Plus 如何减少样板代码。

## Wisdom (Communities)

- [Dromara 开源社区 — Gitee 组织主页](https://gitee.com/dromara)
  - **覆盖内容**：RuoYi-Vue-Plus 所属的 Dromara 开源社区，包含项目 issue 讨论、PR 评审、版本发布公告。适合提交 bug、阅读其他人的问题讨论、了解框架演进方向。
  - **何时取用**：在完成全部课程后，将学习成果转化为对开源项目的贡献时加入；遇到课程未覆盖的边界问题时搜索 issue 历史。

- [Sa-Token 官方社区 — Gitee Issues](https://gitee.com/dromara/sa-token/issues)
  - **覆盖内容**：Sa-Token 框架的使用问题讨论、常见踩坑记录、作者答疑。因为 ruoyi-admin 的认证层重度依赖 Sa-Token，该社区的很多讨论直接适用。
  - **何时取用**：在调试 token 行为（并发登录、超时、踢人下线、多客户端隔离）遇到困惑时，优先在这里搜索而非泛泛 Google。

## Gaps

- Spring Boot 自动配置原理（`@SpringBootApplication`、`@EnableAutoConfiguration`）属于 Spring Boot 基础知识，不在本模块范围，未单独收录资源。若学习者在追踪 `DromaraApplication.main()` 启动流程时遇到障碍，可参考 [Spring Boot Reference — Auto-configuration](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)。
- 跨模块依赖（如 `ruoyi-common-satoken`、`ruoyi-system` 中 `LoginUser` 和 `SysUserVo` 的定义）将在后续模块教学中展开，本阶段仅做引用层面的说明。

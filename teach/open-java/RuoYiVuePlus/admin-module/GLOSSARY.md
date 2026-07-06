# Admin 启动模块与认证入口 - 术语表

## 一、架构与框架层

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Spring Boot / Spring Boot 框架 | 基于 Spring 的快速应用开发框架，提供自动配置、内嵌容器和起步依赖 | 整个 ruoyi-admin 模块的运行基础，DromaraApplication.main() 即为 Spring Boot 启动入口 |
| @SpringBootApplication / 启动注解 | Spring Boot 核心注解，组合了 @SpringBootConfiguration、@EnableAutoConfiguration 和 @ComponentScan 三个注解 | 标注在 DromaraApplication 类上，触发自动配置和 Bean 扫描 |
| Auto-configuration / 自动配置 | Spring Boot 根据 classpath 中的依赖自动配置 Bean 的机制 | 启动时自动配置 Sa-Token、Redis、MyBatis-Plus、Jetty 等 200+ 组件 |
| Component Scan / 组件扫描 | Spring 自动发现并注册 @Component、@Service、@Controller 等注解标记的 Bean | 启动时扫描 web/controller/、web/service/、web/listener/ 包，注册所有认证相关 Bean |
| BufferingApplicationStartup / 启动性能追踪 | Spring Boot 3.x 引入的应用启动步骤收集器，可记录每个 Bean 的初始化耗时 | 在 DromaraApplication 中配置缓冲区大小为 2048，通过 /actuator/startup 端点查看启动性能 |
| Jetty / Jetty 内嵌容器 | 轻量级 Java Web 服务器和 Servlet 容器，内存占用比 Tomcat 更小 | RuoYi 使用 Jetty 替代默认的 Tomcat，配置了线程池（min 8, max 256），适合长连接网关场景 |
| DromaraServletInitializer / WAR 部署初始化器 | 继承 SpringBootServletInitializer 的类，用于将 Spring Boot 应用部署到外部 Servlet 容器 | 当需要以 war 包形式部署到独立 Tomcat/Jetty 服务器时使用；jar 包部署时不生效 |
| Sa-Token / Sa-Token 认证授权框架 | 轻量级 Java 权限认证框架，提供登录认证、Token 签发、会话管理、权限注解等功能 | 整个认证层构建在 Sa-Token 之上，StpUtil.login()、@SaIgnore、SaLoginParameter 均源于此 |
| Strategy Pattern / 策略模式 | 行为设计模式：定义一组算法，将每个算法封装到独立类中，使它们可以互相替换 | IAuthStrategy 接口 + 5 个 @Service 实现类构成策略模式，通过 Bean 命名约定动态路由 |
| Open-Closed Principle / 开闭原则 | 对扩展开放、对修改关闭的软件设计原则 | 新增认证方式只需新增 @Service 实现类，无需修改 AuthController 或任何已有策略代码 |

## 二、配置与属性层

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| application.yml / 应用配置文件 | Spring Boot 的核心配置文件，包含 370+ 行配置项 | 集中管理验证码、密码策略、Sa-Token 会话、数据源、Redis 等全部配置 |
| CaptchaProperties / 验证码配置类 | 绑定 application.yml 中 captcha.* 配置的 Java 配置类 | PasswordAuthStrategy 中通过 captchaProperties.getEnable() 决定是否执行图片验证码校验 |
| captcha.enable / 验证码开关 | 全局控制图片验证码校验是否启用的布尔配置 | 设为 false 可全局跳过图片验证码校验，适用于内部工具或无验证码需求的场景 |
| captcha.type / 验证码类型 | 取值 math（数学计算题）或 char（字符），控制生成的验证码形式 | 由 CaptchaController 读取，决定生成数学算式验证码还是字母数字组合验证码 |
| user.password.maxRetryCount / 最大重试次数 | 密码错误最大允许次数，超过后触发账号锁定 | SysLoginService.checkLogin() 中用 @Value 注入，错误计数达上限时抛出异常 |
| user.password.lockTime / 锁定时间 | 密码错误次数达上限后的锁定分钟数 | Redis 中错误计数 key 的 TTL 等于此值，过期后自动清零，无需手动解锁 |
| Token / 令牌 | 用户登录成功后由服务端签发的凭证，客户端后续请求需携带此令牌以证明身份 | Sa-Token 签发后存入 Redis，前端在请求头 Authorization 字段中携带 |
| Concurrent Login / 并发登录 | 同一账号在多个设备/浏览器同时登录的行为 | 由 sa-token.is-concurrent 配置控制，设为 false 时新登录会挤掉旧会话 |
| Client Isolation / 客户端隔离 | 不同客户端（PC、App、小程序）拥有独立的会话超时、设备类型、授权方式配置 | sys_client 表的每条记录代表一个客户端，通过 clientId 区分，各客户端策略互不影响 |
| sys_client / 客户端配置表 | 存储不同客户端（如 PC 端、App 端）的授权类型、超时策略、状态等配置的数据表 | AuthController 通过 clientService.queryByClientId() 查询，校验 grantType 和客户端状态 |
| Client Timeout / 客户端超时 | 每个客户端独立的 Token 有效期（秒）和无操作超时（秒） | 从 sys_client 表读取，在 buildLoginParameter() 中设置到 SaLoginParameter，使不同客户端有不同会话策略 |

## 三、认证策略层

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| IAuthStrategy / 认证策略接口 | 定义认证策略契约的 Java 接口，包含静态工厂方法和实例方法 | 5 个策略实现类的父接口；其静态 login() 方法根据 grantType 拼接 Bean 名称并路由到具体实现 |
| grantType / 授权类型 | 标识本次登录使用的认证方式的字符串（如 "password"、"sms"、"email"、"social"、"xcx"） | 前端登录请求传入，AuthController 校验其是否在客户端授权列表内，然后传给 IAuthStrategy.login() 路由 |
| AuthController / 认证控制器 | 处理登录、注册、退出、社交绑定等请求的 REST 控制器 | 标注 @SaIgnore 使所有接口无需登录即可访问；login() 方法负责解析请求、校验客户端、分发策略 |
| @SaIgnore / 跳过鉴权注解 | Sa-Token 提供的注解，标注后该接口或 Controller 不进行登录鉴权 | AuthController 类上标注，因为登录、注册等接口必须在用户未登录状态下访问 |
| LoginBody / 登录请求体 | 通用的登录请求数据结构，包含 clientId、grantType 及具体认证方式的字段 | AuthController.login() 将 JSON 请求体解析为 LoginBody，提取 clientId 和 grantType 进行策略分发 |
| PasswordAuthStrategy / 密码认证策略 | 基于用户名 + 密码 + 图片验证码的认证实现 | grantType="password"，实现图片验证码校验（一次性，取出即删）、BCrypt 密码比对、失败计数锁定 |
| SmsAuthStrategy / 短信认证策略 | 基于手机号 + 短信验证码的认证实现 | grantType="sms"，按 phoneNumber 查询用户，调用 SMS4J 发送验证码，验证码比对后不删除（允许重试） |
| EmailAuthStrategy / 邮箱认证策略 | 基于邮箱 + 邮箱验证码的认证实现 | grantType="email"，按 email 查询用户，结构几乎与 SmsAuthStrategy 相同，仅查询字段不同 |
| SocialAuthStrategy / 第三方认证策略 | 基于 OAuth 第三方平台授权的认证实现 | grantType="social"，通过 JustAuth 完成 OAuth 回调认证，通过 sys_social 表查找绑定的系统用户 |
| XcxAuthStrategy / 小程序认证策略 | 基于微信小程序 wx.login() 的认证实现 | grantType="xcx"，用 JustAuth 的 AuthWechatMiniProgramRequest 换取 openid，返回 XcxLoginUser（包含 openid） |
| BCrypt / BCrypt 密码哈希算法 | 基于 Blowfish 加密的密码哈希算法，内置加盐机制，每次哈希结果不同但可校验 | PasswordAuthStrategy 中用 BCrypt.checkpw() 比对用户输入的明文密码与数据库中存储的哈希值 |
| JustAuth / 第三方登录开源组件 | 支持 30+ 平台（Gitee、GitHub、微信、QQ 等）的 OAuth 登录组件 | SocialAuthStrategy 和 XcxAuthStrategy 中调用 SocialUtils.loginAuth() 完成第三方平台认证 |
| SMS4J / 短信发送组件 | Java 多通道短信发送框架，支持阿里云、腾讯云等多个短信服务商 | SmsAuthStrategy 中用于发送短信验证码到用户手机 |
| OAuth / 开放授权协议 | 允许第三方应用在用户授权下访问其资源的开放标准 | 第三方登录流程使用 OAuth 2.0，JustAuth 封装了各平台的 OAuth 实现细节 |
| Supplier\<Boolean\> / 延迟执行函数 | Java 函数式接口，用于将计算延迟到真正需要时才执行 | SysLoginService.checkLogin() 的第三个参数，避免在已锁定状态下还执行 BCrypt.checkpw 等昂贵操作 |
| Consumer\<T\> / 消费型函数接口 | Java 函数式接口，接收一个参数执行操作，无返回值 | buildLoginParameter() 中使用 Consumer\<SaLoginParameter\> 让策略以 lambda 形式追加自定义参数 |

## 四、用户与会话层

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| LoginUser / 登录用户上下文 | 封装登录用户核心信息的上下文对象，包含 userId、username、deptId、权限集合等字段 | LoginHelper.login() 将 LoginUser 传入 Sa-Token，后续可通过 LoginHelper.getLoginUser() 获取 |
| XcxLoginUser / 小程序登录用户 | 继承 LoginUser，额外包含 openid 字段 | XcxAuthStrategy 中构建此对象，将微信小程序的 openid 一并传入会话上下文 |
| LoginVo / 登录响应对象 | 登录成功后返回给前端的响应数据结构，包含 accessToken、expireIn、clientId 等 | 每个策略的 login() 方法最终构建 LoginVo 返回，XcxAuthStrategy 还会设置 openid 字段 |
| SaLoginParameter / Sa-Token 登录参数 | Sa-Token 提供的登录参数模型，包含设备类型、Token 有效期、无操作超时、扩展数据 | buildLoginParameter() 构建此对象，携带客户端配置和策略自定义参数，传给 LoginHelper.login() |
| LoginHelper / 登录辅助工具类 | 封装 Sa-Token 操作的静态工具类，提供 login()、getLoginUser()、getUserId() 等方法 | 所有策略调用 LoginHelper.login() 签发 token；业务代码通过 LoginHelper.getLoginUser() 获取当前用户 |
| StpUtil / Sa-Token 工具类 | Sa-Token 框架提供的核心静态工具类，提供登录、退出、鉴权、会话管理等全部 API | SysLoginService.logout() 中调用 StpUtil.logout() 触发 doLogout 回调 |
| SysUserVo / 系统用户视图对象 | 数据库表 sys_user 对应的 VO 对象，包含用户名、密码、手机号、邮箱、状态等字段 | 各策略通过 MyBatis-Plus 的 voOne() 直接加载，用于用户存在性和状态校验 |
| SysClientVo / 系统客户端视图对象 | 数据库表 sys_client 对应的 VO 对象，包含 clientId、grantType、timeout、status 等字段 | AuthController 查询后校验 grantType 是否在授权列表内，并传给 buildLoginParameter() 设置超时 |
| LoginType / 登录类型枚举 | 枚举类型，包含 PASSWORD、SMS、EMAIL 等值 | SysLoginService.checkLogin() 第一个参数，用于区分不同认证方式的日志记录和错误提示 |
| UserOnlineDTO / 在线用户数据传输对象 | 封装在线用户信息（IP、归属地、浏览器、OS、登录时间、Token 等）的 DTO | UserLoginSuccessListener 构建此对象并写入 Redis，作为后台"在线用户"页面的数据源 |

## 五、事件与监听层

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Spring Event / Spring 事件机制 | Spring 框架提供的发布-订阅模式，允许 Bean 之间通过事件进行解耦通信 | 登录成功后通过 UserLoginSuccessEvent 将"发生了登录"的事实传递给监听器，控制器不需要知道有哪些副作用 |
| @EventListener / 事件监听注解 | Spring 注解，标注在方法上表示该方法监听指定类型的 ApplicationEvent | UserLoginSuccessListener.handleLoginSuccess() 标注此注解，自动接收 UserLoginSuccessEvent |
| Java record / Java 记录类 | Java 17 引入的不可变数据载体，自动生成构造器、equals、hashCode、toString、访问器方法 | UserLoginSuccessEvent 使用 record 定义，一行代码替代传统 40+ 行的 POJO Event 类 |
| UserLoginSuccessEvent / 登录成功事件 | Java record，携带 loginId、tokenValue、loginParameter 三个字段 | UserActionListener 发布此事件，UserLoginSuccessListener 消费此事件执行业务副作用 |
| UserActionListener / Sa-Token 生命周期监听器 | 实现 SaTokenListener 接口，将 Sa-Token 框架事件翻译为 Spring 事件的桥梁组件 | doLogin() 发布 UserLoginSuccessEvent；doLogout/doKickout/doReplaced() 清除 Redis 在线缓存 |
| UserLoginSuccessListener / 登录成功业务监听器 | 消费 UserLoginSuccessEvent 的 Spring 事件监听器，执行登录后的 5 项业务操作 | 解析 User-Agent、IP 归属地、写入在线用户缓存、记录登录日志、更新用户表登录信息 |
| LoginInfoEvent / 登录日志事件 | 登录成功/失败/退出时发布的日志事件对象 | SysLoginService.recordLoginInfo() 发布，由 ruoyi-common-log 模块的 LogListener 异步写入数据库 |
| doKickout / 踢人下线 | 管理员将指定用户强制下线的操作 | 调用 StpUtil.kickout(loginId) 触发 UserActionListener.doKickout()，清除 Redis 中的 token 和在线缓存 |
| doReplaced / 顶替下线 | 同一账号在新设备登录时，旧会话被顶掉的操作 | 当 is-concurrent: false 时触发，UserActionListener.doReplaced() 清除旧会话的在线缓存 |

## 六、服务与控制器层

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| SysLoginService / 系统登录服务 | 封装登录校验、用户构建、登录日志、最近登录信息更新等公共逻辑的服务类 | 所有策略调用其 checkLogin() 做失败计数校验、buildLoginUser() 构建 LoginUser、recordLoginInfo() 记录日志 |
| SysRegisterService / 系统注册服务 | 处理用户注册的服务类，包含密码 BCrypt 加密、默认角色分配等逻辑 | AuthController.register() 调用，完成新用户的创建和密码加密 |
| CaptchaController / 验证码控制器 | 生成和获取验证码的 REST 控制器 | 提供图形验证码、短信验证码、邮箱验证码的获取接口 |
| AuthController.logout() / 退出登录接口 | 处理用户主动退出的控制器方法 | 调用 loginService.logout() 记录日志，然后 StpUtil.logout() 清除 token |
| ValidatorUtils / 校验工具类 | 请求体字段合法性校验的工具类 | 每个策略在解析 LoginBody 后调用 ValidatorUtils.validate() 进行字段校验 |

## 七、数据与工具层

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| Redis / Redis 缓存 | 高性能键值存储数据库，支持多种数据类型和 TTL 自动过期 | 存储验证码（一次性使用）、在线用户缓存、登录错误计数、Sa-Token 会话信息 |
| MyBatis-Plus / MyBatis 增强框架 | MyBatis 的增强工具，提供 Lambda 查询、自动分页、VO 映射、代码生成等功能 | 各策略中通过 userMapper.lambda().eq(...).voOne() 进行类型安全查询，跳过 Entity 转换 |
| voOne() / 直接返回 VO | MyBatis-Plus 提供的查询方法，直接返回单个 VO 对象，不经过 Entity | 各策略加载用户时使用，如 userMapper.lambda().eq(SysUser::getUserName, username).voOne() |
| CacheNames / 缓存键名常量 | 定义 Redis 缓存 key 前缀的常量类 | PWD_ERR_CNT_KEY（密码错误计数）、ONLINE_TOKEN_KEY（在线用户）、CAPTCHA_CODE_KEY（验证码） |
| SpringUtils / Spring 容器工具类 | 封装 ApplicationContext 获取 Bean 操作的静态工具类 | IAuthStrategy.login() 中通过 SpringUtils.getBean(beanName) 获取策略实例；UserActionListener 中获取上下文 |
| ip2region / IP 归属地离线数据库 | 离线 IP 地址定位数据库，无需网络请求即可解析 IP 的归属地（国家-省-市） | UserLoginSuccessListener 中通过 AddressUtils.getRealAddressByIP(ip) 解析客户端 IP 的地理位置 |
| User-Agent / 用户代理解析 | HTTP 请求头中的 User-Agent 字段，包含浏览器、操作系统等信息 | UserLoginSuccessListener 中通过 Hutool 的 UserAgentUtil.parse() 解析并提取浏览器和操作系统名称 |
| sys_social / 第三方账号绑定表 | 存储第三方平台（如 Gitee、微信）账号与系统用户的绑定关系的数据表 | SocialAuthStrategy 中查询此表，通过 OAuth 获取的 authId 找到绑定的系统用户 ID |
| openid / 微信用户唯一标识 | 微信平台为每个用户在每个小程序/公众号下生成的唯一标识 | XcxAuthStrategy 用 wx.login() 的 code 换取 openid，存储到 XcxLoginUser 中并在 LoginVo 中返回 |
| GlobalConstants / 全局常量类 | 系统中定义的各种常量，如 CAPTCHA_CODE_KEY = "captcha_codes:" | 验证码校验时拼接 Redis key：CAPTCHA_CODE_KEY + uuid（图片验证码）或 phoneNumber（短信验证码） |
| DataPermissionHelper / 数据权限辅助类 | 用于跳过或控制 MyBatis-Plus 数据权限过滤的辅助工具 | updateLastLoginInfo() 中调用 DataPermissionHelper.ignore() 跳过数据权限，因为更新自己的登录信息不应受权限限制 |

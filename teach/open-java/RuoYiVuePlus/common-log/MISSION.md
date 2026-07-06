# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-log 操作日志模块

## Why
学习者要能彻底读懂 `ruoyi-common-log` 这个公共模块：它本身只有 7 个 Java 类，通过自定义注解 `@Log` + AOP 切面 + Spring 事件机制，实现了操作日志的「零侵入记录」。理解它，等于理解 RuoYi-Vue-Plus 如何用「声明式注解 + AOP 拦截 + 事件解耦」三层设计，让业务代码只需加一个注解就能自动记录操作日志，而日志的存储、查询、清理等下游逻辑完全解耦。达到能给同事讲清「@Log 注解怎么变成一条数据库日志」「为什么用事件而不是直接写库」「如何自定义一个新事件类型」，并能在此基础上排查日志未记录问题或扩展自定义日志场景。重点是**读懂设计动机与真实调用链**，不是背注解参数。

## Success looks like
- 能用一句话说清 `ruoyi-common-log` 模块与 `@Log` 注解的关系，并说出模块的 7 个 Java 文件各自承担什么职责（1 个注解、1 个切面、3 个枚举、2 个事件类）。
- 能解释 `LogAspect` 如何通过 `@Around("@annotation(controllerLog)")` 拦截所有标注了 `@Log` 的方法，并说出从拦截到入库的完整 7 步链路：AOP 环绕拦截 → StopWatch 计时 → proceed() 执行目标方法 → 构建 OperLogEvent 填充请求上下文（IP/URL/用户/方法名）→ 解析 @Log 注解参数（title/businessType/operatorType）→ 按配置保存请求参数和响应结果 → `SpringUtils.context().publishEvent(operLog)` 发布事件。
- 能讲清三种枚举（`BusinessType` / `OperatorType` / `BusinessStatus`）各自控制日志的哪个维度，以及它们如何通过 `ordinal()` 存入数据库 int 字段——BusinessType 标记操作性质（新增/修改/删除/导出等 10 种），OperatorType 标记操作人来源（后台/手机端/其他），BusinessStatus 标记执行结果（成功/失败）。
- 能讲清为什么模块用 `SpringUtils.context().publishEvent(operLog)` 发事件而不是在切面里直接写数据库，以及这种设计对「日志存储可替换」「日志监听器可热插拔」意味着什么——切面只管拦截与组装，存储由 `SysOperLogServiceImpl.recordOper()` 通过 `@EventListener` + `@Async` 异步消费，双方通过事件对象解耦。
- 能完整追踪「Controller 方法加 @Log → AOP 拦截 → 提取请求上下文（IP/用户/浏览器/OS）→ 解析注解参数 → 填充 OperLogEvent → 发布 Spring 事件 → `SysOperLogServiceImpl.recordOper()` 异步消费 → MapstructUtils 转换 → 插入 `sys_oper_log` 表」这条链路中的每一环。
- 能正确区分 `OperLogEvent`（操作日志事件，23 个字段，由 LogAspect 在 Controller 方法执行后发布）和 `LoginInfoEvent`（登录事件，5 个字段，由 `SysLoginService` / `SysRegisterService` 在登录/注册时发布），并说出它们分别被哪个 Service 的哪个方法消费（`SysOperLogServiceImpl.recordOper()` 和 `SysLoginInfoServiceImpl.recordLoginInfo()`），以及消费端如何通过 `@Async` + `@EventListener` 实现异步非阻塞存储。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会在事件消费环节联系到 `ruoyi-modules/ruoyi-system` 模块的 `SysOperLogServiceImpl` 和 `SysLoginInfoServiceImpl` 实现（点到为止）。
- 目标是「读懂」而非「能改造框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。
- 课程短小精悍（每课几分钟可完成），强调一手资料和 AI 追问。

## Out of scope
- 数据库表结构（`sys_oper_log`、`sys_logininfor`）的完整建表语句与索引设计——仅在与事件字段对照时点到。
- 日志清理策略（定时任务删除过期日志）的完整实现。
- `SysLoginInfoServiceImpl` 和 `SysOperLogServiceImpl` 的完整 MyBatis-Plus 持久化与分页查询细节——只讲 `@EventListener` 解耦关系，不展开 CRUD 实现。
- 前端操作日志查询页面的实现。
- 与其他日志框架（Logback/Log4j2/TLog）的关系——本模块是「业务操作日志」，不是「技术运行日志」。
- `LoginInfoEvent` 的发布端（`SysLoginService` / `SysRegisterService`）完整业务逻辑——只讲事件对象的构建与发布时机。

# ruoyi-common-log 日志模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**@Log**：
自定义操作日志记录注解（`ruoyi-common-log/annotation/Log.java`），标注在 Controller 方法上即可自动记录操作日志。提供 6 个可配置属性：`title`（模块名）、`businessType`（[[glossary:BusinessType]]）、`operatorType`（[[glossary:OperatorType]]）、`isSaveRequestData`（是否保存请求参数，默认 true）、`isSaveResponseData`（是否保存响应参数，默认 true）、`excludeParamNames`（[[glossary:excludeParamNames | 排除参数名]]）。是零侵入操作日志记录的入口——加一个注解，其他全自动。
_Avoid_: 「日志注解」（太泛，Spring 里有太多日志相关注解，@Log 特指操作日志）。

**LogAspect**：
操作日志记录的 AOP [[glossary:AOP切面 | 切面类]]（`ruoyi-common-log/aspect/LogAspect.java`），通过 `@Around("@annotation(controllerLog)")` 拦截所有标注了 [[glossary:@Log]] 的方法。核心流程：`doAround` 启动 StopWatch 计时 -> 执行目标方法 -> 调用 `handleLog` 组装 [[glossary:OperLogEvent]] -> 通过 `SpringUtils.context().publishEvent(operLog)` 发布事件。handleLog 内部自动获取 IP、URL、当前登录用户（`LoginHelper.getLoginUser()`）、方法名、请求方式、耗时等，异常时自动翻转 [[glossary:BusinessStatus]] 为 FAIL 并记录异常消息。通过 `AutoConfiguration.imports` 自动注册，无需手动配置。
_Avoid_: 「日志拦截器」（Interceptor 是另一种机制；LogAspect 是 AspectJ AOP 切面，不是 Spring Interceptor）。

**BusinessType**：
业务操作类型枚举（`ruoyi-common-log/enums/BusinessType.java`）。定义了 10 种操作类型：OTHER / INSERT / UPDATE / DELETE / GRANT / EXPORT / IMPORT / FORCE / GENCODE / CLEAN，分别对应其它、新增、修改、删除、授权、导出、导入、强退、生成代码、清空数据。[[glossary:@Log]] 的 `businessType` 属性默认值为 OTHER，Controller 方法通过指定具体类型来标记操作性质（如 `@Log(title = "用户管理", businessType = BusinessType.INSERT)`）。
_Avoid_: 「操作类型」（太泛，容易与 [[glossary:OperatorType]] 混淆；BusinessType 回答"做了什么操作"而非"谁做的"）。

**BusinessStatus**：
操作状态枚举（`ruoyi-common-log/enums/BusinessStatus.java`），仅两个值：SUCCESS / FAIL。[[glossary:LogAspect]] 在 `handleLog` 中根据是否有异常自动赋值：无异常设为 SUCCESS (`BusinessStatus.SUCCESS.ordinal()` 即 0)，捕获到异常后翻转为 FAIL (`BusinessStatus.FAIL.ordinal()` 即 1)。该值最终写入 `sys_oper_log` 表的 `status` 字段。
_Avoid_: 「成功/失败标志」（丢失了它在系统中作为枚举存在的事实，且 ordinal 值影响数据库持久化）。

**OperatorType**：
操作人类别枚举（`ruoyi-common-log/enums/OperatorType.java`），区分三类操作来源：OTHER（其它）、MANAGE（后台管理用户）、MOBILE（手机端用户）。[[glossary:@Log]] 的 `operatorType` 属性默认值为 MANAGE，由 Controller 方法按实际场景声明。该值与 [[glossary:BusinessType]] 正交——BusinessType 回答"做了什么"，OperatorType 回答"谁做的（哪个端）"。
_Avoid_: 「用户类型」（容易和系统用户角色/权限混淆，它特指操作用户的来源端）。

**OperLogEvent**：
操作日志事件类（`ruoyi-common-log/event/OperLogEvent.java`），包含 20+ 字段（title、businessType、operatorType、method、operUrl、operIp、operName、userId、deptId、deptName、jsonResult、operParam、costTime、errorMsg 等），实现 `Serializable`。[[glossary:LogAspect]] 组装后通过 [[glossary:Spring事件机制 | Spring 事件机制]] 发布，由 `ruoyi-system` 模块的 `SysOperLogServiceImpl.recordOper()` 异步消费并写入 `sys_oper_log` 表。是 [[glossary:事件解耦 | 解耦]] 设计中的"消息体"——common-log 只管发，system 模块只管收。
_Avoid_: 「操作日志实体」（它不是 JPA/MyBatis 实体，是 Spring 事件载体；真正的实体在 system 模块的 `SysOperLog`）。

**LoginInfoEvent**：
登录事件类（`ruoyi-common-log/event/LoginInfoEvent.java`），字段较少：`username`、`status`（"0" 成功 / "1" 失败）、`message`、`request`（`HttpServletRequest`）、`args`（额外参数）。由 `SysLoginService` 和 `SysRegisterService` 在 admin 模块中构造并发布，由 `SysLoginInfoServiceImpl.recordLoginInfo()` 异步消费后写入 `sys_login_info` 表。与 [[glossary:OperLogEvent]] 共同体现 common-log 模块的职责——定义事件契约，不负责持久化。
_Avoid_: 「登录日志」（模糊了事件和持久化记录的边界；LoginInfoEvent 是事件，SysLoginInfo 是实体）。

**Spring 事件机制（ApplicationEvent / publishEvent / @EventListener）**：
Spring Framework 内置的观察者模式实现。核心三要素：(1) 事件对象 —— 可以是任意 POJO（Spring 4.2+ 不再强制继承 `ApplicationEvent`），如 [[glossary:OperLogEvent]] 和 [[glossary:LoginInfoEvent]]；(2) 发布者 —— 通过 `ApplicationContext.publishEvent(event)` 发布事件，本项目由 `SpringUtils.context().publishEvent()` 和 `SysLoginService` 分别发布两种事件；(3) 监听者 —— 通过 `@EventListener` 注解标记方法，可配合 `@Async` 实现异步消费。整个日志模块基于此机制实现 [[glossary:事件解耦]]。
_Avoid_: 「消息队列」（Spring 事件是 JVM 内同步/异步通信，不跨越进程；MQ 是跨进程的）。

**AOP 切面（Aspect / @Around / ProceedingJoinPoint）**：
面向切面编程（Aspect-Oriented Programming）的三个核心构件。`@Aspect` 声明一个类为切面；`@Around("@annotation(controllerLog)")` 定义一个环绕通知，拦截所有标注 [[glossary:@Log]] 的方法；`ProceedingJoinPoint` 是连接点对象，通过 `proceed()` 放行目标方法执行，并可从 `getTarget()`、`getSignature()`、`getArgs()` 获取目标类的反射信息。[[glossary:LogAspect]] 正是利用这三者实现了"在目标方法执行前后自动记录日志"的零侵入效果——Controller 代码完全不知道自己被记录了日志。
_Avoid_: 「拦截器」（Interceptor 工作在 HandlerMapping 层面，AOP 工作在代理层面，粒度不同。两者都叫"拦截"但机制完全不同）。

**操作日志 vs 系统日志（Business Operation Log vs Technical System Log）**：
两类日志的根本区别：(1) **操作日志**——记录"谁在什么时候做了什么事"，面向业务审计，存储于 `sys_oper_log` 表，可查询、可导出，由本模块的 [[glossary:@Log]] + [[glossary:LogAspect]] + [[glossary:OperLogEvent]] 驱动；(2) **系统日志**——记录"程序运行中发生了什么"，面向开发运维，通过 `@Slf4j` + `log.info/error/debug` 输出到控制台或文件（如 `logback-spring.xml` 配置的磁盘日志），是 `LogAspect.handleLog` 内部 `catch` 块中 `log.error("记录操作日志异常", exp)` 的用途——操作日志写入失败时降级为系统日志记录。不要再把两者称为"日志"而不加限定词。
_Avoid_: 不加限定地说「日志」（无法区分是写入 sys_oper_log 表的操作日志还是 slf4j 输出的系统日志，两者性质完全不同）。

**excludeParamNames（敏感参数排除）**：
[[glossary:@Log]] 注解的字符串数组属性，用于排除请求参数中不需要记录的字段。在 `setRequestValue` 方法中两处生效：(1) GET 请求时通过 `MapUtil.removeAny(paramsMap, excludeParamNames)` 移除指定 key；(2) PUT/POST/DELETE 请求时将参数序列化为 JSON 字符串，使用 `JsonUtils.toJsonStringExcludeFields(arg, exclude)` 排除指定字段。典型场景：`@Log(title = "用户管理", excludeParamNames = {"password", "oldPassword"})` —— 密码字段不会出现在操作日志的 `oper_param` 列中。同时框架内置常量 `SystemConstants.EXCLUDE_PROPERTIES`（包含 `password`、`pwd` 等）也会自动排除。
_Avoid_: 「参数过滤」（filter 在 Servlet 中有特殊含义；这里精确匹配字段名排除）。

**事件解耦（Event-Driven Decoupling）**：
common-log 模块采用的设计模式：日志生产者（[[glossary:LogAspect]]、`SysLoginService`）只管收集信息并发布 Spring 事件，完全不感知谁来消费、怎么存储；日志消费者（`SysOperLogServiceImpl`、`SysLoginInfoServiceImpl` 在 ruoyi-system 模块中）通过 `@EventListener` + `@Async` 异步监听事件并持久化。好处：(1) common-log 不依赖 system 模块，保持模块独立；(2) 日志写入不阻塞主业务线程（@Async）；(3) 如果未来需要增加额外的日志消费者（如发送到 Kafka、ES），只需新增 `@EventListener` 方法，发布者代码无需任何改动。
_Avoid_: 「异步日志」（异步是手段不是目的；解耦才是设计意图，异步只是解耦带来的性能优化副作用）。

## 待收录
- 无 —— 课程尚未开始，术语将在学习过程中逐步收录。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

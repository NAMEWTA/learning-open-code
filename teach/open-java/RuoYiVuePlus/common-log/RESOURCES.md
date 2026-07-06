# ruoyi-common-log 操作日志模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-log 模块全部 7 个文件_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-log/src/main/java/org/dromara/common/log/)
  `annotation/Log.java` — @Log 注解定义（6 个属性：title、businessType、operatorType、isSaveRequestData、isSaveResponseData、excludeParamNames）。
  `enums/BusinessStatus.java` — 操作状态（SUCCESS、FAIL）。
  `enums/BusinessType.java` — 业务操作类型（OTHER、INSERT、UPDATE、DELETE、GRANT、EXPORT、IMPORT、FORCE、GENCODE、CLEAN）。
  `enums/OperatorType.java` — 操作人类别（OTHER、MANAGE、MOBILE）。
  `aspect/LogAspect.java` — AOP 切面，`@Around("@annotation(controllerLog)")` 拦截 + 构建 OperLogEvent + `SpringUtils.context().publishEvent()` 发布。
  `event/LoginInfoEvent.java` — 登录事件（username、status、message、request、args）。
  `event/OperLogEvent.java` — 操作日志事件（23 个字段，从 operId 到 costTime，覆盖 title/businessType/operatorType/operName/userId/deptId/deviceType/browser/os/operUrl/operIp/operParam/jsonResult/status/errorMsg 等完整日志维度）。

  任何关于「操作日志怎么记录」的问题，最终答案在这 7 个文件里。

- [官方文档: _Spring AOP 官方文档_ — Spring Framework（docs.spring.io）](https://docs.spring.io/spring-framework/reference/core/aop.html)
  理解 `@Aspect` / `@Around` / `@annotation()` 切点表达式 / `ProceedingJoinPoint` / `JoinPoint` 的机制时查阅。`LogAspect.doAround()` 的核心原理来源。

- [官方文档: _Spring 事件机制_ — Spring Framework（docs.spring.io）](https://docs.spring.io/spring-framework/reference/core/beans/context-introduction.html#context-functionality-events)
  理解 `ApplicationEventPublisher.publishEvent()` / `@EventListener` / 事件驱动解耦的设计思想时查阅。解释「为什么切面不直接写库」的核心原理来源。

- [代码: _操作日志消费端 — SysOperLogServiceImpl_](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-system/src/main/java/org/dromara/system/service/impl/SysOperLogServiceImpl.java)
  `recordOper(OperLogEvent)` 方法通过 `@Async` + `@EventListener` 异步消费操作日志事件，用 `MapstructUtils.convert()` 将事件转为 `SysOperLogBo`，补充 IP 地理位置后写入 `sys_oper_log` 表。理解「事件发布后谁在听」的关键代码。

- [代码: _登录事件消费端 — SysLoginInfoServiceImpl_](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-system/src/main/java/org/dromara/system/service/impl/SysLoginInfoServiceImpl.java)
  `recordLoginInfo(LoginInfoEvent)` 方法通过 `@Async` + `@EventListener` 异步消费登录事件，解析 User-Agent 获取浏览器/操作系统，补充 IP 地理位置后写入 `sys_logininfor` 表。理解「登录事件如何变成登录日志」的关键代码。

- [代码: _LoginInfoEvent 发布端 — SysLoginService / SysRegisterService_](RuoYi-Vue-Plus/ruoyi-admin/src/main/java/org/dromara/web/service/)
  `SysLoginService.java` 在登录成功/失败时构建并发布 `LoginInfoEvent`；`SysRegisterService.java` 在注册时发布。理解「登录事件在什么时机产生」时查阅。

- [代码: _@Log 注解使用现场_](RuoYi-Vue-Plus/ruoyi-admin/src/main/java/org/dromara/web/controller/)
  搜索 `@Log(title = ` 可找到 Controller 层大量使用注解的真实场景，如用户管理、角色管理、字典管理、参数配置等。理解「注解怎么用」时查阅。

- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明，含日志、权限、代码生成等章节。理解模块在整体架构中的位置时查阅。

- [官方文档: _Hutool 工具集_ — Dromara（hutool.cn）](https://hutool.cn/docs/)
  `LogAspect` 使用 `cn.hutool.core.map.MapUtil`、`cn.hutool.core.util.ArrayUtil`、`cn.hutool.core.util.ObjectUtil` 进行参数处理和过滤判断。理解切面中工具方法行为时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「日志没记录」「如何自定义日志字段」「@Log 注解不生效」等实践问题时，Issues 区最贴近维护者意图。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + 上述官方文档支撑。
- Spring AOP 代理机制（JDK 动态代理 vs CGLIB、自调用失效、`@Transactional` 与 `@Log` 的执行顺序）的深入原理不在本课覆盖范围，仅在实际遇到「注解不生效」问题时作为排查方向提及。

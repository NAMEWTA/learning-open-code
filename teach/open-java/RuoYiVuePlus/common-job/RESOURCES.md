# ruoyi-common-job 定时任务模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-job 模块_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-job/src/main/java/org/dromara/common/job/config/SnailJobConfig.java)
  模块唯一的 Java 文件。任何关于「这个模块做了什么」的问题，最终答案在这个类里。43 行代码，4 个注解 + 1 个事件监听方法。
- [代码: _SnailJob 示例任务目录_](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-job/src/main/java/org/dromara/job/snailjob/)
  7 个真实的 SnailJob 任务示例，覆盖普通任务、广播任务、静态分片、Map 任务、MapReduce 任务、DAG 工作流。理解「怎么写一个 SnailJob 任务」时对照查阅。
- [配置文件: _application-dev.yml snail-job 配置段_](RuoYi-Vue-Plus/ruoyi-admin/src/main/resources/application-dev.yml)
  SnailJob 客户端连接的完整配置：`enabled` 开关、`group` 组名、`token` 令牌、`server.host/port` 服务端地址、`namespace` 命名空间、客户端 `port` 漂移。理解配置项含义时查阅。
- [官方文档: _SnailJob 官方文档_ — Aizuda（snailjob.com）](https://snailjob.com/)
  本模块封装的分布式任务调度框架权威说明。理解 `@JobExecutor`、`JobArgs`、`ExecuteResult`、任务类型、服务端管理控制台时查阅。
- [代码: _SnailJob Server 启动类_](RuoYi-Vue-Plus/ruoyi-extend/ruoyi-snailjob-server/src/main/java/org/dromara/snailjob/SnailJobServerApplication.java)
  SnailJob 调度服务端的 Spring Boot 启动入口。理解「谁在调度任务」时需要知道服务端的存在。
- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration`、`@ConditionalOnProperty`、`@EventListener` 机制时查阅。第 2 课的核心原理来源。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明，含定时任务章节。理解模块在整体架构中的位置时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「SnailJob 客户端连不上服务端」「任务不调度」等问题时，Issues 与讨论区最贴近维护者意图。
- [社区: _SnailJob 官方社区_](https://snailjob.com/)
  SnailJob 框架本身的问题（版本兼容、任务类型用法、配置参数）可在其官方社区查阅。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + SnailJob 官方文档 + 上述资源支撑。

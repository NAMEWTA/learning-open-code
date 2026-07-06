# ruoyi-job 任务调度模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-modules/ruoyi-job/` 与 `RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-job/`）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _SnailJob 官方文档_ — aizuda（snailjob.io）](https://snailjob.io/docs/)
  本模块的基石框架。理解 SnailJob 的任务调度模型（JobExecutor、MapExecutor、ReduceExecutor、DAG 工作流）、客户端配置项（group/token/namespace/server）、以及服务端管理后台的使用时查阅。
- [官方源码: _SnailJob GitHub_ — aizuda（GitHub）](https://github.com/aizuda/snail-job)
  框架源码，`snail-job-client-job-core` 中的 `JobExecutor`、`AbstractJobExecutor`、`MapHandler`、`JobArgs`、`MapArgs`、`ReduceArgs` 等核心类的定义。理解 `@JobExecutor` 注解的扫描机制和任务注册流程时查阅。
- [掘金专栏: _SnailJob 系列教程_ — 老马 / opensnail（掘金）](https://juejin.cn/user/2758517619252548/posts)
  每个示例任务的 JavaDoc 都链接了对应的掘金文章。涵盖正常任务、广播任务、静态分片、Map 任务、MapReduce 任务、DAG 工作流的分步讲解。理解每个 demo 的编写意图时查阅。对应链接已记录在各任务类的 `@see` 注释中。
- [官方文档: _Spring Boot AutoConfiguration_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `SnailJobConfig` 如何通过 `@AutoConfiguration` + `AutoConfiguration.imports` 实现自动装配，以及 `@ConditionalOnProperty` 如何用 `snail-job.enabled` 做开关控制。
- [官方文档: _Spring Scheduling_ — Spring（docs.spring.io）](https://docs.spring.io/spring-framework/reference/integration/scheduling.html)
  `SnailJobConfig` 上 `@EnableScheduling` 的作用：开启 Spring 的定时任务执行能力，配合 SnailJob 的调度触发。
- [代码: _ruoyi-modules/ruoyi-job/src/main/java/org/dromara/job/snailjob/_ — 本仓库](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-job/src/main/java/org/dromara/job/snailjob/)
  模块第一现场。8 个 demo 任务类覆盖了 SnailJob 的 6 种核心任务模式。任何「这个模式到底怎么写」的问题，最终答案在这里。
- [配置: _application-dev.yml snail-job 段_ — 本仓库](RuoYi-Vue-Plus/ruoyi-admin/src/main/resources/application-dev.yml)
  客户端连接 SnailJob 服务端的所有配置项：enabled/group/token/server/namespace/port/host。理解「客户端如何找到服务端」时查阅。
- [代码: _SnailJobConfig.java_ — 本仓库](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-job/src/main/java/org/dromara/common/job/config/SnailJobConfig.java)
  自动装配入口。理解 `@EnableSnailJob` + `SnailClientStartingEvent` + `SnailLogbackAppender` 远程日志挂载时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「SnailJob 版本升级兼容性」「客户端连不上服务端怎么排查」等集成问题时，Issues 和讨论区是最贴近维护者意图的反馈源。
- [社区: _SnailJob 官方 Issue / 讨论_](https://github.com/aizuda/snail-job/issues)
  SnailJob 框架本身的问题、feature request、最佳实践讨论。遇到「广播任务在某些条件下不执行」「MapReduce 结果丢失」等框架行为问题时查阅。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + SnailJob 官方文档 + 掘金教程文章支撑。
- SnailJob 服务端部署文档位于其官方文档站点，本课程仅交叉引用，不纳入讲解范围（与 Out of scope 一致）。

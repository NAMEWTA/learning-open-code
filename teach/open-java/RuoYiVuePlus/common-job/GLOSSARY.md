# ruoyi-common-job 定时任务模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**SnailJob**：
Aizuda 社区出品的开源分布式任务调度与重试框架。采用「服务端（Server）+ 客户端（Client）」架构：Server 负责任务的持久化、调度、分发和监控；Client 嵌入业务应用，接收调度指令并执行任务。`ruoyi-common-job` 封装了 Client 侧的自动接入逻辑。
_Avoid_: 「Spring 定时任务」（Spring 的 `@Scheduled` 是单机本地调度，SnailJob 是分布式调度平台）。

**SnailJobConfig**：
`ruoyi-common-job` 模块唯一的 Java 类（`org.dromara.common.job.config.SnailJobConfig`），仅 43 行。用 `@AutoConfiguration` + `@ConditionalOnProperty` + `@EnableScheduling` + `@EnableSnailJob` 四个注解完成 SnailJob 客户端的自动接入，并用 `@EventListener(SnailClientStartingEvent.class)` 挂载远程日志 Appender。
_Avoid_: 「SnailJob 客户端配置」（它是自动装配入口，不是手动配置类）。

**@EnableSnailJob**：
SnailJob 客户端 starter 提供的开关注解（`com.aizuda.snailjob.client.starter.EnableSnailJob`）。标注在任意 `@Configuration` 类上，触发 SnailJob 客户端的全部自动装配——包括连接服务端、注册任务执行器、接收调度指令。`SnailJobConfig` 把它和 Spring Boot 的 `@AutoConfiguration` 合在一起，实现「依赖即生效」。
_Avoid_: 「启用 SnailJob 功能开关」（它是框架级注解，不仅是开关）。

**@ConditionalOnProperty**：
Spring Boot 条件装配注解。`SnailJobConfig` 使用 `@ConditionalOnProperty(prefix = "snail-job", name = "enabled", havingValue = "true")` 实现：只有配置文件中 `snail-job.enabled=true` 时，整个配置类才生效。这使得 SnailJob 客户端可以通过配置文件一键开关，不需要改代码。
_Avoid_: 「条件判断」（它是 Spring Boot 自动装配级别的条件控制，不是业务 if-else）。

**SnailLogbackAppender**：
SnailJob 提供的 Logback 日志追加器（`com.aizuda.snailjob.client.common.appender.SnailLogbackAppender`）。挂载到 Logback 的根 Logger 上后，任务执行过程中的所有日志会自动回传到 SnailJob 服务端，在服务端控制台即可查看任务运行日志，无需登录每台机器。
_Avoid_: 「日志收集器」（它是 Logback Appender 的具体实现，不是独立的日志系统）。

**SnailClientStartingEvent**：
SnailJob 客户端启动时发布的事件（`com.aizuda.snailjob.client.common.event.SnailClientStartingEvent`），在客户端完成初始化、准备连接服务端之前触发。`SnailJobConfig.onStarting()` 通过 `@EventListener` 监听此事件，在其回调中挂载远程日志 Appender，确保日志上报在调度开始前就绪。
_Avoid_: 「客户端启动回调」（它是 Spring 事件，不是回调接口）。

**@JobExecutor**：
SnailJob 客户端提供的注解（`com.aizuda.snailjob.client.job.core.annotation.JobExecutor`），标注在任务类上，`name` 属性指定任务名称。SnailJob 服务端按此名称调度任务，客户端根据名称找到对应的 Bean 和方法执行。方法是约定名 `jobExecute(JobArgs)`，返回 `ExecuteResult`。
_Avoid_: 「任务调度器」（它标记的是任务执行器，不是调度器本身）。

**JobArgs**：
SnailJob 任务执行参数 DTO。携带任务参数（`getJobParams()`）、工作流上下文（`getWfContext()`）、分片参数（`getShardingArgs()`）等信息。由 SnailJob 客户端在执行任务时自动组装并传入 `jobExecute()` 方法。
_Avoid_: 「任务输入参数」（它是 SnailJob 框架定义的参数对象，不是普通的 String/Map）。

**ExecuteResult**：
SnailJob 任务执行结果封装。`ExecuteResult.success(data)` 报告成功及可选数据；`ExecuteResult.failure(msg)` 报告失败及原因。SnailJob 客户端根据返回结果更新任务状态和日志，服务端控制台据此展示执行记录。
_Avoid_: 「返回值」（它是框架定义的结果封装，不是普通返回值）。

**SnailJobLog**：
SnailJob 客户端日志工具类。`SnailJobLog.LOCAL` 输出到本地日志文件；`SnailJobLog.REMOTE` 输出到本地同时回传 SnailJob 服务端。任务中使用 `REMOTE` 可以让运维在服务端控制台直接看到任务运行详情，是分布式排查的关键工具。
_Avoid_: 「日志记录器」（它是 SnailJob 特殊定制的双通道日志工具，不是 Slf4j Logger）。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

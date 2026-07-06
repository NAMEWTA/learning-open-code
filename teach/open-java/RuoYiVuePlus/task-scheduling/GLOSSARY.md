# ruoyi-job 任务调度模块 Glossary

记录学习者在 7 节课程中**真正理解**的核心术语。覆盖 SnailJob 基础、6 种任务模式、DAG 工作流三大块。

## Terms

**SnailJob**：
由爱组搭（aizuda）开源的企业级分布式任务调度与重试平台。RuoYi-Vue-Plus 使用它的客户端 SDK（`snail-job-client-starter` + `snail-job-client-job-core`），通过 `@EnableSnailJob` 启动客户端，向独立部署的 SnailJob 服务端注册任务并等待调度。
_Avoid_: 「XXL-JOB」（同类产品，但 SnailJob 提供了 MapReduce 和 DAG 工作流等差异化能力）。

**@JobExecutor**：
SnailJob 的注解式任务注册方式。贴在 Spring Bean 类上，`name` 属性指定任务名。客户端启动时会扫描所有 `@JobExecutor`，把 name → 类映射注册到 SnailJob 服务端。任务触发时，框架通过反射调用类中的 `jobExecute(JobArgs)` 方法。
_Avoid_: 「@Scheduled」（Spring 原生定时注解，和 SnailJob 调度是两个体系，`@EnableScheduling` 只是开启线程池）。

**AbstractJobExecutor**：
SnailJob 提供的任务执行器抽象基类。继承它并重写 `doJobExecute(JobArgs)` 即可定义类式任务。相比注解式，继承式需要在 SnailJob 后台手动创建任务并指定全限定类名，但可以在基类中统一处理异常、日志、钩子等横切关注点。

**JobArgs**：
任务执行参数对象，由 SnailJob 框架注入到 `jobExecute` 方法中。携带三类信息：① `getJobParams()` 服务端配置的静态任务参数；② `getWfContext()`/`appendContext()` DAG 工作流上下文的读写；③ `getTaskBatchId()`/`getJobId()` 本次执行的元信息。

**ExecuteResult**：
任务执行结果对象。三个工厂方法：`success()` 成功、`success(obj)` 成功并携带返回数据、`failure()`/`failure("原因")` 失败。若 `jobExecute` 抛出未捕获异常，框架会自动捕获并标记为失败（可能触发重试）。

**SnailJobLog.LOCAL / REMOTE**：
SnailJob 的双通道日志。`LOCAL` 写本地日志文件（同普通 `log.info()`）；`REMOTE` 通过 `SnailLogbackAppender` 上报到 SnailJob 服务端，在后管「调度日志」面板可见。推荐两种都写。

**SnailLogbackAppender**：
Logback 的追加器实现。在 `SnailClientStartingEvent` 事件中挂载到 Root Logger，将日志实时异步推送到 SnailJob 服务端。`SnailJobLog.REMOTE` 的底层就是它。

**@EnableSnailJob**：
SnailJob 客户端启动注解，贴在配置类上。作用：扫描所有 `@JobExecutor` 并注册到服务端、初始化客户端通信通道、开启任务调度监听。在 `SnailJobConfig` 上与 `@EnableScheduling` 配合使用。

**@ConditionalOnProperty**：
Spring Boot 条件装配注解。`SnailJobConfig` 用它实现 `snail-job.enabled=true` 的总开关——为 false 时整个配置类不加载，SnailJob 客户端完全不启动。这是开发环境省资源的机制。
_Avoid_: 「开关」（泛称，Spring 语境下特指条件装配）。

**广播任务**：
SnailJob 的一种路由策略：任务触发时，所有在线客户端实例各自执行一次（而非随机挑一个）。适用场景：各实例清自己的本地缓存、刷新自己的配置、上报自己的 JVM 指标。不适用：有全局副作用的操作（如发全员邮件——会重复发送）。
_Avoid_: 「群发任务」（广播的核心是「每个实例都需要做的事」，不是「向外部群发消息」）。

**静态分片**：
分片规则由服务端预先定义（在后台任务配置中填写每个分片的 jobParams 参数）。调度时服务端将各分片参数下发给集群中的执行器，各执行器按参数范围独立处理。特点是分片数固定、改规则要改后台配置。

**Map 任务（动态分片）**：
分片规则由客户端代码在运行时动态决定。根 Map 方法（`@MapExecutor` 不带 taskName）拆分数据后，通过 `MapHandler.doMap(list, taskName)` 把子任务提交到 SnailJob 队列。子 Map 方法（`@MapExecutor(taskName="xxx")`）各处理一片数据，结果独立返回，不汇总。

**MapHandler**：
Map 任务的子任务分发器。由 SnailJob 框架注入到根 Map 方法中。核心方法 `doMap(List<?> list, String taskName)` 将数据列表拆分成多个子任务并提交到集群队列。分发是异步的——doMap 返回时子任务可能还在排队。

**@MapExecutor**：
Map/MapReduce 任务的注解。不带 `taskName` 时标识根 Map 方法（拆分数据 + 调用 MapHandler 分发），带 `taskName` 时标识子 Map 方法（处理一片数据）。一个类只能有一个无 taskName 的根 Map。

**MapReduce 任务**：
在 Map 任务基础上增加 `@ReduceExecutor` 汇总阶段。所有子 Map 任务执行完毕后，Reduce 方法通过 `reduceArgs.getMapResult()` 收集所有子任务返回值，做最终聚合。所有子任务成功才触发 Reduce（屏障语义）。

**@ReduceExecutor**：
MapReduce 任务的汇总阶段注解。贴在 Reduce 方法上，方法签名 `ExecuteResult reduce(ReduceArgs)`。在所有子 Map 成功后自动被调用，不是手动调用的。

**ReduceArgs**：
Reduce 阶段的参数对象。核心方法 `getMapResult()` 返回所有子 Map 返回值的 List。注意框架序列化可能导致类型变更（如 int → String），需手动转换。

**屏障（Barrier）**：
MapReduce 的隐式同步点：Reduce 方法只在所有子 Map 任务全部成功后才会被触发。任一子任务失败则 Reduce 不执行，整批任务标记为失败。这是分布式计算中「所有前置任务完成后才继续」的经典模式。

**DAG 工作流**：
有向无环图（Directed Acyclic Graph）工作流。将多个任务节点编排成依赖图——无依赖的节点可并行执行，有依赖的节点等待上游完成后执行。在 SnailJob 后台可视化编排拓扑，节点间通过 `wfContext` 传递数据。
_Avoid_: 「流水线」（Pipeline，线性串联；DAG 支持分支和汇聚，拓扑更灵活）。

**wfContext（工作流上下文）**：
DAG 工作流中各节点共享的 `Map<String, Object>`。上游节点通过 `jobArgs.appendContext("key", value)` 写入，下游节点通过 `jobArgs.getWfContext("key")` 读取。数据仅在当前工作流实例内有效，工作流结束后销毁。传递复杂对象时使用 JSON 序列化。
_Avoid_: 「全局变量」（有明确的生命周期和隔离边界，不同于无限制的全局变量）。

**BillDTO**：
本模块 DAG 工作流 demo 的数据传输对象（Java Record）。包含 `billId`、`billChannel`（渠道）、`billDate`（日期）、`billAmount`（金额）四个字段。在微信→汇总和支付宝→汇总两条路径上作为数据契约流通。

**命名空间（namespace）**：
SnailJob 的环境隔离机制。配置 `snail-job.namespace: ${spring.profiles.active}` 使 dev/prod 环境的任务互不可见。客户端只向匹配的 namespace 注册任务，服务端也只向匹配的 namespace 下发调度。

**组（group）**：
SnailJob 的二级隔离单位（命名空间 → 组 → 任务）。客户端配置 `snail-job.group` 指定自己属于哪个组，服务端将任务分配给对应组的客户端实例。组的创建在 SnailJob 后台管理完成。

**自动装配（AutoConfiguration.imports）**：
Spring Boot 3.x 的自动装配入口文件。`ruoyi-common-job` 的 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` 中列出了 `SnailJobConfig`，使得引入该依赖即可自动装配 SnailJob 全部能力。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

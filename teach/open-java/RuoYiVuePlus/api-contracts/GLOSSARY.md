# ruoyi-api 模块 Glossary

记录学习者在课程中**真正理解**的核心术语。覆盖依赖倒置、SPI 契约、事件解耦三大块。

## Terms

**依赖倒置原则（DIP）**：
高层模块不应依赖低层模块，两者都应依赖抽象。在 RuoYi 中的具体体现：`common-translation` 不依赖 `ruoyi-system`，两者都依赖 `ruoyi-api` 中的 `UserService` 接口。运行时的实现绑定由 Spring DI 完成。
_Avoid_: 「解耦」（太泛，不说明是编译时还是运行时解耦）。

**SPI（Service Provider Interface）**：
本项目中指 `ruoyi-api` 里的服务接口——定义方只提供接口签名，实现方在各自模块提供具体逻辑。与 Java SPI（`META-INF/services`）机制不同，这里是纯 Spring Bean 注入，不需要配置文件。
_Avoid_: 「Java SPI」（容易与本项目实际使用的 Spring DI 方式混淆）。

**契约层（Contract Layer）**：
`ruoyi-api` 的角色称谓——它是模块间通信的「宪法」，规定「你可以调什么方法、传什么参数、拿回什么类型」，但不规定「怎么做」。包含接口（行为契约）、DTO/模型（数据契约）、事件（通知契约）三种形态。

**接口隔离（Interface Segregation）**：
一个类同时实现多个接口，不同消费者按需注入不同接口类型。如 `SysUserServiceImpl implements ISysUserService, UserService`——内部增删改查走 `ISysUserService`，外部查询走 `UserService`。通过接口类型天然约束了调用权限。
_Avoid_: 「多接口实现」（不传达「不同消费者看到不同接口」的设计意图）。

**DTO（Data Transfer Object）**：
在 `ruoyi-api` 中，DTO 是独立于 Entity 的纯数据传输对象。它只包含跨模块传输需要的字段，不含 ORM 注解、不含敏感字段（如 password）、不含内部标记（如 delFlag）。数据库表结构变更时，只要 DTO 不变，消费者不受影响。

**Java record**：
Java 14 引入的不可变数据类。`StartProcessReturnDTO` 和 `FlowCopyDTO` 使用 record，继承 `java.lang.Record`（而非 `Serializable`）。选择条件：字段不可变 + 纯数据载体 + 不需要 setter/Jackson 反序列化。
_Avoid_: 「DTO」（record 是不变 DTO 的子集，不能互换）。

**Spring ApplicationEvent**：
Spring 框架内置的观察者模式实现。`FlowProcessEventHandler` 通过 `SpringUtils.context().publishEvent()` 发布事件，业务模块通过 `@EventListener` 订阅。事件类定义在 ruoyi-api 中，使发布方和订阅方都只依赖 api 模块。

**@EventListener condition**：
Spring 事件监听的 SpEL 过滤表达式。如 `condition = "#processEvent.flowCode.startsWith('leave')"`。运行时 Spring 先求值再决定是否调用方法。用于让业务模块只处理自己关心的流程事件，避免无关事件触发业务逻辑。

**FlowProcessEventHandler**：
工作流事件的唯一发布枢纽（在 workflow 模块）。将 WarmFlow 引擎的 `Instance`/`Task` 对象转换为 ruoyi-api 的通用事件对象后发布。它是流程引擎内部数据与业务模块可见数据之间的翻译层。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

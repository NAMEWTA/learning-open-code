# 设计模式与架构设计 — 术语表

> 本术语表收录课程中涉及的所有设计模式、架构概念和工程术语。每个术语的释义都基于 RuoYi-Vue-Plus 项目中的实际应用场景。

## 设计模式

### GoF 创建型模式

- **工厂模式 (Factory Pattern)** — 将对象创建逻辑封装在工厂类/方法中，调用方无需知道具体构造细节。本项目实例：`OssFactory` 负责创建和管理 S3 客户端实例，`EncryptorManager` 通过反射创建加密器，Spring `@Bean` 方法声明式创建 Bean。`_Avoid_` 与「简单工厂」混淆——本项目的工厂基本都包含缓存和配置感知逻辑，远超简单工厂的范畴。

- **构建者模式 (Builder Pattern)** — 将复杂对象的构建过程与表示分离，通过链式调用逐步设置参数。本项目实例：`Options.builder()` 流畅构建 OSS 上传选项，`QueryBuilder` 和 `LambdaQueryBuilder` 提供类型安全的 SQL 查询构建，Lombok `@Builder` 和 `@Accessors(chain=true)` 是轻量级替代。`_Avoid_` 与「setter 链式调用」混淆——真正的构建者模式在 `build()` 时可以做完整性校验。

- **单例模式 (Singleton Pattern)** — 保证全局只有一个实例。本项目实例：Spring 容器管理的所有 `@Service`/`@Component` Bean 默认是单例，`OssFactory` 内部的静态 `ConcurrentHashMap` 缓存，前端 Axios 实例 (`service`) 是模块级单例，`isRelogin` 标志防止重复弹窗。`_Avoid_` 在单例 Bean 中添加实例级可变字段（线程安全问题）。

### GoF 结构型模式

- **适配器模式 (Adapter Pattern)** — 将一个接口转换为另一个接口，使不兼容的类能协作。本项目实例：`CaffeineCacheDecorator` 将 Caffeine 的 `Cache<K,V>` API 适配为 Spring 的 `Cache` 接口，`PlusSpringCacheManager` 将 Redisson `RMap` 适配为 Spring `CacheManager`。

- **装饰器模式 (Decorator Pattern)** — 在不修改原对象的前提下，动态添加新功能。本项目实例：`CaffeineCacheDecorator` 为 Redis L2 缓存包裹 Caffeine L1 层，`XssHttpServletRequestWrapper` 为请求参数添加 XSS 过滤，`RepeatedlyRequestWrapper` 使请求体可多次读取，`DecryptRequestBodyWrapper` / `EncryptResponseBodyWrapper` 添加加解密能力。

- **外观模式 (Facade Pattern)** — 为子系统提供统一高层接口，降低使用复杂度。本项目实例：ruoyi-api 的 `UserService` 等接口为外部模块提供简化的系统服务调用入口，`EncryptorManager` 将多算法加密子系统收敛为 `encrypt()/decrypt()` 两个方法，前端 `$modal` 插件统一 Element Plus 的多套消息 API。

- **组合模式 (Composite Pattern)** — 将对象组织成树结构，使客户端能统一处理单个对象和组合对象。本项目实例：`TreeBuildUtils` 提供通用的树结构构建能力，`SysMenuServiceImpl` 构建菜单树，`SysDeptServiceImpl` 构建部门树，前端 `SidebarItem` 组件递归渲染菜单树。

- **代理模式 (Proxy Pattern)** — 为另一个对象提供替身以控制访问。本项目实例：Spring AOP 切面体系 (`LogAspect`、`RateLimiterAspect`、`RepeatSubmitAspect`) 通过动态代理拦截方法调用，MyBatis 插件 (`PlusDataPermissionInterceptor` 等) 代理 SQL 执行过程。

### GoF 行为型模式

- **策略模式 (Strategy Pattern)** — 定义一系列算法，使其可以互相替换。本项目实例：`IAuthStrategy` 接口 + 5 个 `@Service` 实现（Password、Sms、Email、Social、Xcx）通过 grantType 动态路由，`SensitiveStrategy` 枚举用 lambda 函数定义 17 种脱敏规则，前端 `useTableSelection` 接受 `getRowId` 策略函数。

- **模板方法模式 (Template Method Pattern)** — 在父类中定义算法骨架，子类重写特定步骤。本项目实例：`AbstractOssClientImpl.initialize()` 是模板方法，调用子类的 `doInitialize()`，`AbstractEncryptor` 在构造器中完成配置校验后由子类实现具体的加解密逻辑。

- **观察者模式 (Observer Pattern)** — 定义一对多依赖，当对象状态变化时自动通知依赖者。本项目实例：Spring Events 体系——`OperLogEvent`（操作日志）、`LoginInfoEvent`（登录记录）、`UserLoginSuccessEvent`（登录成功）通过 `@EventListener` + `@Async` 异步处理，前端 Vue 3 的 `watch`/`watchEffect`/`computed` 是响应式观察者。

- **责任链模式 (Chain of Responsibility)** — 将请求沿处理链传递，每个处理器决定处理或传递。本项目实例：Servlet Filter 三层链 (CryptoFilter → RepeatableFilter → XssFilter)，Spring Interceptor 链，MyBatis Plugin 四层链（数据权限 → SQL 日志 → 加密 → 解密），前端 Axios 请求/响应拦截器链。

- **命令模式 (Command Pattern)** — 将请求封装为对象，解耦调用者和执行者。本项目实例：SnailJob 的 6 种任务执行器（注解/类/广播/静态分片/Map/MapReduce），Warm-Flow 工作流任务命令（完成/委派/转办/加签/减签）。

- **状态模式 (State Pattern)** — 对象行为随内部状态变化。本项目实例：`SensitiveStrategy` 枚举携带行为（Function<String,String> desensitizer），`UserStatus`、`TaskStatusEnum`、`BusinessStatus` 等状态枚举控制业务流转。

## 架构模式

- **分层架构 (Layered Architecture)** — 将系统划分为水平层次，上层依赖下层。本项目采用 5 层架构：Layer 0 (基础设施基础) → Layer 1 (基础设施能力) → Layer 2 (横切组装) → Layer 3 (业务模块) → Layer 4 (API 合约) → Layer 5 (启动入口)。

- **依赖注入 (Dependency Injection / IoC)** — 将对象的依赖创建和管理交给容器，而非对象自身。本项目统一使用构造器注入（Lombok `@RequiredArgsConstructor`），避免了字段注入的不可变性问题和循环依赖隐患。

- **依赖倒置 (Dependency Inversion)** — 高层模块不应依赖低层模块，两者都应依赖抽象。本项目通过 ruoyi-api 合约层实现：业务模块依赖 API 接口而非彼此的实现类，运行时由 Spring 容器注入实现。

- **多级缓存 (Multi-level Cache)** — 使用多层缓存加速数据访问。本项目采用 Caffeine L1（本地，纳秒级）+ Redis L2（分布式，毫秒级）架构，`TransactionAwareCacheDecorator` 保证事务一致性。

- **事件驱动架构 (Event-Driven Architecture)** — 通过事件消息实现组件间的松耦合通信。本项目使用 Spring `ApplicationEvent` + `@EventListener` + `@Async` 实现登录事件、操作日志、工作流事件的异步处理。

- **自动配置 (Auto-Configuration)** — Spring Boot 的 SPI 机制，通过 `AutoConfiguration.imports` 文件声明配置类，实现按条件自动装配。本项目所有 common 模块都通过此机制注册。

- **模块化架构 (Modular Architecture)** — 将系统拆分为独立模块，每个模块有明确的职责边界。本项目 22 个 common 模块按 7 大功能组（基础/持久化/安全/数据/集成/新兴/社交调度）组织，6 个业务模块通过 API 合约层通信。

- **Repository/仓储模式** — 将数据访问逻辑封装在专门的仓储层中。项目使用 MyBatis-Plus 的 `BaseMapper` 作为仓储基类，`BaseMapperPlus` 提供自动 Entity→VO 映射。

## 工程规范

- **R&lt;T&gt;** — 统一响应包装类，位于 `ruoyi-common-core/.../domain/R.java`，字段为 `code` + `msg` + `data`。替代了旧版 RuoYi 的 AjaxResult。

- **PageResult&lt;T&gt;** — 分页响应包装类，字段为 `total` + `rows`。替代了旧版 RuoYi 的 TableDataInfo。

- **BaseException** — i18n 感知的异常基类，使用 `module + code + args` 模式从消息资源文件中解析国际化错误消息。

- **ServiceException** — final 类运行时异常，带 code + message + detailMessage，支持 StrFormatter 格式化。是业务逻辑中最常用的异常类型。

- **@AutoConfiguration** — Spring Boot 3.x/4.x 的自动配置注解，替代旧版 `@Configuration` + `spring.factories`。本项目所有 common 模块的配置类均使用此注解。

- **AutoConfiguration.imports** — 位于 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`，是 Spring Boot 3.x/4.x 的 SPI 文件格式，替代旧版 `spring.factories`。

- **@RequiredArgsConstructor** — Lombok 注解，为 `final` 字段生成构造器。本项目统一使用此注解实现构造器注入，避免字段注入。

- **Validation Group** — 校验分组接口 (`AddGroup`、`EditGroup`、`QueryGroup`)，配合 Bean Validation 实现不同场景的差异化校验。

- **YmlPropertySourceFactory** — 自定义 `PropertySourceFactory`，使 `@PropertySource` 注解能加载 YAML 文件（Spring 原生只支持 `.properties`）。

## 前端模式

- **Composable (组合式函数)** — Vue 3 Composition API 的代码复用单元，遵循 `useXxx` 命名约定。本项目 9 个 composable 按功能域组织在 `hooks/` 目录下。

- **Setup Store** — Pinia 的函数式 Store 语法（与 Options Store 相对），使用 `ref`/`reactive`/`computed` 等 Composition API 定义状态。本项目 7 个 Pinia Store 全部使用 Setup Store 语法。

- **AxiosPromise&lt;T&gt;** — 项目自定义的 Promise 类型包装，匹配 `{ code, msg, data }` 响应形状而非原始 axios 响应。

- **RSA+AES 混合加密** — 前端加密策略：RSA 加密 AES 密钥（慢但安全），AES 加密业务数据（快但需要共享密钥）。通过 `VITE_APP_ENCRYPT` 环境变量和 `isEncrypt` 请求头双层控制。

- **动态路由 (Dynamic Routes)** — 后端菜单数据在运行时编译为 Vue Router 路由记录。核心流程：`getRouters()` API → `filterAsyncRouter()` 递归转换 → `router.addRoute()` 注册。

- **Vite Glob Import** — `import.meta.glob()` 在编译时构建所有视图文件的静态映射表，运行时通过路径字符串查找对应的懒加载函数。是前端动态路由的视图解析基础。

## 收录规则

- 收录标准：在本课程中首次被讲解、且在 RuoYi-Vue-Plus 源码中有明确对应实现的术语。
- 不收录 Spring Boot/Vue 3 框架本身的通用术语（如 `@RestController`、`v-model`），除非项目有特殊的封装或使用方式。
- `_Avoid_` 标注：指出该术语最容易与什么概念混淆，帮助学习者避免理解偏差。

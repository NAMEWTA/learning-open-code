> **服务工作流：** `../T-teach/T-teach.md`
> **产物文件名：** `mission.md`
> **父目录规则：** 本模板产物写入 `YYYY-MM-DD-<kebab-name>/` change 目录内

# Mission: RuoYi-Vue-Plus 设计模式、架构设计与工程规范

## Why

RuoYi-Vue-Plus 是一个生产级、企业级 Java + Vue 全栈后台管理系统，代码量超过 20 万行、横跨 30+ Maven 模块和 50+ 前端 API 域。它不仅仅是「能跑起来的 CRUD 脚手架」——它是 **17 种 GoF 设计模式 + 18 种前端架构模式 + 严谨的工程规范体系** 的真实落地案例。

大多数开发者学习设计模式时面临的核心困境是：看懂了教科书上的 UML 图，但不知道在真实项目中长什么样、怎么组合、何时该用、何时不该用。本课程的目标就是把 RuoYi-Vue-Plus 当作一个 **设计模式实战博物馆**，带你逐一解剖每个模式在真实代码中的形态、解决的问题、与其他模式的关系，以及背后的架构决策。

完成本课程后，你将不再仅仅会「用 Spring Boot 写接口」，而是能够：
- 看懂一个大型项目的架构骨架，理解模块拆分的商业逻辑；
- 在自己的项目中主动、恰当地应用设计模式，而非生搬硬套；
- 按照企业级工程规范组织代码，让团队协作不再混乱；
- 识别反模式和过度设计，在简洁与扩展之间找到平衡。

## Success looks like

- **设计模式识别**：打开 ruoyi-admin 的 `IAuthStrategy`，能立刻认出这是「策略模式」并且口述其核心结构：策略接口 → 5 个具体策略类 → 接口上的静态工厂方法通过 grantType 动态路由。能举一反三，在 `SensitiveStrategy` 枚举、`CellMergeStrategy`、前端 `useTableSelection` 等位置认出同样的模式思想。
- **架构设计推理**：能画出 RuoYi-Vue-Plus 的 5 层依赖架构图（Infrastructure Base → Infrastructure Capabilities → Cross-cutting Assembly → Business Modules → Entry Point），解释为什么 ruoyi-api 只依赖 ruoyi-common-core、为什么 ruoyi-admin 不直接依赖各个 common 模块而是通过传递依赖引入、为什么加密模块要同时提供 MyBatis 拦截器和 Servlet Filter 两条通道。
- **模式组合理解**：能分析「数据权限」功能中同时用到了哪几种模式（AOP 代理 + MyBatis 拦截器责任链 + SpEL 模板策略 + 工厂模式 + 装饰器模式），并解释它们为什么需要协同工作。
- **规范落地能力**：能按照项目规范新增一个业务模块——正确的包结构、统一的 R/PageResult 响应格式、BaseEntity 继承、validation group 分组校验、`@AutoConfiguration` 注册、`AutoConfiguration.imports` SPI 文件、异常通过 GlobalExceptionHandler 统一处理。
- **前端架构思维**：能解释 Vue 3 前端的 7 层架构（组件 → 组合式函数 → 状态管理 → API 仓库层 → 拦截器中间件 → 路由守卫 → 指令权限），以及为什么 Axios 拦截器使用 RSA+AES 混合加密而非单一加密方案。
- **反模式识别**：能指出项目中故意使用 Service Locator（`SpringUtils`）的场景并解释权衡——为什么在策略工厂中通过 bean 名称动态查找比注入所有策略实现更合适。

## Constraints

- 要求已有至少一个 Spring Boot 项目的开发经验，理解 `@Service`、`@Component`、`@Configuration`、依赖注入等基本概念。
- 要求了解 GoF 23 种设计模式的基本定义（不需要精通，但至少知道策略模式、工厂模式、代理模式这些名词）。
- 要求对 Vue 3 Composition API 有基本了解（前端部分的模式分析使用 Vue 3 代码示例）。
- 不要求预先读过 RuoYi-Vue-Plus 源码——本课程会逐文件引导阅读。
- 建议按顺序学习：创建型模式 → 结构型模式 → 行为型模式 → 架构模式 → 前端模式 → 工程规范，后续课程会引用前面已讲过的知识。

## Out of scope

- GoF 23 种设计模式的基础定义和教科书示例（只做简要回顾，重点放在项目实战）。
- Spring Boot / MyBatis-Plus / Vue 3 等框架的入门教学（已有对应课程覆盖）。
- 具体业务逻辑的深度讲解（用户管理、角色管理、工作流等，已有独立的 ruoyi-system、ruoyi-workflow 等课程）。
- 部署运维、CI/CD、容器化等 DevOps 话题。
- 数据库设计、SQL 优化、索引策略等 DBA 话题。
- React 前端的设计模式（已有独立的 ruoyi-react 课程）。

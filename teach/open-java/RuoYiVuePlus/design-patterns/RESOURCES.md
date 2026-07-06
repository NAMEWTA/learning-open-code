> **服务工作流：** `../T-teach/T-teach.md`
> **产物文件名：** `resources.md`
> **父目录规则：** 本模板产物写入 `YYYY-MM-DD-<kebab-name>/` change 目录内

# 设计模式、架构设计与工程规范 Resources

## Knowledge

### 一手资料：项目源码（最高信任度）

- **RuoYi-Vue-Plus 后端源码** — `RuoYi-Vue-Plus/` 目录
  - **ruoyi-admin/** — 启动入口与认证策略（策略模式、观察者模式、Spring 事件）
  - **ruoyi-common/** — 22 个基础设施模块（工厂、装饰器、适配器、代理、责任链等模式的集中营）
  - **ruoyi-api/** — API 合约层（外观模式、依赖倒置）
  - **ruoyi-modules/** — 6 个业务模块（分层架构、模板方法、组合模式）
  - **ruoyi-extend/** — 3 个外部服务包装器

- **plus-ui-vue 前端源码** — `plus-ui-vue/src/` 目录
  - **hooks/** — 9 个组合式函数（组合模式、策略模式思想）
  - **store/modules/** — 7 个 Pinia store（单例模式、观察者模式）
  - **utils/request.ts** — Axios 拦截器链（责任链模式、加密策略模式）
  - **plugins/** — 6 个 Vue 插件（门面模式）
  - **api/** — 55+ API 文件（仓储模式）

- **已有教学课程** — `speculo/.speculo/doc/` 目录
  - 已有 200+ 节 HTML 课程覆盖各模块，本课程会链向相关课程的深度讲解

### 设计模式理论参考

- [Refactoring.Guru — Design Patterns](https://refactoring.guru/design-patterns)
  - **覆盖内容**：GoF 23 种设计模式的完整目录，含 UML 图、伪代码示例、各语言实现。是本课程的理论对照参考——每当我们分析项目中的一个模式实例时，可对照此站的标准定义来理解「标准模式」与「实战变体」的差异。
  - **何时取用**：学习每节设计模式课程前，如果你对某个模式的定义已经模糊，先花 2 分钟浏览对应模式的标准定义，再回来看项目实战。

- [Baeldung — Design Patterns in Java](https://www.baeldung.com/java-design-patterns-series)
  - **覆盖内容**：Java 生态下各设计模式的实现教程，侧重 Spring Boot 集成。包括策略模式 + Spring DI、观察者模式 + @EventListener、工厂模式 + @Bean 等。
  - **何时取用**：当你想看「教科书式 Java 实现」与本项目「生产级实战实现」的差异对比时。

### 架构设计参考

- [Spring Boot Reference — Auto-configuration](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  - **覆盖内容**：Spring Boot 3.x/4.x 的自动配置机制，`@AutoConfiguration`、`AutoConfiguration.imports` 文件格式、条件注解。直接对应 common 模块的配置注册模式。
  - **何时取用**：学习第 21 节（配置管理与自动装配）之前必读。

- [MyBatis-Plus 官方文档 — 插件机制](https://baomidou.com/guides/plugin-system/)
  - **覆盖内容**：MyBatis 拦截器接口、`InnerInterceptor`、插件链的执行顺序。直接对应 PlusDataPermissionInterceptor、MybatisEncryptInterceptor 等实现。
  - **何时取用**：学习第 12 节（责任链模式）MyBatis 插件链部分时参考。

- [Sa-Token 官方文档 — 框架设计](https://sa-token.cc/doc.html#/frame/)
  - **覆盖内容**：Sa-Token 的架构设计、StpLogic 组件模型、DAO 抽象层、JWT 集成模式。对应 ruoyi-common-satoken 模块的设计。
  - **何时取用**：学习架构分层时理解认证框架如何被封装为可插拔的 common 模块。

### 前端架构参考

- [Vue 3 官方文档 — Composables](https://cn.vuejs.org/guide/reusability/composables.html)
  - **覆盖内容**：组合式函数的命名约定、状态管理、与 Pinia 的关系。直接对应 hooks/ 目录下的 9 个 composable。
  - **何时取用**：学习第 15 节（组合式函数与状态管理）之前必读。

- [Pinia 官方文档 — Setup Stores](https://pinia.vuejs.org/zh/core-concepts/#setup-stores)
  - **覆盖内容**：Setup Store 语法、与 Options Store 的对比、store 间互相引用。直接对应 store/modules/ 下的 7 个 Pinia store。
  - **何时取用**：学习第 15 节（状态管理）时配合阅读。

- [Axios 官方文档 — Interceptors](https://axios-http.com/docs/interceptors)
  - **覆盖内容**：请求/响应拦截器的注册与执行顺序。直接对应 utils/request.ts 中的拦截器链。
  - **何时取用**：学习第 16 节（中间件与拦截器链）之前必读。

## Wisdom (Communities)

- [Dromara 开源社区](https://gitee.com/dromara) — RuoYi-Vue-Plus 所属社区，包含项目 issue 讨论、PR 评审、版本发布
- [RuoYi-Vue-Plus 官方文档](https://gitee.com/dromara/RuoYi-Vue-Plus) — 项目 README、更新日志、框架集成说明
- [Vue 3 中文社区](https://cn.vuejs.org/community/) — Vue 生态的最佳实践讨论

## Gaps

- GoF 23 种设计模式的基础知识（UML 图、标准定义）不在本课程范围，仅做简要回顾。如果学习者需要系统补习设计模式基础，建议先通读 Refactoring.Guru 的目录。
- 本项目有少部分模式实例未覆盖（如 Memento 备忘录模式、Visitor 访问者模式），因为这些在 Java 企业开发中使用频率较低，本课程聚焦实战中高频出现的模式。
- 微服务架构模式（服务发现、配置中心、熔断降级等）不属于本项目范畴，因为 RuoYi-Vue-Plus 是单体多模块架构而非微服务架构。

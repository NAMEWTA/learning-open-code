# Mission: 读懂 RuoYi-Vue-Plus 的 Spring Boot Admin 监控模块

## Why
学习者要能完整理解 `ruoyi-monitor-admin` 模块如何基于 **Spring Boot Admin**（codecentric）构建集中式服务监控中心，掌握 SBA Server + Client 的协作原理、自注册监控模式、Spring Security 安全保护机制、以及自定义事件通知器的实现。学会这些后，你可以在自己的 Spring Boot 项目中搭建类似的监控体系，快速定位服务上下线、健康异常、配置变更等运行时问题，成为团队中能「一眼看清系统状态」的人。

## Success looks like
- 能用一段话讲清 `@EnableAdminServer` 注解如何将一个普通 Spring Boot 应用变成监控中心，以及 SBA Server（展示层）+ SBA Client（数据上报）+ Spring Boot Actuator（数据源）三者的协作关系。
- 能解释 `application.yml` 中 **自注册模式**的配置逻辑：monitor-admin 如何同时引入 `spring-boot-admin-starter-server` 和 `spring-boot-admin-starter-client`，通过 `spring.boot.admin.client.url` 指向自身实现自监控，以及 `instance.service-host-type: IP`、`metadata` 凭证传递的作用。
- 能逐行读懂 `SecurityConfig.java` 的安全过滤链：如何放行静态资源（`/assets/**`）和登录页、要求其余请求认证、配置表单登录 + HTTP Basic 双认证、禁用 CSRF 和 frameOptions 的原因。
- 能读懂 `CustomNotifier.java` 的事件驱动设计：继承 `AbstractEventNotifier`、通过 `doNotify()` 拦截 `InstanceStatusChangedEvent`、使用 Reactor `Mono.fromRunnable()` 异步处理、以及将 6 种 SBA 状态码（UP/OFFLINE/RESTRICTED/OUT_OF_SERVICE/DOWN/UNKNOWN）映射为中文业务语义的 switch 表达式。
- 能动手将另一个 Spring Boot 应用（如 ruoyi-admin）接入 SBA 监控：添加 client 依赖、配置 `spring.boot.admin.client.url`、暴露 Actuator 端点，并在 SBA 管理后台验证该应用出现在监控列表中。

## Constraints
- 学习者需具备 Spring Boot 基础（理解自动装配、application.yml 配置、starter 依赖机制）。
- 学习者需了解 Spring Security 基本概念（FilterChain、formLogin、authorizeHttpRequests）。
- 本模块为纯后端 Java，不涉及前端 UI 定制——SBA 自带的管理界面（Vue.js 构建）仅做功能演示，不深入其前端源码。
- 讲解全部基于本仓库真实代码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- SBA 的 UI 界面定制与品牌化（自定义 logo、样式、页面布局）——本课程关注后端配置与扩展，不涉及 SBA 前端源码。
- 告警通道集成（邮件、钉钉、企业微信、短信等通知方式）——CustomNotifier 仅演示日志记录模式，扩展为真实告警属于运维工程范畴。
- SBA Server 的集群部署与高可用架构——本模块为单实例部署，不涉及 Hazelcast 分布式存储或服务发现集成。
- Spring Boot Actuator 自定义端点和 HealthIndicator 的编写——仅在「SBA 从哪里拿数据」层面交叉引用，不深入 Actuator 扩展开发。
- 微服务（Cloud）版本中 SBA 通过 Nacos/Eureka 服务发现自动纳管所有实例的机制——本仓库为单体 admin 版本。
- Prometheus + Grafana 等外部监控体系的对接。

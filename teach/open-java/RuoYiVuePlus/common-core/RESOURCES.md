# ruoyi-common-core 核心基础模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-core 模块根路径_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-core/src/main/java/org/dromara/common/core/)
  一切关于「core 模块有哪些类、每个类做什么」的问题，最终答案在这 65 个 Java 文件里。核心包结构：`domain/`（响应体）、`constant/`（常量）、`enums/`（枚举）、`exception/`（异常体系）、`config/`（自动配置）、`utils/`（工具类）、`validate/`（自定义校验）、`xss/`（XSS 防护）、`factory/`（工厂类）、`service/`（服务接口）。

- [代码: _统一响应体 R.java_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-core/src/main/java/org/dromara/common/core/domain/R.java)
  整个项目所有 Controller 的统一返回信封。核心字段 code/msg/data，静态工厂 `ok()`/`fail()`/`warn()` 覆盖所有响应场景。课程 0001 的解剖对象。

- [代码: _分层异常体系_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-core/src/main/java/org/dromara/common/core/exception/)
  `base/BaseException.java`（国际化基类）→ `file/FileException.java`、`user/UserException.java`（模块分支），`ServiceException.java`、`SseException.java`（独立分支）。课程 0001 的解剖对象。

- [代码: _全局常量与枚举_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-core/src/main/java/org/dromara/common/core/constant/) 和 [enums/](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-core/src/main/java/org/dromara/common/core/enums/)
  6 个常量接口 + 7 个枚举类。`GlobalConstants` 定义 Redis key 前缀协议，`CacheNames` 编码缓存策略，`BusinessStatusEnum` 内置流程状态机。课程 0001 和 0005 的解剖对象。

- [代码: _核心工具类_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-core/src/main/java/org/dromara/common/core/utils/)
  18+ 工具类，覆盖字符串、日期、流操作、MapStruct 转换、Spring 容器、Servlet 请求、国际化消息、树构建、数据校验等。课程 0002 和 0003 的解剖对象。

- [官方文档: _Hutool 工具集_ — Dromara（hutool.cn）](https://hutool.cn/docs/)
  `StringUtils`、`DateUtils`、`StreamUtils`、`ObjectUtils` 等大量工具类封装了 Hutool 的方法。理解底层行为时查阅。

- [官方文档: _MapStruct 官方指南_（mapstruct.org）](https://mapstruct.org/documentation/stable/reference/html/)
  `MapstructUtils` 是对 MapStruct 的静态工具封装。理解编译期代码生成的原理和 `@Mapper` 注解时查阅。

- [官方文档: _Jakarta Bean Validation 规范_（beanvalidation.org）](https://beanvalidation.org/3.0/spec/)
  理解 `@Xss`、`@DictPattern`、`@EnumPattern` 如何自定义校验约束时查阅。课程 0004 涉及 ConstraintValidator 接口。

- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  `ApplicationConfig`、`ThreadPoolConfig`、`ValidatorConfig` 使用 `@AutoConfiguration` 实现零配置接入。课程 0006 的核心原理来源。

- [官方文档: _ip2region 离线 IP 地址库_ — Lion Li（gitee）](https://gitee.com/lionsoul/ip2region)
  `RegionUtils` 和 `AddressUtils` 基于 ip2region 实现离线 IP 地址解析。理解 xdb 文件的二分查找算法时查阅。课程 0007 涉及。

- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目整体设计说明，含核心模块、工具类、验证码等章节。理解模块在整体架构中的位置时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「这个工具类为什么这样封装」「某工具方法的最佳实践」时，Issues 与讨论区最贴近维护者意图。Hutool 和 RuoYi-Vue-Plus 同属 Dromara 社区，问题常能交叉解答。

- [社区: _Hutool Gitee Issues_](https://gitee.com/dromara/hutool)
  当需要理解 `StringUtils`、`DateUtils`、`StreamUtils` 等对 Hutool 的封装时，Hutool 社区提供了底层方法的行为说明。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + 上述官方文档支撑。
- `ip2region` 官方 xdb 文件生成和更新流程不是本课覆盖范围，仅涉及查询 API。

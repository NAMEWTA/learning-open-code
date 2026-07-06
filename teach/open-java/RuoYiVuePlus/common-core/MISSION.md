# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-core 核心基础模块

## Why
学习者要能彻底读懂 `ruoyi-common-core` 这个模块——它是整个 RuoYi-Vue-Plus 项目的**基石**：65 个 Java 文件，涵盖统一响应体 `R`、分层异常体系、全局常量与枚举、18+ 工具类、自定义校验注解和线程池配置。`ruoyi-common-redis`、`ruoyi-common-sms`、`ruoyi-common-oss`、`ruoyi-admin` 等所有子模块都直接或间接依赖它。理解这个模块，等于掌握了 RuoYi-Vue-Plus 的**技术骨架**和**编码规范**——从 Controller 如何返回统一 `R` 结果，到 Service 如何抛 `ServiceException` 被全局异常处理器兜底，再到枚举如何驱动业务逻辑、工具类如何封装常用操作、自定义校验注解如何增强 Bean Validation。达到能回答「为什么所有模块都依赖 core」「如何给项目加一个自定义校验注解」「怎么用 MapstructUtils 做对象转换」「枚举体系的设计模式是什么」的程度。重点是**读懂每一层的设计动机与真实调用路径**。

## Success looks like
- 能用一句话说清 `ruoyi-common-core` 的四大支柱：响应体（`R`/`PageResult`）、异常体系（`BaseException`/`ServiceException`）、常量与枚举、工具类集合，并说出该模块在项目依赖树中的位置。
- 能解释 `R<T>` 的统一响应设计：为什么只有 code/msg/data 三个字段，静态工厂方法 `ok()`/`fail()`/`warn()` 如何覆盖所有 API 返回场景。
- 能讲清异常体系的分层结构：`BaseException`（国际化）→ `FileException`/`UserException` 的分支设计，`ServiceException` 和 `SseException` 独立于该体系的理由。
- 能解释 `DeviceType`、`LoginType`、`UserStatus`、`BusinessStatusEnum` 等枚举是如何利用字段值 + 方法组合实现「数据驱动」的，而不是简单的标签。
- 能追踪自定义校验注解的完整链路：`@Xss` → `XssValidator`、`@DictPattern` → `DictPatternValidator`、`@EnumPattern` → `EnumPatternValidator` 如何融入 Jakarta Bean Validation 生命周期。
- 能讲清 `StringUtils`、`DateUtils`、`StreamUtils`、`MapstructUtils` 等核心工具类的设计思路和典型使用场景，以及它们封装了哪些第三方库（Hutool、MapStruct）。
- 能解释 `ServletUtils` 和 `SpringUtils` 如何桥接 Spring 容器与非 Spring 管理的代码，`MessageUtils` 如何通过动态 `MessageSource` 实现 i18n。
- 能讲清 `AddressUtils` 和 `RegionUtils` 如何基于 ip2region 库实现 IP 地址到地理位置的离线解析。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端架构和设计模式。
- 目标是「读懂」而非「从零复写」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路 / 手写小片段」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。
- 课程短小精悍（每课几分钟可完成），强调一手资料和 AI 追问。

## Out of scope
- core 模块以外的其他 common 模块（redis、sms、oss、mail 等）的具体实现细节——仅在与 core 模块交互时点到。
- 前端代码如何使用 `R` 响应体进行 axios 拦截处理——只在讨论 API 契约时提到。
- Spring Security / Sa-Token 的认证鉴权细节——那是 `ruoyi-framework` 模块的职责，本课只涉及 `LoginBody` 等请求模型。
- MyBatis-Plus、数据库表结构和 SQL——那是 `ruoyi-common-mybatis` 和业务模块的职责。
- 微服务架构下的服务间调用——本模块是单体/微服务共享的基础层，不涉及 Spring Cloud 相关内容。

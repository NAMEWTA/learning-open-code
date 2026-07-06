# ruoyi-common-core 核心基础模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**R&lt;T&gt;**：
RuoYi 的统一 API 响应体（`org.dromara.common.core.domain.R`）。泛型类，核心字段为 `code (int)`、`msg (String)`、`data (T)`。通过静态工厂方法 `ok()`/`fail()`/`warn()` 构造实例，是所有 Controller 返回值的统一信封。
_Avoid_: 「ResponseResult」、「ApiResponse」——项目中就叫 `R`。

**PageResult&lt;T&gt;**：
分页查询的统一响应结构（`org.dromara.common.core.domain.PageResult`）。包含 `total (long)` 和 `rows (Collection&lt;T&gt;)` 两个字段。通过 `build()` 静态工厂构造，内置空集合兜底。
_Avoid_: 「PageInfo」、「IPage」——那是 MyBatis-Plus 的分页对象，不是 API 层。

**BaseException**：
core 模块的国际化异常基类（`org.dromara.common.core.exception.base.BaseException`）。继承 `RuntimeException`，有 `module`、`code`、`args`、`defaultMessage` 四个字段。重写 `getMessage()` 通过 `MessageUtils.message(code, args)` 动态解析 i18n 消息。是 `FileException` 和 `UserException` 的父类。
_Avoid_: 「业务异常基类」——它不限于业务场景，是多模块统一的异常根。

**ServiceException**：
通用业务异常（`org.dromara.common.core.exception.ServiceException`）。final 类，独立于 `BaseException` 继承体系。支持 `{}` 占位符消息格式化（基于 Hutool `StrFormatter`），支持链式调用。被全局异常处理器捕获后转为 `R.fail()`。
_Avoid_: 「服务异常」——它可以在任何层抛出，不限于 Service 层。

**SseException**：
SSE（Server-Sent Events）场景专用异常（`org.dromara.common.core.exception.SseException`）。结构与 `ServiceException` 高度一致但独立成类，便于全局异常处理器针对 SSE 场景做差异化处理。
_Avoid_: 「推送异常」——SSE 是具体技术名。

**GLOBAL_REDIS_KEY**：
框架级 Redis key 前缀，值为 `"global:"`，定义在 `org.dromara.common.core.constant.GlobalConstants`。所有系统级缓存 key（验证码、限流、防重提交等）都挂在这个命名空间下，与多租户和业务 key 隔离。
_Avoid_: 「全局前缀」——它专指 Redis key 命名空间。

**CacheNames**：
缓存组名称常量接口（`org.dromara.common.core.constant.CacheNames`）。每个常量值为 `key#ttl#maxIdle#maxSize#local` 格式，在常量名中编码缓存策略。如 `SYS_CONFIG = "sys_config"`（永不过期）、`SYS_USER_NAME = "sys_user_name#30d"`（30 天过期）。
_Avoid_: 「缓存配置」——它只是名称约定，不是配置类。

**HttpStatus**：
HTTP 返回状态码常量接口（`org.dromara.common.core.constant.HttpStatus`）。覆盖 200/201/301/400/401/403/404/500 等标准状态码，外加自定义 `WARN = 601`。被 `R` 的工厂方法使用。
_Avoid_: 不要与 `org.springframework.http.HttpStatus` 混淆——RuoYi 这个是自定义常量接口。

**DictService**：
字典服务接口（`org.dromara.common.core.service.DictService`）。声明 `getDictLabel()`、`getDictValue()`、`getAllDictByDictType()` 等方法。被 `DictPatternValidator` 通过 `SpringUtils.getBean()` 获取实现类。是 core 模块中唯一声明「依赖外部实现」的接口。
_Avoid_: 「字典工具类」——它是需要外部服务的接口，不是纯工具。

**PermissionService**：
权限服务接口（`org.dromara.common.core.service.PermissionService`）。声明 `getRolePermission(userId)` 和 `getMenuPermission(userId)` 两个方法，返回 `Set&lt;String&gt;` 权限标识集合。实现类在 `ruoyi-framework` 中提供。
_Avoid_: 无。

**SpringUtils**：
Spring 容器工具类（`org.dromara.common.core.utils.SpringUtils`）。继承 Hutool `SpringUtil`，增加了 Bean 定义查询（`containsBean`/`isSingleton`/`getType`）、AOP 代理获取（`getAopProxy`）、虚拟线程检测（`isVirtual`）等功能。`@Component` 注册为 Bean，通过 `ApplicationContextAware` 获得 context。
_Avoid_: 「SpringContextHolder」——RuoYi 早期版本的类名。

**ServletUtils**：
Servlet 请求工具类（`org.dromara.common.core.utils.ServletUtils`）。继承 Hutool `JakartaServletUtil`，提供 `getRequest()`/`getResponse()`/`getParameter()`/`getClientIP()`/`renderString()` 等方法。基于 `RequestContextHolder` 获取当前请求上下文。
_Avoid_: 「HttpUtils」、「RequestUtils」——它是专门处理 Servlet 规范的工具类。

**MessageUtils**：
国际化消息工具类（`org.dromara.common.core.utils.MessageUtils`）。唯一的公开方法是 `message(code, args)`。内部通过 `SpringUtils.getBean(MessageSource.class)` 获取 `MessageSource`，基于 `LocaleContextHolder` 的 locale 解析 i18n 消息。找不到 key 时优雅降级返回原 code。
_Avoid_: 「i18n 工具」——它只读消息，不管理语言切换。

**MapstructUtils**：
MapStruct Plus 转换工具类（`org.dromara.common.core.utils.MapstructUtils`）。通过静态字段 `CONVERTER = SpringUtils.getBean(Converter.class)` 获取单例，提供 `convert(source, targetClass)` / `convert(sourceList, targetClass)` / `convert(map, beanClass)` 等静态方法。
_Avoid_: 「对象转换工具」——它特指 MapStruct Plus 框架。

**@DictPattern**：
字典值校验注解（`org.dromara.common.core.validate.dicts.DictPattern`）。自定义 Jakarta Bean Validation 约束，校验字段值是否属于指定字典类型 `dictType` 的合法值。底层由 `DictPatternValidator` 通过 `DictService` 查询字典数据做校验。
_Avoid_: 「字典校验」——容易与数据字典本身的 CRUD 混淆。

**@EnumPattern**：
枚举值校验注解（`org.dromara.common.core.validate.enums.EnumPattern`）。校验输入值是否属于指定枚举的某个字段值。通过反射调用枚举 getter 提取合法值集合，支持 `@Repeatable` 多规则组合。
_Avoid_: 「枚举注解」——它做的是校验，不是定义枚举。

**@Xss**：
XSS 防护校验注解（`org.dromara.common.core.xss.Xss`）。校验输入值是否包含 HTML 标签（基于 Hutool `HtmlUtil.RE_HTML_MARK` 正则），包含则校验失败。
_Avoid_: 「防注入注解」——XSS 和 SQL 注入是不同概念。

**ValidatorUtils**：
参数校验工具类（`org.dromara.common.core.utils.ValidatorUtils`）。唯一方法是 `validate(object, groups...)`。通过 `SpringUtils.getBean(Validator.class)` 获取 Jakarta Validator，支持分组校验。校验不通过直接抛 `ConstraintViolationException`。
_Avoid_: 「Bean 校验工具」——它是包装了 Jakarta Bean Validation 的工具。

**BusinessStatusEnum**：
流程业务状态枚举（`org.dromara.common.core.enums.BusinessStatusEnum`）。覆盖 CANCEL/DRAFT/WAITING/FINISH/INVALID/BACK/TERMINATION 七种状态。内置 `checkStartStatus()`/`checkCancelStatus()`/`checkBackStatus()` 等状态机校验方法和 `STATUS_MAP` 枚举缓存。
_Avoid_: 「流程状态枚举」——它专门用于工作流/审批场景。

**Constant Interface Pattern**（常量接口模式）：
core 模块中 `Constants`、`GlobalConstants`、`HttpStatus`、`CacheNames`、`RegexConstants`、`SystemConstants` 全部使用 `interface` 而非 `class` 定义常量。利用接口字段隐式 `public static final` 的特性避免冗余修饰符。
_Avoid_: 「常量类」——它们确实不是 class 而是 interface。

**Fail-Fast 校验模式**：
`ValidatorConfig` 中设置 `hibernate.validator.fail_fast = true`，表示参数校验遇到第一个失败即立即返回，不再继续校验后续字段。与之相对的是 Fail-All 模式（所有字段都校验完再汇总）。
_Avoid_: 「快速失败」——容易与构建/部署领域的 Fail-Fast 混淆。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

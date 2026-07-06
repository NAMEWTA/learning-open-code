# ruoyi-common-sensitive 数据脱敏模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**数据脱敏 (Data Masking / Desensitization)**：
对敏感数据（手机号、身份证、邮箱等）进行变形处理，在保留数据格式特征的前提下隐藏真实内容。本模块在 **JSON 序列化输出阶段**执行脱敏——数据库存明文，只在返回给前端时掩码。这不同于数据库存储加密。
_Avoid_: 「加密」（加密可逆，脱敏不可逆）、「数据隐藏」（太泛）。

**@Sensitive 注解**：
本模块的核心入口注解，标注在 VO 字段上即可触发脱敏（`org.dromara.common.sensitive.annotation.Sensitive`）。三个属性：`strategy()` 指定脱敏策略（必填），`roleKey()` 和 `perms()` 按角色/权限条件化脱敏（可选）。被 `SensitiveJsonFieldProcessor.supports()` 检测到后进入脱敏管线。
_Avoid_: 「脱敏标签」（它是一个注解，不是标签）。

**SensitiveStrategy 脱敏策略枚举**：
枚举类型，定义 17 种脱敏策略（`org.dromara.common.sensitive.core.SensitiveStrategy`）。每个枚举值持有一个 `Function<String, String> desensitizer`，底层调用 hutool 的 `DesensitizedUtil` 或 RuoYi 自定义的 `DesensitizedUtils`。代表「怎么脱」——是策略模式的体现。
_Avoid_: 「脱敏方法集」（它是一个枚举，不仅是方法集合）。

**SensitiveJsonFieldProcessor 脱敏处理器**：
实现 `JsonFieldProcessor` 接口，`@Order(100)` 控制执行顺序（`org.dromara.common.sensitive.handler.SensitiveJsonFieldProcessor`）。`supports()` 检查字段是否有 `@Sensitive` 注解，`process()` 根据策略执行脱敏。是连接「注解声明」与「策略执行」的桥梁，也是 JSON 序列化管线的插件点。
_Avoid_: 「脱敏拦截器」（它不是 AOP 拦截器，是 Jackson 序列化处理器）。

**JsonFieldProcessor JSON字段处理器接口**：
`ruoyi-common-json` 模块定义的核心扩展点接口（`org.dromara.common.json.enhance.JsonFieldProcessor`）。三阶段生命周期：`collect`（收集需处理的字段）→ `prepare`（批量预处理）→ `process`（逐字段替换值）。脱敏处理器只在 `supports()` 和 `process()` 两个方法做文章，属于最简实现。
_Avoid_: 「Jackson 序列化器」（它比 Jackson StdSerializer 抽象层级更高）。

**JsonFieldContext 字段上下文**：
Java 14 `record` 类型（`org.dromara.common.json.enhance.JsonFieldContext`），封装四个信息：`owner`（字段所属对象）、`propertyName`（字段名）、`member`（Jackson 反射成员，用于获取注解）、`value`（字段当前值）。`getAnnotation()` 是其最关键方法——脱敏处理器靠它拿到 `@Sensitive` 注解元数据。
_Avoid_: 「字段元数据对象」（过于笼统）。

**SensitiveService 脱敏服务接口**：
策略接口（`org.dromara.common.sensitive.core.SensitiveService`），唯一方法 `isSensitive(roleKey[], perms[])` 返回 boolean。用户可实现此接口，按当前登录用户的角色/权限决定是否执行脱敏——实现「管理员看明文、普通用户看掩码」。默认为 null（等于不对角色/权限做过滤，始终脱敏）。
_Avoid_: 「脱敏开关」（它控制是否脱敏，但不直接触发脱敏）。

**SensitiveConfig 自动配置类**：
`@AutoConfiguration` 标注的配置类（`org.dromara.common.sensitive.config.SensitiveConfig`）。唯一的 `@Bean` 方法注册 `SensitiveJsonFieldProcessor`，使其成为 Spring 管理的单例 Bean，从而被 `JsonValueEnhancer` 自动发现并接入 JSON 序列化管线。
_Avoid_: 「脱敏配置类」（不够精确，容易与业务配置文件混淆）。

**DesensitizedUtil（hutool）**：
Hutool 工具库提供的脱敏工具类（`cn.hutool.core.util.DesensitizedUtil`）。提供 11 种常用的脱敏方法：`mobilePhone`（手机号）、`idCardNum`（身份证）、`email`（邮箱）、`bankCard`（银行卡）、`chineseName`（中文名）、`fixedPhone`（固话）、`password`（密码）、`address`（地址）、`userId`（用户ID）、`ipv4/ipv6`、`carLicense`（车牌）。`SensitiveStrategy` 的绝大多数枚举项直接调用它。
_Avoid_: 「脱敏库」（它是一个工具类，不是完整的库）。

**DesensitizedUtils（RuoYi自定义）**：
继承 `DesensitizedUtil` 的自定义工具类（`org.dromara.common.core.utils.DesensitizedUtils`）。新增 `mask(value, prefixVisible, suffixVisible, maskLength)` 通用灵活脱敏方法和 `maskHighSecurity(value, prefixVisible, suffixVisible)` 高安全脱敏方法。弥补 hutool 只提供固定规则脱敏的不足——让开发者自行控制前后可见长度和掩码长度。
_Avoid_: 「自定义脱敏算法」（它仍调用 hutool 底层的 StrUtil，是对 hutool 的扩展）。

**roleKey / perms 条件脱敏**：
`@Sensitive` 注解的两个可选属性，用于实现差异化脱敏。`roleKey` 按角色标识过滤（如 `"admin"`），`perms` 按权限标识过滤（如 `"system:user:query"`）。当 `SensitiveService.isSensitive(roleKey, perms)` 返回 true 时才对字段脱敏。二者为 OR 关系（多个角色满足一个即可，多个权限满足一个即可）。
_Avoid_: 「脱敏白名单」（它决定的是「要不要脱敏」，不仅仅是「谁可以豁免」）。

**STRING_MASK 通用字符串脱敏**：
`SensitiveStrategy` 中的一种策略，使用 `DesensitizedUtils.mask(s, 4, 4, 4)`，即前 4 位可见 + 中间 4 个 `*` + 后 4 位可见。适用于没有专用脱敏规则的字符串字段（如自定义编码、地址补充信息等）。与 `FIRST_MASK`（只显示首字符）、`MASK_HIGH_SECURITY`（高安全级，中间全部掩码）构成灵活度递增的三个通用策略。
_Avoid_: 「通用掩码」（可能会与 hutool 的命名混淆）。

## 待收录
- 暂无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

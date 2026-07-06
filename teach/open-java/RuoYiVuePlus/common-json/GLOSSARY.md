# ruoyi-common-json 序列化模块 Glossary

记录学习者在 5 节课程中**真正理解**的核心术语。覆盖 Jackson 配置、序列化处理器、JSON 增强框架、JSON 校验四大块。

## Terms

**Jackson (tools.jackson)**：
本模块的基石库。RuoYi-Vue-Plus 使用 `tools.jackson` 包名而非标准的 `com.fasterxml.jackson`——这是通过 Maven Shade 插件重打包（re-shade）的 Jackson 3.x，目的是避免与其他依赖引入的 Jackson 版本冲突。功能上与 FasterXML Jackson 完全一致。
_Avoid_: 「com.fasterxml.jackson」（本项目中不存在此包名）。

**JsonMapper (Jackson 3.x)**：
Jackson 3.x 的入口类，替代 Jackson 2.x 的 `ObjectMapper`。它是不可变的（immutable），配置通过 `JsonMapper.builder()` 链式构建。本模块通过 `SpringUtils.getBean(JsonMapper.class)` 获取全局单例，所有序列化/反序列化操作都由它驱动。

**SimpleModule**：
Jackson 的模块化扩展机制。本模块在 `JacksonConfig.registerJavaTimeModule()` 中创建了一个 `SimpleModule`，注册了 BigNumberSerializer（Long/BigInteger）、ToStringSerializer（BigDecimal）、LocalDateTimeSerializer、CustomDateDeserializer、CustomLocalDateTimeDeserializer。相当于「在 Jackson 默认能力上插了一组自定义处理器」。

**BigNumberSerializer**：
自定义数字序列化器，继承 `NumberSerializer`。核心逻辑：当 Long/BigInteger 的值在 JavaScript 安全整数范围（[-9007199254740991, 9007199254740991]，即 Number.MAX_SAFE_INTEGER / MIN_SAFE_INTEGER）之内时正常序列化为 JSON number；超出范围时序列化为 JSON string。这解决了「Java Long 传给前端 JS 精度丢失」的经典问题。
_Avoid_: 「Long 转 String 序列化器」（它只对超范围的才转 string，范围内的保持 number）。

**CustomDateDeserializer**：
自定义 `java.util.Date` 反序列化器。不限制输入格式——委托给 Hutool 的 `DateUtil.parse()`，能自动识别 yyyy-MM-dd HH:mm:ss、yyyy/MM/dd、时间戳（毫秒/秒）、ISO 格式等。空字符串返回 null。解决了「前端传的日期格式五花八门，后端不想每种都写一个解析器」的问题。

**CustomLocalDateTimeDeserializer**：
自定义 `java.time.LocalDateTime` 反序列化器。与 CustomDateDeserializer 同级，同样委托给 `DateUtil.parse()` 自动识别格式，最终调用 `parse.toLocalDateTime()` 转换。与 CustomDateDeserializer 唯一的区别就是返回类型——一个返回 Date，一个返回 LocalDateTime。

**JsonEnhancementContext（增强上下文）**：
单次 HTTP 响应增强的数据总线。它持有 `JsonMapper` 引用、一个 `LinkedHashMap` 属性表（三级传输的共享数据）、以及一个 `processingRequired` 标记。`JsonFieldProcessor` 的三个生命周期阶段（collect/prepare/process）通过它的 `setAttribute` / `getAttribute` 传递数据。相当于「一个请求级别的黑板」。
_Avoid_: 「增强参数」「翻译上下文」（二者语义近似但本模块固定叫 EnhancementContext）。

**JsonFieldContext（字段上下文）**：
一条 Java Record，封装了正在处理的字段的四个信息：`owner`（所属对象实例）、`propertyName`（属性名）、`member`（Jackson 元数据 AnnotatedMember）、`value`（当前值）。`getAnnotation(Class)` 方法能从 member 上读取注解——这就是处理器判断「这个字段我管不管」的依据。
_Avoid_: 「字段信息」「属性元数据」（本模块固定叫 FieldContext）。

**JsonFieldProcessor（字段处理器接口）**：
JSON 增强框架的扩展点。定义了三个生命周期方法 + 一个判定方法：`supports()` 判断是否处理该字段；`collect()` 收集阶段记录需要处理的 key；`prepare()` 预处理阶段执行批量 IO（消 N+1）；`process()` 处理阶段返回替换后的值。所有方法都是 `default` 实现（返回原值或不做事），实现者只需覆盖关心的阶段。
_Avoid_: 「字段增强器」（Processor 强调它是处理链中的一环，而非最终入口）。

**JsonValueEnhancer（响应增强器）**：
JSON 增强框架的引擎。持有排序后的 `JsonFieldProcessor` 列表和 `ConcurrentHashMap` 属性元数据缓存。核心方法 `enhance(body)` 的流程：创建 `JsonEnhancementContext` → `collectValue` 递归扫描对象树 → 检查 `processingRequired` → 调用全部 `processor.prepare()` → `renderValue` 渲染增强后的 JSON 树。它还通过 `supports(converterType)` 排除了 `ByteArrayHttpMessageConverter`、`StringHttpMessageConverter`、`ResourceHttpMessageConverter` 三类不需要增强的转换器。

**三阶段生命周期（collect → prepare → process）**：
JSON 增强框架的核心设计模式。collect 阶段遍历对象树所有字段，各 processor 收集需要处理的 key 存入 context；prepare 阶段所有 processor 各执行一次批量操作（如一次性查数据库，而非每个字段查一次）；process 阶段遍历 JSON 树渲染时逐个字段替换值。这三阶段分离是「在序列化过程中做翻译/脱敏」时避免 N+1 查询问题的关键设计。

**@JsonPattern**：
自定义 Jakarta Bean Validation 注解（`@Constraint`），用于校验字符串字段是否为合法 JSON。`type` 属性指定期望的 JSON 类型（OBJECT / ARRAY / ANY），默认 ANY。校验逻辑委托给 `JsonPatternValidator`。可配合 `@NotBlank` 使用（空值由 @NotBlank 处理，@JsonPattern 对空值放行）。

**JsonPatternValidator**：
`@JsonPattern` 的校验器实现，实现 `ConstraintValidator<JsonPattern, String>`。在 `initialize()` 中读取注解的 `type` 属性；在 `isValid()` 中先用 `StringUtils.isBlank` 放行空值（交给 @NotBlank 控制），再根据 `jsonType` 枚举分别调用 `JsonUtils.isJson()` / `isJsonObject()` / `isJsonArray()`。

**JsonType（枚举）**：
JSON 类型枚举，含 OBJECT（对象 `{}`）、ARRAY（数组 `[]`）、ANY（任意）三个值。驱动 `@JsonPattern` 的校验策略和 `JsonPatternValidator` 的分支逻辑。

**JsonUtils**：
业务代码最常直接调用的 JSON 工具类。提供 10 个公开方法：`toJsonString`（序列化）、`parseObject` 三重重载（String/bytes/TypeReference）、`parseMap` / `parseArrayMap`（转 Dict）、`parseArray`（转 List）、`toJsonStringExcludeFields`（序列化并移除字段）、`removeFields`（递归删字段）、`isJson` / `isJsonObject` / `isJsonArray`（格式校验）。底层全部委托给全局 `JsonMapper` 实例。
_Avoid_: 「JSON 工具」（全称是 JsonUtils，位于 utils 包）。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

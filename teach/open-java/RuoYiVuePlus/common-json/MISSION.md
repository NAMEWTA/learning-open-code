# Mission: 全面读懂 RuoYi-Vue-Plus 的 ruoyi-common-json 序列化模块

## Why
学习者要能在脑中完整重建 `ruoyi-common-json` 这个公共模块「提供了什么能力、每个类各管什么、为什么这样设计」的全景，理解它如何基于 **Jackson** (tools.jackson) 构建一套开箱即用的序列化/反序列化/字段增强/JSON校验能力，并能在自己的业务代码里正确选用。重点是**读懂模块设计与各组件职责**，不是从零实现一个 JSON 框架。讲解全部基于本仓库真实代码（已逐文件核对）。

## Success looks like
- 能用一张图讲清模块的「三驾马车」：**JacksonConfig**（序列化配置中心）、**JsonEnhancementConfig**（字段增强入口）、**JsonUtils**（业务工具门面），以及它们各自连接的子组件。
- 能解释 `BigNumberSerializer` 如何通过判断 `longValue() >= MIN_SAFE_INTEGER && <= MAX_SAFE_INTEGER` 来保护 Long 精度传给 JS 前端，以及为什么 `BigDecimal` 用 `ToStringSerializer` 而非自定义 Serializer。
- 能讲清两个自定义反序列化器的智能之处：`CustomDateDeserializer` 和 `CustomLocalDateTimeDeserializer` 都委托给 Hutool 的 `DateUtil.parse()`，天然支持多种日期格式（yyyy-MM-dd、yyyy/MM/dd、时间戳等）。
- 能讲清「JSON 增强框架」的三阶段生命周期：**collect**（收集需增强字段）→ **prepare**（批量预处理，消 N+1）→ **process**（渲染替换），并说清 `JsonEnhancementContext` 作为三者数据总线、`JsonFieldProcessor` 作为扩展点的设计模式。
- 能讲清 `JsonValueEnhancer` 的渲染链路：对象树递归扫描 → 属性元数据缓存 (`ConcurrentHashMap`) → 循环引用保护 (`IdentityHashMap`) → 简单值短路 → 处理后二次增强 (`enhanceTranslatedValue`)。
- 能说清 `@JsonPattern` 校验注解 + `JsonPatternValidator` + `JsonType` 枚举的 Bean Validation 集成方式，以及 `JsonUtils` 中 `isJson` / `isJsonObject` / `isJsonArray` 是如何被校验器复用的。
- 能在「该用哪个工具方法」的场景题里选对：`toJsonString` vs `parseObject` vs `parseMap` vs `parseArrayMap` vs `toJsonStringExcludeFields`。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解以追踪真实代码 + 解释设计动机为主。
- 目标是「读懂并能正确选用」而非「能改框架」——练习以「读代码答问题 / 选型判断 / 复述链路」为主，不要求大量动手编码。
- 全部讲解基于仓库真实代码，引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- Jackson 底层 API 的完整说明（如 `JsonGenerator`、`DeserializationContext` 的全部方法）——仅讲本模块用到的部分。
- 业务模块里具体怎么用这些能力（如某处用了 `@JsonPattern` 校验、某处给某 VO 加了增强注解）——仅在举例时引用，不展开业务。
- JSON 格式本身的规范（RFC 7159）或 AST 树遍历理论。
- 其它 JSON 库对比（如 fastjson、Gson）——本模块只涉及 Jackson（tools.jackson）。

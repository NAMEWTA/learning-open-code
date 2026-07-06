# ruoyi-common-translation 翻译模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**@Translation**：
字段级注解（`org.dromara.common.translation.annotation.Translation`），标注在 VO 的字段上，声明该字段的值需要被翻译。三个参数：`type`（翻译类型，必填）、`mapper`（映射字段名，选填——不填则翻译当前字段值，填写则翻译 mapper 指定字段的值）、`other`（额外参数，选填——如字典类型、业务分类等）。翻译后的值会**替换当前字段的序列化输出**。
_Avoid_: 「翻译器注解」（它是字段标注，不是处理器注解）。

**@TranslationType**：
类型级注解（`org.dromara.common.translation.annotation.TranslationType`），标注在 `TranslationInterface` 实现类上。唯一的参数 `type` 是一个字符串，与 `@Translation(type=...)` 对应，构成「声明类型 - 实现匹配」的绑定。Spring 容器中的实现类通过此注解被 `TranslationJsonFieldProcessor` 识别并注册。
_Avoid_: 「翻译类型定义」（它只声明类型名，不定义翻译逻辑）。

**TranslationInterface\<T\>**：
翻译 SPI 接口（`org.dromara.common.translation.core.TranslationInterface`），所有翻译实现必须实现它。核心方法：`translation(Object key, String other)` 单值翻译；`translationBatch(Set<Object> keys, String other)` 批量翻译（默认实现为逐条调用 `translation` 并打印警告日志）。泛型 `<T>` 为翻译结果的类型（内置实现均为 `String`）。接口还提供了 `collectLongIds`、`parseLongIds`、`joinMappedValues` 三个工具方法，供实现类复用。
_Avoid_: 「翻译器」（它是接口契约，不是具体翻译器）。

**TranslationJsonFieldProcessor**：
翻译模块的核心处理器（`org.dromara.common.translation.core.handler.TranslationJsonFieldProcessor`），实现了 `ruoyi-common-json` 扩展点的 `JsonFieldProcessor` 接口。遵循 **collect → prepare → process** 三阶段生命周期：collect 阶段扫描所有带 `@Translation` 的字段，按 `(type, other)` 分组收集原始值；prepare 阶段对每组调用对应 `TranslationInterface.translationBatch()` 批量翻译；process 阶段将翻译结果写回字段值。`@Order(0)` 确保其在 JSON 管线中首批执行。
_Avoid_: 「翻译过滤器」（它是完整生命周期处理器，不只是过滤）。

**JsonFieldProcessor**：
`ruoyi-common-json` 定义的 JSON 字段处理扩展点接口（`org.dromara.common.json.enhance.JsonFieldProcessor`）。声明了 `supports`（是否处理该字段）、`collect`（收集阶段）、`prepare`（预处理阶段）、`process`（处理阶段）四个方法。翻译模块的 `TranslationJsonFieldProcessor` 是它的一个实现。RuoYi 通过此扩展点实现了「在 JSON 序列化过程中对字段值做后处理」的通用机制。
_Avoid_: 「JSON 处理器」（太泛，不指明它是字段粒度的处理扩展点）。

**JsonEnhancementContext**：
单次 JSON 响应增强的上下文对象（`org.dromara.common.json.enhance.JsonEnhancementContext`）。提供 `setAttribute` / `getAttribute` / `getOrCreateAttribute` 方法，供 `JsonFieldProcessor` 在 collect → prepare → process 三个阶段之间传递共享数据。翻译处理器用它存储「待翻译的批量数据」和「批量翻译结果」。
_Avoid_: 「JSON 上下文」（太泛）。

**JsonFieldContext**：
JSON 序列化时的字段上下文记录（`org.dromara.common.json.enhance.JsonFieldContext`）。包含 `owner`（字段所属的父对象）、`propertyName`（字段名）、`member`（Jackson 注解成员，可通过 `getAnnotation()` 读取字段上的注解）、`value`（字段当前值）。翻译处理器通过 `fieldContext.getAnnotation(Translation.class)` 判断是否需要翻译，通过 `fieldContext.owner()` + mapper 反射获取映射字段的值。
_Avoid_: 「字段信息」（不体现它是序列化管线的上下文）。

**TransConstant**：
翻译类型常量接口（`org.dromara.common.translation.constant.TransConstant`），集中定义了 5 个内置翻译类型字符串常量：`USER_ID_TO_NAME`（`"user_id_to_name"`）、`USER_ID_TO_NICKNAME`（`"user_id_to_nickname"`）、`DEPT_ID_TO_NAME`（`"dept_id_to_name"`）、`DICT_TYPE_TO_LABEL`（`"dict_type_to_label"`）、`OSS_ID_TO_URL`（`"oss_id_to_url"`）。使用常量而非硬编码字符串，避免 `@Translation(type=...)` 和 `@TranslationType(type=...)` 之间的字符串拼写错误。
_Avoid_: 「翻译常量类」（就是它）。

**TranslationConfig**：
翻译模块的 Spring Boot 自动配置类（`org.dromara.common.translation.config.TranslationConfig`），用 `@AutoConfiguration` 标注。唯一的 `@Bean` 方法 `translationJsonFieldProcessor(List<TranslationInterface<?>> list)` 收集容器中所有 `TranslationInterface` 实现，按 `@TranslationType.type()` 建立映射，构造并注册 `TranslationJsonFieldProcessor`。通过 `AutoConfiguration.imports` 文件被 Spring Boot 发现。
_Avoid_: 「翻译配置」（不指明它是自动装配入口）。

**mapper 字段映射**：
`@Translation` 注解的 `mapper` 参数机制。当 `mapper` 非空时，翻译处理器不翻译当前字段的值，而是通过反射调用 `owner` 对象上 `mapper` 指定字段的 getter 获取原始值，然后用该值去查翻译结果，最后写回当前字段。常见场景：`createBy`（创建人 ID）字段可能没有直接存在 VO 里，但 VO 有 `createById` 字段，这时 `@Translation(type="user_id_to_name", mapper="createById")` 写在 `createByName` 字段上。
_Avoid_: 「字段映射」（不体现它是指定翻译源字段的机制）。

**批量翻译退化为逐条（Batch Degradation）**：
当 `TranslationInterface` 的实现类未覆盖 `translationBatch()` 方法时，接口的 default 实现会遍历 keys 逐条调用 `translation()`，并打印一条警告日志：`"翻译类型 [X] 未覆盖 translationBatch 方法，已退化为逐条查询，建议实现批量查询以提升性能"`。这是 N+1 查询问题的来源——如果有 100 个用户 ID 需要翻译，就会执行 100 次数据库查询。所有内置实现都已覆盖 `translationBatch` 来避免此问题。
_Avoid_: 「默认批量翻译」（它恰恰不是批量，而是退化）。

**collectLongIds / parseLongIds / joinMappedValues**：
`TranslationInterface` 提供的三个工具默认方法。`collectLongIds` 将 `Set<Object>` 中的键统一转为 `Set<Long>`，支持单值和逗号分隔字符串两种输入；`parseLongIds` 将逗号分隔字符串解析为 `List<Long>`；`joinMappedValues` 将逗号分隔的 ID 字符串中的每个 ID 通过映射函数转成值，再用逗号拼接返回。内置实现大量复用这三个方法。
_Avoid_: 「工具方法」（太泛，这些是翻译接口的专用辅助方法）。

**SPI 翻译注册机制**：
翻译模块的核心设计模式：`TranslationInterface` 实现类通过 `@TranslationType(type="xxx")` 声明自己能处理哪种类型；`TranslationConfig` 通过 `List<TranslationInterface<?>>` 收集 Spring 容器中所有实现；`TranslationJsonFieldProcessor` 在构造时建立 `Map<String, TranslationInterface<?>>`（type → 实现）。`@Translation(type="xxx")` 在字段上声明需要哪种翻译，运行时 processor 根据 type 找到对应实现执行翻译。这是标准的「策略模式 + 依赖注入」实践，而非 Java SPI（`META-INF/services`）。
_Avoid_: 「Java SPI」（虽然名字像，但它用的是 Spring 依赖注入而非 `ServiceLoader`）。

**三阶段生命周期（collect → prepare → process）**：
`JsonFieldProcessor` 接口定义的字段处理三阶段：
1. **collect**：递归扫描响应对象树时，对每个字段调用。翻译处理器在此阶段收集需要翻译的原始值，按 `(type, other)` 分组存入 `JsonEnhancementContext`。
2. **prepare**：collect 全部完成后调用一次。翻译处理器在此阶段对每组原始值调用 `translationBatch()` 执行批量查询，结果也存入 context。
3. **process**：渲染 JSON 时，对每个字段调用。翻译处理器在此阶段从 context 取出翻译结果，替换字段值。
_Avoid_: 「处理阶段」（须明确三个阶段的名称和顺序）。

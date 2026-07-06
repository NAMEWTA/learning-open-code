# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-translation 翻译模块

## Why
学习者要能彻底读懂 `ruoyi-common-translation` 这个公共模块：它是一个**注解驱动的字段值翻译引擎**，核心思路是「把 ID 变可读名称」——用户 ID 变成昵称、部门 ID 变成部门名、OSS 文件 ID 变成可访问的 URL、字典值变成显示标签。它通过 `@Translation` 注解声明「哪个字段需要翻译、翻译成什么类型」，通过 `TranslationInterface` SPI 接口提供「怎么翻译」的可插拔实现，通过 `TranslationJsonFieldProcessor` 将翻译过程无缝集成到 RuoYi 的 JSON 序列化管线中（`ruoyi-common-json` 的 `JsonFieldProcessor` 扩展点）。学习者要达到能给同事讲清「这个模块的 SPI 机制如何实现一次收集、批量翻译、避免 N+1」「如何自己写一个翻译实现接入现有体系」，并能自己为公司业务添加新的翻译类型（如「订单号 → 订单摘要」）。

## Success looks like
- 能用一句话说清 `ruoyi-common-translation` 在 RuoYi 架构中的位置：它坐在 JSON 序列化管线上，把 API 返回的 ID/编码自动换成人类可读的名称。
- 能解释 `@Translation(type="...", mapper="...", other="...")` 三个参数的含义与配合方式，并正确使用它们标注业务 VO 字段。
- 能讲清 `TranslationInterface<T>` SPI 接口的 `translation()` 与 `translationBatch()` 两个方法的关系，以及为什么默认实现会打印「建议实现批量查询」的警告日志。
- 能追踪 `TranslationJsonFieldProcessor` 的 **collect → prepare → process** 三阶段生命周期：如何按 `(type, other)` 分组收集原始值 → 批量查询 → 将翻译结果写回字段值，实现「一次 DB 查询翻译全部字段」避免 N+1。
- 能说出 5 个内置翻译实现各自对应的 `TransConstant` 常量、依赖的远程服务、以及支持的输入类型（单值/逗号分隔多值）。
- 能按 `TranslationConfig → @AutoConfiguration` 自动装配机制，写出一个自定义翻译实现的完整接入步骤（实现类 + `@TranslationType` 注解 + 注入远程服务 + 覆盖 `translationBatch`）。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java。讲解聚焦后端注解机制与 SPI 扩展点。
- 目标是「读懂」而非「能改造框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 手写简单实现」为主。
- 全部讲解基于仓库真实代码（11 个 Java 文件已逐文件核对），引用具体文件路径、类名与关键行。
- 交互语言：简体中文。

## Out of scope
- `ruoyi-common-json` 模块的 `JsonValueEnhancer` / `JsonFieldProcessor` 扩展点引擎的完整实现——仅在本课讲解 `TranslationJsonFieldProcessor` 如何作为该扩展点的一个实现接入时，简要引用其契约。
- 各远程服务（`UserService`、`DeptService`、`DictService`、`OssService`）的内部实现细节——只讲翻译实现如何调用它们的 API，不讲服务端如何查询数据库。
- Jackson 序列化器 / `ObjectMapper` 的底层原理——只讲翻译处理器如何通过 `ruoyi-common-json` 的抽象层注册到序列化流程。
- 前端如何展示翻译后的字段（只需知道翻译在服务端 JSON 序列化时即完成，前端收到的已是翻译后的值）。

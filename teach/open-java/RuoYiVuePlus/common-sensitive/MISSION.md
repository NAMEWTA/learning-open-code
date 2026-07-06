# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-sensitive 数据脱敏模块

## Why
学习者要能彻底读懂 `ruoyi-common-sensitive` 这个公共模块：它仅 5 个 Java 文件（1 个注解 + 1 个枚举策略 + 1 个处理器 + 1 个配置 + 1 个服务接口），通过注解驱动的方式在 JSON 序列化管线中自动对敏感字段（手机号/邮箱/身份证/银行卡等）进行脱敏处理。理解它，等于理解 RuoYi-Vue-Plus 如何将数据脱敏这个横切关注点**零侵入地织入响应序列化流程**——用自定义注解标注字段，用策略枚举封装脱敏算法，用 JsonFieldProcessor 扩展点介入 Jackson 序列化管线。达到能给同事讲清「一个注解就能自动脱敏是怎么做到的」「如何新增一个自定义脱敏规则」，并能独立排查脱敏不生效的问题。重点是**读懂脱敏注解 → 策略执行 → 序列化管线织入**的完整代码链路，不是从零实现脱敏算法。

## Success looks like
- 能用一句话说清 `ruoyi-common-sensitive` 模块的五个 Java 文件各自承担什么职责，以及它们之间如何协作完成一次字段脱敏。
- 能画出「@Sensitive 注解声明 → SensitiveJsonFieldProcessor 拦截 → SensitiveStrategy 执行 → hutool DesensitizedUtil 脱敏」的调用链图。
- 能逐一说出 `SensitiveStrategy` 枚举中全部 17 种脱敏策略的名称、用途和脱敏效果（如手机号 134****4567、身份证 110***********1234）。
- 能解释 `SensitiveJsonFieldProcessor` 如何借助 `JsonFieldProcessor` 接口的 `supports()` / `process()` 生命周期，在 Jackson 序列化时自动拦截并替换字段值。
- 能手写一段代码：给一个自定义 VO 的字段加 `@Sensitive(strategy = SensitiveStrategy.PHONE)`，让 Controller 返回 JSON 时手机号自动脱敏。
- 能解释 `roleKey` 和 `perms` 参数的作用机制——脱敏规则如何与用户角色/权限绑定，实现「管理员看明文、普通用户看掩码」的差异化返回。
- 能读懂 `DesensitizedUtils.mask()` 和 `maskHighSecurity()` 的灵活脱敏算法，并说出它们与 hutool 内置 `DesensitizedUtil` 的分工关系。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会在「练习场景」中联系到前端请求响应的 JSON 形状变化。
- 目标是「读懂」而非「能改造框架」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 手写代码片段」为主。
- 全部讲解基于仓库真实代码与 hutool DesensitizedUtil 源码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- hutool DesensitizedUtil 的全部内部实现细节（如正则匹配规则）——只讲项目如何调用，不讲 hutool 内部算法。
- ruoyi-common-json 的 JsonValueEnhancer 完整实现细节——仅在与脱敏处理器对接时点到为止。
- 前端如何根据脱敏后的 JSON 展示 UI 组件——本课关注后端序列化管线。
- 数据库存储层面的加密（如 MyBatis TypeHandler 加解密）——脱敏只发生在 JSON 序列化输出端，不改变数据库存储。

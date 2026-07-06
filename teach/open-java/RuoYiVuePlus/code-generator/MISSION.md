# Mission — ruoyi-gen 代码生成器模块深度学习

## Why（为什么学）

ruoyi-gen 是 RuoYi-Vue-Plus 中**开发者效率的核心引擎**。它并非只是一个简单的代码脚手架，而是一套完整的、可扩展的代码生成框架：通过 AnyLine 元数据引擎动态读取任意数据源的表结构，结合 FreeMarker 模板引擎，一键生成从前端（Vue/React）到后端（Java + MyBatis）再到数据库（SQL）的完整功能模块代码。

学习 ruoyi-gen 能获得以下能力：

- 理解"元数据驱动代码生成"这一设计范式的完整实现，掌握从数据库表结构到可运行代码的全自动转换链路
- 学会如何在一个企业级项目中设计和扩展代码生成器：如何添加新的前端框架模板、如何扩展数据库类型支持、如何自定义模板
- 掌握 AnyLine 元数据引擎在动态数据源场景下的集成技巧（与 baomidou dynamic-datasource 联动）
- 理解字段类型自动推断规则（数据库类型 → Java 类型 → 前端控件类型），以及如何按命名约定智能匹配 UI 控件
- 获得一套可直接复用的模板设计思想：如何用 FreeMarker 编写可配置（树表/CRUD、导出/状态/唯一校验/排序）的一体化模板

## Success（成功标准）

完成本课程后，学习者应能：

1. **独立画出 ruoyi-gen 的完整处理流程图**：从用户导入数据库表 → AnyLine 元数据解析 → 配置生成选项 → FreeMarker 模板渲染 → ZIP 下载，涵盖 Controller / Service / TemplateEngineUtils / PathNamedTemplate / 模板文件五个层次
2. **独立添加一个新的前端框架模板**（如 Angular 或 Svelte）：在 `fm/` 下创建模板目录和对应的 `.ftl` 模板文件，修改 `TemplateEngineUtils.getTemplateList()` 的模板选择逻辑，使生成器能产出该框架的前端页面代码
3. **独立为已有表配置并成功生成一套完整的 CRUD 代码**：通过 API 导入表 → 配置表信息（包名、模块名、业务名、模板分类、前端类型）→ 预览验证 → 下载 ZIP，并能解压后直接运行
4. **口述字段类型自动推断的完整规则**：从数据库列类型（varchar/bigint/datetime/decimal 等）→ Java 类型（String/Long/LocalDateTime/BigDecimal）→ 前端控件类型（input/inputNumber/datetime/switch），以及按字段名后缀匹配 HTML 控件的命名约定
5. **理解并修改 MyBatisDataSourceMonitor**：口述它如何解决 AnyLine 与 baomidou 动态数据源之间"同一 JdbcTemplate 对应多种数据库"的适配问题，以及 `ConfigTable.KEEP_ADAPTER`、`feature()`、`key()` 三个关键方法的作用

## Constraints（约束）

- 需要具备 Spring Boot 项目开发经验，理解 Controller → Service → Mapper 的分层结构
- 需要了解 MyBatis-Plus 基本用法（BaseMapper、LambdaQueryWrapper）
- 需要了解 FreeMarker 模板引擎的基本语法（`${}`、`<#if>`、`<#list>`）
- 需要了解 RuoYi-Vue-Plus 的项目结构和包命名约定
- 本课程聚焦 ruoyi-gen 模块本身，不深入讲解 common 模块中被 gen 所依赖的组件内部实现

## Out of scope（非目标）

- 不讲解 FreeMarker 模板引擎的完整语法（仅涉及模板中用到的部分）
- 不深入讲解 AnyLine 框架的完整功能（聚焦在 metadata API 和 adapter 机制）
- 不讲解 baomidou dynamic-datasource 的完整配置和原理（仅讲解与 gen 适配相关的部分）
- 不讲解 RuoYi-Vue-Plus 微服务架构的整体设计
- 不讲解生成的代码如何在 RuoYi-Vue-Plus 中注册路由、配置权限等后续部署步骤

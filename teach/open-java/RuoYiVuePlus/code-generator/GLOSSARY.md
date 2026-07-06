# 代码生成器 - 术语表

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| ruoyi-gen | 代码生成器模块，RuoYi-Vue-Plus 中开发者效率的核心引擎，通过元数据驱动 + 模板引擎一键生成前后端代码 | 整个模块的命名空间与标识 |
| AnyLine | 通用数据操作框架，提供元数据 API（metadata）可自动读取数据库表结构、列信息、主键等 | 导入表时通过 ServiceProxy.metadata() 读取任意数据源的表/列元数据，作为代码生成的原始输入 |
| FreeMarker / FTL | Java 模板引擎，使用 .ftl 后缀的模板文件，通过 ${}、<#if>、<#list> 等指令将数据字典渲染为源码文本 | 所有代码生成模板（fm/ 目录下的 .ftl 文件）均由 FreeMarker 渲染，将 GenTable 上下文转换为 Java/Vue/React/SQL 源码 |
| baomidou dynamic-datasource | 动态数据源切换框架，通过 @DS 注解控制当前线程使用哪个数据源，底层由 DynamicRoutingDataSource 路由代理 | gen 模块通过 @DS("#genTable.dataName") 切换到目标数据源，读取对应数据库的表结构 |
| DynamicRoutingDataSource | baomidou 动态数据源的核心路由代理类，包裹多个真实数据源（MySQL、Oracle、PostgreSQL 等），根据 @DS 注解路由到不同物理库 | MyBatisDataSourceMonitor 通过 instanceof 判断当前数据源是否是 DynamicRoutingDataSource，从而决定 adapter 缓存策略 |
| MyBatisDataSourceMonitor | AnyLine 与 baomidou 动态数据源的桥接器，实现 DataSourceMonitor 接口，解决同一 JdbcTemplate 对应多种数据库的 adapter 匹配问题 | 构造函数 + keepAdapter() + key() + feature() 四个方法协同，确保 AnyLine 在动态数据源环境下正确识别数据库方言 |
| ConfigTable.KEEP_ADAPTER | AnyLine 配置常量，值为 2 表示自定义模式，由 DataSourceMonitor.keepAdapter() 方法决定是否缓存 adapter | MyBatisDataSourceMonitor 构造函数中设为 2，将 adapter 缓存策略完全交给 Monitor 接管 |
| keepAdapter() | DataSourceMonitor 接口方法，返回 true 表示 AnyLine 可缓存 adapter，返回 false 表示每次重新匹配 | 对 DynamicRoutingDataSource 返回 false，阻止 AnyLine 缓存 adapter，从而支持数据源切换 |
| key() | DataSourceMonitor 接口方法，返回 adapter 缓存的唯一键 | 返回 baomidou 当前线程的数据源名称（DynamicDataSourceContextHolder.peek()），避免不同数据源共享同一 adapter |
| feature() | DataSourceMonitor 接口方法，返回 adapter 匹配的特征指纹 | 通过 JDBC DatabaseMetaData 获取产品名 + URL 拼接成特征串，AnyLine 据此选择对应的方言 adapter |
| adapter（适配器） | AnyLine 中针对不同数据库方言（MySQL/Oracle/PostgreSQL/SQLServer）的解析实现 | 每次执行 metadata API 时 AnyLine 根据 feature() 返回值匹配正确的方言 adapter，用于正确解析元数据 |
| @DS 注解 | baomidou 动态数据源的切换注解，参数为数据源名称或 SpEL 表达式 | GenTableServiceImpl 中 importTableSave 和 selectDbTableList 等方法使用 @DS("#genTable.dataName") 切到用户选择的目标数据源 |
| @DSTransactional | 支持跨数据源事务的注解（RuoYi-Vue-Plus 扩展），结合 baomidou 动态数据源实现分布式事务 | importGenTable() 方法使用该注解，同时操作 gen_table 和 gen_table_column 两张表，可能跨多个数据源 |
| AOP 代理 / SpringUtils.getAopProxy() | 通过 Spring AOP 代理对象调用方法，使 @DS、@Transactional 等切面注解生效 | importGenTable 内调用 selectDbTableColumnsByName 时，必须用 SpringUtils.getAopProxy(this) 而非 this，否则 @DS 不生效 |
| ServiceProxy.metadata() | AnyLine 的元数据服务入口，通过 metadata().tables() 列出表，metadata().table(name) 读取单表 | GenTableServiceImpl 中 selectPageDbTableList() 和 selectDbTableColumnsByName() 的核心 API |
| gen_table | 代码生成业务表配置主表，存储表名、类名、包路径、模板分类、前端类型、扩展选项（options JSON）等信息 | 每次生成代码时从此表读取配置，作为 FreeMarker 模板渲染的核心数据来源 |
| gen_table_column | 代码生成字段配置明细表，存储每列的数据库类型、Java 类型、HTML 控件类型、是否参与增/改/查/列表等 | 导入表时为每列初始化一条记录；生成代码时 columns 列表驱动模板中所有字段级逻辑 |
| options（扩展选项） | gen_table 表中的 JSON 字段，存储可选的生成参数（导出开关、状态字段、唯一校验、排序、树参数等） | 设计目的：避免为每个可选功能增加数据库列；通过 JsonUtils 序列化/反序列化；在 buildContext() 中解析为模板变量 |
| tplCategory（模板分类） | gen_table 字段，值为 crud（单表增删改查）或 tree（树表） | 决定模板选择时使用 index.ftl 还是 index-tree.ftl 页面模板 |
| frontendType（前端类型） | gen_table 字段，值为 vue 或 react，对应 fm/ 下的模板子目录名 | 决定前端模板目录（fm/vue/ 或 fm/react/），影响 API、类型、页面模板的选择 |
| dataName（数据源名称） | gen_table 字段，标识该表所在的数据库连接名称 | @DS("#genTable.dataName") 根据此字段动态切换数据源 |
| packageName / moduleName / businessName | 代码生成的包路径三段式：完整包名、模块名、业务名 | 组合后生成 Java 包路径（{packageName}.{moduleName}），前端 API 路径（{moduleName}/{businessName}） |
| ClassName / className | Java 类名（首字母大写/小写），由表名经过前缀移除 + 驼峰命名转换得到 | 所有生成的 Java 文件名、类名、变量声明的核心标识 |
| GenUtils.initTable() | 表初始化工具方法，完成表名→类名转换、设置默认包名/模块名/业务名/作者/前端类型 | 表导入时第一步调用，为 gen_table 填充初始配置值 |
| GenUtils.initColumnField() | 字段类型推断入口方法，完成数据库类型→Java 类型→HTML 控件类型的三层映射 | 表导入时对每个列调用，是代码生成器智能化的核心——决定了每列最终生成的 Java 类型和前端控件 |
| getDbType() | 从原始列类型（如 varchar(255)）中提取纯类型名（varchar） | initColumnField 中第一层映射的起点 |
| getColumnLength() / getColumnScale() | 从原始列类型中提取长度（如 255）和精度（如 2） | 数值类型精度阶梯推断的关键输入，决定 Integer/Long/BigDecimal 的选择 |
| COLUMNTYPE_STR / TEXT / TIME / NUMBER | GenConstants 中定义的四大数据库类型分类数组 | 第二层映射：根据纯类型名属于哪个分类，进入不同的 Java 类型推断分支 |
| resolveNumberJavaType() | 数值类型的 Java 类型推断方法，按类型 + 长度 + 精度 + 字段名四维联合判断 | 处理 decimal、float、bigint、int、number 等数值类型的 Integer/Long/Double/BigDecimal 选择 |
| isBooleanColumn() | 判断字段是否为布尔类型：tinyint(1) 且字段名匹配开关命名约定 | 优先于数值类型判断，满足条件则 javaType=Boolean，htmlType=switch |
| isSwitchColumn() | 判断字段名是否匹配开关控件命名约定：后缀 status/flag/enabled/disabled/available/visible 或前缀 is_/has_/enable_/disable_ | 第三层映射中优先级最高的字段名匹配规则，满足则 htmlType 覆盖为 switch |
| isSortColumn() | 判断字段名是否匹配排序字段命名约定：后缀 sort/order_num/order/rank/seq/sequence | 满足则 htmlType 覆盖为 inputNumber（数字输入控件） |
| Java 类型（javaType） | 生成 Java 代码中的字段类型：String、Integer、Long、Double、BigDecimal、Boolean、LocalDateTime | 每个字段导出为 gen_table_column.javaType，驱动 Domain/VO/BO 中的类型声明和 import 语句 |
| HTML 控件类型（htmlType） | 生成前端页面中的表单控件类型：input、textarea、select、radio、checkbox、datetime、switch、inputNumber、imageUpload、fileUpload、editor | 每个字段在 gen_table_column.htmlType 中存储，驱动前端页面模板中的控件选择 |
| 查询方式（queryType） | 生成后端查询条件的匹配方式：EQ（精确）、LIKE（模糊）、BETWEEN（范围） | 控制生成的 Mapper XML 和 BO 中查询条件的 SQL 写法 |
| 参与场景开关（isInsert/isEdit/isList/isQuery） | 四个布尔字段，控制该列是否在新增表单、编辑表单、数据列表、查询条件中出现 | 黑名单机制排除系统字段（create_time、update_by 等）和主键字段，其余默认全部参与 |
| TemplateEngineUtils | 模板引擎核心工具类，负责 FreeMarker 初始化、上下文构建（buildContext）、模板列表组装（getTemplateList）、输出文件名计算（getFileName） | gen 模块中信息密度最高的类，连接 GenTable 领域模型与 FreeMarker 模板之间的所有转换逻辑 |
| buildContext() | 将 GenTable 对象的所有信息展开为扁平的 FreeMarker 键值字典 | 是模板渲染前的最后一步数据转换，输出 30+ 个模板变量 |
| setColumnFeatureContext() | 预扫描所有列的 htmlType，生成 needEditor、needImageUpload 等布尔特征开关 | 让模板只需一个 if 判断，避免在模板中遍历 columns 列表做复杂过滤 |
| getTemplateList() | 按 tplCategory + frontendType + 数据库类型三维组合，选择 13~16 个模板文件 | 下载和预览代码时调用，决定本次生成使用哪些模板 |
| PathNamedTemplate | 模板包装器，将 FreeMarker Template 对象与模板路径名（pathName）绑定 | 装饰器模式实现：模板既知道自己是什么（pathName），又能执行渲染（delegate.render()） |
| getFileName() | 根据模板路径的模式匹配，计算生成文件的目标路径 | 决定渲染后的代码写入 ZIP 时的目录结构和文件名 |
| getFrontendPageExtension() | 从通配符匹配到的前端页面模板文件名中提取扩展名（.vue / .tsx / .svelte） | 支持前端页面模板的扩展名由文件名自描述，无需 Java 端维护映射表 |
| getFrontendPagePath() | React 页面放 pages 目录，其他前端类型放 views 目录 | 一个小巧的差异化逻辑，适配不同前端框架的目录约定 |
| setNumberFormat("computer") | FreeMarker 配置项，禁用数字千分位格式化 | 防止雪花 ID（19 位 Long）渲染成 "1,234,567,890" 非法字面量 |
| buildRenderContext() | GenTableServiceImpl 中构建渲染上下文的入口方法：查表→设主键→buildContext→选模板 | 预览和下载共享的渲染准备流程 |
| previewCode() / downloadCode() | 预览返回模板路径→代码内容的 Map；下载将渲染结果打包为 ZIP byte[] | 两者共享 buildRenderContext()，区别仅在于输出形式 |
| synchDb() | 同步数据库最新列结构：对比 gen_table_column 与 AnyLine 实时元数据，处理新增/删除/变更列 | 数据库表结构变更后，保持 gen_table_column 与真实数据库结构一致 |
| @Lock4j | 分布式锁注解，按指定 key（如数据源名）锁定，防止并发冲突 | importTableSave 使用 @Lock4j(keys={"#dataName"}) 防止同一数据源并发导入导致重复记录 |
| @RepeatSubmit | 防重复提交注解，基于 Redis 实现请求级去重 | importTableSave 使用该注解防止用户快速双击提交按钮 |
| Snowflake 雪花 ID | 分布式唯一 ID 生成算法，产出 19 位 Long 型 ID | RuoYi-Vue-Plus 表主键使用雪花 ID，因此 FreeMarker 必须设置 setNumberFormat("computer") |
| BaseEntity | MyBatis-Plus 基础实体类，包含 createBy、createTime、updateBy、updateTime 等公共字段 | 生成的 Domain 类继承 BaseEntity，模板通过 isSuperColumn() 跳过这些字段的生成 |
| gen_ 前缀表 | gen 模块自身的数据表（gen_table、gen_table_column） | 导入表时过滤掉 gen_ 前缀的表，防止代码生成器导入自己的配置表 |
| fm/ 模板目录 | FreeMarker 模板文件的根目录，位于 ruoyi-gen/src/main/resources/fm/ | 按子目录组织：java/（后端）、vue/、react/（前端）、sql/（菜单 SQL）、xml/（Mapper XML） |
| 字典类型（dictType） | gen_table_column 中的字段，关联系统字典表，值为字典类型编码 | 前端生成时根据 dictType 为目标控件（select/radio/checkbox/switch）添加字典数据源绑定 |
| isDictColumn() | 判断当前列是否属于字典控件列：已配置 dictType 且 htmlType 支持字典（select/radio/checkbox/switch） | 决定是否生成字典翻译相关代码（前端字典请求、后端字典转换） |
| getTsType() | 返回 TypeScript 类型（string / number / boolean） | types.ts.ftl 模板中为每个字段自动输出正确的 TS 类型声明 |
| 树表（TPL_TREE） | 支持树形结构数据的模板分类，需要配置 treeCode、treeParentCode、treeName 参数 | 生成时使用 index-tree 页面模板，Domain 继承 TreeEntity，包含 parentId 等树形字段 |
| generator.yml | gen 模块的全局配置文件，定义 author、packageName、autoRemovePre、tablePrefix 等默认值 | 导入表时 GenUtils.initTable() 从此配置读取默认值填充 gen_table |
| 表前缀移除（autoRemovePre / tablePrefix） | 导入表时自动从表名中去除前缀（如 sys_），转换为类名 | 例如 sys_user 移除 sys_ 后类名为 User |
| Hutool TemplateUtil | Hutool 工具包对多种模板引擎的统一封装 | TemplateEngineUtils 通过 TemplateUtil.createEngine() 创建 FreeMarker 引擎实例 |
| 元数据驱动代码生成 | 代码生成器设计范式：以数据库元数据（表结构、列信息）为输入，驱动模板渲染产出代码 | ruoyi-gen 的核心设计理念，区别于硬编码的代码脚手架 |

# ruoyi-common-excel Excel 模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**Fesod Sheet**：
本模块的基石框架。对 Apache POI 的高层封装，提供注解驱动的 Excel 读写、转换器（Converter）扩展点、写处理器（WriteHandler）链、事件监听（AnalysisEventListener）等。本模块通过实现 Fesod Sheet 的 Converter / WriteHandler / ReadListener 接口来注入项目级能力，而不是直接操作 POI 的低层 API。
_Avoid_: "POI"（Fesod Sheet 是 POI 的上层封装，本模块代码几乎不直接 import POI 类）。

**Converter（转换器）**：
Fesod Sheet 定义的类型转换扩展点（`org.apache.fesod.sheet.converters.Converter<T>`）。声明 `supportJavaTypeKey()`（支持什么 Java 类型）、`convertToJavaData()`（Excel 单元格 -> Java 字段）、`convertToExcelData()`（Java 字段 -> Excel 单元格）。本模块注册了 3 个自定义 Converter：`ExcelBigNumberConvert`、`ExcelDictConvert`、`ExcelEnumConvert`。
_Avoid_: "类型转换器"（泛称，本模块专指 Fesod Sheet 的 Converter 体系）。

**WriteHandler（写处理器）**：
Fesod Sheet 的写入生命周期钩子。`SheetWriteHandler` 在 Sheet 创建后回调（适合做下拉校验、合并区域）；`CellWriteHandler` 在单元格写入后回调（适合做样式、批注）。本模块的 `CellMergeStrategy`、`ExcelDownHandler`、`DataWriteHandler` 都实现了这些接口，通过 `registerWriteHandler()` 挂载到导出链上。
_Avoid_: "写拦截器"（它是扩展点回调，不是 AOP 拦截器）。

**AnalysisEventListener（解析事件监听器）**：
Fesod Sheet 的读取生命周期接口。每解析一行数据回调 `invoke(data, context)`，全解析完回调 `doAfterAllAnalysed()`，发生异常回调 `onException()`。本模块的 `DefaultExcelListener` 实现它，是导入链路的核心。

**@CellMerge**：
自定义注解（`annotation/CellMerge.java`）。标注在实体字段上，表示导出 Excel 时该列需要合并连续相同值的单元格。`index` 指定列索引（-1 时自动推断），`mergeBy` 声明合并需依赖的其他字段（如合并"部门名称"时必须同"部门编号"才合并）。由 `CellMergeHandler` 解析，由 `CellMergeStrategy` 执行。
_Avoid_: "合并单元格注解"（它是列值重复合并，不是任意区域合并）。

**@ExcelDictFormat**：
自定义注解（`annotation/ExcelDictFormat.java`）。标注字段的字典转换规则。`dictType` 指定字典类型（如 `sys_user_gender`），走项目字典服务查库；`readConverterExp` 指定内联转换表达式（如 `0=男,1=女,2=未知`），不走库。导出时将编码转标签，导入时将标签反转回编码。由 `ExcelDictConvert` 和 `ExcelDownHandler` 消费。

**@ExcelEnumFormat**：
自定义注解（`annotation/ExcelEnumFormat.java`）。标注字段的枚举转换规则。`enumClass` 指定枚举类，`codeField` / `textField` 指定枚举中表示"编码"和"文本"的属性名（默认 `code` / `text`）。由 `ExcelEnumConvert` 消费，内部用 `ConcurrentHashMap` 缓存枚举映射避免重复反射。

**@ExcelDynamicOptions**：
自定义注解（`annotation/ExcelDynamicOptions.java`）。标注字段的下拉数据来源为一个运行时提供者。`providerClass` 指定 `ExcelOptionsProvider` 接口的实现类，由 Spring 容器获取实例并调用 `getOptions()` 返回 `Set<String>`。适合「下拉选项来自数据库」的场景（如动态部门列表），不需要在注解上写死。

**@ExcelRequired**：
自定义注解（`annotation/ExcelRequired.java`）。标注必填列，导出模板时将该列表头字体标红（默认 `IndexedColors.RED`），提示用户该列必填。仅作用于视觉效果，不参与校验逻辑。由 `DataWriteHandler` 消费。

**@ExcelNotation**：
自定义注解（`annotation/ExcelNotation.java`）。标注列头批注，导出模板时在表头单元格添加批注（Comment），内容为注解的 `value`。仅用于单表头场景。由 `DataWriteHandler` 消费。

**DropDownOptions（下拉选项）**：
POJO（`core/DropDownOptions.java`）。描述 Excel 导出时的下拉选项配置：`index` / `nextIndex` 指定一级和二级下拉所在列，`options` 是一级选项列表，`nextOptions` 是二级选项 Map（一级值 -> 对应的二级列表）。支持通过 `buildLinkedOptions()` 从业务实体列表自动构建级联结构。

**ExcelDownHandler（下拉处理器）**：
`core/ExcelDownHandler.java`，实现 `SheetWriteHandler`。在 Sheet 创建后遍历所有字段的注解（`@ExcelDictFormat` / `@ExcelEnumFormat` / `@ExcelDynamicOptions`），为每列生成 Excel 数据校验下拉。选项少时用 POI 的显式列表约束（`createExplicitListConstraint`），选项多时转为隐藏 Sheet + 名称管理器（`createFormulaListConstraint`），避免 Excel 打开缓慢。

**CellMergeHandler（合并分析器）**：
`core/CellMergeHandler.java`，静态工厂类。扫描实体类上所有带 `@CellMerge` 的字段，按数据行逐一比对相邻行的字段值，相同时记录为 `CellRangeAddress` 合并区域。支持 `mergeBy` 依赖字段——只有当依赖字段也相同时才合并。

**CellMergeStrategy（合并执行器）**：
`core/CellMergeStrategy.java`，继承 Fesod Sheet 的 `AbstractMergeStrategy`，实现 `SheetWriteHandler`。在 `afterSheetCreate` 中提前写入合并区域（防止后续数据写入覆盖），在 `merge()` 中清理合并区域内非首行的重复值（设 `cell.setBlank()`）。

**DataWriteHandler（批注必填处理器）**：
`handler/DataWriteHandler.java`，同时实现 `SheetWriteHandler` 和 `CellWriteHandler`。在导出时扫描 `@ExcelRequired` 将表头字体标红、扫描 `@ExcelNotation` 添加 POI 批注。仅在表头行（`context.getHead()` 为 true）时生效，数据行不做处理。

**ExcelBuilder（导出构造器）**：
`utils/ExcelBuilder.java`，整个模块的**唯一对外 API**。链式调用 DSL，提供 `of()`（列表导出）、`writer()`（自定义写出）、`template()`（模板导出）、`read()`（导入）四个静态入口。导出时将 `ExcelBigNumberConvert`、`DataWriteHandler`、`ExcelDownHandler` 自动注册到 Fesod Sheet 的 WriterBuilder；开启 `merge()` 时自动注册 `CellMergeStrategy`。

**ExcelWriterWrapper（写出包装器）**：
`utils/ExcelWriterWrapper.java`，Java Record。对 Fesod Sheet 的 `ExcelWriter` 做一层安全包装，只暴露 `write()` / `fill()` 方法，隐藏 `finish()` 等不可控操作，防止业务代码提前关闭 IO 流。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。

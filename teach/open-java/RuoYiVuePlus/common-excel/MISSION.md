# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-excel Excel 导入导出模块

## Why
学习者要能彻底读懂 `ruoyi-common-excel` 这个公共模块：它基于 **Fesod Sheet**（Apache POI 的上层封装），提供了一套注解驱动的 Excel 导入导出能力，覆盖单元格合并、字典/枚举双向转换、大数字精度保护、下拉选项（含级联联动）、必填标注与批注等企业级高频需求。21 个 Java 文件、6 个注解、3 个转换器、7 个核心类、2 个工具类，构成了 RuoYi 整个后台管理系统的数据导入导出基础设施。理解它，等于掌握 RuoYi 如何把 Fesod Sheet 的通用能力"项目化"——注入项目字典服务、接入 Jakarta Validation、挂载自定义写处理器。达到能给同事讲清"从 Controller 一个 `@PostMapping` 到浏览器下载 Excel 文件，中间经过了哪些处理器""导入时为什么字典值能自动转回编码"，并能照葫芦画瓢为新业务加导出列或自定义校验。

## Success looks like
- 能用一句话说清 `ruoyi-common-excel` 与 Fesod Sheet 的关系，并画出模块的"注解层 - 转换器层 - 处理器层 - 工具层"四层架构。
- 能逐一解释 6 个自定义注解（`@CellMerge`, `@ExcelDictFormat`, `@ExcelEnumFormat`, `@ExcelDynamicOptions`, `@ExcelRequired`, `@ExcelNotation`）各自挂在哪一层、最终由哪个处理器/转换器消费。
- 能讲清 `ExcelDictConvert` 如何判断走字典服务（`dictType`）还是走表达式解析（`readConverterExp`），以及导入时为什么能把"男"转回 `"0"`。
- 能讲清 `ExcelEnumConvert` 的双 Map 缓存策略（`ENUM_MAP_CACHE` / `ENUM_REVERSE_MAP_CACHE`）如何避免反射开销，以及导入时如何校验"填的值必须在枚举定义范围内"。
- 能完整追踪导出链路：`ExcelBuilder.of(data, clazz).toResponse(response)` → `createWriterBuilder`（注册 BigNumberConvert + DataWriteHandler + ExcelDownHandler）→ `writeSheet`（可选注册 CellMergeStrategy）→ `builder.doWrite(data)`，并说出每一环的关键类。
- 能完整追踪导入链路：`ExcelBuilder.read(inputStream, clazz).doRead()` → `DefaultExcelListener`（逐行 validate + 收集）→ `ExcelResult.getAnalysis()` 返回"成功 X 条，错误 Y 条"的回执。
- 能讲清 `ExcelDownHandler` 如何处理四种下拉数据源（`@ExcelDictFormat` / `@ExcelEnumFormat` / `@ExcelDynamicOptions` / 外部传入 `DropDownOptions`），以及"选项 > 20 个或总字符超 255 时切换为隐藏 Sheet 方案"的原因。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，涉及前端时仅点到 Controller 的 `MultipartFile` 接收和 `HttpServletResponse` 写出。
- 目标是「读懂设计动机与调用链」而非「手写一个 Excel 框架」——课程以追踪真实代码、解释为什么这样设计为主，练习以「读代码答问题 / 填调用链空白」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- Apache POI 底层 API（`Workbook`, `Sheet`, `Cell`, `CellStyle` 等）的全面讲解——只在涉及合并区域、下拉校验等 Fesod Sheet 未完全封装的部分点到为止。
- Fesod Sheet 框架本身的源码分析——只讲项目如何调用其 API，不讲 Fesod Sheet 内部实现。
- 字典服务 `DictService` 的完整实现（属于 `ruoyi-common-core`）——仅在 `ExcelDictConvert` 和 `ExcelDownHandler` 调用它时点到。
- Jakarta Validation 的完整注解体系——仅在 `DefaultExcelListener.invoke()` 调用 `ValidatorUtils.validate()` 时点到。
- 前端 Excel 上传/下载组件的实现细节。

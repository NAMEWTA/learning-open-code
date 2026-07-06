# ruoyi-common-excel Excel 模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（含 Fesod Sheet 依赖源码）。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-excel 模块全部 21 个 Java 文件_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-excel/src/main/java/org/dromara/common/excel/)
  注解层 6 个：`annotation/CellMerge.java`, `ExcelDictFormat.java`, `ExcelEnumFormat.java`, `ExcelDynamicOptions.java`, `ExcelRequired.java`, `ExcelNotation.java`；转换器层 3 个：`convert/ExcelBigNumberConvert.java`, `ExcelDictConvert.java`, `ExcelEnumConvert.java`；核心处理器 7 个：`core/DefaultExcelListener.java`, `ExcelListener.java`, `ExcelResult.java`, `DefaultExcelResult.java`, `CellMergeStrategy.java`, `CellMergeHandler.java`, `ExcelDownHandler.java`, `DropDownOptions.java`, `ExcelOptionsProvider.java`；工具类 2 个：`utils/ExcelBuilder.java`, `ExcelWriterWrapper.java`；写处理器 1 个：`handler/DataWriteHandler.java`。任何关于「这个模块做了什么」的问题，最终答案在这些文件里。

- [代码: _Fesod Sheet 源码_](file:///Users/wta/.m2/repository/org/apache/fesod/)
  `Converter` 接口、`AnalysisEventListener`、`SheetWriteHandler`、`CellWriteHandler`、`AbstractMergeStrategy` 等接口和基类。理解「为什么这 21 个文件这样组织」时对照查阅。Fesod Sheet 是 Apache POI 的高层封装，本项目通过实现其扩展点（Converter / WriteHandler / ReadListener）来注入项目级能力。

- [代码: _Excel 导入导出真实使用现场_](RuoYi-Vue-Plus/ruoyi-admin/src/main/java/org/dromara/web/controller/)
  各业务 Controller 中的导出方法（`@PostMapping("/export")`）和导入方法（`@PostMapping("/importData")`），构成完整的业务闭环。`SysUserController`, `SysPostController` 等都有典型的导入导出调用。

- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明，含 Excel 导入导出章节。理解模块在整体架构中的位置时查阅。

- [官方文档: _Apache POI 官方文档_](https://poi.apache.org/components/spreadsheet/)
  理解底层 `CellRangeAddress`, `DataValidation`, `Name` 等概念时查阅。Fesod Sheet 对 POI 做了大量封装，但合并区域和下拉校验仍直接操作 POI API。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「导出大文件 OOM」「下拉选项不生效」「合并单元格位置偏移」等实际问题时，Issues 与讨论区最贴近维护者意图。

## Gaps
- Fesod Sheet 官方文档较少，其 API 用法主要通过本仓库代码和 Fesod Sheet sources jar 学习。
- `ExcelDownHandler` 中级联下拉的 Excel 名称管理器机制较复杂，需结合 Excel 的 INDIRECT 函数理解——这部分在课程第 4 课有详细拆解。

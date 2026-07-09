# 主题研报批量检索全链路 资源

## 知识

- [a-stock-data SKILL.md — 流程 C: 主题研报批量检索（2473-2502行）](../../../open-trading/a-stock-data/SKILL.md#L2473)
  完整的多关键词 iwencai 搜索 + 东财 PDF 补充代码。适用于：快速复制全链路模板，替换关键词列表即可运行。

- [a-stock-data SKILL.md — iwencai 语义搜索 + 去重（705-808行）](../../../open-trading/a-stock-data/SKILL.md#L705)
  `iwencai_search()` 和 `dedup_articles()` 的完整实现，包含 X-Claw 鉴权头构造和 30s 超时处理。适用于：理解 iwencai API 调用规范。

- [a-stock-data SKILL.md — 东财研报 API + PDF 下载（534-668行）](../../../open-trading/a-stock-data/SKILL.md#L534)
  `eastmoney_reports()` 和 `download_pdf()` 的完整实现，含翻页逻辑、Referer 鉴权、PDF 模板拼 URL。适用于：东财数据源的翻页和 PDF 下载规范。

- [a-stock-data SKILL.md — em_get 防封限流（115-148行）](../../../open-trading/a-stock-data/SKILL.md#L115)
  东财接口统一节流入口，3秒间隔。适用于：理解为什么批量 PDF 下载需要耐心等待。

- [a-stock-data SKILL.md — 行业研报 qType=1 变体（614-668行）](../../../open-trading/a-stock-data/SKILL.md#L614)
  同一 `reportapi.eastmoney.com/report/list` 端点，`qType=1` 拉行业研报。适用于：主题研究时补充行业层面观点。

## 智慧（社区）

- [a-stock-data GitHub Issues](https://github.com/simonlin1212/a-stock-data/issues)
  项目问题反馈和讨论区。适用于：iwencai key 申请、接口变动等实际使用问题。

- [iwencai 开放平台文档](https://openapi.iwencai.com/doc)
  iwencai 官方 API 文档（需登录）。适用于：查询 channel 参数、size 上限等接口细节。

## 空白

- iwencai 搜索结果的 score 字段计算逻辑不透明（语义相关度? 时效性加权?），暂无公开文档说明。
- 主题关键词扩展策略（如同义词、产业链上下游术语）暂无系统化工具推荐，目前依赖人工构建 query 列表。

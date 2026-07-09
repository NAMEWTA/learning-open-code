# 使命：研报层

## 为什么
学习者需要从机构研报中提取决策参考信息——个股评级、三年EPS预测、行业趋势判断、以及通过自然语言搜索发现概念关联，用于搭建量化投研的机构视角数据层。东财reportapi免费且覆盖最全，同花顺提供机构一致预期作为交叉验证，iwencai的NL搜索能力是唯一能做"人形机器人 行星滚柱丝杠"这种跨主题检索的数据源。

## 成功的样子
- 能用 `eastmoney_reports()` 拉取任意A股的研报列表，读懂评级和三年EPS预测字段
- 能用 `download_pdf()` 下载研报PDF，理解Referer鉴权机制和文件名清洗的必要性
- 能用 `eastmoney_industry_reports()` 切换 qType 拉取行业研报，并通过全行业查询发现行业码
- 能用 `ths_eps_forecast()` 获取同花顺机构一致预期EPS，区分均值与最小值列
- 能用 `iwencai_search()` 执行自然语言语义搜索研报，理解 X-Claw 鉴权和去重逻辑
- 知道本层所有东财端点统一走 `em_get()` 限流保护

## 约束条件
- 学习时间：每天 30-60 分钟
- 基础要求：Python requests/pandas 基础，了解 A 股基本面概念（EPS、PE、评级）
- 环境：需安装 requests + pandas + lxml（同花顺HTML解析）

## 不在范围内
- 不涉及研报内容的自然语言处理或情感分析
- 不涉及基于研报数据的自动交易策略
- 不涉及 iwencai API Key 的申请流程

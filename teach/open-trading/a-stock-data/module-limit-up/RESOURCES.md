# 打板层 资源

## 知识

- [SKILL.md 打板层章节 (§8.1-§8.3)](https://github.com/simonlin1212/a-stock-data/blob/main/SKILL.md)
  打板层完整代码块：东财四池（zt/zb/dt/yzt）+ `_em_zt_api()` helper、同花顺 `ths_limit_up_pool()`、`limit_up_sentiment()` 情绪速算。适用于：复制即用的代码参考、字段含义速查、已知坑点列表。

- [东方财富涨停板行情中心](https://quote.eastmoney.com/)
  东财四池的数据源头——涨停池、炸板池、跌停池、昨涨停池的 web 端展示。适用于：理解 push2ex 接口背后的业务逻辑，验证接口返回数据。

- [同花顺涨停揭秘](https://data.10jqka.com.cn/)
  同花顺涨停原因题材与封板成功率的数据源头。适用于：理解 `field` 参数背后的内部字段编码，验证题材归因数据。

- [a-stock-data 项目源码](https://github.com/simonlin1212/a-stock-data)
  项目完整代码仓库——`a_stock_data/api/eastmoney/limit_up.py` 为打板层实现文件。适用于：查看完整实现细节、了解异常处理逻辑。

## 智慧（社区）

- [a-stock-data GitHub Issues](https://github.com/simonlin1212/a-stock-data/issues)
  项目问题追踪，含涨停板池数据源变更、push2ex 限流策略讨论等实测反馈。适用于：了解已知坑点、参与功能改进讨论。

- [淘股吧（TGB）打板交流](https://www.taoguba.com.cn/)
  国内最大的短线交易社区，打板/连板/龙头战法讨论活跃。适用于：检验打板情绪指标在实际交易中的有效性，获取社区实战经验。

## 空白

- 缺少东方财富 push2ex 接口的官方文档——`_em_zt_api()` 端点与参数来自网络抓包分析，字段编码靠实测推演
- 缺少同花顺数据接口的官方文档——`field` 参数内部 ID（如 `330324`、`133971`）无公开说明，照抄即可
- 缺少涨停板数据在中国量化交易中的学术研究参考文献——目前仅有社区实战经验，缺少严谨的回测统计

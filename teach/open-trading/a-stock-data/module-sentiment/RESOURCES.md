# 舆情互动层 资源

## 知识

- [SKILL.md 舆情互动层章节 (§10.1-§10.2)](https://github.com/simonlin1212/a-stock-data/blob/main/SKILL.md)
  舆情层完整代码块：cninfo_irm() 互动易两步请求、ths_hot_list() 同花顺热榜、em_hot_rank() 东财人气榜、em_hot_concept() 个股概念命中。适用于：复制即用的代码参考、字段含义速查。

- [巨潮资讯网 irm.cninfo.com.cn](https://irm.cninfo.com.cn/)
  深沪两市官方投资者互动平台。互动易问答的第一手数据源。适用于：理解互动易的数据结构和提问/回复机制。

- [同花顺热榜 dq.10jqka.com.cn](https://dq.10jqka.com.cn/fuyao/hot_list_data/out/hot_list/v1/stock)
  同花顺热门股票排行，含人气值、概念标签、排名变化。适用于：了解市场短期关注焦点、热点概念轮动。

- [东方财富人气榜](https://emappdata.eastmoney.com/stockrank/)
  东财端内的个股人气排名体系，含排名变化、热门概念命中。适用于：与同花顺热榜交叉验证热点强度。

## 智慧（社区）

- [a-stock-data GitHub Issues](https://github.com/simonlin1212/a-stock-data/issues)
  项目问题追踪，含互动易 orgId 解析、东财人气榜前缀代码补全等实测反馈。适用于：了解已知坑点、贡献修复。

- [TradingAgents 社区](https://github.com/simonlin1212/TradingAgents-astock)
  a-stock-data 的上层消费项目——AI 驱动的 A 股投研 Agent。适用于：看舆情层在实际 AI Agent 中如何用于"公司回应传闻""热点概念归因"等场景。

## 空白

- 缺少巨潮互动易 API 的官方文档——cninfo_irm() 的两步请求链路靠抓包分析推演
- 缺少同花顺热榜接口的官方说明——字段含义（如 rate/hot_rank_chg/concept_tag）靠实测校准
- 缺少东方财富人气榜 getHotStockRankList 端点的官方文档——个股概念命中逻辑为逆向工程
- 缺少舆情数据与股价走势的量化相关性研究——三源热度交叉验证的统计显著性需进一步分析

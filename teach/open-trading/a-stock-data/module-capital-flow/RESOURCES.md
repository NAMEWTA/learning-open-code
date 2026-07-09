# 资金面/筹码层 资源

## 知识

- [a-stock-data SKILL.md §Layer 4 资金面/筹码层](https://github.com/nicedoc/learning-open-code/blob/main/open-trading/a-stock-data/SKILL.md#layer-4-%E8%B5%84%E9%87%91%E9%9D%A2--%E7%AD%B9%E7%A0%81%E5%B1%82v30-%E6%96%B0%E5%A2%9E) — 5 个端点的完整源码与使用示例（SKILL.md:1390-1586）
- [东方财富数据中心 — 融资融券](https://data.eastmoney.com/rzrq/) — 融资融券余额、买入/偿还的原始数据页面
- [东方财富数据中心 — 大宗交易](https://data.eastmoney.com/dzjy/) — 大宗交易明细的官方数据门户
- [东方财富数据中心 — 股东户数](https://data.eastmoney.com/gdhs/) — 股东户数变化的季度数据
- [东方财富 — 个股资金流向](https://data.eastmoney.com/zjlx/) — 主力/大单/中单/小单资金流的可视化页面

## 智慧（社区）

- [聚宽量化社区 — 资金面因子](https://www.joinquant.com/) — 融资余额变化率、股东户数变化率等因子的量化策略讨论
- [雪球 — 筹码分析](https://xueqiu.com/) — 散户与机构持仓分析的实战讨论（搜索"股东户数"或"筹码集中度"）
- [集思录 — 融资融券数据](https://www.jisilu.cn/) — 两融余额趋势、分级基金与杠杆资金分析社区

## 空白

- 融资融券数据的盘中实时更新：当前 datacenter 源为日级快照，盘中的融资买入/偿还变化无法获取，需寻找盘中实时数据源
- 股东户数的日级数据：当前为季度级（RPT_HOLDERNUMLATEST），日级高频数据仅东财 Level-2 提供
- 资金流120日的回测有效性：主力净流入与未来收益的相关性需要用户自行验证，暂无内置回测框架

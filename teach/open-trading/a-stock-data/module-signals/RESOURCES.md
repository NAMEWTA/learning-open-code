# 信号层 资源

## 知识

- [a-stock-data SKILL.md §Layer 3 信号层](https://github.com/nicedoc/learning-open-code/blob/main/open-trading/a-stock-data/SKILL.md#layer-3-%E4%BF%A1%E5%8F%B7%E5%B1%82) — 8 个信号端点的完整源码与使用示例
- [同花顺数据开放平台](https://data.10jqka.com.cn/) — 同花顺热点接口的数据来源背景
- [东方财富数据中心](https://data.eastmoney.com/) — 东财 datacenter 的原始数据门户（龙虎榜、解禁、大宗交易等）
- [沪深港通资金流向](https://data.eastmoney.com/hsgt/index.html) — 北向资金官方数据页面（注意：东财页面的历史数据可能比 hexin API 更全）

## 智慧（社区）

- [聚宽量化社区](https://www.joinquant.com/) — 量化交易因子讨论，可对比信号层端点的因子构建思路
- [BigQuant 社区](https://bigquant.com/) — AI 量化平台，有龙虎榜因子、北向资金因子的实战分享

## 空白

- 同花顺热点 reason tags 的完整标签字典：已知是编辑部人工标注，但未见官方标签体系文档
- 东财板块归属的行业分类标准（申万/中信/东财自研？）：当前方案直接用板块名自解释，未做精确分类
- 北向资金自缓存的长期回测效果：本地 CSV 模式首次仅当天数据，需实际运行积累后方可评估历史覆盖

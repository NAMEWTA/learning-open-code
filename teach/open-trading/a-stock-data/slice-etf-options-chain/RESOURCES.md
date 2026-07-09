# ETF期权链分析全链路 资源

## 知识

- [a-stock-data SKILL.md -- ETF期权层(Layer 9)](https://github.com/simonlin1212/a-stock-data/blob/main/SKILL.md) — V3.3.0 新增期权层完整源码，包含 sina_option_codes/tquote/greeks 三个核心函数、字段映射表和 4 个踩坑说明
- [L1 module-options 模块导览](../module-options/lessons/0001-options-module-tour.html) — ETF期权层入门课，讲解三个函数的参数、返回值与希腊字母基本含义
- [L1 module-options 速查表](../module-options/reference/options-overview.html) — 合约清单流程、T 型报价 17 字段索引、希腊字母 13 字段索引、6 个已知坑点汇总
- [CBOE VIX 白皮书](https://www.cboe.com/tradable_products/vix/vix_white_paper.pdf) — VIX 指数方法论，理解 IV（隐含波动率）计算原理的权威来源
- [期权希腊字母入门 (Investopedia)](https://www.investopedia.com/trading/greeks/) — 对 Delta/Gamma/Theta/Vega/Rho 的通俗解释，适合不熟悉期权的开发者速览

## 智慧（社区）

- [a-stock-data Issues](https://github.com/simonlin1212/a-stock-data/issues) — 新浪期权接口变更、字段失效的反馈渠道
- [集思录 期权论坛](https://www.jisilu.cn/) — 国内期权交易者社区，讨论 IV 偏度、合成期货等实战话题
- [上海证券交易所 ETF 期权专区](https://www.sse.com.cn/assortment/options/etf/) — 官方合约规格、行权价列表、保证金规则

## 空白

- 新浪源返回的数据质量（实时性、准确性）与交易所原生接口的对比尚未覆盖
- IV 曲面（跨月份 IV 形态）的可视化方法未涉及
- 期权链分析结果的自动化报告模板（HTML/JSON）尚未建立
- 希腊字母的本地 BSM 重算（对比新浪预计算值）未覆盖——仅简述了"交易所预计算"的优势

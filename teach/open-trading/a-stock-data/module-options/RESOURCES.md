# ETF期权层 资源

## 知识

- [SKILL.md ETF期权层章节 (§9)](https://github.com/simonlin1212/a-stock-data/blob/main/SKILL.md)
  ETF期权层完整代码块：sina_option_codes()、sina_option_tquote()、sina_option_greeks()、_sina_opt_list()。适用于：复制即用的代码参考、字段含义速查、4 个关键踩坑点。

- [新浪财经股票期权页面](https://stock.finance.sina.com.cn/option/)
  新浪期权的 Web 端展示——T 型报价、希腊字母、IV 的可视化版本。适用于：理解 T 型报价的视觉布局、验证 API 返回数据。

- [上海证券交易所 — 股票期权](https://www.sse.com.cn/assortment/options/)
  上交所期权合约规格、交易规则、做市商制度。适用于：理解合约月份规则、行权价格间距、到期日计算。

- [CBOE 期权教育 — 希腊字母](https://www.cboe.com/education/)
  CBOE 官方期权教育资源，涵盖 Delta/Gamma/Theta/Vega 的概念解释和实战案例。适用于：深入理解希腊字母在风险管理中的物理含义（中文课程侧重 API 使用，此资源补概念深度）。

## 智慧（社区）

- [a-stock-data GitHub Issues](https://github.com/simonlin1212/a-stock-data/issues)
  项目问题追踪，含 V3.3.0 期权层新增反馈、新浪源可用性变化等。适用于：了解已知坑点、跟踪新浪源稳定性。

- [期权论坛 — 期权酱](https://www.optionjiang.com/)
  中文期权投资者社区，含期权链分析、IV 偏度讨论、希腊字母实战案例。适用于：检验数据理解、讨论期权策略时参考。

## 空白

- 缺少新浪 hq.sinajs.cn 期权接口的官方文档——`_sina_opt_list()` 的字段映射完全靠实测推演，字段含义依赖逐位校准
- 缺少不同交易所（上交所 vs 深交所）期权合约的差异对比文档——当前 4 只 ETF 期权均为上交所品种
- 缺少隐含波动率偏度（IV Skew）和期限结构（Term Structure）的自动化分析函数——当前仅提供原始数据拉取

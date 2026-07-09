# 基础数据层 资源

## 知识

- [a-stock-data SKILL.md §6 基础数据层 (L1720-1857)](../../open-trading/a-stock-data/SKILL.md) — 源码级知识源，包含 mootdx finance()/F10()、eastmoney_stock_info()、sina_financial_report() 的完整实现与参数说明
- [mootdx 官方文档](https://github.com/rainx/mootdx) — 通达信 Python 客户端库，finance() 和 F10() 的原始 API 参考
- [mootdx 0.11.x BESTIP Bug 说明](https://github.com/rainx/mootdx/issues) — 为什么不能直接用 `Quotes.factory(market='std')`，必须使用项目内置的 tdx_client() 包装函数
- [东方财富 push2 API 字段映射](https://push2.eastmoney.com/api/qt/stock/get) — eastmoney_stock_info() 的原始数据源，fields 参数 f57/f58/f84/f85/f127/f116/f117/f189/f43 的字段含义
- [新浪财经财报 API](https://quotes.sina.cn/cn/api/openapi.php/CompanyFinanceService.getFinanceReport2022) — sina_financial_report() 的原始数据源，report_list 结构说明
- [通达信 finance() 函数 37 字段完整速查](https://rainx.gitbooks.io/mootdx/content/) — 包含 liutongguben/zongguben/eps/bvps/roe/profit/income 等完整列表
- [a-stock-data SKILL.md §3 Prerequisites (L98-188)](../../open-trading/a-stock-data/SKILL.md) — UA 常量、em_get() 限流核心函数与 tdx_client() 包装函数

## 智慧（社区）

- [mootdx GitHub Issues](https://github.com/rainx/mootdx/issues) — 通达信协议变更、字段新增、版本兼容性问题讨论
- [聚宽 JoinQuant 社区](https://www.joinquant.com/help) — 财务因子选股思路讨论，可作为跨源数据拼装的实战案例参考
- [Tushare 社区](https://tushare.pro/) — 财务数据 API 设计参考，可用于对比不同数据源的字段覆盖度

## 空白

- 东方财富 push2 API 完整字段文档（网上多为社区逆向整理，无官方文档）
- 新浪财报 API 的 report_type 参数完整列表与版本变更历史
- 通达信 finance() 37 字段的官方定义文档（字段名来自 Python 库的字段映射）
- F10 九大类数据的结构化解析方案（当前仅提供原始文本，无 NER/语义解析工具）

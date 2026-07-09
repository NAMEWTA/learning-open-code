# A 股多源数据获取链路 资源

## 知识

- [TradingAgents-Astock CLAUDE.md](../../../open-trading/TradingAgents-astock/CLAUDE.md) — 项目架构、数据源表、已知问题与注意事项
- [interface.py](../../../open-trading/TradingAgents-astock/tradingagents/dataflows/interface.py) — VENDOR_METHODS 路由注册表 + route_to_vendor 降级链（230 行）
- [a_stock.py](../../../open-trading/TradingAgents-astock/tradingagents/dataflows/a_stock.py) — A 股 17 个数据方法实现 + _em_get 防封限流 + mootdx 客户端（2141 行）
- [utils.py](../../../open-trading/TradingAgents-astock/tradingagents/dataflows/utils.py) — safe_ticker_component 安全校验 + 中文 ticker 自动解析入口
- [config.py](../../../open-trading/TradingAgents-astock/tradingagents/dataflows/config.py) — 数据源配置与默认参数（32 行）
- [stockstats_utils.py](../../../open-trading/TradingAgents-astock/tradingagents/dataflows/stockstats_utils.py) — StockStats 技术指标计算适配 + yfinance OHLCV 加载
- [mootdx 官方文档](https://github.com/mootdx/mootdx) — 通达信 TCP 数据接口 Python 封装

## 智慧（社区）

- [TradingAgents-Astock Issues](https://github.com/simonlin1212/TradingAgents-astock/issues) — 数据层相关 issue（#46 中文 ticker 解析、#66 网络抖动提示优化）
- [通达信数据格式参考](https://www.tdx.com.cn/) — 通达信官方数据格式文档

## 空白

- 东财 API 反向工程文档 — 目前所有东财端点均为社区逆向，无官方文档
- 同花顺 API 字段完整说明 — `_ths_eps_forecast` 依赖 pd.read_html 解析，字段映射依赖经验
- 百度 PAE 接口稳定性 — 资金流接口已于 2026-05 下线（v0.2.7 迁移至东财 push2），其余端点未经验证长期 SLA

# 数据获取层模块 资源

## 知识

- [TradingAgents-Astock CLAUDE.md](https://github.com/simonlin1212/TradingAgents-astock/blob/main/CLAUDE.md)
  项目维护者编写的架构文档，包含数据层所有数据源表、中文股票名解析链路、东财防封限流机制的详细说明。适用于：理解数据层设计决策和已知问题。
- [mootdx 文档](https://github.com/fatcarter/mootdx)
  通达信 TCP 数据接口的 Python 封装。适用于：理解 OHLCV K 线、财务快照、F10 文本的获取方式。
- [东方财富数据中心 API](https://data.eastmoney.com/)
  东财 datacenter-web 和 push2 接口的官方入口。适用于：了解龙虎榜、限售解禁、板块行情等数据的字段定义。

## 智慧（社区）

- [TradingAgents-Astock Issues](https://github.com/simonlin1212/TradingAgents-astock/issues)
  项目 Issue 跟踪，包含数据源故障（百度 PAE 下线、东财风控封 IP 等）的根因分析和修复记录。适用于：了解数据源稳定性问题和社区驱动的修复方案。

## 空白

- 各数据源的官方 API 文档分散且部分无文档（腾讯 qt.gtimg.cn、新浪 money.finance 为内部接口），暂无统一规范文档
- 百度股市通 PAE 接口无公开文档，资金流接口已于 2026-05 下线（v0.2.7 已迁移至东财 push2）
- 同花顺 10jqka 接口为 HTML 抓取方式，无结构化 API 文档

# 使命：数据获取层模块——多源 A 股数据直连

## 为什么
理解 TradingAgents-Astock 如何在不依赖任何付费 API（如 Tushare）和第三方数据库（如 akshare）的前提下，通过 7 个免费数据源的 HTTP/TCP 直连，稳定获取 A 股行情、基本面、新闻、资金流等全维度数据。掌握这套数据层架构后，能够在自己的量化/投研项目中复刻类似的多源容错数据管道。

## 成功的样子
- 能画出 dataflows 模块在项目整体架构中的位置，说出它向上层 Agent 暴露了哪些数据方法
- 能解释 `interface.py` 的 vendor 路由模式（VENDOR_METHODS → route_to_vendor），以及如何新增一个数据源
- 能说出 7 个数据源各自的协议、数据类型和故障降级关系
- 能解释东财防封限流机制（`_em_get`）的设计原理和适用边界
- 能追踪一条"用户输入中文股票名 → 6 位代码 → 行情数据"的完整解析链路

## 约束条件
- 具备 Python 基础，了解 HTTP API 和数据获取的基本概念
- 学习时间：单节课 15 分钟内完成

## 不在范围内
- Agent 角色的 prompt 设计与辩论逻辑（见 module-agents）
- LangGraph 工作流图的节点编排与条件路由（见 module-graph）
- LLM 客户端工厂与 provider 路由（见 module-llm-clients）
- 技术指标计算的具体公式（StockStats 封装细节）

# 行情层 资源

## 知识

- [SKILL.md 行情层章节 (§1.1-§1.3)](https://github.com/simonlin1212/a-stock-data/blob/main/SKILL.md)
  行情层完整代码块：mootdx K线/bars()/frequency参数表、腾讯 tencent_quote() 88 字段索引、百度 baidu_kline_with_ma()。适用于：复制即用的代码参考、字段含义速查。

- [mootdx 官方文档 (pytdx)](https://github.com/rainx/pytdx)
  通达信 TCP 协议 Python 封装。适用于：深入理解 K 线 frequency 参数、quotes 46 个字段含义、transaction 逐笔成交结构。

- [腾讯财经 qt.gtimg.cn 行情接口分析（社区逆向）](https://blog.csdn.net/qq_26948675/article/details/132947808)
  腾讯行情接口字段索引与编码说明（GBK/`~`分隔/88字段）。适用于：理解 tencent_quote() 的字段映射逻辑。

- [stockstats 技术指标库](https://github.com/jealous/stockstats)
  基于 pandas 的技术指标计算库（MACD/RSI/BOLL/MA 等）。适用于：需要在百度 MA 均线基础上扩展更多指标。

## 智慧（社区）

- [a-stock-data GitHub Issues](https://github.com/simonlin1212/a-stock-data/issues)
  项目问题追踪，含 mootdx 0.11.x BESTIP bug、frequency 参数名修复等实测反馈。适用于：了解已知坑点、贡献修复。

- [TradingAgents 社区](https://github.com/simonlin1212/TradingAgents-astock)
  a-stock-data 的上层消费项目——AI 驱动的 A 股投研 Agent。适用于：看行情层在实际 AI Agent 中如何组合调用。

## 空白

- 缺少通达信 TCP 协议（TDX 7709 端口）的官方文档——mootdx 为社区逆向实现，数据字段含义靠实测推演
- 缺少百度股市通 API 的官方文档——baidu_kline_with_ma() 端点和参数来自网络抓包分析
- 缺少腾讯财经 qt.gtimg.cn 的官方说明——字段索引靠社区逐位校准

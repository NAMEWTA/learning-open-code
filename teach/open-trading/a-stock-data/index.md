# a-stock-data 教学主题索引

> A股全栈数据工具包 — 10层架构 · 40端点 · 13数据源 · 零第三方数据封装依赖
>
> 最后更新：2026-07-09

---

## 教学主题列表

| 序号 | 主题目录 | 层级 | 标题 | 状态 |
|------|---------|------|------|------|
| 1 | `00-overview/` | L0 | a-stock-data 项目总览 — 10层架构与核心设计哲学 | ✅ 已完成 |
| 2 | `module-market-data/` | L1 | 行情层三源体系：mootdx K线+五档盘口、腾讯PE/PB/市值、百度K线MA均线 | ✅ 已完成 |
| 3 | `module-research/` | L1 | 研报层：东财研报+PDF下载、同花顺一致预期EPS、iwencai语义搜索 | ✅ 已完成 |
| 4 | `module-signals/` | L1 | 信号层 — 8端点覆盖题材归因→资金验证→席位跟踪→风险预警完整信号链 | ✅ 已完成 |
| 5 | `module-infrastructure/` | L1 | 基础设施：em_get限流、tdx_client连接、市场前缀与数据源优先级 | ✅ 已完成 |
| 6 | `module-capital-flow/` | L1 | 资金面/筹码层 — 融资融券、大宗交易、股东户数、分红送转、主力资金流120日 | ✅ 已完成 |
| 7 | `module-news/` | L1 | 新闻层 — 东财个股新闻、全球7x24快讯（财联社替代方案） | ✅ 已完成 |
| 8 | `module-fundamentals/` | L1 | 基础数据层 — mootdx 37字段快照+F10九类、东财个股元信息、新浪财报三表 | ✅ 已完成 |
| 9 | `module-filings/` | L1 | 公告层 — 巨潮cninfo公告全文检索+翻页、_cninfo_orgid关键修复、mootdx F10摘要 | ✅ 已完成 |
| 10 | `module-limit-up/` | L1 | 打板层 — 东财四池+同花顺涨停揭秘+打板情绪速算（V3.3新增） | ✅ 已完成 |
| 11 | `module-options/` | L1 | ETF期权层 — T型报价+希腊字母+IV（交易所预计算、免本地BSM，V3.3新增） | ✅ 已完成 |
| 12 | `module-sentiment/` | L1 | 舆情互动层 — 互动易问答+同花顺热榜+东财人气榜+个股概念命中（V3.3新增） | ✅ 已完成 |
| 13 | `slice-single-valuation/` | L2 | 单票完整估值全链路 — 实时价→一致预期EPS→前向PE/PEG/消化年数 | ✅ 已完成 |
| 14 | `slice-batch-comparison/` | L2 | 批量估值对比全链路 — 多股并行估值+横向DataFrame排列 | ✅ 已完成 |
| 15 | `slice-thematic-research/` | L2 | 主题研报批量检索：iwencai多关键词NL搜索+去重+东财PDF交叉补充 | ✅ 已完成 |
| 16 | `slice-new-target-research/` | L2 | 新标的快速调研全链路 — 7步流水线（1分钟） | ✅ 已完成 |
| 17 | `slice-limit-up-sentiment/` | L2 | 打板情绪分析全链路 — 四池拉取→涨停揭秘→情绪速算→综合判断 | ✅ 已完成 |
| 18 | `slice-etf-options-chain/` | L2 | ETF期权链分析全链路 — 合约清单→T型报价→希腊字母→IV偏度→风险评估 | ✅ 已完成 |
| 19 | `deep-dive-em-throttling/` | L4 | 东财防封限流机制深度剖析 — 串行限流+会话复用+连接重试的设计权衡 | ✅ 已完成 |
| 20 | `deep-dive-tdx-fallback/` | L4 | mootdx客户端三级fallback深度剖析 — BESTIP空串Bug、TCP探测与版本兼容 | ✅ 已完成 |

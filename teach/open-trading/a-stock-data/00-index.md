# a-stock-data · 架构教学 Wiki

> 📊 整体进度：20/20 goals · 100% · 全部完成
> 🕐 最后更新：2026-07-09

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ██████████ 100% |
| L1 模块总览 | 11 | 11 | ██████████ 100% |
| L2 垂直切片 | 6 | 6 | ██████████ 100% |
| L4 深度剖析 | 2 | 2 | ██████████ 100% |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/0001-project-map.html)**
  > 15 分钟建立全局地图，再进入各模块。
- **[📄 a-stock-data 项目总览参考](00-overview/reference/00-overview.html)**
  > 技术栈：Python + mootdx + requests + pandas + stockstats · 架构风格：自包含单文件 Skill · 10 层架构

---

## 📦 L1 · 模块总览（11 模块）

### module-infrastructure — 基础设施与核心机制
- **[📘 模块导览短课（上）](module-infrastructure/lessons/0001-infrastructure-module-tour.html)** — 数据源优先级体系与风控阈值
- **[📘 模块导览短课（下）](module-infrastructure/lessons/0002-infrastructure-module-tour.html)** — em_get/tdx_client/get_prefix/eastmoney_datacenter 四大核心函数
- **[📄 模块总览参考](module-infrastructure/reference/infrastructure-overview.html)**
  > 职责：东财统一防封限流、mootdx 连接容错、市场前缀映射、数据中心统一查询
- **关联深度剖析**：
  - [🧠 东财防封限流机制](deep-dive-em-throttling/lessons/0001-problem-frame.html)
  - [🧠 mootdx 三级 fallback](deep-dive-tdx-fallback/lessons/0001-problem-frame.html)

### module-market-data — 行情层
- **[📘 模块导览短课](module-market-data/lessons/0001-market-data-module-tour.html)**
- **[📄 模块总览参考](module-market-data/reference/market-data-overview.html)**
  > 职责：mootdx K线+盘口、腾讯 PE/PB/市值、百度 K线 MA 均线 — 不封IP首选数据层
- **关联垂直切片**：
  - [🔪 单票完整估值](slice-single-valuation/lessons/0001-flow-map.html)
  - [🔪 批量估值对比](slice-batch-comparison/lessons/0001-flow-map.html)

### module-research — 研报层
- **[📘 模块导览短课（上）](module-research/lessons/0001-research-module-tour.html)** — 东财研报+PDF下载+行业研报
- **[📘 模块导览短课（下）](module-research/lessons/0002-ths-eps-iwencai.html)** — 同花顺一致预期EPS+iwencai语义搜索
- **[📄 模块总览参考](module-research/reference/research-overview.html)**
  > 职责：东财个股/行业研报+PDF、同花顺机构一致预期、iwencai NL语义搜索
- **关联垂直切片**：
  - [🔪 单票完整估值](slice-single-valuation/lessons/0001-flow-map.html)
  - [🔪 主题研报检索](slice-thematic-research/lessons/0001-flow-map.html)
  - [🔪 新标的调研](slice-new-target-research/lessons/0001-flow-map.html)

### module-signals — 信号层
- **[📘 模块导览短课 1](module-signals/lessons/0001-signals-module-tour.html)** — 热点归因与北向资金
- **[📘 模块导览短课 2](module-signals/lessons/0002-signals-blocks-flow.html)** — 板块归属与资金流向
- **[📘 模块导览短课 3](module-signals/lessons/0003-signals-tiger-lockup-industry.html)** — 龙虎榜、解禁与行业排名
- **[📄 模块总览参考](module-signals/reference/signals-overview.html)**
  > 职责：8端点覆盖完整信号链——发现机会→归属归因→资金验证→席位跟踪→风险预警
- **关联垂直切片**：
  - [🔪 新标的调研](slice-new-target-research/lessons/0001-flow-map.html)

### module-capital-flow — 资金面/筹码层
- **[📘 模块导览短课（上）](module-capital-flow/lessons/0001-capital-flow-module-tour.html)** — 融资融券+大宗交易
- **[📘 模块导览短课（下）](module-capital-flow/lessons/0002-capital-flow-holder-fundflow.html)** — 股东户数+分红送转+120日资金流
- **[📄 模块总览参考](module-capital-flow/reference/capital-flow-overview.html)**
  > 职责：V3.0新增——融资融券、大宗交易、股东户数、分红送转、主力资金流
- **关联垂直切片**：
  - [🔪 新标的调研](slice-new-target-research/lessons/0001-flow-map.html)

### module-news — 新闻层
- **[📘 模块导览短课](module-news/lessons/0001-news-module-tour.html)**
- **[📄 模块总览参考](module-news/reference/news-overview.html)**
  > 职责：东财个股新闻 JSONP 解析 + 全球 7×24 快讯（财联社替代方案）

### module-fundamentals — 基础数据层
- **[📘 模块导览短课（上）](module-fundamentals/lessons/0001-fundamentals-module-tour.html)** — mootdx 快照+F10+东财元信息
- **[📘 模块导览短课（下）](module-fundamentals/lessons/0002-sina-three-tables.html)** — 新浪财报三表+跨源拼装
- **[📄 模块总览参考](module-fundamentals/reference/fundamentals-overview.html)**
  > 职责：mootdx 37字段季报+F10九类、东财个股信息、新浪三表（V3.2.1修复）

### module-filings — 公告层
- **[📘 模块导览短课](module-filings/lessons/0001-filings-module-tour.html)**
- **[📄 模块总览参考](module-filings/reference/filings-overview.html)**
  > 职责：巨潮 cninfo 公告全文检索（V3.2.2 orgId动态化修复）+ mootdx F10 摘要

### module-limit-up — 打板层 ★V3.3
- **[📘 模块导览短课（上）](module-limit-up/lessons/0001-limit-up-module-tour.html)** — 东财四池
- **[📘 模块导览短课（下）](module-limit-up/lessons/0002-ths-sentiment-secrets.html)** — 同花顺涨停揭秘+情绪速算
- **[📄 模块总览参考](module-limit-up/reference/limit-up-overview.html)**
  > 职责：涨停/炸板/跌停/昨涨停四池 + 涨停原因题材 + 封板成功率 + 连板梯队
- **关联垂直切片**：
  - [🔪 打板情绪分析](slice-limit-up-sentiment/lessons/0001-flow-map.html)

### module-options — ETF期权层 ★V3.3
- **[📘 模块导览短课](module-options/lessons/0001-options-module-tour.html)**
- **[📄 模块总览参考](module-options/reference/options-overview.html)**
  > 职责：50ETF/300ETF/科创50/500ETF 期权 T型报价+希腊字母+IV（交易所预计算）
- **关联垂直切片**：
  - [🔪 ETF期权链分析](slice-etf-options-chain/lessons/0001-flow-map.html)

### module-sentiment — 舆情互动层 ★V3.3
- **[📘 模块导览短课](module-sentiment/lessons/0001-sentiment-module-tour.html)**
- **[📄 模块总览参考](module-sentiment/reference/sentiment-overview.html)**
  > 职责：互动易问答（AI独家信源）+ 同花顺热榜 + 东财人气榜 + 个股概念命中

---

## 🔪 L2 · 垂直切片（6 条核心链路）

### slice-single-valuation — 单票完整估值全链路
- **[📘 课程 1：流程地图](slice-single-valuation/lessons/0001-flow-map.html)**
  > 入口、数据流和四步调用链。
- **[📘 课程 2：估值公式详解](slice-single-valuation/lessons/0002-valuation-detail.html)**
  > 链路：tencent_quote → ths_eps_forecast → forward_pe/PEG/消化年数 → full_valuation 汇总
  > 所属模块：[行情层](module-market-data/reference/market-data-overview.html) · [研报层](module-research/reference/research-overview.html)

### slice-batch-comparison — 批量估值对比全链路
- **[📘 课程](slice-batch-comparison/lessons/0001-flow-map.html)**
  > 链路：股票列表 → [tencent_quote × N + ths_eps_forecast × N] → 估值计算 → DataFrame 横向排列
  > 所属模块：[行情层](module-market-data/reference/market-data-overview.html) · [研报层](module-research/reference/research-overview.html)

### slice-thematic-research — 主题研报批量检索全链路
- **[📘 课程 1：流程地图](slice-thematic-research/lessons/0001-flow-map.html)**
  > 四阶段调用链：关键词列表 → iwencai 并行搜索 → 去重 → 东财 PDF 补充
- **[📘 课程 2：阶段详解](slice-thematic-research/lessons/0002-stage-deep-dive.html)**
  > X-Claw 鉴权、uid 去重逻辑、PDF Referer 异常处理
  > 所属模块：[研报层](module-research/reference/research-overview.html)

### slice-new-target-research — 新标的快速调研全链路
- **[📘 课程 1：流程地图](slice-new-target-research/lessons/0001-flow-map.html)**
  > 7步流水线概览 + Mermaid 时序图 + 并行优化机会
- **[📘 课程 2：各阶段详解](slice-new-target-research/lessons/0002-stage-details.html)**
  > 7步详解 + 5种降级策略 + 并行优化 + 场景判断练习
  > 所属模块：[研报层](module-research/reference/research-overview.html) · [信号层](module-signals/reference/signals-overview.html) · [资金面层](module-capital-flow/reference/capital-flow-overview.html)

### slice-limit-up-sentiment — 打板情绪分析全链路
- **[📘 课程 1：流程地图](slice-limit-up-sentiment/lessons/0001-flow-map.html)**
  > 四池 → 涨停揭秘 → 情绪速算 的数据流与关键坑点
- **[📘 课程 2：情绪判断](slice-limit-up-sentiment/lessons/0002-sentiment-judgment.html)**
  > 5个核心指标、连板梯队健康度、晋级率、进攻/观察/防守三层框架
  > 所属模块：[打板层](module-limit-up/reference/limit-up-overview.html)

### slice-etf-options-chain — ETF期权链分析全链路
- **[📘 课程 1：流程地图](slice-etf-options-chain/lessons/0001-flow-map.html)**
  > 5步流水线：选标的 → 合约清单 → 选月 → T型报价 → 希腊字母
- **[📘 课程 2：IV偏度与风险](slice-etf-options-chain/lessons/0002-iv-skew-risk.html)**
  > IV偏度判断、希腊字母风险框架、三类异常路径降级
  > 所属模块：[ETF期权层](module-options/reference/options-overview.html)

---

## 🧠 L4 · 深度剖析（2 个核心设计）

### deep-dive-em-throttling — 东财防封限流机制
- **[📘 课程 1：问题背景](deep-dive-em-throttling/lessons/0001-problem-frame.html)**
  > 为什么需要限流？东财风控的实际触发案例与阈值
- **[📘 课程 2：核心机制](deep-dive-em-throttling/lessons/0002-core-mechanism.html)**
  > 四层防护：串行锁+随机抖动+会话复用+连接重试。令牌桶 vs 串行限流的权衡
  > 关联模块：[基础设施层](module-infrastructure/reference/infrastructure-overview.html)

### deep-dive-tdx-fallback — mootdx 客户端三级 fallback
- **[📘 课程 1：问题背景](deep-dive-tdx-fallback/lessons/0001-problem-frame.html)**
  > BESTIP.HQ 空串 Bug 根因——为什么干净环境裸调就崩溃
- **[📘 课程 2：核心机制](deep-dive-tdx-fallback/lessons/0002-core-mechanism.html)**
  > _probe() TCP 探测 → BESTIP 测速 → 裸 factory → RuntimeError。锁版本 vs 动态探测的取舍
  > 关联模块：[基础设施层](module-infrastructure/reference/infrastructure-overview.html)

---

## 📊 源码覆盖统计

| 指标 | 数值 |
|------|------|
| 源码文件 | SKILL.md（2648行/109.6KB）— 100% 覆盖 |
| 公共函数 | ~60 个 — 100% 被至少一篇文档引用 |
| 核心功能 | 4套调研流程 + 打板情绪 + ETF期权链 — 全部有L2垂直切片 |
| 数据层 | 10层 + 基础设施 — 全部有L1模块总览 |
| 豁免文件 | 5（.github/、assets/、CHANGELOG.md、LICENSE、README.md） |

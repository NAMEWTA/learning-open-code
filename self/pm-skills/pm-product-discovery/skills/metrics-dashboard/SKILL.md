---
name: metrics-dashboard
description: "定义并设计产品指标仪表盘，包含关键指标、数据源、可视化类型和告警阈值。适用于创建指标仪表盘、定义 KPI、搭建产品分析，或构建数据监控计划。"
---

## 产品指标仪表盘

设计全面的产品指标仪表盘，包含正确的指标、可视化方式和告警阈值。

### 背景

你正在为 **$ARGUMENTS** 设计指标仪表盘。

如果用户提供了文件（现有仪表盘、分析数据、OKR 或战略文档），请先阅读。

### 领域背景

**指标 vs KPI vs 北极星指标**：指标 = 所有可衡量的事物。KPI = 长期跟踪的少数关键定量指标。北极星指标 = 一个以客户为中心的、可作为业务成功先行指标的 KPI。

**好指标的 4 项标准**（Ben Yoskovitz，《Lean Analytics》）：(1) 可理解——创建共同语言。(2) 可比较——跨时间而非快照。(3) 比率或速率——比整数更具揭示性。(4) 能改变行为——黄金法则：「如果一个指标不会改变你的行为，它就是一个坏指标。」

**8 种指标类型**：虚荣 vs 可行动（只有可行动指标能改变行为）、定性 vs 定量（WHAT vs WHY——二者都需要；永远不要停止与客户交谈）、探索性 vs 报告型（探索数据以发现意外洞察）、滞后 vs 先行（先行指标实现更快的学习周期，例如客户投诉可预测流失）。

**5 个行动步骤**：(1) 对照 4 项好指标标准审计指标。(2) 更新仪表盘——确保所有关键指标都是好指标。(3) 识别虚荣指标——注意如何使用它们。(4) 分类先行 vs 滞后指标。(5) 挑一个问题深入数据挖掘。

案例研究和更多详情：[Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics) by Ben Yoskovitz

### 操作指引

1. **确定指标框架**——将指标组织为层级：

   **北极星指标**：最能捕捉核心价值交付的单一指标

   **输入指标**（3-5 个）：驱动北极星的杠杆

   **健康指标**：确保整体产品健康的护栏

   **业务指标**：收入、成本和单位经济学

2. **对每个指标，定义**：

   | 指标 | 定义 | 数据源 | 可视化 | 目标值 | 告警阈值 |
   |---|---|---|---|---|---|
   | [名称] | [精确计算：分子/分母、时间窗口] | [数据来源] | [折线图 / 柱状图 / 数字 / 漏斗] | [目标值] | [何时触发告警] |

3. **设计仪表盘布局**：
   ```
   ┌─────────────────────────────────────────────┐
   │  北极星指标: [指标] — [当前值]               │
   │  趋势: [↑/↓ X% vs 上期]                      │
   ├──────────────────┬──────────────────────────┤
   │  输入指标 1       │  输入指标 2               │
   │  [迷你图]         │  [迷你图]                  │
   ├──────────────────┼──────────────────────────┤
   │  输入指标 3       │  输入指标 4               │
   │  [迷你图]         │  [迷你图]                  │
   ├──────────────────┴──────────────────────────┤
   │  健康: [延迟] [错误率] [NPS]                  │
   ├─────────────────────────────────────────────┤
   │  业务: [MRR] [CAC] [LTV] [流失]             │
   └─────────────────────────────────────────────┘
   ```

4. **设置审视频率**：
   - **每日**：运行健康（错误、延迟、关键流程）
   - **每周**：输入指标和参与趋势
   - **每月**：北极星指标、业务指标、OKR 进度
   - **每季度**：战略评审和指标重新校准

5. **定义告警**：
   - 什么阈值触发调查？
   - 谁接收告警以及通过什么渠道？
   - 预期响应时间是多少？

6. **根据用户背景推荐工具**：
   - Amplitude、Mixpanel、PostHog 用于产品分析
   - Looker、Metabase、Mode 用于基于 SQL 的仪表盘
   - Datadog、Grafana 用于运行健康

逐步思考。将仪表盘规范保存为 markdown 文档。

---

### 延伸阅读

- [The Ultimate List of Product Metrics](https://www.productcompass.pm/p/the-ultimate-list-of-product-metrics)
- [The North Star Framework 101](https://www.productcompass.pm/p/the-north-star-framework-101)
- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [AARRR (Pirate) Metrics: The 5-Stage Framework for Growth](https://www.productcompass.pm/p/aarrr-pirate-metrics)
- [The Google HEART Framework: Your Guide to Measuring User-Centric Success](https://www.productcompass.pm/p/the-google-heart-framework)
- [Funnel Analysis 101: How to Track and Optimize Your User Journey](https://www.productcompass.pm/p/funnel-analysis)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm)（视频课程）

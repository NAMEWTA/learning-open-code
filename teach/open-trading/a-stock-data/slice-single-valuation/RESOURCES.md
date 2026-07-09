# 单票完整估值全链路 资源

## 知识

- [a-stock-data SKILL.md — 估值计算公式（2324-2384行）](../../../open-trading/a-stock-data/SKILL.md#L2324)
  包含 `forward_pe()`、`pe_digestion()`、`calc_peg()` 三个核心公式及投资框架速查。适用于：每次估值计算时查阅公式定义。

- [a-stock-data SKILL.md — 完整调研流程 A：单票完整估值（2385-2460行）](../../../open-trading/a-stock-data/SKILL.md#L2385)
  `full_valuation(code)` 函数的完整实现，从腾讯实时行情到同花顺一致预期 EPS 再到估值汇总。适用于：理解端到端调用链。

- [a-stock-data SKILL.md — tencent_quote 行情接口（400-494行）](../../../open-trading/a-stock-data/SKILL.md#L400)
  腾讯财经实时行情拉取，返回 PE(TTM)、PB、总市值、换手率等字段。适用于：Layer 1 行情层数据获取。

- [a-stock-data SKILL.md — ths_eps_forecast 一致预期（669-704行）](../../../open-trading/a-stock-data/SKILL.md#L669)
  同花顺机构一致预期 EPS 直连获取，解析 HTML 表格。适用于：Layer 2 研报层数据获取，注意「均值」列才是机构一致预期。

- [a-stock-data SKILL.md — 防封铁律与 em_get 限流（115-148行）](../../../open-trading/a-stock-data/SKILL.md#L115)
  东财接口限流策略和 `em_get()` 统一节流入口。适用于：理解为什么本链路选腾讯/同花顺而非东财接口。

## 智慧（社区）

- [a-stock-data GitHub Issues](https://github.com/simonlin1212/a-stock-data/issues)
  项目问题反馈和讨论区。适用于：接口异常报错时查看是否已知问题、提交新发现。

## 空白

- 暂无专门针对 A 股 PEG 估值框架的中文社区或书籍推荐——当前以 SKILL.md 文档为主要知识来源。
- 估值公式的数学推导（对数消化的数学原理）暂无独立资源，由课程自行解释。

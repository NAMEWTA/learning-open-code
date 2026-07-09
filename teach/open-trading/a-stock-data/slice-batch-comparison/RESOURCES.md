# 批量估值对比 资源

## 知识

- [a-stock-data SKILL.md §流程B: 批量估值对比](https://github.com/simonlin1212/a-stock-data) — 批量估值代码示例，for循环+异常处理的模板
- [a-stock-data SKILL.md §流程A: 单票完整估值](https://github.com/simonlin1212/a-stock-data) — full_valuation() 完整实现，批量对比的基础
- [a-stock-data SKILL.md §数据源优先级](https://github.com/simonlin1212/a-stock-data) — 腾讯行情不封IP vs 同花顺EPS需串行的设计原则
- teach/ 内前置课程：
  - [slice-single-valuation](../../slice-single-valuation/lessons/0001-flow-map.html) — 单票估值四步链路（批量对比的前置基础）
  - [module-market-data](../../module-market-data/lessons/0001-market-data-module-tour.html) — 行情层模块导览
  - [module-research](../../module-research/lessons/0001-research-module-tour.html) — 研报层模块导览

## 智慧（社区）

- [a-stock-data Issues](https://github.com/simonlin1212/a-stock-data/issues) — 端点失效反馈与修复讨论
- [集思录](https://www.jisilu.cn/) — A股量化数据社区，讨论估值/折溢价/事件驱动策略

## 空白

- 行业分位值计算（当前PE在历史PE中的分位数）尚未标准化
- 批量估值的HTML/Excel自动导出报告模板未覆盖
- 估值与股价走势的叠加可视化未涉及

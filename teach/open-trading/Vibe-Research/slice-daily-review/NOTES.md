# 教学笔记：每日复盘全链路

## 批量生成模式
本主题为批量生成模式（goal 驱动），使用默认使命。目标读者为具备编程基础的开发者，已修完 L1-backend 和 L1-frontend。

## 教学重点
- 8 路并行加载的时序与状态管理是核心难点
- `pending(done)` 的双态占位逻辑（加载中 vs 数据源不可用）体现了前端优雅降级的设计思路
- AI 复盘的数据组装方式（`dataSummary` 拼接指数行情 → prompt → chatStream 流式返回）是闭环的关键
- `pctColor()` 的红涨绿跌规则是中国 A 股产品的有意选择，与国际惯例不同

## 与邻近主题的关系
- slice-ai-chat 覆盖 AskAiButton 的对话面板与 function-calling 工具系统，本主题只关注 AI 复盘按钮的触发路径
- slice-stock-data 覆盖个股数据页的估值/财务/资金面链路，本主题只关注每日复盘页面的 8 路聚合数据

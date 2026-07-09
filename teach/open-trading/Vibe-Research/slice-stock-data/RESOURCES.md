# 个股数据查询全链路 资源

## 知识

- [个股数据页：`frontend/src/pages/StockData.tsx`](../../../../open-trading/Vibe-Research/frontend/src/pages/StockData.tsx)
  30+ API 并行调用编排、竞态守卫、A股/美股分支路由、fire-and-forget 策略。本节核心分析目标。
- [API 客户端：`frontend/src/lib/api.ts`](../../../../open-trading/Vibe-Research/frontend/src/lib/api.ts)
  全部接口类型定义（30+ 接口）、ApiError 错误封装、鉴权头注入、fetch 统一封装。类型系统参考。
- [后端路由层：`backend/app.py` (L305-601)](../../../../open-trading/Vibe-Research/backend/app.py)
  个股数据相关 20+ 端点注册、分级缓存策略（5/15/30 分钟）、_validate 校验、_cached 通用缓存封装。
- [财报速览组件：`frontend/src/components/ui/EarningsSnapshot.tsx`](../../../../open-trading/Vibe-Research/frontend/src/components/ui/EarningsSnapshot.tsx)
  前向一致预期 + 估值分位 + 财务数据的机械分档信号标签生成。前端二次计算的典型案例。
- [A股数据层：`backend/astock.py`](../../../../open-trading/Vibe-Research/backend/astock.py)
  五层数据源封装，full_valuation/valuation_percentile/financials/eastmoney_reports/stock_news/margin_trading 等 30+ 函数。DependencyMissing 惰性导入模式。
- [全球股票数据层：`backend/gstock.py`](../../../../open-trading/Vibe-Research/backend/gstock.py)
  美股/港股数据聚合，us_hk_stock 函数、东财域内源、关键财务指标提取。

## 智慧（社区）

- [GitHub 仓库：simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)
  项目上游仓库，适用于核对最新版本变更和 issue。
- [React 并发模式文档](https://react.dev/reference/react/useRef)
  useRef 竞态守卫的官方说明，适用于理解 runIdRef 的并发安全策略。
- [FastAPI 异步与并发](https://fastapi.tiangolo.com/async/)
  FastAPI 的 async def vs def 路由函数选择，适用于理解各端点的同步/异步设计。

## 空白

- 当前未找到独立第三方的 Vibe-Research StockData 页面深度架构解读文章。
- 各数据源（腾讯/东财/同花顺/mootdx/akshare）的限流阈值和风控策略未公开文档化，仅靠代码推断。

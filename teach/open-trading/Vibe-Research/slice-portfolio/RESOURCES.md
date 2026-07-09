# 持仓管理全链路 资源

## 知识

- [backend/portfolio.py] — 持仓数据层核心：add_holding 加权合并、close_position 已实现盈亏、get_portfolio 实时盈亏计算、start_scheduler 后台刷新
- [backend/app.py:123-230] — HTTP 端点层：/api/portfolio GET/POST/DELETE、/api/portfolio/close POST/DELETE、/api/portfolio/refresh POST
- [frontend/src/pages/Portfolio.tsx] — 前端持仓页面：录入表单、浮动盈亏表格、已清仓列表、自动/手动刷新
- [frontend/src/lib/api.ts:178-252] — TypeScript 类型定义与 API 客户端：Holding、ClosedPosition、PortfolioData 接口及 api 方法

## 智慧（社区）

- [Vibe-Research README](https://github.com/nicetuku/Vibe-Research) — 项目整体介绍与启动说明

## 空白

- 持仓管理的前端状态管理（useState/useEffect 模式）已在 module-frontend 主题中覆盖，此处不重复
- 腾讯行情接口 astock.tencent_quote 的数据格式和限流策略属于 module-a-stock-data 范围

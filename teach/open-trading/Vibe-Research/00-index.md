# Vibe-Research · 架构教学 Wiki

> 📊 整体进度：11/11 goals · 100% · 已执行 2 轮
> 🕐 最后更新：2026-07-08 23:55

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ██████████ |
| L1 模块总览 | 4 | 4 | ██████████ |
| L2 垂直切片 | 6 | 6 | ██████████ |
| L3 微观 API | — | — | 合并至 L1 reference |
| L4 深度剖析 | — | — | 暂无触发条件 |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/0001-project-map.html)**
  > 15 分钟建立全局地图——定位、技术栈、架构分层和后续阅读路线。
- **[📄 Vibe-Research 项目总览参考](00-overview/reference/00-overview.html)**
  > 技术栈：Python 3.10+ FastAPI + React 19 + TypeScript + Tailwind · 架构风格：前后端分离 + 多数据源聚合 · 5 个顶层模块

---

## 📦 L1 · 模块总览

### module-backend — 后端 FastAPI 数据引擎与 AI 接口层
- **[📘 模块导览短课](module-backend/lessons/0001-backend-module-tour.html)**
  > 15 分钟理解 30+ REST 端点、中间件链、缓存策略和 10 个数据层模块的协作方式
- **[📄 模块总览参考](module-backend/reference/backend-overview.html)**
  > 职责：A 股/美港股数据聚合中枢 + AI 对话系统（API/CLI/MCP 三条通道）
- **关联垂直切片**：
  - [🔪 每日复盘全链路](slice-daily-review/lessons/0001-flow-map.html)
  - [🔪 资讯雷达全链路](slice-intel-radar/lessons/0001-flow-map.html)
  - [🔪 个股数据查询全链路](slice-stock-data/lessons/0001-flow-map.html)
  - [🔪 AI 对话全链路](slice-ai-chat/lessons/0001-flow-map.html)
  - [🔪 持仓管理全链路](slice-portfolio/lessons/0001-flow-map.html)
  - [🔪 研报管理全链路](slice-reports/lessons/0001-flow-map.html)

### module-frontend — 前端 React 玻璃暖橙主题投研看板
- **[📘 模块导览短课](module-frontend/lessons/0001-frontend-module-tour.html)**
  > 15 分钟掌握 10 页面路由、Zustand 状态管理、AI 流式对话和 Tailwind 主题系统
- **[📄 模块总览参考](module-frontend/reference/frontend-overview.html)**
  > 职责：Vite + React 19 + TypeScript + ECharts 6 投研看板界面

### module-a-stock-data — A 股数据工具箱（十层 40 端点）
- **[📘 模块导览短课](module-a-stock-data/lessons/0001-a-stock-data-module-tour.html)**
  > 15 分钟了解十层数据架构、数据源优先级策略和与 backend/astock.py 的移植关系
- **[📄 模块总览参考](module-a-stock-data/reference/a-stock-data-overview.html)**
  > 职责：A 股全栈数据引擎，自包含、零第三方数据封装依赖

### module-global-stock-data — 全球股票数据工具箱（八层 18 端点）
- **[📘 模块导览短课](module-global-stock-data/lessons/0001-global-stock-data-module-tour.html)**
  > 15 分钟了解八层数据架构、东财域内合规子集和韩股 .KS 后缀规则
- **[📄 模块总览参考](module-global-stock-data/reference/global-stock-data-overview.html)**
  > 职责：美股/港股/韩股数据引擎，覆盖行情/财务/技术指标

---

## 🔪 L2 · 垂直切片

### slice-daily-review — 每日复盘全链路
- **[📘 课程 1：链路地图](slice-daily-review/lessons/0001-flow-map.html)**
  > 入口、8 路并行加载架构和关键数据流
- **[📘 课程 2：主成功路径](slice-daily-review/lessons/0002-main-path.html)**
  > 链路：React DailyReview → Vite 代理 → /api/market/* /api/indices /api/quote → market.py/astock.py → 腾讯/东财 → AI 复盘闭环
  > 所属模块：[module-backend](module-backend/reference/backend-overview.html)

### slice-intel-radar — 资讯雷达全链路
- **[📘 课程 1：链路地图](slice-intel-radar/lessons/0001-flow-map.html)**
  > 12 赛道 108 RSS 源聚合架构
- **[📘 课程 2：强制刷新路径](slice-intel-radar/lessons/0002-refresh-flow.html)**
  > POST /api/radar/refresh 全量重抓→缓存更新→AI 要点提炼
  > 所属模块：[module-backend](module-backend/reference/backend-overview.html)

### slice-stock-data — 个股数据查询全链路
- **[📘 课程 1：链路地图](slice-stock-data/lessons/0001-flow-map.html)**
  > 代码输入→30+端点并行→多维聚合
- **[📘 课程 2：估值与财务路径](slice-stock-data/lessons/0002-valuation-finance.html)**
  > PE/PB 分位、一致预期、财务三表速览
- **[📘 课程 3：资金面与信号路径](slice-stock-data/lessons/0003-fund-flow-signals.html)**
  > 两融/龙虎榜/大宗/解禁/概念归属
  > 所属模块：[module-backend](module-backend/reference/backend-overview.html)
- **[📄 端点速查表](slice-stock-data/reference/stock-data-flow-map.html)** — 30+ /api/* 端点一览

### slice-ai-chat — AI 对话全链路（API + CLI + MCP）
- **[📘 课程 1：三条通道全景](slice-ai-chat/lessons/0001-flow-map.html)**
  > API function-calling / CLI 纯文本 / MCP 工具暴露的端到端对比
- **[📘 课程 2：API 接入通道](slice-ai-chat/lessons/0002-api-channel.html)**
  > OpenAI 兼容 function-calling 循环 + SSE NDJSON 流式协议 + 投研五维分析框架
- **[📘 课程 3：CLI 与 MCP](slice-ai-chat/lessons/0003-cli-mcp.html)**
  > 4 种 CLI 适配 + MCP JSON-RPC over stdio 服务
  > 所属模块：[module-backend](module-backend/reference/backend-overview.html)

### slice-portfolio — 持仓管理全链路
- **[📘 课程 1：链路地图](slice-portfolio/lessons/0001-flow-map.html)**
  > 录入→加权平均成本合并→实时行情盈亏→已清仓记录→后台定时刷新
  > 所属模块：[module-backend](module-backend/reference/backend-overview.html)

### slice-reports — 研报上传与管理全链路
- **[📘 课程 1：链路地图](slice-reports/lessons/0001-flow-map.html)**
  > 拖拽上传→base64 编码→行业关键词归档→blob 下载（带鉴权头）
  > 所属模块：[module-backend](module-backend/reference/backend-overview.html)

---

## 📊 源码覆盖统计

| 指标 | 数值 |
|------|------|
| L0 总览 | 1 主题（1 课 + 1 参考） |
| L1 模块 | 4 主题（各 1 课 + 1 参考） |
| L2 垂直切片 | 6 主题（共 12 课 + 4 参考） |
| 总课程数 | 17 节 lesson |
| 总参考文档 | 11 篇 reference |
| 总源码引用 | 约 245 处 |
| 豁免文件 | 15（vendor/自动生成/二进制/截图/配置） |

---

> 💡 **阅读建议**：先看 L0 建立全局地图 → 选感兴趣的 L1 模块了解架构 → 对具体功能看 L2 垂直切片追踪完整数据流。每节课 15 分钟内完成，独立自包含。

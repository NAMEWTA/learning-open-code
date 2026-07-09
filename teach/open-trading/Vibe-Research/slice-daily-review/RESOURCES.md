# 每日复盘全链路 资源

## 知识

### 源码入口（链路顺序：前端页面 → API 层 → 数据层 → 外部数据源）

- **`frontend/src/pages/DailyReview.tsx`** (477 行)
  页面组件：8 路数据并行加载（指数/全球市场/市场总览/短线情绪/成交额TOP20/自选行情/AI复盘）+ A股红涨绿跌色彩规则。适用于：理解前端数据加载时序、状态管理与优雅降级策略。

- **`frontend/src/lib/api.ts`** (276 行)
  API 客户端：类型定义（IndexQuote/MarketOverview/ShortTermEmotion/TurnoverTop/GlobalIndex）+ api.indices/quote/marketOverview/emotion/turnoverTop/globalIndices。适用于：理解前后端数据契约与错误处理约定。

- **`frontend/src/lib/llm.ts`** (119 行)
  AI 复盘流式调用：LLM 配置管理（localStorage）+ chatStream NDJSON 流式解析。适用于：理解 AI 复盘从 prompt 组装到流式渲染的完整路径。

- **`frontend/src/components/ui/AskAiButton.tsx`** (214 行)
  AI 对话面板：侧边栏展开/工具调用溯源/中止控制。适用于：理解"问 AI"入口的交互模式与数据溯源展示。

- **`frontend/src/lib/watchlist.ts`** (30 行)
  自选股本地存储：localStorage 读写 + 代码解析 + 去重合并。适用于：理解自选股数据的持久化方案。

- **`backend/app.py:71-73`** — `/api/health` 健康检查端点
- **`backend/app.py:251-279`** — `/api/market/overview` + `/api/market/emotion` + `/api/market/turnover-top` 三端点
- **`backend/app.py:282-288`** — `/api/global/indices` 全球指数端点
- **`backend/app.py:305-323`** — `/api/indices` + `/api/quote` A股指数+行情端点
  适用于：理解 FastAPI 端点如何从 HTTP 请求一路委托到 market.py/astock.py。

- **`backend/market.py`** (187 行)
  市场数据层：`_sentiment()` / `_sectors()` / `get_overview()` / `get_short_term_emotion()` / `get_turnover_top()` / `get_global_indices()`。全站共享 TTL 缓存（5分钟）。适用于：理解缓存策略、数据聚合逻辑与降级返回。

- **`backend/astock.py`** — `index_quote()` / `tencent_quote()`（A股行情核心函数）
- **`backend/gstock.py`** — `global_indices()`（全球指数快照）

### 参考文档（已完成 L0/L1，可交叉引用）

- [项目总览 · 0001-project-map](../../00-overview/lessons/0001-project-map.html) — 整体架构与技术栈
- [00-overview 参考图谱](../../00-overview/reference/00-overview.html) — 源码索引与模块职责速查
- [后端模块总览](../../module-backend/lessons/0001-backend-module-tour.html) — app.py 全端点注册与中间件
- [前端模块总览](../../module-frontend/lessons/0001-frontend-module-tour.html) — 前端路由、页面组件与 API 调用模式

## 智慧（社区）

- [Vibe-Research GitHub Issues](https://github.com/astock/Vibe-Research/issues)
  项目 issue 跟踪，适用于：了解已知数据源故障、缓存策略讨论与实际使用反馈。

## 空白

- 腾讯财经 qt.gtimg.cn 的完整 API 文档（非官方接口，无公开文档；仅能通过源码逆向理解参数语义）
- 东财 push2ex 涨停池接口的速率限制与风控策略文档（非公开接口，限流规则靠经验积累）

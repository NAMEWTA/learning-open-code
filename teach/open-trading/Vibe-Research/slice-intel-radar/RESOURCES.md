# 资讯雷达全链路 资源

## 知识

- [newsradar.py](https://github.com/anthropics/vibe-research/blob/main/backend/newsradar.py) — 资讯雷达数据层完整源码。12 赛道 108 RSS 源的并发抓取、XML 解析、合规过滤、缓存策略全在此文件。
- [news_sources.json](https://github.com/anthropics/vibe-research/blob/main/backend/news_sources.json) — 108 个 RSS 源定义文件。每个源包含 name/hint/type/url 字段，按 12 个行业赛道分组。
- [app.py:233-248](https://github.com/anthropics/vibe-research/blob/main/backend/app.py) — GET /api/radar 和 POST /api/radar/refresh 两个端点的注册代码。展示了路由层如何委托数据层。
- [Intel.tsx](https://github.com/anthropics/vibe-research/blob/main/frontend/src/pages/Intel.tsx) — 资讯雷达前端页面。InvestmentNewsPanel 组件展示了完整的 React 数据获取→状态管理→条件渲染→用户交互模式。
- [api.ts](https://github.com/anthropics/vibe-research/blob/main/frontend/src/lib/api.ts) — 前端 API 客户端。RadarData/RadarItem/Industry 类型定义，以及 api.radar() 和 api.radarRefresh() 的调用封装。
- [Python concurrent.futures 文档](https://docs.python.org/3/library/concurrent.futures.html) — ThreadPoolExecutor 官方文档。理解 newsradar.py 中 `max_workers=40` 的并发模型。
- [RSS 2.0 规范](https://www.rssboard.org/rss-specification) — RSS 标准协议。理解 newsradar.py 中 XML 解析时查找的 item/link/pubDate/description 等节点。

## 智慧（社区）

- [r/algotrading](https://reddit.com/r/algotrading) — 量化交易 Reddit 社区。适用于：讨论数据管道架构、RSS 源选型和合规过滤策略。
- [r/Python](https://reddit.com/r/Python) — Python 社区。适用于：ThreadPoolExecutor 最佳实践、XML 解析性能优化。

## 空白

- 暂未找到专门讨论"多 RSS 源聚合 + 合规过滤"设计模式的文章或书籍。newsradar.py 的实现本身是目前最高质量的参考。
- RSS 源的长期维护策略（源失效检测、自动切换备用源）—— newsradar.py 当前对失败源静默跳过，缺少监控告警机制。

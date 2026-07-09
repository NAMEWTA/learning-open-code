# 新闻层 资源

## 知识

- [a-stock-data SKILL.md §Layer 5 新闻层](https://github.com/nicedoc/learning-open-code/blob/main/open-trading/a-stock-data/SKILL.md#layer-5-%E6%96%B0%E9%97%BB%E5%B1%82) — 3 个新闻端点的完整源码与使用示例（SKILL.md:1587-1719）
- [东方财富个股新闻搜索](https://so.eastmoney.com/) — eastmoney_stock_news() 的 Web 端对应页面
- [东方财富 7x24 快讯](https://kuaixun.eastmoney.com/) — eastmoney_global_news() 的 Web 端对应页面
- [财联社（已迁移）](https://www.cls.cn/) — cls_telegraph() 的原始数据源，2026-05 起 API 下线，仅作历史参考
- [东方财富 search-api-web JSONP 接口说明](https://www.eastmoney.com/) — JSONP 回调机制与参数结构

## 智慧（社区）

- [雪球 — 新闻与公告](https://xueqiu.com/) — 个股新闻讨论与解读，适合验证东财新闻的覆盖完整度
- [华尔街见闻](https://wallstreetcn.com/) — 全球宏观资讯的付费替代源（相比免费的东财7x24更深度但需付费）

## 空白

- 财联社新 API 的逆向方案：cls.cn 迁移到 Next.js 后新版 API 需签名认证，当前无公开破解，无法免费接入
- 新闻去重与聚合：当前两个新闻源可能存在重复报道，项目未提供内置去重逻辑
- 新闻推送/流式订阅：当前为拉取模式（poll），非推送模式（push），实时性受轮询间隔限制
- 非中国大陆新闻源：当前仅覆盖东财体系，无路透社/Bloomberg/Yahoo Finance 等国际新闻源

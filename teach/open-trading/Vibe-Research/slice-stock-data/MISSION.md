# 使命：个股数据查询全链路

## 为什么
L1-backend 已经建立了后端 10 个模块的全局地图，现在需要深入到所有页面中最复杂的 StockData 页面——它单次查询就拉起 30+ 个并行 API，覆盖行情/估值/财务/研报/公告/资金面/龙虎榜/解禁/概念/互动易十多个数据维度。只有理解前端如何编排这些并行请求、后端路由如何分发到 astock.py 和 gstock.py、各端点如何分级缓存，才能真正掌握"一条查询链路如何支撑起整个个股决策仪表盘"。

## 成功的样子
- 能说明 StockData.tsx 中"竞态守卫 + 主数据并行 + 资金面 fire-and-forget"三层请求编排策略。
- 能将前端 30+ API 调用映射到 app.py 中对应的路由函数，并说出各端点的缓存 TTL 与数据源。
- 能画出 6 位代码输入 → Vite 代理 → FastAPI 路由分发 → astock.py/gstock.py → 多数据源 → 并行返回 JSON → 前端 Tab 展示的完整链路。
- 能理解"异步非阻塞"在个股页面的实际含义：外围 10 个端点不阻塞主数据展示，失败静默降级。

## 约束条件
- L2 垂直切片，聚焦一条链路，不展开每个数据模块的内部细节（L1 已覆盖），不深入每个端点的逐行实现。
- 每节 lesson 保持 15 分钟内完成；速查表分流到 reference/stock-data-flow-map.html。
- 教学产物只写入 `teach/open-trading/Vibe-Research/slice-stock-data/`。
- 批量生成模式，使用自动生成的默认使命，不交互等待用户输入。

## 不在范围内
- 不展开 astock.py 中腾讯/东财/同花顺的具体 HTTP 请求构造（L1-a-stock-data 已覆盖）。
- 不展开 gstock.py 的 push2/push2delay 主机 latch 策略（L1-global-stock-data 已覆盖）。
- 不展开前端 GlassCard/PageHeader 等 UI 组件的实现细节（L1-frontend 已覆盖）。
- 不分析 K 线/行情页面/每日复盘/资讯雷达等其它页面的请求链路。

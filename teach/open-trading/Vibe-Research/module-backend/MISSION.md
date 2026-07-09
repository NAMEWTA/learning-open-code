# 使命：Vibe-Research 后端 FastAPI 模块总览

## 为什么
学习者已通过 L0 项目地图了解了 Vibe-Research 整体架构（前端 React :5899 ← Vite 代理 → 后端 FastAPI :8900 ← → 多数据源），现在需要深入到后端这一数据引擎中枢。掌握后端 10 个 Python 模块的职责边界、30+ API 端点的分组逻辑、中间件链和缓存策略后，才能读懂后续 L2 的各垂直切片（每日复盘/资讯雷达/个股数据/AI 对话/持仓管理/研报管理）中请求如何从 HTTP 入口一路走到数据源。

## 成功的样子
- 能用一句话概括后端模块的核心职责（A 股/美港股数据聚合中枢 + AI 对话引擎 + 本地持久化）。
- 能将 30+ /api/* 端点按功能正确分组到对应的 Python 模块。
- 能画出 app.py 路由层 → 各数据模块 → 外部数据源的请求流向。
- 能说明中间件链（CORS + 可选鉴权）和分级缓存策略（5分钟/15分钟/30分钟/全站共享）的运作方式。

## 约束条件
- 本主题是 L1 模块总览，只建立后端 10 个模块的全局地图，不展开每条执行链路的异常分支和逐行源码分析。
- 每节 lesson 保持 15 分钟内完成；接口清单、模块详解和缓存策略分流到 reference。
- 教学产物只写入 `teach/open-trading/Vibe-Research/module-backend/`。
- 批量生成模式，MISSION 使用自动生成的默认使命，不交互等待用户输入。

## 不在范围内
- 不深入展开 backend/astock.py 中腾讯/东财/同花顺的具体 HTTP 请求构造。
- 不分析 chat.py 中 function-calling 的 prompt 工程细节。
- 不展开 cli_runtime.py 中各 CLI 的 spawn 和超时处理。
- 不分析 mcp_server.py 的 JSON-RPC 协议实现。
- 不分析前端如何消费这些 API。

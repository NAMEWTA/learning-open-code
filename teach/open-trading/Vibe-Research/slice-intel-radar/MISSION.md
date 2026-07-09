# 使命：资讯雷达全链路

## 为什么
掌握一个完整的 React + FastAPI + 多源 RSS 聚合数据管道的端到端实现——从 108 个公开 RSS 源的并发抓取、合规过滤、缓存策略，到前端 12 赛道展示与 AI 要点提炼。这是理解"全栈数据管线"设计模式的最佳实战切片：每一层都有清晰的职责边界和优雅的错误降级。

## 成功的样子
- 能画出资讯雷达的完整链路时序图（用户点击 → React → API → newsradar → 108 RSS → 缓存 → 渲染）
- 能说出 fetch_radar() 和 get_radar() 的区别（强制抓取 vs 读缓存/骨架降级）
- 能解释 ThreadPoolExecutor 并发模型为什么能应对 108 个源的抓取
- 能定位一条资讯从 RSS XML 节点到前端列表项的完整数据流转

## 约束条件
- 学习时间：2 节课 × 15 分钟 = 30 分钟
- 前置条件：已完成 L1-backend 和 L1-frontend 模块总览
- 源码语言：Python (后端) + TypeScript/React (前端)

## 不在范围内
- AI 对话引擎的实现细节（chat.py 的 function-calling 流程）——属于 L2-ai-chat 切片
- 前端 UI 组件的样式系统和设计令牌——属于 L1-frontend
- RSS 协议规范和 XML 解析标准——仅讲 newsradar.py 中的实际用法

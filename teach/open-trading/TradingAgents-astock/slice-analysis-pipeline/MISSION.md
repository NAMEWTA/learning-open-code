# 使命：分析决策全链路——从股票代码到 Buy/Hold/Sell

## 为什么
我想理解 TradingAgents-Astock 从输入一只 A 股代码到输出最终投资决策的**完整代码执行路径**。不是单个模块的独立分析，而是数据如何经过 7 个阶段流转、每层如何修改状态、条件分支在哪里、以及链路中途失败的降级逻辑。这对于后续自己修改 Agent 拓扑、增减分析节点、调优决策逻辑是必不可少的。

## 成功的样子
- 能画出全链路 7 阶段节点图，准确说出每层输入/输出/职责
- 能用 `propagate("600519", "2026-07-08")` 这条入口追踪整个 `graph.invoke()` 的执行过程
- 能解释质量门控不通过时链路如何跳过后续阶段
- 能读懂 Bull/Bear 辩论和风险三方辩论的轮次控制逻辑

## 约束条件
- 已学完 L0 项目全景 + L1 模块总览（agents / graph / dataflows）
- 学习时间：每节短课 15 分钟以内
- 不需要逐行读源码，重点在控制流和数据流

## 不在范围内
- 数据源的具体 HTTP 协议细节（属于 L2 slice-data-fetching）
- LLM provider 路由与模型注册（属于 L2 slice-llm-routing）
- CLI / Web UI 的交互界面（属于 L2 slice-cli-flow / slice-web-ui-flow）

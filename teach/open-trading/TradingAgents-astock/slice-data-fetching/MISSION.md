# 使命：A 股多源数据获取链路

## 为什么
理解 TradingAgents-Astock 如何从 7 个免费数据源（mootdx TCP / 腾讯 / 东财 / 新浪 / 同花顺 / 财联社 / 百度）零外部服务依赖地拉取 A 股行情、财务、新闻、资金流数据，掌握 vendor 路由降级链、东财防封限流、中文 ticker 自动解析三条核心链路的实现原理，以便后续能自行扩展数据源或调试数据获取故障。

## 成功的样子
- 能画出 `get_data_inflo → route_to_vendor → a_stock.get_xxx → _em_get/mootdx/HTTP → 返回` 的完整调用链路
- 能解释 VENDOR_METHODS 的 17 个方法分类、3 种 vendor 覆盖差异，以及 fallback 链的构建规则
- 遇到网络超时、东财封 IP、中文股票名解析失败时，能定位根因并给出修复方向

## 约束条件
- 已完成 L0 项目全景图和 L1 dataflows 模块总览
- 本节聚焦数据获取链路，不涉及 Agent 分析逻辑和 Graph 工作流编排
- 每节短课 ≤1500 中文、≤4 个 h2 章节

## 不在范围内
- Agent 层的分析决策逻辑（归属 slice-analysis-pipeline）
- Graph 层的节点编排与状态传递（归属 module-graph）
- LLM 供应商路由与适配（归属 slice-llm-routing）

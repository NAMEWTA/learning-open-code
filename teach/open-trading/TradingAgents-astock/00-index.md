# TradingAgents-Astock · 架构教学 Wiki

> 📊 整体进度：12/12 goals · 100% · 已执行 3 轮
> 🕐 最后更新：2026-07-08

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ██████████ |
| L1 模块总览 | 6 | 6 | ██████████ |
| L2 垂直切片 | 5 | 5 | ██████████ |
| L3 微观 API | 6 | 6 | ██████████ |
| L4 深度剖析 | 0 | 0 | — |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/0001-project-map.html)**
  > 12 分钟建立全局地图——7 Analyst 多空辩论架构、双 LLM 设计、技术栈与目录结构。
- **[📄 项目总览参考](00-overview/reference/00-overview.html)**
  > 技术栈：Python + LangGraph + LangChain · 架构风格：多 Agent 辩论 Pipeline · 9 个 LLM 供应商 · 7 个免费数据源

---

## 📦 L1 · 模块总览

### module-agents — Agent 系统模块
- **[📘 模块导览短课](module-agents/lessons/0001-agents-module-tour.html)**
  > 15 分钟理解 7 Analyst + Bull/Bear 辩论 + 三方风险辩论 + Manager 决策的完整 Agent 体系
- **[📄 模块总览参考](module-agents/reference/agents-overview.html)**
  > 职责：Agent 角色注册、prompt 工厂、结构化输出、质量门控
  > 分层：analysts/ → researchers/ → risk_mgmt/ → managers/ → trader/ → utils/
- **[🔬 API 参考 (L3)](module-agents/reference/agents-api.html)** — 27 个源文件的公共接口速查
- **关联垂直切片**：
  - [🔪 完整分析决策链路](slice-analysis-pipeline/lessons/0001-flow-map.html)

### module-dataflows — 数据获取层模块
- **[📘 模块导览短课](module-dataflows/lessons/0001-dataflows-module-tour.html)**
  > 15 分钟理解 vendor 路由模式与 7 数据源直连架构
- **[📄 模块总览参考](module-dataflows/reference/dataflows-overview.html)**
  > 职责：多源 A 股数据获取、vendor 路由、ticker 安全校验
  > 数据源：mootdx (TCP) + 腾讯 + 东财 + 新浪 + 同花顺 + 财联社 + 百度
- **[🔬 API 参考 (L3)](module-dataflows/reference/dataflows-api.html)** — 含 _em_get 防封限流机制
- **关联垂直切片**：
  - [🔪 A 股多源数据获取链路](slice-data-fetching/lessons/0001-flow-map.html)

### module-graph — LangGraph 工作流引擎模块
- **[📘 模块导览短课](module-graph/lessons/0001-graph-module-tour.html)**
  > 15 分钟理解 7 阶段 Pipeline 的 LangGraph 拓扑与双 LLM 调度
- **[📄 模块总览参考](module-graph/reference/graph-overview.html)**
  > 职责：状态图拓扑、条件路由、信号处理、反思机制、SQLite 断点续跑
- **[🔬 API 参考 (L3)](module-graph/reference/graph-api.html)** — TradingAgentsGraph 完整接口
- **关联垂直切片**：
  - [🔪 完整分析决策链路](slice-analysis-pipeline/lessons/0001-flow-map.html)

### module-llm-clients — LLM 客户端适配层模块
- **[📘 模块导览短课](module-llm-clients/lessons/0001-llm-clients-module-tour.html)**
  > 15 分钟理解 11 种 provider 工厂路由与双 LLM 策略
- **[📄 模块总览参考](module-llm-clients/reference/llm-clients-overview.html)**
  > 职责：provider 路由、模型注册表、统一客户端接口
- **[🔬 API 参考 (L3)](module-llm-clients/reference/llm-clients-api.html)** — factory + base_client + 4 种客户端
- **关联垂直切片**：
  - [🔪 LLM 供应商路由链路](slice-llm-routing/lessons/0001-flow-map.html)

### module-cli — CLI 命令行界面模块
- **[📘 模块导览短课](module-cli/lessons/0001-cli-module-tour.html)**
  > 15 分钟理解 Typer 交互式 CLI 的 8 步引导流程
- **[📄 模块总览参考](module-cli/reference/cli-overview.html)**
  > 职责：交互式循环、config 构建、报告保存（Markdown + JSON）
- **[🔬 API 参考 (L3)](module-cli/reference/cli-api.html)** — main/cli 入口 + 报告保存接口
- **关联垂直切片**：
  - [🔪 CLI 命令执行链路](slice-cli-flow/lessons/0001-flow-map.html)

### module-web — Streamlit Web UI 模块
- **[📘 模块导览短课](module-web/lessons/0001-web-module-tour.html)**
  > 15 分钟理解 Streamlit 页面布局、后台线程模型与进度推送
- **[📄 模块总览参考](module-web/reference/web-overview.html)**
  > 职责：Web UI 渲染、后台分析运行、进度追踪、PDF 导出
- **[🔬 API 参考 (L3)](module-web/reference/web-api.html)** — runner + progress + pdf_export 接口
- **关联垂直切片**：
  - [🔪 Web UI 交互全链路](slice-web-ui-flow/lessons/0001-flow-map.html)

---

## 🔪 L2 · 垂直切片

### slice-analysis-pipeline — 完整分析决策链路
- **[📘 课程 1：链路地图](slice-analysis-pipeline/lessons/0001-flow-map.html)**
  > 从 stock ticker 到 Buy/Hold/Sell 的 7 阶段全景地图
- **[📘 课程 2：主成功路径](slice-analysis-pipeline/lessons/0002-main-path.html)**
  > 7 Analyst 并行研报 → 质量门控 → Bull/Bear 辩论 → Manager → Trader → 风险辩论 → PM
- **[📘 课程 3：异常与边界路径](slice-analysis-pipeline/lessons/0003-error-path.html)**
  > 质量门控不通过、数据获取失败、辩论轮次上限等边界处理
- **[📄 长链路速查](slice-analysis-pipeline/reference/analysis-pipeline-flow-map.html)**
- 所属模块：[module-agents](module-agents/reference/agents-overview.html) · [module-graph](module-graph/reference/graph-overview.html) · [module-dataflows](module-dataflows/reference/dataflows-overview.html)

### slice-data-fetching — A 股多源数据获取链路
- **[📘 课程 1：链路地图](slice-data-fetching/lessons/0001-flow-map.html)**
  > 7 数据源 vendor 路由全景与数据方法注册表
- **[📘 课程 2：主成功路径](slice-data-fetching/lessons/0002-main-path.html)**
  > K 线/财务/新闻三大主路径的完整调用链
- **[📘 课程 3：异常与边界路径](slice-data-fetching/lessons/0003-error-path.html)**
  > 东财封 IP、中文 ticker 解析失败、网络超时等异常处理
- **[📄 数据源速查](slice-data-fetching/reference/data-fetching-flow-map.html)**
- 所属模块：[module-dataflows](module-dataflows/reference/dataflows-overview.html)

### slice-web-ui-flow — Web UI 交互全链路
- **[📘 课程 1：链路地图](slice-web-ui-flow/lessons/0001-flow-map.html)**
  > Streamlit 页面布局 + 后台线程 + 进度推送的完整交互地图
- **[📘 课程 2：主成功路径](slice-web-ui-flow/lessons/0002-main-path.html)**
  > 用户输入 → 后台分析 → 报告展示 → PDF 导出的主路径
- 所属模块：[module-web](module-web/reference/web-overview.html)

### slice-cli-flow — CLI 命令执行链路
- **[📘 课程 1：链路地图](slice-cli-flow/lessons/0001-flow-map.html)**
  > Typer 命令解析 + 交互循环 + 配置构建的 6 阶段调用链
- **[📘 课程 2：主成功路径](slice-cli-flow/lessons/0002-main-path.html)**
  > 终端输入 → CLI 交互 → 分析运行 → 报告保存的主路径
- 所属模块：[module-cli](module-cli/reference/cli-overview.html)

### slice-llm-routing — LLM 供应商路由链路
- **[📘 课程 1：链路地图](slice-llm-routing/lessons/0001-flow-map.html)**
  > 11 种 provider 工厂路由 + 双 LLM 策略全景
- **[📘 课程 2：主成功路径](slice-llm-routing/lessons/0002-main-path.html)**
  > MiniMax → OpenAI 兼容客户端 → LLM API 调用的完整路径
- 所属模块：[module-llm-clients](module-llm-clients/reference/llm-clients-overview.html)

---

## 📊 源码覆盖统计

| 指标 | 数值 |
|------|------|
| 源码文件 | 81 / 101（80%） |
| 公共函数/类 | 全覆盖（6 份 L3 API 参考） |
| 核心功能 | 5 / 5（100%） |
| 豁免文件 | 20（14 测试文件 + 5 Alpha Vantage 遗留 + 1 示例脚本） |

---

## 🧭 学习路线建议

1. **入门**：从 [L0 项目全景图](00-overview/lessons/0001-project-map.html) 开始（12 分钟）
2. **模块认知**：按兴趣顺序学习 6 个 L1 模块导览（每个 15 分钟）
3. **深度追踪**：选择感兴趣的 L2 垂直切片，跟踪完整数据流（每个 30-45 分钟）
4. **API 速查**：开发时查阅对应模块的 L3 API 参考文档

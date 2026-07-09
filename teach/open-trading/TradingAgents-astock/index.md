# TradingAgents-Astock 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目全景图 | `./00-overview/` | 7 Analyst 多空辩论架构、双 LLM 设计、技术栈与目录结构 |
| Agent 系统模块 | `./module-agents/` | 7 个 Analyst 角色、Bull/Bear 辩论、三方风险辩论、Manager 决策 |
| 数据获取层模块 | `./module-dataflows/` | 多源 A 股数据直连、vendor 路由模式、7 数据源、东财防封限流 |
| Graph 工作流模块 | `./module-graph/` | LangGraph 节点编排、条件路由、状态传递与双 LLM 调度 |
| LLM 客户端模块 | `./module-llm-clients/` | 11 种 provider 路由工厂、模型注册表、双 LLM 策略 |
| CLI 模块 | `./module-cli/` | 8 步交互引导、10 种 LLM Provider、流式分析展示与 5 级报告保存 |
| Web 模块 | `./module-web/` | Streamlit Web UI 交互界面 |

| 分析决策全链路 | `./slice-analysis-pipeline/` | 从股票代码到 Buy/Hold/Sell 的 7 阶段垂直链路追踪 |

| A 股多源数据获取链路 | `./slice-data-fetching/` | 7 数据源 vendor 路由、K线/财务/新闻主路径、东财防封与异常诊断 |

| Web UI 交互全链路 | `./slice-web-ui-flow/` | 输入→分析→展示完整链路：5状态机、后台线程、进度推送、报告导出 |

| CLI 命令执行链路 | `./slice-cli-flow/` | 从终端输入到报告保存的 6 阶段调用链路与数据流转追踪 |

| LLM 供应商路由链路 | `./slice-llm-routing/` | 11 种 provider 工厂路由、双 LLM 策略与 OpenAI 兼容主路径追踪 |

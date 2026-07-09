# Vibe-Research 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | Vibe-Research 个人 AI 投研系统整体架构、技术栈与设计哲学 |
| 后端 FastAPI 模块 | `./module-backend/` | 后端 app.py 全端点注册、中间件、缓存策略与数据层模块 |
| 前端 React 模块 | `./module-frontend/` | 前端路由、页面组件、状态管理与 API 调用模式 |
| A股数据工具箱 | `./module-a-stock-data/` | a-stock-data 十层数据架构、40 端点与东财限流策略 |
| 全球股票数据工具箱 | `./module-global-stock-data/` | global-stock-data 八层数据架构、18 端点与多市场数据源 |

| 每日复盘全链路 | `./slice-daily-review/` | 8路并行加载→大盘情绪资金→AI复盘闭环的端到端追踪 |

| 资讯雷达全链路 | `./slice-intel-radar/` | React→API→108 RSS并发抓取→合规过滤→缓存→12赛道渲染 |

| 个股数据查询全链路 | `./slice-stock-data/` | 代码输入→30+端点并行→估值/财务/资金面/信号多维聚合展示 |

| AI对话全链路 | `./slice-ai-chat/` | API/CLI/MCP三条通道的端到端实现、function-calling循环与SSE流式协议 |

| 持仓管理全链路 | `./slice-portfolio/` | 录入→加权合并→实时盈亏→已清仓记录的本地持仓台账全链路 |

| 研报管理全链路 | `./slice-reports/` | 拖拽上传→base64编码→行业关键词归档→下载/删除的完整数据流 |

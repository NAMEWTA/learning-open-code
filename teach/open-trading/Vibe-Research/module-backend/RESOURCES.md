# Vibe-Research 后端模块资源

## 知识

- [后端主入口：`open-trading/Vibe-Research/backend/app.py`](../../../../open-trading/Vibe-Research/backend/app.py)
  FastAPI 应用定义，30+ 端点注册、CORS 中间件、可选鉴权中间件、分级缓存策略。后端架构教学的权威来源。
- [A股数据层：`open-trading/Vibe-Research/backend/astock.py`](../../../../open-trading/Vibe-Research/backend/astock.py)
  五层数据源封装（腾讯/东财/同花顺/mootdx/akshare），30+ 数据获取函数，惰性依赖导入模式。
- [美港股数据层：`open-trading/Vibe-Research/backend/gstock.py`](../../../../open-trading/Vibe-Research/backend/gstock.py)
  东财域内合规子集，push2优先/push2delay降级的主机 latch 策略，全球指数+美港股行情+关键财务。
- [市场总览：`open-trading/Vibe-Research/backend/market.py`](../../../../open-trading/Vibe-Research/backend/market.py)
  市场情绪、板块资金流、全球指数快照、短线情绪（连板梯队/炸板率/封板率）、成交额榜。全站共享 5 分钟 TTL 缓存。
- [资讯雷达：`open-trading/Vibe-Research/backend/newsradar.py`](../../../../open-trading/Vibe-Research/backend/newsradar.py)
  12 赛道 108 公开 RSS 源并发抓取，合规过滤，JSON 文件缓存，纯标准库 + 线程池。
- [持仓管理：`open-trading/Vibe-Research/backend/portfolio.py`](../../../../open-trading/Vibe-Research/backend/portfolio.py)
  本地 JSON 持久化，加权平均成本合并，原子写入（tmp + rename），后台 30 分钟定时刷新。
- [AI 对话层：`open-trading/Vibe-Research/backend/chat.py`](../../../../open-trading/Vibe-Research/backend/chat.py)
  OpenAI 兼容 function-calling 流式对话，投研五维分析框架，SSRF 防护，最大 6 轮工具调用。
- [CLI 运行时：`open-trading/Vibe-Research/backend/cli_runtime.py`](../../../../open-trading/Vibe-Research/backend/cli_runtime.py)
  四种 CLI（Claude/Qwen/DeepSeek/Codex）的检测与 spawn，三种提示词投递方式，300s 超时兜底。
- [MCP Server：`open-trading/Vibe-Research/backend/mcp_server.py`](../../../../open-trading/Vibe-Research/backend/mcp_server.py)
  纯标准库 JSON-RPC over stdio，复用 chat.py 工具定义，暴露 A 股数据工具给 Claude Code agent。
- [我的研报：`open-trading/Vibe-Research/backend/myreports.py`](../../../../open-trading/Vibe-Research/backend/myreports.py)
  Base64 上传、本地文件存储、文件名关键词自动行业分类、白名单扩展名校验。
- [依赖清单：`open-trading/Vibe-Research/backend/requirements.txt`](../../../../open-trading/Vibe-Research/backend/requirements.txt)
  核心层（fastapi/uvicorn/requests）+ 全栈数据源（akshare/mootdx/pandas），标注了渐进依赖策略。

## 智慧（社区）

- [GitHub 仓库：simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)
  项目上游仓库，适用于核对后端 issue 和最新版本更新。
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
  FastAPI 框架的权威文档，适用于理解路由注册、中间件、依赖注入等框架机制。
- [Starlette 中间件文档](https://www.starlette.io/middleware/)
  FastAPI 底层框架的中间件文档，适用于理解 CORS 和自定义中间件的执行顺序。

## 空白

- 当前未找到独立第三方的 Vibe-Research 后端深度架构解读文章。
- 后端的测试覆盖情况暂未纳入 L1 扫描范围，适合在后续 L3 API 参考中补充。

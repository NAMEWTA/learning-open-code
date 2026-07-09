# Vibe-Research 项目整体架构资源

## 知识

- [本地 README：`open-trading/Vibe-Research/README.md`](../../../../open-trading/Vibe-Research/README.md)
  项目定位、功能列表、数据源说明、快速开始、AI 接入方式、合规声明与免责声明的主来源。
- [后端主入口：`open-trading/Vibe-Research/backend/app.py`](../../../../open-trading/Vibe-Research/backend/app.py)
  FastAPI 应用定义，全部 /api/* 端点注册、中间件链、缓存策略。架构教学的 API 层面权威来源。
- [前端包清单：`open-trading/Vibe-Research/frontend/package.json`](../../../../open-trading/Vibe-Research/frontend/package.json)
  前端依赖与技术栈声明：React 19、TypeScript、Vite 6、Tailwind 3、ECharts 6、Zustand 5。
- [前端路由表：`open-trading/Vibe-Research/frontend/src/router.tsx`](../../../../open-trading/Vibe-Research/frontend/src/router.tsx)
  10 个页面入口的路由映射，是理解前端功能模块划分的最佳起点。
- [A 股数据工具箱：`open-trading/Vibe-Research/a-stock-data/SKILL.md`](../../../../open-trading/Vibe-Research/a-stock-data/SKILL.md)
  A 股全栈数据工具包接口文档，十层数据架构、40 个端点，后端 `astock.py` 的上游来源。
- [全球股票数据工具箱：`open-trading/Vibe-Research/global-stock-data/SKILL.md`](../../../../open-trading/Vibe-Research/global-stock-data/SKILL.md)
  美股/港股数据工具包接口文档，八层数据架构、18 个端点，后端 `gstock.py` 的上游来源。
- [后端依赖清单：`open-trading/Vibe-Research/backend/requirements.txt`](../../../../open-trading/Vibe-Research/backend/requirements.txt)
  Python 后端依赖，核心层（fastapi/uvicorn/requests）+ 全栈数据源（akshare/mootdx/pandas）。
- [前端主题配置：`open-trading/Vibe-Research/frontend/tailwind.config.ts`](../../../../open-trading/Vibe-Research/frontend/tailwind.config.ts)
  Tailwind CSS 主题配置，玻璃暖橙主题的 CSS 变量定义与自定义阴影。

## 智慧（社区）

- [GitHub 仓库：simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)
  项目主页，适用于核对 issue、release、README 更新与真实使用反馈；本 L0 课程以本地子模块快照为准。
- [项目官网：viberesearch.wiki](https://viberesearch.wiki)
  产品介绍与演示，适用于了解产品层面的功能展示和使用场景。
- [上游数据源生态：a-stock-data](https://github.com/simonlin1212/a-stock-data)
  A 股数据引擎的上游仓库，用于跟进最新端点和数据源扩展。
- [上游数据源生态：global-stock-data](https://github.com/simonlin1212/global-stock-data)
  美股/港股数据引擎的上游仓库，用于跟进最新端点。

## 空白

- 当前未找到独立第三方的 Vibe-Research 深度源码解读文章；后续深入某个模块时应优先补充来自 issue、PR 或 release discussion 的真实设计背景。
- 项目的测试覆盖和 CI/CD 配置暂时未纳入 L0 扫描范围，适合在 L1 后端模块中作为独立主题补充。

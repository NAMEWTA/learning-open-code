# 前端 React 模块 资源

## 知识

- [React 19 官方文档](https://react.dev/) — 函数组件、Hooks、StrictMode、ErrorBoundary 等核心概念
- [TypeScript 5.7 手册](https://www.typescriptlang.org/docs/) — 前端类型定义与类型安全
- [Tailwind CSS 3.4 文档](https://tailwindcss.com/docs) — utility-first CSS、dark mode、自定义主题配置
- [Vite 6 文档](https://vite.dev/) — 开发服务器、HMR、代理配置、生产构建
- [React Router 7 文档](https://reactrouter.com/) — createBrowserRouter、Layout Route、参数路由
- [Zustand 5 文档](https://docs.pmnd.rs/zustand) — 轻量全局状态管理
- [ECharts 6 文档](https://echarts.apache.org/) — K线图、资金流图、估值分位图配置
- [Lucide React 图标库](https://lucide.dev/icons) — 侧边栏、按钮、状态指示图标

## 源码入口（按优先级）

| 文件 | 用途 | 关键度 |
|------|------|--------|
| `frontend/src/router.tsx` | React Router 路由表，定义 10 个页面 + 重定向 | 核心 |
| `frontend/src/main.tsx` | React 挂载入口，Root + Provider + ErrorBoundary | 核心 |
| `frontend/src/lib/api.ts` | API 客户端，30+ 接口类型 + 鉴权头 + 优雅降级 | 核心 |
| `frontend/src/lib/llm.ts` | AI 流式对话客户端（SSE NDJSON 解析） | 核心 |
| `frontend/src/lib/ai-models.ts` | AI 模型配置清单（9 个 API 提供商 + 7 个 CLI 订阅） | 核心 |
| `frontend/src/components/layout/Layout.tsx` | 侧边栏 + 主内容区布局，导航配置 | 核心 |
| `frontend/src/index.css` | 玻璃暖橙主题 CSS 变量（暗/亮双模式） | 重要 |
| `frontend/tailwind.config.ts` | Tailwind 主题扩展（色板、字体、阴影） | 重要 |
| `frontend/vite.config.ts` | Vite 配置（代理 :8900、路径别名、代码分割） | 重要 |
| `frontend/src/components/ui/GlassCard.tsx` | 玻璃质感基础容器组件 | 辅助 |
| `frontend/src/components/ui/PageHeader.tsx` | 页面标题组件 | 辅助 |
| `frontend/src/components/ui/AskAiButton.tsx` | 嵌入式 AI 对话面板（流式+工具调用） | 辅助 |
| `frontend/src/components/ui/SaveNoteButton.tsx` | 存入研究记录按钮 | 辅助 |
| `frontend/src/components/ui/Disclaimer.tsx` | 免责声明组件 | 辅助 |
| `frontend/src/components/ui/EarningsSnapshot.tsx` | 财报速览卡组件 | 辅助 |
| `frontend/src/components/common/ErrorBoundary.tsx` | React 错误边界 | 辅助 |
| `frontend/src/lib/watchlist.ts` | 自选股 localStorage 读写工具 | 辅助 |
| `frontend/src/lib/notes.ts` | 研究记录 localStorage 读写工具 | 辅助 |
| `frontend/src/lib/utils.ts` | cn() 工具函数（clsx + tailwind-merge） | 辅助 |
| `frontend/src/hooks/useDarkMode.ts` | 暗/亮主题切换 Hook | 辅助 |
| `frontend/src/data/sectors.json` | 板块中心静态配置（常看赛道列表） | 辅助 |

## 智慧（社区）

- [React subreddit](https://www.reddit.com/r/reactjs/) — React 社区讨论与最佳实践
- [Tailwind CSS Discord](https://tailwindcss.com/discord) — Tailwind 官方社区，组件设计参考

## 空白

- 前端测试策略：项目当前无前端测试框架，需关注后续是否引入 Vitest 或 Testing Library
- 性能监控：未发现 Lighthouse CI 或 Web Vitals 埋点，可作为后续优化方向

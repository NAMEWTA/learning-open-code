# 使命：Frontend core 数据层

## 为什么
学习者已看过 workspace 页面层，现在需要理解 DeerFlow 前端如何把 UI 事件转成 Gateway 请求：LangGraph SDK 与 REST 两条通道、认证外壳、线程流式状态，以及 skills/MCP/uploads 等配置域的同一套 api + hooks 模式。掌握后，调试 API 失败或改数据契约时能直接落到 `frontend/src/core/`，而不是在组件树里盲搜。

## 成功的样子
- 能区分 workspace 组件与 core 数据层的职责边界，并交叉引用 workspace 模块。
- 能判断一次出站请求应走 LangGraph SDK（`getAPIClient`）还是 REST（`fetcher.ts`）。
- 能说明 `AuthProvider` 与 `getServerSideUser` 如何配合，以及 CSRF/cookie 契约为何集中在 `fetcher.ts`。
- 能从一个聊天提交追到 `useThreadStream` → `getAPIClient` → Gateway `/api/langgraph`。
- 能说出 skills、mcp、uploads 三个域的 `api.ts` + `hooks.ts` 分工。

## 约束条件
- 本主题是 L1 模块导览，15 分钟内建立方向感；长接口清单放入 reference。
- 读者有 React/Next.js 与 TanStack Query 基础。
- 不深入 Gateway 路由实现或 LangGraph graph 内部协议。

## 不在范围内
- workspace 页面布局、消息组件、artifact/sidecar UI 细节（见 module-frontend-workspace）。
- streamdown、rehype、i18n 渲染辅助模块的逐项讲解。
- 每个 core 子域的完整源码深挖；后续可拆成 L2 垂直切片课。

# Renderer 核心与 UI Shell 资源

## 知识

- [AionU renderer 根入口](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/main.tsx) — provider 栈、配置 bootstrap、运行时故障弹窗与 `createRoot` 挂载都从这里开始。
- [AionU 路由入口](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/components/layout/Router.tsx) — 查看 `HashRouter`、保护路由、懒加载页面和旧路由重定向。
- [AionU UI Shell](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/components/layout/Layout.tsx) — 观察侧栏、标题栏、导航历史、深链、通知、托盘事件如何被统一接入。
- [AionU renderer 启动准备](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/services/bootstrapRenderer.ts) — 解释为什么 renderer 要先等 `configService.initialize()` 再进入业务页面。
- [AionU renderer hooks 上下文](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/context/) — 理解 `AuthProvider`、`LayoutContext`、`NavigationHistoryProvider` 这些 provider 的状态边界。
- [导航 E2E 证据](../../../../open-ai-desktop/AionU/tests/e2e/specs/navigation.e2e.ts) — 佐证 `/guid`、设置页与跨页导航是 renderer 的核心可观察行为。
- [renderer 单元测试目录](../../../../open-ai-desktop/AionU/tests/unit/renderer/) — 可回查 shell、通知、消息流、设置控件等稳定行为，避免只凭肉眼读源码。
- [React `createRoot` 参考](https://react.dev/reference/react-dom/client/createRoot) — 对照理解 renderer 最终如何挂载到 DOM 根节点。
- [React Router `HashRouter` 参考](https://reactrouter.com/api/declarative-routers/HashRouter) — 对照 AionU 在 Electron/Web 双形态里为什么选择 hash 路由。

## 智慧（社区）

- [AionUi GitHub Discussions](https://github.com/iOfficeAI/AionUi/discussions) — 适合验证你对 renderer 路由、设置页入口和交互设计的理解是否贴近维护者意图。
- [AionUi GitHub Issues](https://github.com/iOfficeAI/AionUi/issues) — 适合搜索历史 bug，观察 shell、导航、通知等问题是如何被报告和修复的。

## 空白

- 当前缺少专门面向 renderer 架构的上游设计文档，很多判断仍需从源码和测试反推。
- hooks 目录规模较大，但缺少官方分层说明；后续课程需要把 system/chat/file/mcp/ui hooks 再拆成独立主题。

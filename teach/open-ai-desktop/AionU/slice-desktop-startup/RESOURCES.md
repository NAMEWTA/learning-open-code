# 桌面启动到首屏全链路资源

## 知识

- [L0：AionU 项目总览参考](../00-overview/reference/00-overview.html)
  用于确认 Electron main、process、preload、renderer、aioncore backend 和 WebHost 在全局架构里的相对位置。
- [L1：Electron 主入口与生命周期参考](../module-main-entry/reference/main-entry-overview.html)
  用于理解 `packages/desktop/src/index.ts` 的模式分支、backend 启动、窗口创建和退出清理职责。
- [L1：Process 基础设施参考清单](../module-process-infra/reference/process-infra-overview.html)
  用于确认 `initializeProcess()` 之前后发生的 storage、bridge、i18n 和 backend 二进制解析前置工作。
- [L1：Renderer 核心与 UI Shell 参考](../module-renderer-core/reference/renderer-core-overview.html)
  用于理解 renderer 的 provider 栈、启动闸门、路由守卫和 UI shell 入口。
- `open-ai-desktop/AionU/packages/desktop/src/index.ts`
  本 L2 的主源码入口，覆盖 Electron 顶层分支、`handleAppReady()`、backend 启动、窗口创建和 renderer 装载。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/main.tsx`
  renderer bootstrap 的主入口，覆盖 Sentry、配置初始化、provider、失败弹窗和 React root render。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/components/layout/Router.tsx`
  首屏路由落点的直接依据，覆盖登录页、受保护布局、默认 `/guid` 和兜底跳转。
- `open-ai-desktop/AionU/tests/e2e/specs/app-launch.e2e.ts`
  启动烟雾测试依据，验证窗口标题、renderer body 可见和无关键 console error。

## 智慧（社区）

本主题是仓库内源码考古切片，当前没有引入外部社区资源。后续若要讨论 Electron 启动性能、backend 子进程托管或 Playwright Electron 测试策略，可再补充 Electron、Playwright 或项目 issue 讨论。

## 空白

- 未读取 aioncore 源码，因此 backend 内部健康检查、迁移和 REST 接口行为只按 AionU 桌面侧调用边界描述。
- 未读取 Playwright fixtures，因此本主题只使用 `app-launch.e2e.ts` 中可见断言，不推断 fixture 如何启动 Electron。

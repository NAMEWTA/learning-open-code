# 使命：Renderer 核心与 UI Shell

## 为什么
本主题服务于 AionU 源码学习主线：先建立 renderer 启动后的整体心智模型，再进入具体页面、会话和设置子系统。用户需要知道 React 根入口如何把 provider、路由和 UI shell 串起来，否则后续读任何页面都会缺少定位坐标。

## 成功的样子
- 能从 `packages/desktop/src/renderer/main.tsx` 解释应用何时开始渲染、何时等待配置就绪、何时显示启动失败 UI。
- 能从 `Router.tsx` 和 `Layout.tsx` 说清认证保护、主要路由入口、侧栏壳层与系统级 hook 的分工。
- 能据此决定下一步该深入页面实现、hook 机制还是与 main/preload 的交界。

## 约束条件
- 以 15 分钟内可完成的短课交付，先建立骨架，不扩写具体页面业务。
- 只覆盖 renderer 核心组织方式，避免滑向完整路由百科或全部 hook 细节。
- 所有材料写入 `teach/open-ai-desktop/AionU/module-renderer-core/`，不改动与本 goal 无关的主题。

## 不在范围内
- `common/adapter` 如何把业务请求映射到 REST/WS。
- 单个页面内部实现，例如 conversation、team、cron、settings 的业务细节。
- main process、preload、backend 生命周期的深入展开。

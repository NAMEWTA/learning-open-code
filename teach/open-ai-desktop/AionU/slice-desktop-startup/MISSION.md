# 使命：桌面启动到首屏全链路

## 为什么
这组 L2 短课要帮助学习者把 AionU 桌面启动时散落在 Electron main、process 基础设施、preload、renderer bootstrap、Router 与 E2E 烟雾测试里的代码连成一条可调试链路。掌握这条链后，排查“窗口没出来”“首屏空白”“backend 启动失败但 UI 还在”等问题时，可以按阶段定位，而不是在整个桌面工程里盲搜。

## 成功的样子
- 能从 `app.whenReady()` 追到 `handleAppReady()`、`initializeProcess()`、`startBackendOrExit()`、`createWindow()` 和 renderer 装载。
- 能解释 preload 如何把 backend port、初始语言和 backend 失败状态暴露给 renderer。
- 能说清 React bootstrap 为什么先等认证与 renderer 配置，再把默认路由导向 `/guid` 或失败弹窗。
- 能用 `app-launch.e2e.ts` 判断这条链路被测试证明到了哪一层、没有证明哪一层。

## 约束条件
- 本主题只写入 `teach/open-ai-desktop/AionU/slice-desktop-startup/`。
- 源项目 `open-ai-desktop/AionU/` 只读，不修改项目级索引、`_progress.json` 或 `_progress.md`。
- 每节 lesson 控制为 15 分钟短课；长时序、源码索引和边界表放到参考文档。

## 不在范围内
- 不展开 aioncore 内部启动实现，只讲 Electron 如何托管并暴露 backend 状态。
- 不深入每个 bridge 子模块、托盘、pet、deep link、自动更新或 WebUI 静态服务内部。
- 不把 app-launch E2E 扩展成端到端业务验证；它在本主题里只作为启动烟雾测试证据。

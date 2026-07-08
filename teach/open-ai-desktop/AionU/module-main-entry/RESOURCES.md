# Electron 主入口与生命周期 资源

## 知识

- [`open-ai-desktop/AionU/packages/desktop/src/index.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/index.ts)
  本主题的一手入口源码。适用于：确认模式分支、窗口创建、backend 启动顺序、协议注册和退出生命周期。
- [`open-ai-desktop/AionU/packages/desktop/src/process/startup/backendStartup.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/process/startup/backendStartup.ts)
  把“启动 backend 成功 / 失败 / 取消”的语义压缩成可测试单元。适用于：理解入口为何把异常处理外提而不把细节塞进 `index.ts`。
- [`open-ai-desktop/AionU/packages/desktop/src/process/startup/quitCleanup.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/process/startup/quitCleanup.ts)
  退出清理的统一收尾器。适用于：追踪 `before-quit`、超时保护、backend 停止与 pet 窗口销毁。
- [`open-ai-desktop/AionU/packages/desktop/src/process/startup/backendStartupFailure.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/process/startup/backendStartupFailure.ts)
  启动失败分类器。适用于：把入口里记录到的故障状态映射成可恢复、可提示的失败类型。
- [`open-ai-desktop/AionU/tests/unit/bootstrap/backendStartup.test.ts`](../../../../open-ai-desktop/AionU/tests/unit/bootstrap/backendStartup.test.ts)
  单元测试证据。适用于：验证 `startBackendOrExit()` 的默认退出行为、非退出模式和取消语义。
- [`open-ai-desktop/AionU/tests/e2e/specs/app-launch.e2e.ts`](../../../../open-ai-desktop/AionU/tests/e2e/specs/app-launch.e2e.ts)
  启动烟雾测试。适用于：确认“窗口可开、renderer 已加载、启动期无关键 console error”这三个外部可观察结果。
- [`teach/open-ai-desktop/AionU/00-overview/lessons/0001-project-map.html`](../00-overview/lessons/0001-project-map.html)
  L0 项目导览。适用于：在进入主入口前，先回忆 AionU 的桌面壳、backend 和 WebHost 三条主线。

## 智慧（社区）

当前主题未额外收录外部社区资源。原因是本轮目标是建立本地源码入口坐标，仓库内也没有专门针对 Electron main process 的架构讨论索引；等后续进入 WebHost、打包发布或故障恢复时，再补充 Issue / PR 讨论入口更有价值。

## 空白

- 缺少仓库内正式的“桌面启动时序图”文档，导致入口知识主要散落在代码注释和测试中
- 缺少针对 `backendStartupFailure.ts` 各类失败样本的文档化案例，后续 L2/L3 若要讲恢复路径，需要补充真实日志样本

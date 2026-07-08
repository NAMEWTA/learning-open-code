# 使命：Capacitor 移动端与 PWA 宿主

## 为什么
学习者需要能在 super-productivity 中快速判断一个移动端问题属于 Angular 应用、Capacitor 原生壳、PWA/service worker、Android/iOS feature，还是平台桥接层。掌握这个边界后，排查后台保存、提醒、分享、Widget、OAuth、WebDAV、PWA 缓存等问题时不会在错误层级里兜圈。

## 成功的样子
- 能从 `src/main.ts` 判断 PWA service worker 与 native 平台生命周期的分界。
- 能解释 `capacitor.config.ts`、`android/`、`ios/` 与 Angular feature 目录各自承担什么职责。
- 能沿 Android `window.SUPAndroid`、iOS Capacitor plugin、通用 mobile notification effect 找到平台桥接入口。
- 能给后续 L2 课拆出后台 flush、Android reminder、share/widget、iOS WebDAV、PWA 缓存等垂直切片。

## 约束条件
- 本主题是 L1 模块总览，短课控制在 15 分钟内，长入口清单放入参考文档。
- 讲解必须基于当前源码，不泛泛介绍 Capacitor 或 PWA 概念。
- 只写入本主题目录，不同步源码、项目索引或进度台账。

## 不在范围内
- 不深入讲任务领域模型、同步 op-log 内部算法或 Electron 桌面宿主。
- 不覆盖 Android/iOS 发布签名、商店上架和完整 CI 发布流程。
- 不逐行讲完每个 native service、receiver、plugin；这些留给 L2/L3。

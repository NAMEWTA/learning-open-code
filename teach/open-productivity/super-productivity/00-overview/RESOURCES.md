# super-productivity 项目整体架构总览资源

## 知识

- [README.md](../../../../open-productivity/super-productivity/README.md)
  产品定位、功能清单、下载渠道、官方 Wiki、社区入口。适用于判断项目面向用户解决什么问题。
- [package.json](../../../../open-productivity/super-productivity/package.json)
  脚本、依赖和包构建入口。适用于识别 Angular、Electron、Capacitor、Playwright、NgRx、package 构建链路。
- [angular.json](../../../../open-productivity/super-productivity/angular.json)
  Angular application builder、入口文件、资产、service worker、测试与 lint 配置。适用于理解 Web/PWA 构建边界。
- [ARCHITECTURE-DECISIONS.md](../../../../open-productivity/super-productivity/ARCHITECTURE-DECISIONS.md)
  当前活跃架构决策。适用于提炼跨模块设计哲学和后续源码阅读约束。
- [src/main.ts](../../../../open-productivity/super-productivity/src/main.ts)
  Angular bootstrap、NgRx root、Effects、service worker、插件初始化、Capacitor 生命周期。适用于建立应用启动主线。
- [src/app/app.routes.ts](../../../../open-productivity/super-productivity/src/app/app.routes.ts)
  顶层路由、懒加载页面和主要业务入口。适用于提炼用户可见功能域。
- [src/app/root-store/feature-stores.module.ts](../../../../open-productivity/super-productivity/src/app/root-store/feature-stores.module.ts)
  feature store 与 effects 注册清单。适用于识别核心状态域和跨平台 effect。
- [electron/start-app.ts](../../../../open-productivity/super-productivity/electron/start-app.ts)
  Electron 主进程启动、窗口、托盘、IPC、空闲检测和退出流程。适用于理解桌面宿主边界。
- [packages/README.md](../../../../open-productivity/super-productivity/packages/README.md)
  插件包和插件 API 概览。适用于理解 monorepo packages 的插件侧用途。
- [docs/sync-and-op-log/package-boundaries.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/package-boundaries.md)
  同步包依赖方向文档。适用于后续学习 sync-core、sync-providers、app wiring 的边界。
- [docs/sync-and-op-log/README.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/README.md)
  Operation Log 与 sync 文档入口，明确 `SUP_OPS`、IndexedDB、本地持久化和 sync providers 的整体关系。
- [docs/sync-and-op-log/operation-log-architecture.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/operation-log-architecture.md)
  操作日志架构权威说明。适用于后续深入本地持久化、IndexedDB store、回放和同步一致性。
- [packages/super-sync-server/package.json](../../../../open-productivity/super-productivity/packages/super-sync-server/package.json)
  SuperSync 服务端依赖和脚本入口。适用于识别 Fastify、Prisma、Docker 部署等服务端线索。
- [Angular 文档](https://angular.dev/)
  Angular application、standalone bootstrap、router、service worker 的官方参考。适用于核对框架概念。
- [NgRx 文档](https://ngrx.io/docs)
  Store、Effects、Entity、Devtools 的官方参考。适用于理解项目的状态管理模式。
- [Electron 文档](https://www.electronjs.org/docs/latest)
  主进程、BrowserWindow、IPC、应用生命周期的官方参考。适用于阅读 `electron/`。
- [Capacitor 文档](https://capacitorjs.com/docs)
  移动端 WebView、App lifecycle、原生插件桥接的官方参考。适用于阅读 Android/iOS 分支。

## 智慧（社区）

- [Super Productivity GitHub Discussions](https://github.com/super-productivity/super-productivity/discussions)
  官方讨论区。适用于验证功能意图、贡献方向和维护者对架构问题的解释。
- [Super Productivity Issues](https://github.com/super-productivity/super-productivity/issues)
  真实缺陷和功能请求。适用于把源码学习连接到实际维护场景。
- [r/superProductivity](https://www.reddit.com/r/superProductivity/)
  用户社区。适用于观察真实使用痛点，但技术判断仍以源码、ADR 和官方讨论为准。

## 空白

- 本次 L0 未逐一核对 Jira、GitHub、GitLab、OpenProject、Linear、ClickUp、Azure DevOps 等第三方 API 官方文档；后续学习 issue provider 垂直切片时需要补充。
- 本次 L0 未深入移动端原生工程的 Gradle、Xcode、Fastlane 配置；后续移动打包专题再补充平台官方资料。

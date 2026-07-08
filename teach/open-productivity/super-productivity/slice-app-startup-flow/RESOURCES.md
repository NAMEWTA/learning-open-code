# 应用启动与数据初始化全链路资源

## 知识

- [`src/main.ts`](../../../../open-productivity/super-productivity/src/main.ts)
  Angular standalone bootstrap、provider 注册、APP_INITIALIZER、路由、service worker、Capacitor 生命周期和后台 flush 的主入口。
- [`src/app/app.component.ts`](../../../../open-productivity/super-productivity/src/app/app.component.ts)
  根组件启动副作用入口；用于确认 `StartupService.init()`、初始同步后 banner、onboarding 和全局 shell 行为。
- [`src/app/app.routes.ts`](../../../../open-productivity/super-productivity/src/app/app.routes.ts)
  顶层路由入口；用于区分页面空白是路由/懒加载问题还是启动数据问题。
- [`src/app/core/startup/startup.service.ts`](../../../../open-productivity/super-productivity/src/app/core/startup/startup.service.ts)
  启动后初始化任务、单实例检查、备份/持久化、主题预加载、Electron ready、插件初始化等待点。
- [`src/app/core/data-init/data-init.service.ts`](../../../../open-productivity/super-productivity/src/app/core/data-init/data-init.service.ts)
  初始数据加载入口；实例化后触发 op-log hydration，并通过 `DataInitStateService` 广播首次数据完成。
- [`src/app/op-log/persistence/operation-log-hydrator.service.ts`](../../../../open-productivity/super-productivity/src/app/op-log/persistence/operation-log-hydrator.service.ts)
  数据落地核心；负责快照、旧库迁移、schema migration、op replay、recovery 和 `loadAllData` dispatch。
- [`src/app/imex/sync/sync-trigger.service.ts`](../../../../open-productivity/super-productivity/src/app/imex/sync/sync-trigger.service.ts)
  初始同步完成信号和后续自动同步触发器；用于判断 UI 是否应继续等待同步。
- [`src/app/imex/sync/sync-wrapper.service.ts`](../../../../open-productivity/super-productivity/src/app/imex/sync/sync-wrapper.service.ts)
  一轮同步包装器；负责并发闸门、下载优先、上传、错误处理和“当前同步完成或未启用”的等待信号。
- [`src/app/plugins/plugin.service.ts`](../../../../open-productivity/super-productivity/src/app/plugins/plugin.service.ts)
  插件运行时初始化；发现内置/上传插件、自动启用迁移插件、加载 enabled 插件和处理失败状态。
- [相邻参考：Angular 应用装配与全局壳层](../module-angular-app-shell/reference/angular-app-shell-overview.html)
  用于确认 bootstrap、route、root shell 和 feature store 注册边界。
- [相邻参考：Operation Log 与同步模块](../module-op-log-sync/reference/op-log-sync-overview.html)
  用于继续深入 op-log 持久化、sync wrapper 和远端 operation apply。
- [相邻参考：插件系统、插件 API 与运行时加载](../module-plugin-system/reference/plugin-system-overview.html)
  用于继续追踪插件初始化后的 manifest、loader、runner、bridge 和 issue provider 扩展。

## 智慧（社区）

- [johannesjo/super-productivity GitHub Issues](https://github.com/johannesjo/super-productivity/issues)
  真实启动、同步、IndexedDB、Electron 和插件问题报告；适用于验证故障排查入口是否贴近维护者语境。
- 本仓库相邻教学主题：`module-angular-app-shell`、`module-op-log-sync`、`module-plugin-system`
  适用于把 L2 启动切片与 L1 模块边界互相校验，避免在一个切片里过度展开算法细节。

## 空白

- 尚未为本切片单独建立 L3/L4 深剖；需要后续补充 `OperationLogHydratorService`、`SyncTriggerService` 和 `PluginService.initializePlugins()` 的微观 API 课程。

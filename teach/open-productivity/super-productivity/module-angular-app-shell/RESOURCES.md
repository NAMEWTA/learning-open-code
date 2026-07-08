# Angular 应用装配与全局壳层资源

## 知识

- 本地源码：`open-productivity/super-productivity/src/main.ts`
  Angular renderer 的启动总入口。适用于核对 `bootstrapApplication`、providers、NgRx 根注册、router、service worker、插件初始化、DataInit 和 Capacitor 生命周期。
- 本地源码：`open-productivity/super-productivity/src/app/app.routes.ts`
  顶层 URL 到页面入口的映射表。适用于从浏览器地址、hash route 或默认页跳转反查功能入口。
- 本地源码：`open-productivity/super-productivity/src/app/app.component.ts`
  根组件行为入口。适用于理解主题、快捷键、onboarding、粘贴任务、背景图、全局菜单和启动服务触发点。
- 本地源码：`open-productivity/super-productivity/src/app/app.component.html`
  全局 UI 壳层模板。适用于观察 side nav、header、right panel、`router-outlet`、mobile bottom nav、onboarding 与 context menu 如何装配。
- 本地源码：`open-productivity/super-productivity/src/app/root-store/feature-stores.module.ts`
  feature reducer/effects 注册表。适用于从业务域反查 NgRx feature key、effects 和平台条件注册。
- 本地源码：`open-productivity/super-productivity/src/app/core-ui/layout/`
  壳层布局状态、响应式断点和 side panel 控制。适用于排查 add task bar、notes、issue panel、mobile bottom nav、滚动和焦点恢复。
- 本地源码：`open-productivity/super-productivity/src/app/core/startup/`
  启动后的平台与体验初始化。适用于排查单实例检查、备份提示、持久化请求、Electron ready、插件延迟初始化和浏览器 unload 守卫。
- L0 课程：`teach/open-productivity/super-productivity/00-overview/lessons/0001-project-map.html`
  项目全局地图。适用于回到 Angular renderer、Electron/Capacitor 宿主、packages 边界的总体位置。
- 官方文档：[Angular `bootstrapApplication`](https://angular.dev/api/platform-browser/bootstrapApplication)
  用于理解本仓库采用的 standalone bootstrap 形态。
- 官方文档：[NgRx Store](https://ngrx.io/guide/store)
  用于理解 `StoreModule.forRoot`、`StoreModule.forFeature` 与 reducer/effects 分层。

## 智慧（社区）

- [Super Productivity GitHub Discussions](https://github.com/super-productivity/super-productivity/discussions)
  适用于验证启动、路由和 UI 壳层问题是否已有维护者或用户讨论。
- [Super Productivity Issues](https://github.com/super-productivity/super-productivity/issues)
  适用于查询启动回归、移动端后台行为、service worker、插件初始化或壳层 UI 缺陷。

## 空白

- 暂未找到专门讲解本项目 Angular app shell 的外部架构文章；本主题以本地源码、L0 课程和官方框架文档为主。

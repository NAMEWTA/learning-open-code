# 使命：Angular 应用装配与全局壳层

## 为什么
学习者已经通过 L0 建立了 super-productivity 的全局地图，现在需要能沿着 Angular renderer 的启动链路定位问题：从应用启动、URL 路由、根组件壳层到全局状态注册，知道每一步由哪个入口负责。

## 成功的样子
- 能用一句话说明 Angular 应用壳层在整体架构中的职责。
- 能从一个 URL 反查到 `APP_ROUTES`、页面入口和根组件承载位置。
- 能从启动异常反查到 `bootstrapApplication`、`APP_INITIALIZER`、`DataInitService`、service worker、Capacitor 生命周期或插件初始化。
- 能判断 UI 壳层问题应先看 `AppComponent`、`core-ui/layout` 还是 feature store/effects。

## 约束条件
- 本主题是 L1 模块总览，不展开任务领域、操作日志同步、插件 API 或 Electron 主进程细节。
- 每节课控制在 15 分钟内，lesson 只保留定位技能所需材料，接口清单与长表格放入 reference。
- 课程事实以当前本地源码快照为准。

## 不在范围内
- 任务、项目、标签等业务领域模型的完整讲解。
- op-log 同步算法、冲突处理和持久化深剖。
- Electron/Capacitor 原生工程的独立生命周期全景。
- Angular、NgRx、Material 的通用入门教程。

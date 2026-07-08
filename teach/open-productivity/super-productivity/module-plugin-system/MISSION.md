# 使命：插件系统、插件 API 与运行时加载

## 为什么
用户需要在阅读 super-productivity 插件相关源码时，快速判断一个行为属于插件发现、运行时加载、插件 API、桌面主进程能力，还是 issue provider 扩展链路。掌握这个边界后，后续才能安全地分析插件加载失败、插件权限、OAuth、Node 执行和外部工作项适配问题。

## 成功的样子
- 能从 `StartupService._initPlugins()` 追到 `PluginService.initializePlugins()`，并说明它不同于 Angular provider token 接线。
- 能区分插件作者可见的 `PluginAPI`、renderer 内的 `PluginBridgeService`、Electron 主进程的 OAuth/Node 能力。
- 能判断一个 issue provider 插件应先读 registry、adapter、sync adapter，还是普通 issue feature effects。

## 约束条件
- 本主题是 L1 模块总览，只建立入口地图和职责边界，不展开每个插件或每个安全分支的完整实现。
- 课程保持 15 分钟短课；长清单、入口表和判断表放入参考页。
- 文档输出使用简体中文，并只写入本主题目录。

## 不在范围内
- 不讲完整 Angular 壳层、Electron 宿主、同步系统、任务领域和 issue provider 内置实现细节。
- 不审计第三方社区插件的安全性。
- 不生成 L2 深挖课程；只记录后续 L2 线索。

# 使命：应用启动与数据初始化全链路

## 为什么
学习者需要能在 super-productivity 冷启动、首屏空白、数据未出现、同步等待或插件未加载时，沿着真实源码从 `src/main.ts` 追到数据落地和延迟初始化入口。掌握这条链路后，排查启动问题时不会把 Angular provider 注册、NgRx hydration、初始同步、迁移提示和插件运行时混为一谈。

## 成功的样子
- 能按顺序说出 `src/main.ts`、`src/app/app.component.ts`、`src/app/core/startup/startup.service.ts`、`src/app/core/data-init/data-init.service.ts` 和同步触发器的职责。
- 能判断一个启动异常应先查 APP_INITIALIZER、DataInit、op-log hydration、SyncWrapper、迁移服务还是 PluginService。
- 能解释为什么插件初始化要等待初始数据加载和当前同步结束。
- 能从“应用停在启动态”“插件没运行”“SuperSync 加密迁移提示异常”等症状选择正确入口。

## 约束条件
- 本主题是 L2 垂直切片，只讲应用启动到数据初始化落地的主路径和关键边界。
- 短课控制在 15-20 分钟内；长入口清单、时序表和故障排查放入 reference。
- 只写入 `teach/open-productivity/super-productivity/slice-app-startup-flow/`。

## 不在范围内
- 不逐行展开完整 op-log 冲突解决、vector clock 算法或 provider 协议。
- 不讲 Angular、NgRx、RxJS 的通用入门知识。
- 不修改源项目代码、其他教学主题、进度文件或项目索引。

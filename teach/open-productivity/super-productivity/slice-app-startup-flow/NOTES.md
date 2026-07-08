# 教学笔记：应用启动与数据初始化全链路

- 本主题来自 teach-goal L2 worker 任务单；只覆盖 `slice-app-startup-flow` 目录。
- 课程中源码引用尽量使用完整相对路径，例如 `src/app/core/startup/startup.service.ts`，减少 SNAPSHOT 中裸符号污染。
- 重点教学判断：`src/main.ts` 的 `PLUGIN_INITIALIZER_PROVIDER` 是 provider token 接线，不是当前实际插件初始化执行链；实际路径在 `src/app/core/startup/startup.service.ts` 的延迟 `_initPlugins()`。
- 后续适合拆 L3/L4：op-log hydration、初始同步触发器、插件发现/加载、SuperSync 加密迁移 banner。

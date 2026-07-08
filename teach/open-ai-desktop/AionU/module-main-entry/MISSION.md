# 使命：Electron 主入口与生命周期

## 为什么
这节主题要帮学习者建立 AionU 桌面壳的第一层读码抓手：当应用启动、切到 WebUI、执行重置密码、或准备退出时，究竟是哪一段主入口代码在编排这些分支。掌握这一层后，后续看窗口、托盘、deep link、backend 恢复和 WebHost 复用时，不会把入口调度和具体实现混在一起。

## 成功的样子
- 能从 `packages/desktop/src/index.ts` 说清楚桌面模式、WebUI 模式、`--resetpass` 和 `--version` 的分流顺序
- 能解释为什么 `initializeProcess()` 必须先于 backend 启动，以及 `startBackendOrExit()` 在入口里扮演什么角色
- 能指出退出阶段由 `installQuitCleanup()` 托底，知道 backend、托盘和 pet 窗口在哪里被收尾

## 约束条件
- 本轮只做 L1 模块总览，不展开 renderer、preload、数据库修复或 WebHost 内部实现
- 短课必须控制在 15 分钟内完成，正文聚焦一个目标，长表格和候选路线放到 `reference/`
- 工作区可能有其他改动，只允许修改 `teach/open-ai-desktop/AionU/module-main-entry/` 及与本主题直接相关的项目教学索引/台账

## 不在范围内
- 不讲 renderer 首屏 Provider 栈和页面路由
- 不深入 `@aionui/web-host`、`deepLink`、托盘菜单、宠物窗口的内部代码
- 不做 backend 故障分类的逐条异常考古，只在参考文档中给出入口映射

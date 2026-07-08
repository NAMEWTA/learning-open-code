# 使命：Electron 桌面宿主、窗口、IPC 与系统集成

## 为什么
学习者要能在 super-productivity 中判断一个能力到底属于 Electron 主进程、preload bridge、Angular renderer，还是系统级集成。掌握这张边界图后，后续排查桌面启动、窗口安全、托盘、idle、协议、本地文件、插件 Node/OAuth 或本地 REST API 时，不会把 renderer 业务逻辑和主进程权限混在一起。

## 成功的样子
- 能用一句话说明 Electron 宿主在本项目中的职责。
- 能从 `electron/main.ts` 追到窗口创建、IPC 注册和桌面能力初始化入口。
- 能区分主进程模块、`preload.ts` 暴露的 `window.ea`、renderer 的 IPC 调用和系统能力实现。
- 能按参考清单定位 tray、idle、protocol、local file、plugin node executor、plugin OAuth、本地 REST API 的第一源码入口。

## 约束条件
- 本主题是 L1 模块总览，只建立边界、入口和读法，不展开完整启动/关闭 L2 切片。
- 每节 lesson 控制在 15 分钟内；长表格、接口清单和系统能力矩阵放入 reference。
- 只写入 `teach/open-productivity/super-productivity/module-electron-host/`。

## 不在范围内
- 不逐行讲解 app ready、before-quit、before-close IPC 的完整生命周期。
- 不深挖 Angular renderer 装配、op-log 同步算法、插件运行时业务 API。
- 不修改源项目代码、项目级索引、进度文件或其他教学主题目录。

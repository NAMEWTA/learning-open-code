# 使命：Electron 启动、窗口创建与关闭前同步全链路

## 为什么
读者需要能维护 Super Productivity 的桌面端启动和退出体验：定位启动黑屏、IPC 失效、关闭前同步卡住、finish-day 弹窗不释放等问题时，知道该从 Electron main process 追到哪里，再从 Angular renderer 接回哪里。

## 成功的样子
- 能从 `electron/main.ts` 追到 `startApp()`、`createWindow()`、IPC 注册与窗口事件绑定。
- 能判断一个行为属于 Electron main process、本地能力 IPC、preload bridge，还是 Angular renderer。
- 能解释关闭前同步保护如何等待多个 renderer 注册项，并判断用户选择 finish-day、quit、cancel 时窗口是否应真正关闭。

## 约束条件
- 本主题是 L2 垂直切片，只覆盖“启动到关闭保护”的主链路与关键边界。
- lesson 必须是 15 分钟内可完成的短课；长表格和排障内容放入 reference。
- SNAPSHOT 中的源码路径使用源项目内相对路径，不带项目父目录前缀。

## 不在范围内
- 不展开 Angular 全量 bootstrap、NgRx store、同步算法、托盘菜单与任务组件的所有实现细节。
- 不把 Electron 启动和 Angular bootstrap 写成一个同步调用栈。

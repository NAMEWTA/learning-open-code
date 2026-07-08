# 使命：计划排程、时间追踪与专注反馈

## 为什么
用户需要在 Super Productivity 源码中快速定位“计划一天、安排时间、开始追踪、处理空闲、完成专注、回顾工时”这组能力的模块边界。掌握这张 L1 地图后，后续阅读 time-tracking 或 focus-mode 的 L2 垂直切片时，不会把 UI 视图、持久状态、平台 idle 线索和统计回顾混在一起。

## 成功的样子
- 能说清 Planner、Schedule、Boards、time-tracking、focus-mode、idle、reminder、metric、history/worklog 各自负责什么。
- 能从路由或 store 注册处找到每个 feature 的第一阅读入口。
- 能判断一个时间相关改动应该落在 task/work-context、planner、timeTracking、metric 还是 Electron idle 边界。

## 约束条件
- 本主题是 L1 模块总览，单节 lesson 控制在 15 分钟内。
- 目标读者具备 TypeScript、Angular、NgRx 基础。
- 只生成 `teach/open-productivity/super-productivity/module-planning-time/` 下的教学产物。

## 不在范围内
- 不展开 time-tracking 的完整持久化和同步垂直切片。
- 不深入讲 FocusMode timer reducer 的每个状态转移。
- 不讲 Electron Wayland idle 检测的完整平台兼容实现。

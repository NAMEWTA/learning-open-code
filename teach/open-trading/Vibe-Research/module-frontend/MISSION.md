# 使命：Vibe-Research 前端 React 模块总览

## 为什么
Vibe-Research 前端采用 Vite + React 19 + TypeScript + Tailwind CSS 构建，运行在 :5899 端口。理解前端模块的整体架构、页面划分、状态管理和数据流通模式，是后续深入各页面垂直切片的必要前提。

## 成功的样子
- 能够画出前端文件的组件树，说出每个目录和关键文件的职责
- 能够对照路由表说出 10 个页面各自的功能和对应源码文件
- 能够解释前端如何通过 API 客户端与后端通信、如何通过 Zustand 管理全局状态、如何通过 localStorage 持久化用户数据

## 约束条件
- 本课程为 L1 模块级总览，不深入单个页面的 UI 细节（留给 L2 垂直切片）
- 课程时长控制在一节短课内（15 分钟），超出内容分流到参考文档

## 不在范围内
- 后端 API 实现细节（见 module-backend）
- 数据工具箱内部实现（见 module-a-stock-data、module-global-stock-data）
- 单页面的完整交互流程（留给 L2 切片）

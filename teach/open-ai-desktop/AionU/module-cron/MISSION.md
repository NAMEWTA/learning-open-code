# 使命：Cron 定时任务模块

## 为什么
让学习者能在 AionU 源码中快速定位定时任务模块的边界：用户从列表页、会话页或 AI 对话创建任务后，前端如何读取任务、展示状态、调用后端 `/api/cron/*`，并与会话历史保持关联。

## 成功的样子
- 能说清 Cron 模块在 renderer、common adapter、conversation runtime 之间的位置。
- 能按“页面入口 → hook 状态层 → adapter API → 会话关联”的顺序追踪一次任务创建或立即执行。
- 能从 reference 查到 Cron 相关路由、hook、工具函数、HTTP/WS 接口和测试证据。

## 约束条件
- 本轮是 L1 模块总览，只覆盖职责、接口、分层、依赖和调用示例。
- lesson 必须保持 15 分钟短课；完整清单放入 reference。

## 不在范围内
- 不展开 aioncore 后端调度器内部实现。
- 不逐行讲解 `CreateTaskDialog` 和 `TaskDetailPage` 的所有 UI 分支。

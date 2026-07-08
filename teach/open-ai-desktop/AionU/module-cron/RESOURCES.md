# Cron 定时任务模块资源

## 知识

- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/cron/`
  Cron renderer 模块源码。适用于确认列表页、详情页、创建弹窗、状态组件、hook 与工具函数的真实边界。
- `open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts`
  Cron 前端调用面与 `/api/cron/*` 映射。适用于核对 CRUD、runNow、skill、WebSocket 事件和会话关联接口。
- `open-ai-desktop/AionU/tests/unit/cron/`
  Cron 单元测试。适用于验证时区修复、状态标签、hook 订阅、未读状态和关联会话刷新行为。
- `open-ai-desktop/AionU/tests/e2e/specs/cron-crud.e2e.ts`
  端到端测试。适用于理解 AI 对话创建任务、修改任务、删除任务后保留会话历史的产品预期。
- `open-ai-desktop/AionU/docs/prds/cron/cron-entry-optimization.md`
  Cron 入口优化 PRD。适用于理解空态图标收敛和“对话创建 / 手动创建”双路径入口的设计动机。
- [AionUi GitHub 仓库](https://github.com/iOfficeAI/AionUi)
  上游项目入口。适用于追踪 Cron 模块后续变更、issue 与 release 背景。

## 智慧（社区）

- [AionUi GitHub Issues](https://github.com/iOfficeAI/AionUi/issues)
  适用于检索真实用户对定时任务创建、执行、通知、会话历史和跨平台行为的反馈。

## 空白

- 本轮未找到独立的 Cron 后端调度器设计文档；后续 L2/L3 若要讲执行器内部，需要继续追踪 aioncore `/api/cron/*` 实现。

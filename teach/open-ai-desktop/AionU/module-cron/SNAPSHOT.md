# 课程快照：module-cron

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T17:54:54+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `open-ai-desktop/AionU/docs/prds/cron/cron-entry-optimization.md` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/index.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/cron/useCronJobs.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/cron-crud.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/unit/cron/CronStatusTag.dom.test.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/unit/cron/cronUtils.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/unit/cron/repairCronJobTimeZone.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/unit/cron/useCronJobs.dom.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/components/layout/Router.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/components/layout/Sider/SiderNav/SiderScheduledEntry.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/main.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/Messages/components/MessageCronTrigger.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/CreateTaskDialog.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/TaskDetailPage.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/cron/components/CronJobManager.tsx` | 课程分析引用 | 🟡 辅助 |

## 引用概念与协议

| 概念 / 协议 | 用途 |
|------------|------|
| `/api/cron/*` | Cron backend API 总族 |
| `/api/cron/jobs` | 任务列表、创建与基础 CRUD |
| `/api/cron/jobs/:cron_job_id/conversations` | 查询任务关联会话 |
| `/api/cron/jobs/:job_id` | 单任务详情、更新与删除 |
| `/api/cron/jobs/:job_id/run` | 手动触发任务 |
| `/api/cron/jobs/:job_id/skill` | 任务关联 Skill |
| `/api/cron/jobs?conversation_id=...` | 按会话过滤任务 |
| `POST /api/cron/jobs/:id/run` | lesson 中用于讲手动执行的调用示例 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-cron-module-tour | `lessons/0001-cron-module-tour.html` | Cron 定时任务模块导览短课 |

## 参考资料

- `reference/cron-overview.html` — AionU Cron 定时任务模块参考总览

## 快照摘要
- 课程数：1
- 引用源文件数：16
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0

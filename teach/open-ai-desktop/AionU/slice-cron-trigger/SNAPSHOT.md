# 课程快照：Cron 任务创建与触发全链路

## 源项目信息

- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T19:27:07+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/index.tsx` | `/scheduled` 列表页、创建入口、启停入口、keep-awake 设置 | 核心 |
| `packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/CreateTaskDialog.tsx` | 表单到 `addJob` / `updateJob` 负载的创建与编辑主路径 | 核心 |
| `packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/TaskDetailPage.tsx` | 详情页读取、启停、run-now、防重入、删除与执行后导航 | 核心 |
| `packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/CronStatusTag.tsx` | active、paused、error 状态显示边界 | 辅助 |
| `packages/desktop/src/renderer/pages/cron/ScheduledTasksPage/resolveCronAgentConfig.ts` | assistant、provider、model、workspace 到 `agent_config` 的转换 | 辅助 |
| `packages/desktop/src/renderer/pages/cron/useCronJobs.ts` | 列表、单会话、会话状态 map、未读执行、关联会话刷新 hook | 核心 |
| `packages/desktop/src/renderer/pages/cron/cronUtils.ts` | schedule 构造、timezone、执行会话标题与状态判断 | 核心 |
| `packages/desktop/src/renderer/pages/cron/repairCronJobTimeZone.ts` | 旧任务缺失 timezone 的修复边界 | 辅助 |
| `packages/desktop/src/renderer/pages/conversation/platforms/aionrs/localCronCommands.ts` | AI 对话侧 Cron 响应清理与本地处理边界 | 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/aionrs/useAionrsMessage.ts` | 完成消息后调用 `processLocalCronResponse` 并合并展示内容 | 辅助 |
| `packages/desktop/src/common/adapter/ipcBridge.ts` | `ipcBridge.cron` HTTP/WS contract、cron 类型与 artifact 类型 | 核心 |
| `tests/e2e/specs/cron-crud.e2e.ts` | AI 对话创建、修改、删除、列表/详情可见与会话保留证据 | 证据 |
| `tests/unit/cron/useCronJobs.dom.test.ts` | hook 获取、启停、事件订阅、未读、关联会话刷新证据 | 证据 |
| `tests/unit/cron/cronUtils.test.ts` | timezone、schedule 构造和执行会话标题格式证据 | 证据 |
| `tests/unit/cron/repairCronJobTimeZone.test.ts` | 缺失 timezone 修复与并发去重证据 | 证据 |
| `tests/unit/cron/CronStatusTag.dom.test.tsx` | 状态标签 active、paused、error 优先级证据 | 证据 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | `lessons/0001-flow-map.html` | 从创建入口追踪到 adapter、事件刷新、run-now 和 AI 对话路径 |
| 02 | `lessons/0002-create-edit-path.html` | 拆解 `CreateTaskDialog` 创建与编辑分流、`addJob` / `updateJob` 写入边界 |
| 03 | `lessons/0003-run-now-refresh.html` | 拆解详情页 run-now 防重入、会话 cache 修正、导航和测试缺口 |
| 04 | `lessons/0004-ai-local-cron-and-tests.html` | 拆解 AI 对话入口、`localCronCommands` 展示清理和测试证据边界 |

## 已生成参考文档

| 文件 | 描述 |
|------|------|
| `reference/cron-trigger-flow-map.html` | Cron 任务创建与触发全链路速查图谱，覆盖入口、层级、时序、边界、测试证据和交叉链接 |

## 快照摘要

- 课程数：4
- 参考文档数：1
- 引用源文件数：16
- 学习记录数：0

# 课程快照：Team 创建并运行全链路

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T19:26:14+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/renderer/pages/team/components/TeamCreateModal.tsx` | 创建 Team 表单、leader 选择、payload 组装与错误边界 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/team/components/teamCreateModelResolver.ts` | 创建 leader 时解析默认 model，保证后续发送框可用 | 🟡 辅助 |
| `packages/desktop/src/renderer/pages/team/index.tsx` | `/team/:id` 页面入口与 Team record 装载 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/team/TeamPage.tsx` | Team 工作台总装、slot 布局、workspace、权限 provider 与 run view 接入 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/team/hooks/TeamTabsContext.tsx` | 成员 slot active 状态、排序、删除回退与本地持久化 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/team/components/TeamTabs.tsx` | 成员 tab、状态点、待确认徽标、拖拽和 E2E selector | 🟡 辅助 |
| `packages/desktop/src/renderer/pages/team/hooks/useTeamSession.ts` | Team agent/session/list 事件订阅与 Team record 刷新 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/team/components/TeamChatView.tsx` | leader/member 发送分流、run ack 应用、conversation runtime 注入 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/team/components/teamSendRuntime.ts` | slot 级发送 gate、stop handler 与 stale run reconcile | 🔴 核心 |
| `packages/desktop/src/renderer/pages/team/hooks/useTeamRunView.ts` | Team run ack、run event、child turn event 与 reconnect reconcile | 🔴 核心 |
| `packages/desktop/src/renderer/pages/team/hooks/TeamPermissionContext.tsx` | Team session 预热与权限模式写回 | 🟡 辅助 |
| `packages/desktop/src/common/types/team/teamTypes.ts` | Team record、assistant slot、run ack、run event 和 WebSocket 事件共享类型 | 🔴 核心 |
| `tests/e2e/cases/teams/team-create.e2e.ts` | 创建 Team UI 主线和无 assistant 边界证据 | 🔴 核心 |
| `tests/e2e/cases/teams/team-agent-lifecycle.e2e.ts` | assistant-first 创建、添加成员、成员 tab 与 `assistant_id` 保留证据 | 🔴 核心 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | `lessons/0001-flow-map.html` | Team 创建并运行全链路短课 |

## 已生成参考文档

| 编号 | 参考文件 | 描述 |
|------|---------|------|
| 01 | `reference/team-run-flow-map.html` | Team 创建、成员 slot、发送、事件回流与 E2E 证据图谱 |

## 快照摘要
- 课程数：1
- 引用源文件数：14
- 学习记录数：0

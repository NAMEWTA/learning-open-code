# Team 创建并运行全链路资源

## 知识

- `packages/desktop/src/renderer/pages/team/components/TeamCreateModal.tsx`
  创建 Team 的真实 UI 入口，覆盖名称校验、leader assistant 选择、默认 model 解析、`ipcBridge.team.create` 调用与错误展示。
- `packages/desktop/src/renderer/pages/team/index.tsx` 与 `packages/desktop/src/renderer/pages/team/TeamPage.tsx`
  Team 页面装载与工作台总装，适用于追踪 `/team/:id`、Team record、slot 布局、workspace、权限 provider 与 run view。
- `packages/desktop/src/renderer/pages/team/hooks/TeamTabsContext.tsx` 与 `packages/desktop/src/renderer/pages/team/components/TeamTabs.tsx`
  成员 slot 的 active 状态、排序、重命名、删除、状态点和 E2E selector 的主要来源。
- `packages/desktop/src/renderer/pages/team/components/TeamChatView.tsx`、`packages/desktop/src/renderer/pages/team/components/teamSendRuntime.ts` 与 `packages/desktop/src/renderer/pages/team/hooks/useTeamRunView.ts`
  Team run 与发送动作的核心链路：leader/member 分流、ack 即时入视图、slot gate、stop、WebSocket 事件回流与 reconcile。
- `packages/desktop/src/common/types/team/teamTypes.ts`
  Team record、assistant slot、run ack、run event、child turn 与 session/list 事件的共享契约。
- `tests/e2e/cases/teams/team-create.e2e.ts`
  产品层验证侧栏创建按钮、创建 modal、表单填写、创建后导航和侧栏刷新。
- `tests/e2e/cases/teams/team-agent-lifecycle.e2e.ts`
  契约层验证 assistant-first Team 创建、添加 teammate、成员 tab 出现和 `assistant_id` 保留。
- `teach/open-ai-desktop/AionU/module-team-mode/reference/team-mode-overview.html`
  L1 Team Mode 模块总览，适合回查接口清单、WebSocket 事件和模块职责。
- `teach/open-ai-desktop/AionU/module-common-adapter/reference/common-adapter-overview.html`
  L1 common adapter 总览，适合回查 `ipcBridge.team` 如何承接 HTTP 与 WebSocket。
- `teach/open-ai-desktop/AionU/module-conversation-runtime/reference/conversation-runtime-overview.html`
  L1 conversation runtime 总览，适合理解 TeamChatView 为什么复用 ACP / aionrs Chat。

## 智慧（社区）

- [AionUi GitHub 仓库](https://github.com/iOfficeAI/AionUi)
  当前子模块上游。适用于查找 Team Mode 相关 issue、PR 讨论和变更背景。

## 空白

- 本轮未检索到本地仓库内独立的 Team run 架构决策记录；因此参考文档以源码、L1 课程和 E2E 作为可信来源。

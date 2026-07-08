# Team Mode 事件模型资源

## 知识

- `teach/open-ai-desktop/AionU/module-team-mode/reference/team-mode-overview.html`
  L1 Team Mode 总览，适合先确认页面入口、接口清单和事件名，不重复阅读创建流程。
- `teach/open-ai-desktop/AionU/slice-team-run/reference/team-run-flow-map.html`
  L2 Team run 主链路图谱，适合回顾创建、发送、ack 和事件回流在整条链路中的位置。
- `open-ai-desktop/AionU/packages/desktop/src/common/types/team/teamTypes.ts`
  Team run、child turn、slot work 和事件 payload 的共享类型契约，是本主题的语义底座。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/team/hooks/useTeamRunView.ts`
  ack、WebSocket run event、child turn event、reconnect 和结构事件 reconcile 的核心状态合成点。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/team/components/TeamChatView.tsx`
  leader/member 发送分流与 `onTeamRunAck` 注入点，用于理解 REST ack 如何进入 run view。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/team/components/teamSendRuntime.ts`
  slot 级发送 gate 与 stop handler，适合排查“哪个输入框应该被锁住”。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/team/hooks/TeamTabsContext.tsx`
  active slot、switchTab 和本地 tab 状态证据；它不参与 run reducer，可用于区分 tab 状态与 run 状态。
- `open-ai-desktop/AionU/tests/unit/renderer/useTeamRunView.dom.test.tsx`
  覆盖 reconcile、结构事件过滤、终态清理和失败保留本地状态，是事件 reducer 的主要测试证据。
- `open-ai-desktop/AionU/tests/unit/renderer/teamSendRuntime.test.ts`
  覆盖 slot gate、防串扰、暂停优先发送和 stale pause reconcile。
- `open-ai-desktop/AionU/tests/e2e/cases/teams/`
  Team 创建、成员生命周期和 UI 发送证据；阅读时要注意它不等于 send/run event 全链路断言。
- `open-ai-desktop/AionU/tests/e2e/cases/teams/team-tab-context.e2e.ts`
  通过 bridge 获取 run ack 并验证 tab 切换后的 leader conversation 历史，适合作为 ack 可用性的辅助证据。

## 智慧（社区）

- 本轮未引入外部社区。此主题依赖本地源码状态和现有测试语义，最合适的现实反馈渠道是 AionU 仓库内的代码评审、测试失败复盘和后续补测 PR。

## 空白

- 尚未生成 Team Mode 的 L3 API 参考，HTTP/WS 契约仍需从 L1 参考和 `ipcBridge.ts` 交叉查阅。
- E2E 目录存在 leader/member UI 发送案例，但未直接断言 `ITeamRunAck`、`team.run*`、`team.childTurn*` 的合并顺序与 slot gate 结果。

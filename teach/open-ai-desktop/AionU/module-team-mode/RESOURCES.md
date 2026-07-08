# Team Mode 模块总览资源

## 知识

- [L0：AionU 项目总览参考](../00-overview/reference/00-overview.html)
  用于定位 Team Mode 在 Electron renderer、common adapter、aioncore REST/WS 架构中的位置。
- [Common adapter 与 API 映射参考](../module-common-adapter/reference/common-adapter-overview.html)
  用于理解 `ipcBridge.team` 为什么以统一调用面包装 HTTP 与 WebSocket。
- [Renderer 核心与 UI Shell 参考](../module-renderer-core/reference/renderer-core-overview.html)
  用于理解 `/team/:id` 路由、侧栏入口、全局 shell 与 workspace 可用性。
- [Conversation Runtime 与 Agent UI 参考](../module-conversation-runtime/reference/conversation-runtime-overview.html)
  用于理解 Team Mode 复用 ACP / aionrs Chat 与 sendbox 的方式。
- [`open-ai-desktop/AionU/packages/desktop/src/renderer/pages/team/`](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/team/)
  Team Mode renderer 主实现，包含页面装配、tab 状态、权限模式、发送运行时、创建 modal 与 workspace 视图。
- [`open-ai-desktop/AionU/packages/desktop/src/common/types/team/teamTypes.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/types/team/teamTypes.ts)
  Team 前端共享类型和 WebSocket 事件契约，是接口清单的类型来源。
- [`open-ai-desktop/AionU/packages/desktop/src/common/adapter/teamMapper.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/adapter/teamMapper.ts)
  后端 Team payload 到前端模型的字段、角色和状态归一化入口。
- [`open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts`](../../../../open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts)
  `team` 域 HTTP 路由、WebSocket 事件和 `realtime.reconnected` 事件的统一导出位置。
- [`open-ai-desktop/AionU/tests/e2e/cases/teams/`](../../../../open-ai-desktop/AionU/tests/e2e/cases/teams/)
  Team 创建、发送、成员生命周期、权限模式、workspace、tab 持久化、删除等行为证据。
- [`open-ai-desktop/AionU/tests/unit/common-adapter/teamMapper.test.ts`](../../../../open-ai-desktop/AionU/tests/unit/common-adapter/teamMapper.test.ts)
  验证 `lead` / `leader`、状态归一化、assistant-first 字段与 `assistant_id` 必填约束。

## 智慧（社区）

- 当前未引入外部社区资源。本轮任务是源码课程生成，主要可信依据来自本地源码、已有课程、单元测试和 E2E 测试；后续若需要产品设计背景，应再核验 AionU 上游 issue、discussion 或 PR 记录。

## 空白

- `open-ai-desktop/AionU/docs/prds/teams/README.md` 当前为空文件，不能作为产品需求依据。
- 本仓库未包含 aioncore backend 的 Team 调度实现，因此本 L1 只覆盖 AionU TypeScript 侧的页面、类型、adapter 和测试可见行为。

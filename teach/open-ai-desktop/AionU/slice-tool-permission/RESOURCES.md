# 工具调用确认全链路资源

## 知识

- [AionU L0 项目总览](../00-overview/reference/00-overview.html)
  用于确认 AionU 的 Electron renderer、preload、common adapter、aioncore REST / WebSocket 的总体边界。
- [Conversation Runtime 与 Agent UI 参考](../module-conversation-runtime/reference/conversation-runtime-overview.html)
  用于定位 `MessageList`、ACP 平台组件和会话运行时状态在 renderer 中的位置。
- [Preload 与 IPC 参考总览](../module-preload-ipc/reference/preload-ipc-overview.html)
  用于确认 `preload/main.ts` 只暴露受控桥接面，不承载权限业务逻辑。
- [Common Adapter 与 API 映射参考](../module-common-adapter/reference/common-adapter-overview.html)
  用于确认 `conversation.confirmMessage`、`conversation.confirmation.*` 属于 common adapter 的 conversation 域。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/Messages/`
  本切片的主要 UI 与状态阅读入口，覆盖权限卡、工具结果卡、消息合并和 pending confirmation 恢复。
- `open-ai-desktop/AionU/packages/desktop/src/common/chat/approval/ApprovalStore.ts`
  会话级 approval memory 抽象，解释 always allow 与普通一次性确认的边界。
- `open-ai-desktop/AionU/tests/e2e/features/conversations/acp/`
  ACP conversation 的 E2E 证据目录，包含权限卡等待、忙态冲突、发送失败和空回复提示等用户可见行为。

## 智慧（社区）

- 本主题以本地源码、关联 L1/L0 教学和项目测试为准；未引入外部社区判断。

## 空白

- 本轮没有读取 aioncore 后端源码，因此“确认结果如何在后端落到具体工具执行 / 持久化 approval memory”只按前端 contract 与 common approval store 抽象说明，不能当作后端实现细节结论。

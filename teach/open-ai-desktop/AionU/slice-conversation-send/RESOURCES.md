# 发送会话消息全链路资源

## 知识

- [L0：AionU 项目总览](../00-overview/reference/00-overview.html)
  用于确认 AionU 的整体边界：renderer 通过 common adapter 访问 aioncore REST/WS，业务能力不直接由 Electron IPC 承载。
- [L1：Conversation Runtime 与 Agent UI](../module-conversation-runtime/reference/conversation-runtime-overview.html)
  用于回看 `/conversation/:id`、`ChatConversation`、平台 sendbox、runtime gate 与 MessageList 的模块职责。
- [L1：Common Adapter 与 API 映射](../module-common-adapter/reference/common-adapter-overview.html)
  用于确认 `ipcBridge.conversation.sendMessage`、`responseStream`、`turnCompleted` 在 AionU 中实际对应 HTTP + WebSocket。
- [L1：Renderer 核心与 UI Shell](../module-renderer-core/reference/renderer-core-overview.html)
  用于确认 renderer 路由、provider 与页面壳层如何把用户带到 conversation 页面。
- 源码：`open-ai-desktop/AionU/packages/desktop/src/renderer/components/chat/SendBox/index.tsx`
  公共输入框，负责 Enter/按钮提交、空输入拦截、附件/引用拼接、立即清空草稿、调用 `onSend`。
- 源码：`open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/platforms/aionrs/AionrsSendBox.tsx`
  本主题主路径：AionRS 平台发送框，负责模型检查、忙时排队、`markSendStarted`、`ipcBridge.conversation.sendMessage.invoke`。
- 源码：`open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts`
  统一调用面，定义 `conversation.sendMessage` 到 `POST /api/conversations/:id/messages`，以及 `responseStream`、`turnCompleted` WS emitter。
- 源码：`open-ai-desktop/AionU/packages/desktop/src/common/adapter/httpBridge.ts`
  HTTP 请求、`BackendHttpError` 抛出、WebSocket 连接、事件分发与重连策略。
- E2E：`open-ai-desktop/AionU/tests/e2e/features/conversations/aionrs/basic-flow.e2e.ts`
  证明 AionRS 最小路径至少产生用户消息和 AI 文本回复。
- E2E：`open-ai-desktop/AionU/tests/e2e/features/conversations/acp/send-error-surfacing.e2e.ts`
  证明 ACP 发送失败时，UI 会显示后端原始错误，而不是吞掉细节。

## 智慧（社区）

- 本地验证：`.agents/skills/teach/scripts/audit_topic.py`
  作为教学产物质量闸门，验证主题不是 reference-only，短课不过长，并且元文件没有占位符。
- 项目 E2E 套件：`open-ai-desktop/AionU/tests/e2e/features/conversations/`
  作为现实行为证据。遇到源码理解冲突时，优先回到这些测试确认用户可见行为。

## 空白

- 本主题未读取 aioncore 后端源码，因此 `/api/conversations/:id/messages` 内部如何落库、调用 Agent、广播 WS 事件，只能依据 AionU adapter 合同和 E2E 行为推断。

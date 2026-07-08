# 课程快照：发送会话消息全链路

## 源项目信息

- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T19:01:15+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/renderer/pages/conversation/index.tsx` | `/conversation/:id` 页面入口与会话加载 | 🟡 辅助 |
| `packages/desktop/src/renderer/pages/conversation/components/ChatConversation.tsx` | 按 `conversation.type` 分流 AionRS / ACP 平台组件 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/aionrs/AionrsChat.tsx` | AionRS 消息列表、上下文与发送框装配 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/aionrs/AionrsSendBox.tsx` | AionRS 主发送路径、模型检查、队列、runtime 标记、adapter 调用 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/aionrs/useAionrsMessage.ts` | AionRS 流式消息消费、loading 状态、错误终止 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/acp/AcpChat.tsx` | ACP 消息状态 hook 与发送框装配 | 🟡 辅助 |
| `packages/desktop/src/renderer/pages/conversation/platforms/acp/AcpSendBox.tsx` | ACP 发送路径、错误 tips、认证错误与 structured error | 🔴 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/acp/useAcpMessage.ts` | ACP 流式消息消费、request trace、error 终止 | 🟡 辅助 |
| `packages/desktop/src/renderer/pages/conversation/platforms/acp/useAcpInitialMessage.ts` | guid 初始消息发送与失败提示 | 🟡 辅助 |
| `packages/desktop/src/renderer/pages/conversation/platforms/acp/buildSendFailureError.ts` | ACP 发送失败分类与用户可见错误结构 | 🟡 辅助 |
| `packages/desktop/src/renderer/pages/conversation/platforms/useConversationCommandQueue.ts` | 忙时排队、队列限制、drain 与失败恢复 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/conversation/runtime/useConversationRuntimeView.ts` | runtime hydration、turnCompleted 监听、本地发送/停止标记接口 | 🔴 核心 |
| `packages/desktop/src/renderer/pages/conversation/runtime/conversationRuntimeViewStore.ts` | runtime gate 状态机：pending、accepted、failed、completed | 🔴 核心 |
| `packages/desktop/src/renderer/components/chat/SendBox/index.tsx` | 公共输入框提交、空输入拦截、草稿清空、`onSend` 调用 | 🔴 核心 |
| `packages/desktop/src/common/adapter/ipcBridge.ts` | `conversation.sendMessage`、`responseStream`、`turnCompleted` 的统一 adapter 面 | 🔴 核心 |
| `packages/desktop/src/common/adapter/httpBridge.ts` | HTTP POST、`BackendHttpError`、WebSocket 事件分发与重连 | 🔴 核心 |
| `tests/e2e/features/conversations/aionrs/basic-flow.e2e.ts` | AionRS 成功收发、用户消息与 AI 回复落库证据 | 🟡 辅助 |
| `tests/e2e/features/conversations/aionrs/edge-cases.e2e.ts` | AionRS 大文件、删除目录等边界行为证据 | 🟡 辅助 |
| `tests/e2e/features/conversations/acp/send-error-surfacing.e2e.ts` | ACP HTTP 失败时展示后端原始错误的 E2E 证据 | 🔴 核心 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | `lessons/0001-flow-map.html` | AionRS 发送消息主路径与 ACP 失败边界短课 |
| 02 | `lessons/0002-aionrs-main-path.html` | AionRS 主路径拆解短课 |
| 03 | `lessons/0003-acp-error-path.html` | ACP 发送失败边界短课 |

## 已生成参考资料

| 编号 | 参考文件 | 描述 |
|------|---------|------|
| 01 | `reference/conversation-send-flow-map.html` | 入口、层次、时序、异常矩阵、调试索引与交叉链接 |

## 快照摘要

- 课程数：3
- 参考资料数：1
- 引用源文件数：19
- 学习记录数：1

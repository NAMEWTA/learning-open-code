# 课程快照：工具调用确认全链路

## 源项目信息

- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T18:54:48+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/common/chat/approval/ApprovalStore.ts` | approval memory 抽象、always allow cache 语义 | 核心 |
| `packages/desktop/src/common/chat/approval/index.ts` | approval store 对外导出面 | 辅助 |
| `packages/desktop/src/common/adapter/ipcBridge.ts` | confirm endpoint、confirmation list/remove、approval.check contract | 核心 |
| `packages/desktop/src/common/chat/chatLib.ts` | `permission` / `acp_permission` / `acp_tool_call` 消息类型与转换 | 核心 |
| `packages/desktop/src/preload/main.ts` | renderer 与宿主之间的 contextBridge 安全边界 | 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/acp/AcpChat.tsx` | ACP 会话页面挂载 pending confirmation recovery | 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/acp/useAcpMessage.ts` | ACP stream 中 `acp_permission` 的入口处理 | 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/aionrs/AionrsChat.tsx` | aionrs 会话页面挂载 pending confirmation recovery | 核心 |
| `packages/desktop/src/renderer/pages/conversation/platforms/aionrs/useAionrsMessage.ts` | aionrs 将 confirmation-shaped `acp_permission` 改标为 `permission` | 核心 |
| `packages/desktop/src/renderer/pages/conversation/Messages/hooks.ts` | 消息合并、`permission` 按 `call_id` 去重、工具消息边界 | 核心 |
| `packages/desktop/src/renderer/pages/conversation/Messages/MessageList.tsx` | 消息类型分派与 tool summary 预处理 | 核心 |
| `packages/desktop/src/renderer/pages/conversation/Messages/usePendingConfirmationsRecovery.ts` | 缺失 pending confirmation 恢复、去重和移除 | 核心 |
| `packages/desktop/src/renderer/pages/conversation/Messages/components/MessagePermission.tsx` | 通用 permission 卡、`always_allow` 提交 | 核心 |
| `packages/desktop/src/renderer/pages/conversation/Messages/acp/MessageAcpPermission.tsx` | ACP 专用 permission 卡、`confirm_key` 提交 | 核心 |
| `packages/desktop/src/renderer/pages/conversation/Messages/acp/MessageAcpToolCall.tsx` | ACP tool call 状态 / 结果展示，和确认 UI 区分 | 核心 |
| `packages/desktop/src/renderer/pages/conversation/Messages/components/MessageToolGroup.tsx` | 普通工具组确认细节、`Cancel` outcome 与结果展示 | 核心 |
| `packages/desktop/src/renderer/utils/common.ts` | `ToolConfirmationOutcome` 枚举，包括一次允许、总是允许、取消 | 辅助 |
| `tests/e2e/features/conversations/acp/cron-busy.e2e.ts` | 权限卡出现后会话 busy、Cron 冲突和重试的 E2E 证据 | 证据 |
| `tests/e2e/features/conversations/acp/send-error-surfacing.e2e.ts` | ACP 发送失败错误真实展示的 E2E 边界证据 | 证据 |
| `tests/e2e/features/conversations/acp/empty-turn-warning.e2e.ts` | ACP 空回复提示不误造权限卡的 E2E 证据 | 证据 |
| `tests/unit/renderer/pendingConfirmationsRecovery.test.ts` | pending confirmation 构造、去重、移除的单元证据 | 证据 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | `lessons/0001-flow-map.html` | 从需要确认的消息入口追踪到 UI、adapter、安全边界和恢复路径 |

## 已生成参考文档

| 文件 | 描述 |
|------|------|
| `reference/tool-permission-flow-map.html` | 工具调用确认全链路速查图谱，覆盖入口、层级、时序、边界、E2E 证据和交叉链接 |

## 快照摘要

- 课程数：1
- 参考文档数：1
- 引用源文件数：21
- 学习记录数：0

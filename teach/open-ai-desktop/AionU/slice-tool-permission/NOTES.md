# 工具调用确认全链路笔记

- 主题身份：AionU teach-goal 的 L2 垂直切片，目标是“工具调用确认全链路”。
- 关联上游：L0 `00-overview`，L1 `module-conversation-runtime`、`module-preload-ipc`、`module-common-adapter`。
- 阅读结论：renderer 中至少存在三类相邻 UI：`MessageAcpPermission` / `MessagePermission` 是确认卡，`MessageAcpToolCall` 是 ACP 工具状态与结果展示，`MessageToolGroup` 是普通工具组展示且可内嵌 confirmation details。
- 安全边界：`preload/main.ts` 不暴露任意 Node 能力；确认业务从 renderer 走 common adapter 的 HTTP / WS contract，UI 不直接写 `BaseApprovalStore`。
- 边界路径：`usePendingConfirmationsRecovery` 在 ACP 和 aionrs Chat 挂载时列出 pending confirmations，缺失时构造 `permission` 消息并按 `call_id` 去重，收到 remove 事件后移除。

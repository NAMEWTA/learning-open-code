# 使命：工具调用确认全链路

## 为什么

用户需要能审查 AionU 在 ACP / tool call 需要授权时是否真正停在用户确认边界上，并能追踪确认、拒绝或缺失 pending confirmation 后状态如何继续传播。掌握这条链路后，维护者可以定位“工具越权执行”“权限卡不出现”“确认后仍卡住”等高风险问题。

## 成功的样子

- 能从 `acp_permission` / `permission` 消息入口追到 renderer UI、确认提交、adapter 能力和后续状态传播。
- 能区分权限确认 UI / 状态与普通工具调用结果渲染，不把 `acp_tool_call` 误认为确认卡。
- 能说明 `ApprovalStore` 负责会话级 always allow 记忆，而 renderer 不直接写这个 store。
- 能指出至少一个边界路径：页面缺失 pending confirmation 时如何恢复、去重和移除。
- 能用 E2E 测试说明用户可见行为的证据边界。

## 约束条件

- 源项目 `open-ai-desktop/AionU/` 只读。
- 本主题只写入 `teach/open-ai-desktop/AionU/slice-tool-permission/`。
- 不修改项目级 `index.md`、`_progress.json`、`_progress.md`。
- L2 以垂直切片为主，backend / aioncore 内部确认执行不在本轮深挖。

## 不在范围内

- 重写 AionU 权限模型或测试用例。
- 解释所有消息类型、所有工具结果 UI 或全部 conversation runtime。
- 追踪 aioncore 后端对确认结果的最终执行细节。

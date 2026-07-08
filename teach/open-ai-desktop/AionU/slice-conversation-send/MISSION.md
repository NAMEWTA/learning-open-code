# 使命：发送会话消息全链路

## 为什么

本主题帮助学习者把 AionU 中“一条会话消息从输入框发出到流式反馈回到 UI”的路径讲清楚。掌握这条链路后，学习者可以定位发送失败、忙时排队、运行时状态卡住、流事件不渲染等真实问题，而不是只停留在组件名记忆。

## 成功的样子

- 能从 `SendBox` 提交动作追到 AionRS 主路径的 runtime gate、adapter、HTTP 请求与 WS 流。
- 能说清 ACP 与 AionRS 在发送入口、错误反馈和消息流消费上的差异。
- 能用 E2E 文件解释“成功收发”和“后端发送失败如何呈现给用户”两类证据。
- 能指出至少一个边界路径：忙时排队、无模型、HTTP 失败或 runtime completion。

## 约束条件

- 源项目 `open-ai-desktop/AionU/` 只读。
- 本主题只写入 `teach/open-ai-desktop/AionU/slice-conversation-send/`。
- 短课聚焦一条主路径；长表格、分支和异常矩阵放入 `reference/`。
- 不修改项目级 `index.md`、`_progress.json`、`_progress.md`。

## 不在范围内

- 不深入 aioncore 后端内部实现；本主题停在 AionU TypeScript adapter 暴露出的 REST/WS 合同。
- 不完整讲解 Team、Cron、MCP、Preview、Workspace 的所有功能。
- 不覆盖 MessageList 的全部消息类型，只覆盖发送链路必需的 text、tips、error 和流式状态。

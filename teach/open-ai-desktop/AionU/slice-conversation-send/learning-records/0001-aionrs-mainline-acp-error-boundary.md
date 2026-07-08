# AionRS 主线与 ACP 错误边界已确立

本主题把 AionRS 作为短课主路径：`SendBox` 提交后进入 `AionrsSendBox`，再到 runtime gate、`ipcBridge.conversation.sendMessage`、HTTP POST 与 WS 流式事件。ACP 不是另起 endpoint，而是复用 `conversation.sendMessage/responseStream`，其发送失败会转成可见的 tips/error 消息，适合作为本切片的关键边界路径。

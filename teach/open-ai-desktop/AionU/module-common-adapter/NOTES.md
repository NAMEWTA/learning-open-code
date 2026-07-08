# 教学笔记：Common adapter

- 本主题定位为 renderer 调用面的传输适配层，重点解释 `ipcBridge` 如何在同一调用形状下路由到 Electron IPC、HTTP、WebSocket 或本地 stub。
- 课程正文聚焦代表调用链，reference 承接接口域清单、mapper 清单和测试证据。

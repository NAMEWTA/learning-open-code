# NOTES — 教学偏好暂存

> 记录用户在课程中表达的教学偏好，供后续课程设计参考。

- 用户要求「全面详细讲解，结合实际代码」——课程应大量引用真实文件路径、类名、可运行的代码片段，并追踪跨模块的真实调用链，不停留在抽象描述。
- 偏好「鸟瞰图先行」风格（沿用 teach-ruoyi-auth / teach-ruoyi-sms / teach-ruoyi-redis 的全景图 + 分步拆解 + 提取练习的结构）。
- 学习者：全栈背景（Java 后端 + Vue/React 前端）。本模块为纯后端 Java，但每节课会联系前端接入点（SSE → `EventSource`，WebSocket →浏览器原生 `WebSocket`）。
- 本主题（ruoyi-common-push）的目标：读懂双通道消息推送的架构设计与代码实现，并能在业务代码中正确调用 `PushHelper`。
- 语言：简体中文。

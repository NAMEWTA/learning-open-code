# 使命：Team Mode 模块总览

## 为什么
帮助学习者在进入 Team 创建、成员调度、权限模式、workspace 迁移等 L2 切片前，先建立 Team Mode 的模块边界图。学习者应能判断一个 Team 行为属于 renderer 页面状态、common adapter 契约、conversation runtime 复用，还是 backend 会话编排。

## 成功的样子
- 能用一句话说明 Team Mode 在 AionU 整体架构中的职责。
- 能列出 `ipcBridge.team` 的主要 HTTP / WebSocket 接口类别，并知道完整清单在 reference 中。
- 能从 `/team/:id` 路由追踪到 `TeamChatView` 注入 `teamSendMessage` 的调用主线。
- 能指出 Team Mode 与 `module-common-adapter`、`module-renderer-core`、`module-conversation-runtime`、Cron 清理之间的依赖关系。

## 约束条件
- 本轮是 teach-goal 的 L1 模块总览，只写 `teach/open-ai-desktop/AionU/module-team-mode/`。
- lesson 必须是 15 分钟短课；完整接口、测试矩阵和长表格放入 reference。
- 源项目只读，不修复源码或 E2E 测试。

## 不在范围内
- aioncore backend 内部 Team 调度实现。
- Team 创建、成员消息、workspace 迁移等 L2 垂直切片的逐步深挖。
- 修改 AionU 源码、测试、项目级进度台账或教学总索引。

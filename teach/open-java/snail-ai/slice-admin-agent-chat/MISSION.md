# 使命：L2-slice-admin-agent-chat

## 为什么
用户希望掌握 Snail AI 中 Admin 端智能体流式对话的完整纵向路径，以便后续能独立调试“后台发起对话后没有流式输出、没有持久化、usage 为空、Client 未接到任务”等问题，并能评估扩展 Agent 能力时应该改 Server 责任链还是 Agent Client 执行层。

## 成功的样子
- 能从 `POST /agent/{id}/chat` 追踪到 `FluxBridgeChatStreamWriter`、`AgentChatService` 和有序 `AgentChatHandler`。
- 能说清认证上下文、会话记录、模型配置、MCP、RAG、Skill、短期历史和目标 Client 分别在哪个阶段补齐。
- 能定位 gRPC URI `/chat/dispatch`、Client 端 `ChatDispatchStreamingHandler`、`ChatSessionRuntime`、`ClientChatExecutor` 和流式 Advisor。
- 能判断失败、取消、usage 回收、助手消息持久化、短期记忆更新和统计更新的边界。

## 约束条件
- 本主题只写入 `teach/open-java/snail-ai/slice-admin-agent-chat/` 下的教学产物。
- 不修改 Snail AI 源码、不修改 `index.md`、不修改 `_progress.*`，也不碰其他主题目录。
- 课程以当前本地源码快照为准，优先列具体源文件路径，不用泛目录代替证据。
- lesson 控制为 15 分钟内可完成；长清单、接口表和排查 checklist 分流到 reference。

## 不在范围内
- OpenAPI 第三方聊天接口的完整切片。
- Admin 前端页面或构建产物分析。
- 模型适配器、RAG 检索、Memory 存储、MCP SDK 的深度实现。
- 修改或运行 Snail AI 服务端、Agent Client 或数据库。

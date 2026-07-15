# 会话持久化全链路 资源

## 知识

- [源码：jsonl-storage.ts](../../../open-ai-agent/pi/packages/agent/src/harness/session/jsonl-storage.ts)
  JSONL 文件存储引擎。SessionHeader 格式（type/version/id/timestamp/cwd）、Entry 行解析、LeafEntry 写入、路径回溯。适用于：理解每条消息如何序列化为 JSONL 行。

- [源码：jsonl-repo.ts](../../../open-ai-agent/pi/packages/agent/src/harness/session/jsonl-repo.ts)
  JSONL 仓库层。cwd 编码、会话文件命名规则（`{timestamp}_{sessionId}.jsonl`）、create/open/list/delete/fork CRUD 操作。适用于：理解多会话目录管理和 fork 的完整实现。

- [源码：memory-storage.ts](../../../open-ai-agent/pi/packages/agent/src/harness/session/memory-storage.ts)
  内存存储引擎。与 JsonlSessionStorage 实现相同的 SessionStorage 接口，用于测试和临时会话。适用于：对比两种后端的接口一致性设计。

- [源码：memory-repo.ts](../../../open-ai-agent/pi/packages/agent/src/harness/session/memory-repo.ts)
  内存仓库。Map 存储会话实例，与 JsonlSessionRepo 实现相同的 SessionRepo 接口。适用于：理解仓库层的抽象设计。

- [源码：repo-utils.ts](../../../open-ai-agent/pi/packages/agent/src/harness/session/repo-utils.ts)
  仓库工具函数。createSessionId（UUIDv7）、getFileSystemResultOrThrow（Result 解包）、getEntriesToFork（Fork 条目选择）、toSession 工厂。适用于：理解跨存储后端的共享逻辑。

- [源码：compaction.ts](../../../open-ai-agent/pi/packages/agent/src/harness/compaction/compaction.ts)
  上下文压缩核心。token 估算、压缩阈值判断（shouldCompact）、切点选择（findCutPoint）、摘要生成（generateSummary）、完整压缩流程（compact）。适用于：理解何时触发压缩和如何生成摘要。

- [源码：branch-summarization.ts](../../../open-ai-agent/pi/packages/agent/src/harness/compaction/branch-summarization.ts)
  分支摘要。当用户在会话树中切换分支时，自动为被放弃的分支生成摘要。适用于：理解多分支会话的上下文保持机制。

- [源码：utils.ts](../../../open-ai-agent/pi/packages/agent/src/harness/compaction/utils.ts)
  压缩工具函数。文件操作提取（extractFileOpsFromMessage）、文件列表格式化（formatFileOperations）、对话序列化（serializeConversation）。适用于：理解摘要提示词的构建方式。

- [源码：session.ts](../../../open-ai-agent/pi/packages/agent/src/harness/session/session.ts)
  Session 类。树状条目管理、buildSessionContext（上下文重建）、moveTo（分支切换）、各种 append 方法。适用于：理解会话树的数据结构和操作 API。

- [源码：types.ts](../../../open-ai-agent/pi/packages/agent/src/harness/types.ts)
  Harness 类型定义。SessionTreeEntry 联合类型（11 种条目）、SessionStorage 接口、SessionRepo 接口、各类错误码。适用于：完整类型体系速查。

- [前置课程：L1-module-agent](../../../teach/open-ai-agent/pi/module-agent/lessons/0001-agent-module-tour.html)
  pi-agent-core 模块总览。已覆盖 harness 目录五层架构和 Agent 类 API。适用于：在阅读本课前回顾会话层在整体架构中的位置。

## 智慧（社区）

- [Pi Agent Harness GitHub](https://github.com/nicholasoxford/pi)
  主仓库。Issues 和 Discussions 是获取社区智慧的主要渠道。适用于：提交 bug、讨论设计决策。

## 空白

- 目前没有找到关于 JSONL 会话格式的独立规范文档或设计决策记录（ADR），仅能从源码中推断格式约定。
- 没有找到关于 compaction 算法选择（基于 token 的切点 vs 基于轮次的切点）的外部讨论或对比分析。

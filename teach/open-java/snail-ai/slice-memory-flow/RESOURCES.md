# L2-slice-memory-flow 资源

## 知识

- 本地源码：`open-java/snail-ai/docs/architecture/memory-architecture.md`
  记忆系统的设计说明，包含短期滑动窗口、长期抽取召回、注入格式和端到端流程。适用于理解目标架构，但需要与当前源码逐项核对。
- 本地源码：`open-java/snail-ai/docs/guide/memory/index.md`
  当前版本记忆能力状态说明，明确提示长期记忆和向量召回应以源码实现为准。适用于校正架构文档与实现之间的差异。
- 本地源码：`open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/agent/AgentChatService.java`
  对话命令进入责任链的位置，适用于确认 `AgentChatContext` 的初始字段。
- 本地源码：`open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/agent/AgentChatChainService.java`
  顺序执行 `AgentChatHandler` 列表的执行器，适用于理解 `@Order` 对真实链路的影响。
- 本地源码：`open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/ConversationHandler.java`
  `@Order(20)` 阶段，创建或复用会话并写入用户消息记录。
- 本地源码：`open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/ContextCollectorHandler.java`
  `@Order(75)` 阶段，选择 Client、写入短期 store、读取历史消息，是本切片的主来源。
- 本地源码：`open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/LlmCallHandler.java`
  `@Order(80)` 阶段，组装 `ChatDispatchRequest` 并发起 gRPC 流式分发。
- 本地源码：`open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/ChatStreamObserver.java`
  Client completion chunk 回来后的桥接和持久化触发点。
- 本地源码：`open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/persist/ChatResultPersistService.java`
  assistant 回复、短期记忆和用量统计的异步持久化入口。
- 本地源码：`open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-memory/src/main/java/com/aizuda/snail/ai/memory/store`
  `ShortTermMemoryStore`、`InMemoryShortTermMemoryStore`、`DbShortTermMemoryStore` 三个文件，适用于比较短期 store 行为。
- 本地源码：`open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/dto/memory`
  记忆相关跨模块 DTO，适用于理解短期加载请求和长期检索请求契约。
- 本地源码：`open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core/executor/prompt/DefaultPromptFactory.java`
  Client 侧最终 Prompt 组装位置，适用于验证 `historyMessages` 和 `memoryContext` 是否进入 LLM。

## 智慧（社区）

- 本主题暂不引入外部社区资源。
  原因：本课目标是追踪当前本地源码的真实执行顺序，外部社区无法替代源码事实。后续若要讨论长期记忆设计取舍，可补充 Spring AI、向量检索或 Agent memory 相关社区资料。

## 空白

- 当前源码中未找到可执行的长期记忆检索服务、`MemoryInjectionAdvisor` 或 `AgentChatContext#setMemoryContext` 调用点；本主题将其记录为实现缺口，而不是按架构文档假定已完成。

# 记忆功能模块资源

## 知识

- `open-java/snail-ai/docs/architecture/memory-architecture.md`
  Snail AI 官方记忆架构文档。适用于理解短期记忆、长期记忆、记忆类型、状态机和配置项的设计意图。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-memory/src/main/java/com/aizuda/snail/ai/memory`
  当前 Server 侧 memory feature 源码。适用于核对 DTO、指标对象、短期记忆 store 接口和实现。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/chain/ContextCollectorHandler.java`
  Agent 责任链里的上下文收集点。适用于理解短期历史如何进入 `ChatDispatchRequest.historyMessages`。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-agent/src/main/java/com/aizuda/snail/ai/feature/agent/persist/ChatResultPersistService.java`
  Chat 完成后的持久化与助手消息短期记忆追加点。适用于补齐一次对话结束后的写路径。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/dto/memory`
  公共记忆 DTO。适用于识别短期历史加载和长期记忆召回的跨模块契约。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common/enums/memory`
  记忆角色、类型、状态、事件、压缩和摘要枚举。适用于查阅长期记忆的数据语义。
- `open-java/snail-ai/snail-ai-starter/src/main/resources/application.yml`
  默认短期记忆配置。适用于确认 `snail-ai.memory.short-term.store-type` 的本地默认值。

## 智慧（社区）

- [Snail AI 上游 Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  适用于核对记忆模块的最新 Issue、变更说明和维护者讨论。源码与文档不一致时，优先用当前工作区源码和上游变更记录交叉验证。

## 空白

- 当前源码未找到 `MemoryInjectionAdvisor` 的实现类；官方架构文档仍保留相关设计描述，后续讲长期记忆召回前需要再次基于源码确认实际落地点。
- 本 L1 不纳入外部 Spring AI Memory 最佳实践资料；后续如果要设计或重构长期记忆链路，再补充 Spring AI 官方文档与向量检索资料。

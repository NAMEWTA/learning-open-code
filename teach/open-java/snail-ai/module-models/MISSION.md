# 使命：模型适配层模块

## 为什么
学习者需要从源码层面判断 Snail AI 如何把后台或 Agent 下发的模型配置，转换成可调用的 Chat、Embedding 与 Rerank 能力。掌握这个边界后，排查“模型不可用”“adapterKey 配错”“RAG 调不到 embedding/rerank”这类问题时，可以先定位到适配层，再决定是否继续深入 Server、Agent 或 RAG 切片。

## 成功的样子
- 能说明 `snail-ai-models` 在整体架构中承担的模型能力适配职责。
- 能区分 common、core、provider、starter 四层分别解决什么问题。
- 能沿一次 Chat 模型构建过程说清 `Spec`、`Runtime`、`Adapter` 和 `adapterKey` 的关系。
- 能在参考页中快速找到 Chat、Embedding、Rerank 的公共接口和内置 provider。
- 能对照 `models-api.html` 说出 Server 侧 `CryptoHelper`、配置枚举与 `AiModelUsageService` 的职责边界。
- 能列举三类 `*ModelAdapter` SPI 方法签名，并说明 `OpenAiChatModel` 中 `extraBody` 与 `ChunkMerger` 的扩展动机。

## 约束条件
- 读者具备 Java、Spring Boot 和 Spring Bean 注入基础，但不假设熟悉 Spring AI 的全部 API。
- L1 短课只讲模块边界和选择机制；L3 `models-api.html` 提供 API 速查，完整运行时链路见 `slice-model-runtime`。
- 课程保持 15 分钟内完成，长接口清单、provider 行为和扩展检查表放入参考页。
- 当前任务只写入 `teach/open-java/snail-ai/module-models/`。

## 不在范围内
- 不深入讲解 Agent 责任链、RAG 检索、Prompt 组装、模型配置 CRUD 或数据库表设计。
- 不逐行解析 Spring AI `OpenAiChatModel` 的请求、流式响应、工具调用和观测实现。
- 不修改源项目 `open-java/snail-ai/**`、项目级进度台账或教学索引。

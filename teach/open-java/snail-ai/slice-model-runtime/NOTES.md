# 便签

- 用户要求生成 L2 垂直切片主题 `L2-slice-model-runtime`，目标是模型配置到运行时调用。
- 本次只允许写入 `teach/open-java/snail-ai/slice-model-runtime/**`，不得编辑源码、`index.md`、`_progress.*` 或其他主题目录。
- 已有 L1 主题包括 `module-models`、`module-agent-client`、`module-rag`；本主题不重复模块导览，只串联垂直调用链。
- 源码观察：Agent 对话链路中，Server 端 `DispatchModelConfigAssembler` 已解密 API Key 并放入 `ChatDispatchRequest.ModelConfig.apiKey`；Client 端只校验并消费，不再解密。
- 源码观察：Server 本地 `ModelRuntimeHandler` 每次先通过 `ModelConfigHandler.getConfigInfo` 取配置，再通过 `decryptApiKey` 解密，最后进入三类 builder。
- 源码观察：Chat usage 主要在 Client 流式 advisor 链中提取并随 completion chunk 回到 Server 持久化；Embedding 当前转换主要填充 vectors、dimensions、costTimeMs；Rerank 返回 index/score，没有 token usage。
- 源码观察：RAG rerank 对空结果、`ModelCallException` 和其他异常都有降级，最终按原 score 排序；Embedding 维度探测失败会使用并持久化默认维度 1024。

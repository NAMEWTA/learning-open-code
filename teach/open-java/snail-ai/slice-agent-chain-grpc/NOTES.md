# 便签

- 本主题是 Snail AI 的 L2 垂直切片，默认读者已看过 `module-agent-chain`、`module-commons-grpc`、`module-agent-client` 三个 L1。
- 用户明确限制本次只能写入 `teach/open-java/snail-ai/slice-agent-chain-grpc/**`，因此不更新 `teach/open-java/snail-ai/index.md`、`_progress.*` 或其他主题目录。
- 课程重点放在“Server 责任链状态如何一步步变成 `/chat/dispatch` server-streaming 调用”，Client 内部模型执行只讲到 `ChatSessionRuntime` 消费边界。
- 当前源码中 `GrpcChannelUtil.sendServerStreaming` 使用 `CallOptions.DEFAULT`，没有在桥接工具层设置统一 deadline；调试超时要从上层调用、channel、网络和 Client runtime 分别看。

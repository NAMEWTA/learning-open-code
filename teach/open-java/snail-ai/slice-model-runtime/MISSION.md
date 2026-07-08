# 使命：L2-slice-model-runtime（模型配置到运行时调用）

## 为什么
用户需要把 Snail AI 中的模型配置，从 Server 解析、API Key 解密、endpoint/modelKey/provider/adapter 组装，一路追到 Chat、Embedding、Rerank 三类运行时调用，能够定位模型不可用、adapter 选错、RAG 降级、usage 缺失和错误传播这几类真实问题。

## 成功的样子
- 能画出 `ModelResolveHandler -> DispatchModelConfigAssembler -> ChatDispatchRequest.ModelConfig -> Client ChatModelRuntime` 的 Agent 对话链路。
- 能画出 `ModelRuntimeHandler -> ServerModelFacade -> ChatModelRuntime / EmbeddingModelRuntime / RerankModelRuntime` 的 Server 本地模型运行链路。
- 能解释 `ModelConfigInfoDTO`、`ChatDispatchRequest.ModelConfig`、`ConfigExtAttrsDTO` 中哪些字段进入 runtime。
- 能区分 Chat、Embedding、Rerank 的返回结构、usage 边界、异常包装和降级策略。
- 能用具体源码路径定位配置解析、API Key 解密、provider adapter 注册、RAG embedding/rerank 调用点和错误出口。

## 约束条件
- 教学产物只基于当前 `open-java/snail-ai` 源码与已有 L1 主题，不修改业务源码。
- 本主题只写入 `teach/open-java/snail-ai/slice-model-runtime/`。
- 第一节课控制在 15 分钟内完成，字段表、provider 目录、异常矩阵和调试步骤放入 reference。

## 不在范围内
- 不实现新的模型 provider 或修复运行时行为。
- 不展开完整 RAG 摄入算法、MCP 工具执行、OpenAPI chat 入口细节。
- 不评估线上密钥分发安全策略，只记录当前源码中 API Key 的解密和传递边界。

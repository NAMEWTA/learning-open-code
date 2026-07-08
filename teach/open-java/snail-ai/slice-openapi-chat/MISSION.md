# 使命：L2-slice-openapi-chat（OpenAPI 流式对话）

## 为什么
用户需要从第三方 OpenAPI chat 请求一路追到 Agent Client 的模型流式回传，能够定位认证失败、DTO 转换遗漏、SSE 无输出、同步响应超时以及 token usage 缺失这几类真实问题。

## 成功的样子
- 能画出 `OpenAPI 请求 -> 鉴权 -> 服务转换 -> Agent 链 -> gRPC -> Client -> SSE/聚合响应` 的主路径。
- 能说清 `OpenApiChatRequest` 哪些字段进入 `AgentChatCommand`，哪些字段当前只是 DTO 暴露但没有被服务层消费。
- 能区分流式 `event: text/thinking/done/error` 与同步 `Result<OpenApiChatSyncResponse>` 的数据边界。
- 能用源码路径定位认证头、writer 行为、错误返回和 usage 持久化链路。

## 约束条件
- 教学产物只基于当前 `open-java/snail-ai` 源码与已有 L1 主题，不修改业务源码。
- 第一节课控制在 15 分钟内完成，长表格、端点清单和排错步骤放入 reference。
- 本主题只写入 `teach/open-java/snail-ai/slice-openapi-chat/`。

## 不在范围内
- 不实现或修复 OpenAPI chat 行为。
- 不展开模型 provider 适配、RAG 检索算法、MCP 工具执行细节。
- 不覆盖 `deepPlanEnabled`、`webSearchEnabled` 的未来设计，只记录当前链路未消费的事实。

# Commons 与 gRPC 基础模块资源

## 知识

- [Commons 与 gRPC 公共类型 API 字典](./reference/commons-grpc-api.html)
  L3 微观速查：工具类、异常、日志、OpenAPI DTO、embedding 类型与 proto 生成类的签名、约束和调用示例。
- [Client 路由策略 API](./reference/route-strategy-api.html)
  L3 微观速查：`ClientRouteStrategy` 六种实现的选择算法、线程安全、适用场景，以及与 StoreInstance 存储路由的边界区分。
- [Commons 与 gRPC 模块地图](./reference/commons-grpc-overview.html)
  L1 模块总览配套参考：DTO 分类索引、gRPC URI 表、Server/Client 边界与兼容风险。
- [L0 项目地图](../00-overview/lessons/0001-project-map.html)
  用于确认 `snail-ai-commons` 在整体 Maven 模块中的共享基础层定位。
- [Agent 责任链模块导览](../module-agent-chain/lessons/0001-agent-chain-module-tour.html)
  用于衔接 Server 端 `LlmCallHandler` 如何组装 `ChatDispatchRequest` 并发往 Client。
- [Agent Client 执行层模块导览](../module-agent-client/lessons/0001-agent-client-module-tour.html)
  用于确认 Agent Client 如何消费 `/chat/dispatch` 并通过 `RpcClient` 回调 Server。
- `open-java/snail-ai/docs/architecture/overview.md`
  官方架构总览，说明 Commons 是常量、DTO、枚举、gRPC Proto、通用工具和异常的共享基础层。
- `open-java/snail-ai/docs/architecture/distributed.md`
  官方分布式架构说明；其中部分端口和 proto 描述需要以当前源码为准。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-core/src/main/java/com/aizuda/snail/ai/common`
  当前课程的公共 DTO、枚举、工具类和异常源码入口。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-grpc/src/main/proto/snail_ai_grpc_service.proto`
  当前 gRPC 信封的一手定义，包含 `GrpcSnailAiRequest`、`GrpcSnailAiResult` 和 `Metadata`。
- `open-java/snail-ai/snail-ai-commons/snail-ai-commons-grpc/src/main/java/com/aizuda/snail/ai/common/grpc`
  当前 gRPC client、server、handler、常量和已生成 protobuf Java 类源码入口。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-common/src/main/java/com/aizuda/snail/ai`
  Server feature-common RPC、心跳注册、Client 实例管理和路由策略源码入口。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-common/src/main/java/com/aizuda/snail/ai/route/`
  `ClientRouteStrategy`、`RouteStrategyType` 与 First/Random/RoundRobin/ConsistentHash/LRU 六种实现的一手源码。
- `open-java/snail-ai/docs/guide/app/route-strategy.md`
  官方路由策略产品说明；LRU 语义与 `LruClientRoute` 实现存在差异，课程以源码为准。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-common/src/main/java/com/aizuda/snail/ai/agent/common`
  Agent Client 侧 gRPC server、心跳、回调动态代理和 channel 管理源码入口。
- `open-java/snail-ai/snail-ai-agent/snail-ai-agent-executor/snail-ai-agent-executor-core/src/main/java/com/aizuda/snail/ai/agent/core`
  Agent Client 执行核心源码入口，包含消费 `/chat/dispatch` 的 `ChatDispatchStreamingHandler` 与会话运行时。

## 智慧（社区）

- [Snail AI Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  项目真实协作入口；适用于核对 gRPC 契约、DTO 变更和发布版本兼容问题。
- 本地源码评审：`open-java/snail-ai`
  本主题以工作区实际 checkout 为准；当官方文档与源码不一致时，优先回到源码、pom 和生成类核对。

## 空白

- 当前未发现专门覆盖 `GrpcRequestDispatcher`、`GrpcChannelUtil`、`BeatRequestHandler` 或 `GrpcClientInvokeHandler` 的单元测试；本主题的行为判断主要依据源码阅读。
- `docs/architecture/distributed.md` 中的双向流 service 示例与当前源码的统一 unary/server-streaming 信封实现不一致；后续若补文档，应以 `snail_ai_grpc_service.proto` 和 `GrpcServiceDefinitionBuilder` 为准。

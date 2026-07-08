# 使命：Commons 与 gRPC 基础模块

## 为什么
学习者需要看懂 Snail AI 的共享契约层如何把 Server 责任链、Agent Client 执行层和跨端回调连接起来。掌握这一层后，排查对话分发、心跳注册、RAG/Skill 回调或 DTO 字段兼容问题时，可以先判断问题属于业务 DTO、gRPC 信封、URI 路由还是两端消费边界。

## 成功的样子
- 能按类别说明 `commons-core` 中对话、心跳、记忆、Skill、RAG、枚举和工具类的用途。
- 能解释 `commons-grpc` 只提供统一请求/响应信封，业务语义由 `metadata.uri` 和 JSON `body` 承载。
- 能把 Server `feature-common` 的 `/beat`、Client 实例注册、路由选择与 Server 到 Agent Client 的 `/chat/dispatch` 串起来。
- 能识别 proto、URI、DTO 字段、JSON 序列化和生成代码不同步带来的兼容风险。
- 查阅 `reference/commons-grpc-api.html` 时，能按类/接口定位签名、校验约束、返回值、边界条件与调用示例（L3 微观字典）。
- 查阅 `reference/route-strategy-api.html` 时，能对比六种 Client 路由算法、判断线程安全与会话亲和需求，并区分与 StoreInstance 存储路由的差异。

## 约束条件
- 本主题是 L1 模块总览，短课必须在 15 分钟内完成。
- 模块地图、RPC URI 表和兼容风险放入 `reference/commons-grpc-overview.html`；类级 API 字典放入 `reference/commons-grpc-api.html`；Client 路由策略 API 放入 `reference/route-strategy-api.html`。
- 只读 `open-java/snail-ai` 源码，不修改源项目。

## 不在范围内
- 不展开 Agent Client 内部 ChatClient、Advisor、Tool resolver 的完整执行细节。
- 不讲 RAG、Memory、Skill 模块各自的业务算法。
- 不设计新的 proto 或 DTO 迁移方案，只识别当前源码的演进边界。

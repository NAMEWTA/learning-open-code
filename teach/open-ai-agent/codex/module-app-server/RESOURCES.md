# App-server JSON-RPC 服务资源

## 知识

- [codex-rs/app-server/README.md](../../../../open-ai-agent/codex/codex-rs/app-server/README.md)
  官方模块说明，覆盖协议、生命周期、初始化、API Overview、事件、审批、Skills、Apps 与实验 API。适用于确认对外行为。
- [codex-rs/app-server/src/main.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/main.rs)
  二进制入口，展示 CLI 参数、transport URL、session source、严格配置和 remote control 启动模式如何进入 runtime。
- [codex-rs/app-server/src/lib.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/lib.rs)
  runtime 主入口，展示配置加载、transport acceptor、outbound router、processor loop、初始化通知和优雅关闭。
- [codex-rs/app-server/src/message_processor.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/message_processor.rs)
  入站 JSON-RPC 分发中心，展示初始化门禁、实验 API gate、序列化队列和各类 request processor 的路由。
- [codex-rs/app-server/src/request_processors/](../../../../open-ai-agent/codex/codex-rs/app-server/src/request_processors/)
  业务处理器集合，按 Thread、Turn、FS、Config、MCP、Plugin、Account、Process 等领域拆分。
- [codex-rs/app-server/src/transport.rs](../../../../open-ai-agent/codex/codex-rs/app-server/src/transport.rs)
  app-server 对 `codex-app-server-transport` 的本地封装，维护连接状态、通知过滤和 outbound 路由。
- [codex-rs/app-server-protocol/src/rpc.rs](../../../../open-ai-agent/codex/codex-rs/app-server-protocol/src/rpc.rs)
  JSON-RPC 对象定义；注意 wire 上不强制携带 `"jsonrpc":"2.0"` 字段。
- [codex-rs/app-server-protocol/src/protocol/common.rs](../../../../open-ai-agent/codex/codex-rs/app-server-protocol/src/protocol/common.rs)
  `ClientRequest`、`ServerNotification`、`ServerRequest`、`ClientNotification` 的方法枚举源头。
- [codex-rs/app-server-protocol/src/protocol/v1.rs](../../../../open-ai-agent/codex/codex-rs/app-server-protocol/src/protocol/v1.rs)
  初始化、旧审批、认证状态等 V1 类型；仍被统一协议导出层复用。
- [codex-rs/app-server/tests/suite/v2/](../../../../open-ai-agent/codex/codex-rs/app-server/tests/suite/v2/)
  集成测试入口，用于验证各 API 类别的真实请求和通知行为。

## 智慧（社区）

- [OpenAI Codex GitHub Issues](https://github.com/openai/codex/issues)
  适合验证协议变更、客户端集成问题和真实使用场景。
- [OpenAI Codex GitHub Pull Requests](https://github.com/openai/codex/pulls)
  适合追踪 app-server、protocol schema、IDE 集成和 transport 层的设计演进。

## 空白

- 暂未找到 app-server 协议的独立稳定版公开规范；当前以仓库 README、协议 crate 和集成测试作为一手来源。
- WebSocket transport 在 README 中标注为 experimental / unsupported，本主题不把它作为生产集成建议来源。

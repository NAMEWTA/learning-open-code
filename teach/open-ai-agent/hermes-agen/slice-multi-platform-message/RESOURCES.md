# 多平台消息全链路 资源

## 知识

| 资源 | 说明 |
|------|------|
| `gateway/platforms/base.py` (239KB) | BasePlatformAdapter 抽象基类，定义 connect/send/disconnect 接口，MessageEvent 数据模型 |
| `gateway/relay/adapter.py` (27KB) | RelayAdapter — 通用中继适配器，将 WebSocket 传输包装为标准平台适配器 |
| `gateway/relay/ws_transport.py` (34KB) | WebSocket RelayTransport — 与 connector 的实时通信层 |
| `gateway/delivery.py` (22KB) | DeliveryRouter — 四级投递路由与目标解析 |
| `gateway/channel_directory.py` (17KB) | Home Channel 管理与频道别名解析 |
| `gateway/config.py` (102KB) | 网关配置，含 HomeChannel 定义和 24 平台配置 |
| `gateway/session.py` | SessionSource 数据模型 — 描述消息来源的完整上下文 |
| `gateway/run.py` (995KB) | GatewayRunner — 网关启动、适配器生命周期管理 |
| `gateway/stream_consumer.py` (90KB) | 流式响应消费者，将 Agent 输出 push 到适配器 |

## 智慧（社区）

- [python-telegram-bot 文档](https://docs.python-telegram-bot.org/) — Telegram Bot API 封装库，base.py 中 Telegram 适配器的依赖
- [websockets 库文档](https://websockets.readthedocs.io/) — RelayTransport 使用的 WebSocket 客户端库

## 空白

- Discord 平台的 connector 实现代码在本仓库中不可见（connector 为独立仓库），仅能看到 gateway 侧的 RelayTransport 协议层
- 各平台适配器的具体 API 调用细节分散在 base.py 各子类中，暂无集中对比文档

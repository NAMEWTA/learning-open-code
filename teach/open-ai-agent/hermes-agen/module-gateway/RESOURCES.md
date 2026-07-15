# 消息网关模块 资源

## 知识

- [gateway/__init__.py — 模块入口](https://github.com/NousResearch/hermes-agent/blob/main/gateway/__init__.py)
  定义了 gateway 的公开 API：GatewayConfig、SessionContext、DeliveryRouter 等核心导出。适用场景：快速了解模块进口和出口。

- [gateway/config.py — 网关配置管理 (102KB)](https://github.com/NousResearch/hermes-agent/blob/main/gateway/config.py)
  Platform 枚举定义 22+ 平台、GatewayConfig 数据类、配置加载与验证逻辑。适用场景：理解平台注册机制和配置结构。

- [gateway/platforms/base.py — 平台适配器基类](https://github.com/NousResearch/hermes-agent/blob/main/gateway/platforms/base.py)
  所有平台适配器的抽象基类，定义 connect/disconnect/send/get_chat_info 四个核心方法。适用场景：理解平台适配器的统一接口契约。

- [gateway/delivery.py — 消息投递系统 (23KB)](https://github.com/NousResearch/hermes-agent/blob/main/gateway/delivery.py)
  DeliveryRouter 实现消息从 Agent 到目标平台的三级回退路由。适用场景：理解投递规则和 silence narration 过滤。

- [gateway/relay/ — 中继子系统](https://github.com/NousResearch/hermes-agent/blob/main/gateway/relay/)
  RelayAdapter + WebSocketRelayTransport 实现跨网关的消息中继，支持多租户/多实例。适用场景：理解 gateway-gateway 连接器架构。

- [gateway/platform_registry.py — 平台注册中心 (13KB)](https://github.com/NousResearch/hermes-agent/blob/main/gateway/platform_registry.py)
  PlatformEntry + platform_registry 支持内置和插件适配器的动态注册与发现。适用场景：理解平台扩展机制。

## 智慧（社区）

- [Discord — Nous Research](https://discord.gg/NousResearch)
  Hermes Agent 官方社区，包含 gateway 配置、平台对接问题的讨论。适用场景：平台接入故障排查和最佳实践。

- [GitHub Issues — hermes-agent](https://github.com/NousResearch/hermes-agent/issues)
  搜索 "gateway" 标签可查看历史问题和设计讨论。适用场景：理解平台接入的边界情况和已知限制。

## 空白

- 暂无针对 gateway 模块的外部独立文档或教程
- 各平台 API 文档分散在对应官方文档中（Telegram Bot API、Discord Developer Portal 等），未在本列表中逐一收录

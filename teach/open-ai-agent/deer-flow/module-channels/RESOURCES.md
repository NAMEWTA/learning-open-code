# IM channels 与 GitHub webhook 资源

## 知识

- `backend/app/channels/message_bus.py`
  异步 pub/sub 枢纽：`InboundMessage` 入队、`OutboundMessage` 分发给各 channel 回调。
- `backend/app/channels/manager.py`
  核心调度器：消费入站消息、经 `langgraph_sdk` 创建 thread/run、处理命令与流式/非流式回复。
- `backend/app/channels/service.py`
  从 `config.yaml` 的 `channels` 段启动各平台 worker，并挂载 `ChannelManager` 单例。
- `backend/app/channels/base.py`
  抽象 `Channel` 生命周期：start/stop/send，以及 `/connect` 绑定辅助逻辑。
- `backend/app/gateway/routers/channels.py`
  运维向 API：`GET /api/channels/` 状态、`POST /api/channels/{name}/restart` 重启 worker。
- `backend/app/gateway/routers/channel_connections.py`
  用户面向绑定 API：providers、connect code、runtime-config、disconnect。
- `backend/app/gateway/routers/github_webhooks.py`
  `POST /api/webhooks/github`：HMAC 验签、事件分发、503 重试语义。
- `backend/app/gateway/github/dispatcher.py`
  `fanout_event`：按 custom agent 的 `github:` 绑定把 webhook 拆成多条 `InboundMessage`。
- `backend/app/gateway/github/registry.py`、`triggers.py`、`prompts.py`
  agent 绑定查找、触发器过滤、prompt 组装。
- `backend/docs/IM_CHANNEL_CONNECTIONS.md`
  用户绑定流程、connect code、provider 运维说明（仓库内官方文档）。
- `backend/AGENTS.md` — IM Channels System 章节
  消息流、owner-scoped 存储、GitHub event-driven agents 的设计摘要。
- `backend/tests/test_channels.py`、`backend/tests/test_github_webhooks.py`
  channel 服务与 webhook 路由的核心回归测试。
- `backend/tests/test_telegram_channel_connections.py`、`backend/tests/test_slack_channel_connections.py`
  用户绑定与 connect code 流程测试线索。

## 智慧（社区）

- [Slack API — Events API](https://api.slack.com/apis/connections/events-api) — Slack 事件订阅与 Socket Mode 背景，有助于理解 `slack.py` 的双 token 模型。
- [GitHub Docs — Webhooks](https://docs.github.com/en/webhooks) — `X-Hub-Signature-256` 验签与重试语义，对应 `github_webhooks.py` 的 200/503 分流。

## 空白

- 各 IM 平台官方「最佳实践」文档未逐条收录；本主题以 deer-flow 仓库内实现与 `IM_CHANNEL_CONNECTIONS.md` 为准。
- 前端 Settings 里 channel 连接 UI 的交互细节留待 `module-frontend-core` 或垂直切片补充。

# 使命：IM channels 与 GitHub webhook

## 为什么
学习者需要把 deer-flow 的「外部消息入口」放回整体架构：飞书、Slack、Telegram 等 IM 平台，以及 GitHub App webhook，都不是直接调用 lead agent，而是先进入 channel 层，再经 Gateway 的 LangGraph 兼容 API 触发 run。掌握这条边界后，才能判断问题是出在平台适配、用户绑定、webhook 验签，还是 ChannelManager 与 runtime 的衔接。

## 成功的样子
- 能画出「IM 长轮询 / GitHub webhook → MessageBus → ChannelManager → Gateway API」的主链路。
- 能区分 `channels.py`（运维状态）、`channel_connections.py`（用户绑定）与 `github_webhooks.py`（入站 webhook）三类 Gateway 入口。
- 能说明 GitHub 事件为何走 fan-out + fire-and-forget，而飞书/Telegram 可走流式 outbound。

## 约束条件
- 本次是 L1 模块课，只覆盖模块职责、目录骨架、两条主入口和一条消息总线链路。
- lesson 控制在 15 分钟内；接口清单、provider 列表、测试矩阵放入 reference。
- 仅写入 `teach/open-ai-agent/deer-flow/module-channels/`，不修改源项目。

## 不在范围内
- 不逐平台讲解 Feishu/Slack SDK 细节。
- 不讲一次 IM 消息从入站到 agent 回复的完整垂直切片（见 L2 `slice-im-channel-run`）。
- 不讲 Gateway 认证中间件全貌（见 L1 `module-gateway`）。

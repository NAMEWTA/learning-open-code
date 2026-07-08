# 使命：IM channel 入站消息如何触发 run

## 为什么
DeerFlow 的飞书、Slack、Telegram 等 IM 入口与浏览器聊天共用同一套 Gateway runtime。排查「IM 发了消息没反应」「重复回复」「线程忙」时，必须能从平台 adapter 一路指到 `ChannelManager` 如何创建 thread 并调用 `runs.wait` / `runs.stream` / `runs.create`。

## 成功的样子
- 能按层说出：平台 adapter → `MessageBus.publish_inbound` → `ChannelManager._dispatch_loop` → `langgraph_sdk` → Gateway `/api/threads` + `/api/threads/{id}/runs/*`
- 能区分三种 run 模式：阻塞 `wait`、流式 `stream`、GitHub 的 fire-and-forget `create`
- 能解释至少一条异常路径（未绑定身份被拒、同 thread 并发 run 返回 busy）

## 约束条件
- 以传统 IM 长轮询路径为主，GitHub webhook 仅作变体标注
- 单节课 15 分钟内完成，接口表与 provider 差异查 reference 速查页

## 不在范围内
- 各平台 adapter 的验签、卡片 UI、connect 绑定码生成细节（见 L1 `module-channels`）
- lead agent 图内 middleware 与工具执行（见 `module-lead-agent`）

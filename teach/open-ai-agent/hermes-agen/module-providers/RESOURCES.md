# 模型提供商层 资源

## 知识

- [providers/base.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/providers/base.py)
  ProviderProfile 数据类定义（9 KB），声明模型的识别信息、认证端点、客户端/请求级怪癖，以及 5 个可重写钩子。适用于理解单个 provider 的完整配置模型。

- [providers/__init__.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/providers/__init__.py)
  注册中心实现（7 KB），包含 register_provider()、get_provider_profile()、list_providers() 三个公开 API，以及三层懒加载发现机制（bundled plugins → user plugins → legacy per-file modules）。适用于理解 provider 的注册与查找流程。

- [providers/README.md — 源码](https://github.com/NousResearch/hermes-agent/blob/main/providers/README.md)
  模块自述文档，说明目录布局、下游消费者列表、钩子速查表。适用于快速定位 providers/ 在整个项目中的接线关系。

- [plugins/model-providers/README.md — 源码](https://github.com/NousResearch/hermes-agent/blob/main/plugins/model-providers/README.md)
  Provider 插件契约与示例，说明 plugin.yaml 格式、register_provider() 调用时机。适用于学习如何添加新 provider。

- [agent/transports/chat_completions.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/agent/transports/chat_completions.py)
  传输层的 `_build_kwargs_from_profile()` 方法（约 465 行起），展示 provider profile 如何被消费：prepare_messages → build_api_kwargs_extras → build_extra_body。适用于理解 profile → API 调用的完整数据流。

- [agent/chat_completion_helpers.py — 源码](https://github.com/NousResearch/hermes-agent/blob/main/agent/chat_completion_helpers.py)
  LLM 对话补全统一入口（147 KB），在约 793 行通过 `get_provider_profile(agent.provider)` 获取 profile 并委托给 transports 层。适用于理解 LLM 调用链路中 provider profile 的接入点。

## 智慧（社区）

- [r/nousresearch](https://reddit.com/r/nousresearch)
  Nous Research 官方 subreddit，适用于：架构讨论、使用问题、新功能反馈。

- [Hermes Agent Discord](https://discord.gg/nousresearch)
  官方 Discord 社区，适用于：实时问答、bug 报告、功能请求。

## 空白

- 各 provider 插件（plugins/model-providers/ 下 30 个目录）的逐 provider 设计说明文档在公开资料中较少，主要依赖 plugin.yaml 和 __init__.py 源码注释。
- ProviderProfile 各字段的语义（如 supports_vision_tool_messages、api_mode 的可选值）缺乏独立的设计决策记录。
- 从 legacy flag-based 参数传递迁移到 provider profile 的动机与权衡没有公开的 ADR 文档。

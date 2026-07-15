# 使命：模型提供商层

## 为什么
理解 Hermes Agent 如何通过 ProviderProfile 声明式抽象统一管理 30+ 个模型提供商（OpenAI、Anthropic、Gemini、DeepSeek、Kimi 等），以及提供商的注册发现、插件覆盖机制和请求级适配钩子。掌握 providers/ 层后，能独立添加新模型提供商、诊断多 provider 路由问题，并理解 agent/ 层如何通过 provider profile 代替 20+ 个布尔标志来配置 API 调用行为。

## 成功的样子
- 能画出 providers/ 层的三层结构图（ProviderProfile 基类 → 注册中心 → 插件目录）
- 能说出 ProviderProfile 的 5 个可重写钩子（get_hostname、prepare_messages、build_extra_body、build_api_kwargs_extras、fetch_models）的用途
- 能写出注册一个新 provider profile 的最小代码示例
- 能解释 provider profile 如何被 agent/transports/chat_completions.py 消费，替代传统的 flag-based 参数传递

## 约束条件
- 学习方式：阅读教学课程 + 对照源码验证
- 先修要求：已完成 L1-agent-core，理解 Agent 核心通过 chat_completion_helpers 调用 LLM
- 本模块聚焦 providers/ 目录本身和 profile → transport 的消费链路，不深入各 adapter 文件的内部细节

## 不在范围内
- agent/anthropic_adapter.py 内部的 Anthropic Messages API 格式转换细节（属于 adapter 专题）
- agent/codex_responses_adapter.py 的 Codex/OpenAI Responses API 适配（属于 adapter 专题）
- agent/bedrock_adapter.py 的 AWS Bedrock 集成（属于 adapter 专题）
- 各 provider 插件的认证凭证解析逻辑（属于 hermes_cli/auth.py 范畴）

# 教学笔记：模型提供商层

- 本模块代码量小（2 个 .py，28 KB）但覆盖面广 — ProviderProfile 被 10+ 个下游模块消费
- 实际的 adapter 适配逻辑（anthropic_adapter、codex_responses_adapter 等）在 agent/ 目录下，不在 providers/ 目录，教学时需明确边界
- 30 个 provider 插件通过 plugins/model-providers/ 目录管理，注册中心仅负责发现和索引

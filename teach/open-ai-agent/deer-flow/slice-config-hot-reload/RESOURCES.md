# 配置热加载边界 资源

## 知识

- [backend AGENTS.md — Config Hot-Reload Boundary](open-ai-agent/deer-flow/backend/AGENTS.md) — 产品级约定：`get_app_config()` 按请求刷新 vs `startup_config` 快照
- [reload_boundary.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/config/reload_boundary.py) — `STARTUP_ONLY_FIELDS` 注册表与 `startup-only:` 前缀契约
- [app_config.py](open-ai-agent/deer-flow/backend/packages/harness/deerflow/config/app_config.py) — `get_app_config()` 内容签名缓存、`AppConfig.from_file()` 加载链
- [gateway/app.py — lifespan](open-ai-agent/deer-flow/backend/app/gateway/app.py) — `startup_config` 一次性引导 logging、langgraph_runtime、channels、scheduler
- [gateway/deps.py — get_config](open-ai-agent/deer-flow/backend/app/gateway/deps.py) — 每个 HTTP/run 请求走热加载路径
- [test_reload_boundary.py](open-ai-agent/deer-flow/backend/tests/test_reload_boundary.py) — 注册表与 Pydantic schema 双向漂移测试
- [config.example.yaml](open-ai-agent/deer-flow/config.example.yaml) — 运行时配置模板；IDE hover 对 `startup-only` 字段有内联说明
- [GitHub issue #3144](https://github.com/bytedance/deer-flow/issues/3144) — 热加载边界的设计背景

## 智慧（社区）

- [deer-flow GitHub Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `hot reload` / `config reload` / `startup-only` 可见运维踩坑讨论
- [deer-flow Discussions](https://github.com/bytedance/deer-flow/discussions) — 部署与配置变更的实践经验

## 空白

- 官方未提供独立的「配置变更需否重启」CLI 扫描器；当前机器可读来源仅为 `reload_boundary.py` 与 `test_reload_boundary.py`

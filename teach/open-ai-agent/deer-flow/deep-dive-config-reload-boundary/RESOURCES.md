# 配置热加载边界深潜 资源

## 知识

- [DeerFlow backend AGENTS.md — Config Hot-Reload Boundary](https://github.com/bytedance/deer-flow/blob/main/backend/AGENTS.md) — 官方架构说明：请求路径 vs 启动快照、`STARTUP_ONLY_FIELDS` 列表
- [issue #3144](https://github.com/bytedance/deer-flow/issues/3144) — 热加载边界契约来源：Gateway 每请求 `get_app_config()` 与启动单例的分工
- [issue #3107](https://github.com/bytedance/deer-flow/issues/3107) — 刻意不把 `AppConfig` 挂在 `app.state` 的原因
- L2 前置课：[配置热加载切片](../slice-config-hot-reload/lessons/0001-flow-map.html) — 边界总览与决策流程
- L2 参考页：[热加载边界速查](../slice-config-hot-reload/reference/config-hot-reload-flow-map.html) — 完整 `STARTUP_ONLY_FIELDS` 表

## 智慧（社区）

- [DeerFlow GitHub Discussions](https://github.com/bytedance/deer-flow/discussions) — 运维改 `config.yaml` 后行为不符预期时，可对照注册表与日志 `reloading AppConfig` 发帖求证

## 空白

- 尚无独立的「配置运维 runbook」外部文档；排障仍以源码注册表与 `test_reload_boundary.py` 为准

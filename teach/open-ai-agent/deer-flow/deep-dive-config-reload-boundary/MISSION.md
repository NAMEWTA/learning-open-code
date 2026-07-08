# 使命：配置热加载边界的机制与排障

## 为什么
L2 切片已能判断「改完要不要重启」，但运维仍会遇到「日志显示已重载、行为却像旧配置」的误报。我需要读懂 `STARTUP_ONLY_FIELDS` 为何这样设计、签名检测如何触发重载，以及如何把「配置对象已更新」与「启动单例未更新」区分开。

## 成功的样子
- 能解释注册表为何同时覆盖 `AppConfig` 字段与 `channels` 等非 schema 段
- 能说出 `_get_config_signature` 的三元组及其应对 NFS 陈旧 mtime 的意图
- 能列举至少 3 种「像热加载失败、实为启动快照」的误报并给出排障步骤

## 约束条件
- L4 深潜：聚焦 `reload_boundary.py`、`app_config.py` 签名逻辑、`gateway/app.py` lifespan
- 单节短课 15 分钟内；完整字段表与测试索引见参考页

## 不在范围内
- `extensions_config.json` 的 MCP mtime 失效链
- `make config-upgrade` 与 `config_version` 合并
- 前端 Settings 如何展示 feature flags

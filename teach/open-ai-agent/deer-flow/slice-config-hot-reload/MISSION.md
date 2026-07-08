# 使命：配置模型和工具的热加载边界

## 为什么
运维或开发时改 `config.yaml`，我期望「下一条聊天消息就生效」。但 DeerFlow 里有些字段在 Gateway 启动时被快照进引擎单例——改完不重启会 silently 无效或 split-brain。我需要一张可操作的边界图，知道改哪段配置要 `make dev` 重启、哪段保存即生效。

## 成功的样子
- 能说出请求路径 `get_config() → get_app_config()` 与启动路径 `lifespan(startup_config)` 的分工
- 能列举 `reload_boundary.STARTUP_ONLY_FIELDS` 中至少 5 项及各自「为何需重启」
- 能判断常见改动（`models[*].max_tokens`、`memory.debounce_seconds`、`database.backend`、`sandbox.use`）属于热加载还是重启

## 约束条件
- L2 垂直切片：只跟 `config.yaml` 主配置边界，不展开 `extensions_config.json` 的 MCP mtime 失效
- 单节短课 15 分钟内；完整注册表与源码索引查参考页

## 不在范围内
- `make config-upgrade` 与 `config_version` 合并流程
- Docker 卷挂载与 `DEER_FLOW_CONFIG_PATH` 路径解析细节
- 前端 Settings 页如何展示 feature flags

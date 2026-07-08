# 配置与部署 资源

## 知识

- [`teach/open-ai-agent/deer-flow/00-overview/reference/00-overview.html`](../00-overview/reference/00-overview.html)
  L0 总览已标出 nginx、Gateway、Frontend、Redis、provisioner 的服务拓扑，本主题沿用其中的部署锚点。
- [`open-ai-agent/deer-flow/AGENTS.md`](../../../../open-ai-agent/deer-flow/AGENTS.md)
  仓库根目录的服务拓扑表、根 `make` 与模块级命令分工、配置文件位置说明。
- [`open-ai-agent/deer-flow/Install.md`](../../../../open-ai-agent/deer-flow/Install.md)
  官方安装与首次启动流程，适合对照 `make setup` / `make dev` 实操。
- [`open-ai-agent/deer-flow/backend/docs/CONFIGURATION.md`](../../../../open-ai-agent/deer-flow/backend/docs/CONFIGURATION.md)
  `config.yaml` 字段语义、环境变量解析、热加载与 restart-required 边界的权威说明。
- [`open-ai-agent/deer-flow/config.example.yaml`](../../../../open-ai-agent/deer-flow/config.example.yaml)
  主配置模板；`config_version` 与 `make config-upgrade` 的 schema 基准。
- [`open-ai-agent/deer-flow/extensions_config.example.json`](../../../../open-ai-agent/deer-flow/extensions_config.example.json)
  MCP 与 skills 扩展配置模板。
- [`open-ai-agent/deer-flow/Makefile`](../../../../open-ai-agent/deer-flow/Makefile)
  根编排入口：setup、doctor、config、dev/start、docker、up/down。
- [`open-ai-agent/deer-flow/scripts/serve.sh`](../../../../open-ai-agent/deer-flow/scripts/serve.sh)
  本地 dev/prod 统一启动器，被 `make dev` / `make start` 调用。
- [`open-ai-agent/deer-flow/scripts/deploy.sh`](../../../../open-ai-agent/deer-flow/scripts/deploy.sh)
  生产 Docker 构建与启动，被 `make up` / `make down` 调用。
- [`open-ai-agent/deer-flow/docker/docker-compose.yaml`](../../../../open-ai-agent/deer-flow/docker/docker-compose.yaml)
  生产 compose：nginx、frontend、gateway、redis、可选 provisioner。
- [`open-ai-agent/deer-flow/docker/docker-compose-dev.yaml`](../../../../open-ai-agent/deer-flow/docker/docker-compose-dev.yaml)
  开发 compose：热重载 frontend/gateway 与可选 provisioner。
- [`open-ai-agent/deer-flow/backend/pyproject.toml`](../../../../open-ai-agent/deer-flow/backend/pyproject.toml)
  后端 Python 3.12+、`uv` workspace 与可选 extras（postgres、redis 等）。
- [`open-ai-agent/deer-flow/frontend/package.json`](../../../../open-ai-agent/deer-flow/frontend/package.json)
  前端 pnpm 脚本与 Node 22+ 依赖约束。

## 智慧（社区）

- 本轮不引入外部社区。该主题目标是源码考古与本仓库教学产物生成，最可靠的反馈来自在本机执行 `make doctor`、`make check` 和选定部署路径后的健康检查。

## 空白

- 未收录云厂商托管部署（ECS/K8s 裸集群）的运维手册；deer-flow 当前以仓库内 Makefile + compose 为主，云侧差异留给后续部署专题。
- 未展开 `scripts/wizard/` 交互向导的逐步 UI 流程；L1 只点到 `make setup`，细节可在配置专题中补课。

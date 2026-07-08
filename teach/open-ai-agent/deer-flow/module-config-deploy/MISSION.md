# 使命：配置与部署

## 为什么
学习者希望把 deer-flow 从「克隆仓库」到「浏览器能打开 localhost:2026」这条链路讲清楚：配置从哪里来、Makefile 如何编排前后端与 nginx、本地 dev/prod 与 Docker 部署各走哪条脚本。掌握这层后，后续排查「起不来」「端口被占」「配置改了不生效」时能先判断是配置问题还是部署路径问题。

## 成功的样子
- 能说明 `config.yaml` 与 `extensions_config.json` 的分工，以及 `make config` / `make config-upgrade` 各自做什么。
- 能画出 `make dev` 与 `make up` 分别启动哪些服务、统一入口为什么是 nginx:2026。
- 能根据场景选择本地 foreground、daemon 或 Docker dev/prod，并知道 `make doctor` 该何时运行。

## 约束条件
- 本主题是 L1 模块总览，只建立配置与部署边界，不展开 `config.yaml` 每个字段的语义细节。
- 主课控制在 15 分钟内完成；命令清单、环境变量表和 compose 服务表放入 reference。
- 输出使用简体中文；命令、路径和环境变量名保留原始英文。

## 不在范围内
- Gateway 内部 router、agent runtime 和 persistence schema 的实现细节。
- 前端 workspace 页面与 nginx 路由规则的逐行配置解析。
- Kubernetes provisioner 的 Pod 生命周期与 sandbox 内部执行逻辑。

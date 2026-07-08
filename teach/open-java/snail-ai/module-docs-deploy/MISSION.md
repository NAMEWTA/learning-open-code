# 使命：文档与部署模块

## 为什么
学习者需要把 Snail AI 从源码阅读推进到可运行、可验证、可排障的状态。本主题帮助学习者理解文档站、Docker Compose、本地部署、SQL 初始化和 CI 工作流如何共同支撑 Snail AI 的学习、启动与发布。

## 成功的样子
- 能从 VitePress 配置定位文档站导航、侧边栏、主题和构建命令。
- 能说明 `docs/docker/docker-compose.yaml` 中 Server、MySQL、PgVector、Milvus、Elasticsearch、MinIO 的依赖关系。
- 能判断本地启动前应该准备哪个 SQL 脚本、哪些端口和哪些环境变量。
- 能读懂 GitHub Actions 在 tag 推送时如何构建 JAR、Docker 镜像和 Maven 发布产物。
- 能画出 `snail-ai-server` → `snail-ai-server-features` → `snail-ai-feature-common` 的 Maven 模块树，并说明它们如何汇入 `snail-ai-server-exec.jar`。
- 能区分默认 `package` 与 `-P release` 的插件差异，以及何时需要 flatten/GPG/Central 发布链。

## 约束条件
- 本主题是 L1 模块总览，lesson 必须保持 15 分钟内完成。
- 详细文件地图、端口、服务依赖和风险清单放入 `reference/docs-deploy-overview.html`。
- POM 模块树、artifact 坐标与构建插件微观说明放入 `reference/build-modules-api.html`（L3）。
- 只读源项目，不修改 `open-java/snail-ai` 源码。
- 本次任务不更新项目级 `index.md` 或 `_progress.*`。

## 不在范围内
- 不实操启动容器或连接数据库。
- 不展开每张业务表的字段含义，SQL 只讲部署初始化边界。
- 不讲 Server、Agent Client、RAG、模型适配的业务调用链路。

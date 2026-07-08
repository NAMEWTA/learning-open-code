# 文档与部署模块资源

## 知识

- [Snail AI 项目总览](../00-overview/lessons/0001-project-map.html)
  用于确认 Snail AI 的 Server、Agent、模型、RAG、存储和 starter 总体分层。
- [Starter 模块导览](../module-starter/lessons/0001-starter-module-tour.html)
  用于衔接运行时入口、HTTP 端口、gRPC 端口、静态后台和默认配置。
- `open-java/snail-ai/docs/package.json`
  文档站的构建入口，说明 VitePress 脚本、包管理器和 Mermaid/Naive UI 依赖。
- `open-java/snail-ai/docs/.vitepress/config.mts`
  文档站主配置，包含标题、输出目录、静态资源目录、Mermaid 插件、搜索、导航和侧边栏挂载。
- `open-java/snail-ai/docs/.vitepress/config/nav.ts`
  顶部导航结构，部署运维入口从这里进入。
- `open-java/snail-ai/docs/.vitepress/config/sidebar.ts`
  侧边栏结构，部署指南、配置参考、升级和故障排除都在 `/deploy/` 分组下。
- `open-java/snail-ai/docs/deploy/docker.md`
  Docker 部署说明；阅读时要和实际 Compose 文件交叉核对，因为文档描述与当前 YAML 存在差异。
- `open-java/snail-ai/docs/deploy/configuration.md`
  后端配置参考，适合对照 `application.yml` 和环境变量覆盖规则。
- `open-java/snail-ai/docs/deploy/production.md`
  生产部署建议，覆盖资源规划、反向代理、JVM、Agent Client、多存储和检查清单。
- `open-java/snail-ai/docs/deploy/troubleshooting.md`
  常见启动、数据库、向量存储、gRPC、模型调用问题的排查入口。
- `open-java/snail-ai/docs/deploy/upgrade.md`
  升级、备份、回滚和验证流程。
- `open-java/snail-ai/docs/docker/docker-compose.yaml`
  当前最可信的 Compose 执行文件，定义 `snail-ai`、MySQL、PgVector、Milvus、Elasticsearch、MinIO、etcd 服务。
- `open-java/snail-ai/docs/sql/snail_ai_schema.sql`
  MySQL 初始化脚本，包含 22 张业务表、默认管理员和测试应用初始化数据。
- `open-java/snail-ai/docs/sql/snail_ai_schema_pgsql.sql`
  PostgreSQL 初始化脚本，表集合与 MySQL 版本一致，并带有注释语句。
- `open-java/snail-ai/docs/sql/snail_ai_schema_dameng.sql`
  达梦初始化脚本；当前文件编码显示为 ISO-8859，使用前需要单独验证编码和执行兼容性。
- `open-java/snail-ai/snail-ai-starter/src/main/resources/application.yml`
  Server 默认运行配置：HTTP、上下文路径、数据库、gRPC、上传目录、MinIO、短期记忆和日志配置。
- `open-java/snail-ai/snail-ai-starter/Dockerfile`
  Docker 镜像运行边界，说明 Java 21 基础镜像、工作目录、JAR 名称、端口和卷。
- `open-java/snail-ai/.github/workflows/docker-image.yml`
  tag 推送触发的 DockerHub 多架构镜像构建与推送流程。
- `open-java/snail-ai/.github/workflows/maven-publish.yml`
  tag 推送触发的 Maven 构建和 Maven Central 发布流程。
- `open-java/snail-ai/pom.xml`
  根 reactor：Java 21、Spring Boot/AI BOM、`dependencyManagement`、`flatten-maven-plugin` 与 `release` profile。
- `open-java/snail-ai/snail-ai-server/pom.xml`
  Server 聚合 pom，列出 persistence、features、admin、openapi 四个子模块。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/pom.xml`
  Feature 聚合 pom，列出 common/model/agent/rag/skill/memory/resource 七个子模块。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-common/pom.xml`
  Feature 公共 jar，依赖 `snail-ai-feature-model` 与 `snail-ai-commons-grpc`。
- `open-java/snail-ai/snail-ai-starter/pom.xml`
  可执行 JAR 边界：`spring-boot-maven-plugin`、`finalName=snail-ai-server`、`classifier=exec`。

## 智慧（社区）

- [Snail AI Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  项目真实协作入口；适用于核对 Issue、提交部署问题和观察部署脚本演进。
- 本地源码评审：`open-java/snail-ai`
  当前课程以工作区实际 checkout 为准；当部署文档与脚本不一致时，优先回到可执行文件和源码配置验证。

## 空白

- 当前未发现专门验证 `docs/docker/docker-compose.yaml` 全量启动链路的自动化测试。
- 当前未发现数据库增量迁移目录；升级已有生产库时不能把初始化脚本直接当迁移脚本使用。
- 当前文档中有多处仍称 Compose 不包含 Server，但当前 YAML 实际包含 `snail-ai` 服务，需要后续跟踪官方修订。

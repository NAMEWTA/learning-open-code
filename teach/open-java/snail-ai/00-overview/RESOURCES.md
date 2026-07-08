# Snail AI 项目总览资源

## 知识

- [README.md](../../../../open-java/snail-ai/README.md)
  项目自述，说明 Snail AI 的一句话定位、核心特性、公开入口和截图。适用于确认本课程的项目边界。
- [根 POM](../../../../open-java/snail-ai/pom.xml)
  Maven 父工程，定义 Java、Spring Boot、Spring AI、依赖版本和顶层模块。适用于技术栈全景和模块分层判断。
- [系统架构总览](../../../../open-java/snail-ai/docs/architecture/overview.md)
  官方架构文档，描述 Server-Agent 架构、请求生命周期、安全边界和存储边界。适用于建立 L0 全局地图。
- [Agent 责任链](../../../../open-java/snail-ai/docs/architecture/agent-chain.md)
  官方链路文档，列出 Server 端 10 个 Handler、Client 端 Advisor 流水线和 gRPC 到 SSE 的桥接。适用于后续 L2 对话链路切片。
- [RAG 流水线](../../../../open-java/snail-ai/docs/architecture/rag-pipeline.md)
  官方 RAG 文档，覆盖文档摄入、去重、分片、向量检索、BM25、融合和重排序。适用于后续 RAG 模块课。
- [记忆架构](../../../../open-java/snail-ai/docs/architecture/memory-architecture.md)
  官方记忆文档，区分短期滑动窗口和长期向量召回。适用于后续记忆模块和对话后抽取切片。
- [核心概念](../../../../open-java/snail-ai/docs/guide/concepts.md)
  术语入口，定义 Agent、RAG、MCP、Skill、Memory、Client、App、Store Instance。适用于统一课程词汇。
- [启动配置](../../../../open-java/snail-ai/snail-ai-starter/src/main/resources/application.yml)
  当前默认 HTTP、gRPC、数据库、资源存储、短期记忆配置。适用于把文档描述落到运行配置。
- [Docker Compose](../../../../open-java/snail-ai/docs/docker/docker-compose.yaml)
  开发依赖编排，包含 MySQL、PgVector、Milvus、Elasticsearch、MinIO 等服务。适用于识别外部基础设施。
- [SQL 初始化脚本](../../../../open-java/snail-ai/docs/sql/)
  MySQL、PostgreSQL 和达梦初始化脚本。适用于后续持久化模块学习。

## 智慧（社区）

- [Snail AI Gitee 仓库](https://gitee.com/aizuda/snail-ai)
  上游主要代码仓库。适用于追踪 issue、变更记录和维护者讨论。
- [Snail AI GitHub 镜像](https://github.com/aizuda/snail-ai)
  README 中指向的 GitHub 入口。适用于无法访问 Gitee 时查看代码和提交历史。
- [Spring AI 项目社区](https://github.com/spring-projects/spring-ai)
  Snail AI 模型调用和 Advisor 机制的重要上游。适用于理解 Spring AI 抽象的设计意图。

## 空白

- 当前仓库测试资源较少，仅发现 2 个测试文件；后续功能课需要更多依赖源码行为和手工链路验证。
- 文档站部分页面标注 Snail AI 0.0.6，而根 POM 当前 `revision` 为 1.0.0；后续课程应以当前源码和 POM 为准，并记录版本差异。
- 前端后台源码不在当前仓库内完整呈现，`snail-ai-starter/src/main/resources/admin/` 主要是构建产物；前端交互只能作为使用入口参考。

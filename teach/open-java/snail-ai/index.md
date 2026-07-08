# Snail AI 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | Snail AI 架构、模块边界与学习路线 |
| 启动与配置模块 | `./module-starter/` | Spring Boot 入口、配置和部署边界 |
| Server API 入口模块 | `./module-server-entry/` | Admin/OpenAPI 控制器、认证与 SSE |
| Agent 责任链模块 | `./module-agent-chain/` | Server 侧 Handler 链与 gRPC 分发 |
| RAG 功能模块 | `./module-rag/` | 文档摄入、检索、融合与重排 |
| 记忆功能模块 | `./module-memory/` | 短期记忆、长期召回与上下文注入 |
| 模型适配层模块 | `./module-models/` | Chat、Embedding、Rerank 适配边界 |
| Agent Client 执行层模块 | `./module-agent-client/` | gRPC Client、Advisor 与工具执行 |
| 持久化与存储适配模块 | `./module-persistence/` | 业务库、向量库和搜索后端适配 |
| Skill 与 MCP 能力模块 | `./module-skill-mcp/` | Skill 编排、MCP 服务与工具解析 |
| 资源管理模块 | `./module-resource/` | 文件上传、资源元数据与访问控制 |
| Commons 与 gRPC 基础模块 | `./module-commons-grpc/` | 公共 DTO、枚举、协议和 RPC 桥接 |
| 文档与部署模块 | `./module-docs-deploy/` | 文档站、部署脚本、SQL 与工作流 |
| Admin 智能体流式对话 | `./slice-admin-agent-chat/` | 管理端 Agent 对话从 HTTP 到 Client 流式响应 |
| OpenAPI 流式对话 | `./slice-openapi-chat/` | OpenAPI 鉴权、请求转换、SSE 聚合与响应 |
| Agent 责任链到 gRPC 分发 | `./slice-agent-chain-grpc/` | Server Handler 链到 Agent Client 的 RPC 分发 |
| RAG 文档上传摄入 | `./slice-rag-ingestion/` | 文档上传、解析、切块、向量化与索引写入 |
| RAG 对话检索注入 | `./slice-rag-retrieval/` | 对话中知识库检索、融合、重排与提示注入 |
| 短期与长期记忆链路 | `./slice-memory-flow/` | 短期历史、长期召回、上下文收集与持久化 |
| 模型配置到运行时调用 | `./slice-model-runtime/` | 模型配置解析、运行时构建、调用与错误边界 |
| MCP 与 Skill 工具注入 | `./slice-mcp-skill-tools/` | Server 描述符到 Client 工具解析与执行 |
| Client Advisor 流式处理 | `./slice-client-advisor-stream/` | Client 端 advisor 链、chunk 转发、thinking 与 usage |
| 存储实例路由 | `./slice-store-instance-routing/` | StoreInstance 配置到向量/搜索后端路由 |
| 资源上传和访问 | `./slice-resource-upload-access/` | 资源上传、存储策略、访问 URL 与权限边界 |
| OpenAPI Client 示例 | `./slice-openapi-client-example/` | 示例客户端、SDK 请求、认证头与 SSE 消费 |

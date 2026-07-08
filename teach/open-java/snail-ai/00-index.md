# Snail AI · 架构教学 Wiki

> 📊 整体进度：36/36 goals · 100% · 已执行 18 轮
> 🕐 最后更新：2026-07-08

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ████████ |
| L1 模块总览 | 12 | 12 | ████████ |
| L2 垂直切片 | 12 | 12 | ████████ |
| L3 微观 API | 11 | 11 | ████████ |
| L4 深度剖析 | 0 | 0 | — |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/0001-project-map.html)** — 15 分钟建立全局地图
- **[📄 项目总览参考](00-overview/reference/00-overview.html)** — 技术栈、模块边界、学习路线

---

## 📦 L1 · 模块总览

### module-starter — 启动与配置
- [📘 模块导览](module-starter/lessons/0001-starter-module-tour.html) · [📄 总览参考](module-starter/reference/starter-overview.html)

### module-server-entry — Server API 入口
- [📘 模块导览](module-server-entry/lessons/0001-server-entry-module-tour.html) · [📄 总览参考](module-server-entry/reference/server-entry-overview.html) · [🔬 API 参考 (L3)](module-server-entry/reference/server-entry-api.html)
- **关联切片**：[Admin 智能体对话](slice-admin-agent-chat/lessons/0001-flow-map.html) · [OpenAPI 流式对话](slice-openapi-chat/lessons/0001-flow-map.html)

### module-agent-chain — Agent 责任链
- [📘 模块导览](module-agent-chain/lessons/0001-agent-chain-module-tour.html) · [📄 总览参考](module-agent-chain/reference/agent-chain-overview.html) · [🔬 API 参考 (L3)](module-agent-chain/reference/agent-chain-api.html)
- **关联切片**：[责任链到 gRPC 分发](slice-agent-chain-grpc/lessons/0001-flow-map.html)

### module-agent-client — Agent Client 执行层
- [📘 模块导览](module-agent-client/lessons/0001-agent-client-module-tour.html) · [📄 总览参考](module-agent-client/reference/agent-client-overview.html) · [🔬 API 参考 (L3)](module-agent-client/reference/agent-client-api.html)
- **关联切片**：[Client Advisor 流式](slice-client-advisor-stream/lessons/0001-flow-map.html) · [OpenAPI Client 示例](slice-openapi-client-example/lessons/0001-flow-map.html)

### module-rag — RAG 功能
- [📘 模块导览](module-rag/lessons/0001-rag-module-tour.html) · [📄 总览参考](module-rag/reference/rag-overview.html) · [🔬 API 参考 (L3)](module-rag/reference/rag-api.html)
- **关联切片**：[文档摄入](slice-rag-ingestion/lessons/0001-flow-map.html) · [对话检索](slice-rag-retrieval/lessons/0001-flow-map.html)

### module-memory — 记忆功能
- [📘 模块导览](module-memory/lessons/0001-memory-module-tour.html) · [📄 总览参考](module-memory/reference/memory-overview.html)
- **关联切片**：[记忆链路](slice-memory-flow/lessons/0001-flow-map.html)

### module-models — 模型适配层
- [📘 模块导览](module-models/lessons/0001-models-module-tour.html) · [📄 总览参考](module-models/reference/models-overview.html) · [🔬 API 参考 (L3)](module-models/reference/models-api.html)
- **关联切片**：[模型运行时](slice-model-runtime/lessons/0001-flow-map.html)

### module-persistence — 持久化与存储
- [📘 模块导览](module-persistence/lessons/0001-persistence-module-tour.html) · [📄 总览参考](module-persistence/reference/persistence-overview.html) · [🔬 API 参考 (L3)](module-persistence/reference/persistence-api.html)
- **关联切片**：[存储实例路由](slice-store-instance-routing/lessons/0001-flow-map.html)

### module-skill-mcp — Skill 与 MCP
- [📘 模块导览](module-skill-mcp/lessons/0001-skill-mcp-module-tour.html) · [📄 总览参考](module-skill-mcp/reference/skill-mcp-overview.html) · [🔬 API 参考 (L3)](module-skill-mcp/reference/skill-mcp-api.html)
- **关联切片**：[MCP/Skill 工具注入](slice-mcp-skill-tools/lessons/0001-flow-map.html)

### module-resource — 资源管理
- [📘 模块导览](module-resource/lessons/0001-resource-module-tour.html) · [📄 总览参考](module-resource/reference/resource-overview.html) · [🔬 API 参考 (L3)](module-resource/reference/resource-api.html)
- **关联切片**：[资源上传访问](slice-resource-upload-access/lessons/0001-flow-map.html)

### module-commons-grpc — Commons 与 gRPC
- [📘 模块导览](module-commons-grpc/lessons/0001-commons-grpc-module-tour.html) · [📄 总览参考](module-commons-grpc/reference/commons-grpc-overview.html) · [🔬 API 参考 (L3)](module-commons-grpc/reference/commons-grpc-api.html) · [🔬 路由策略 (L3)](module-commons-grpc/reference/route-strategy-api.html)

### module-docs-deploy — 文档与部署
- [📘 模块导览](module-docs-deploy/lessons/0001-docs-deploy-module-tour.html) · [📄 总览参考](module-docs-deploy/reference/docs-deploy-overview.html) · [🔬 构建 POM (L3)](module-docs-deploy/reference/build-modules-api.html)

---

## 🔪 L2 · 垂直切片

| 切片 | 入口 | 所属模块 |
|------|------|---------|
| Admin 智能体流式对话 | [链路地图](slice-admin-agent-chat/lessons/0001-flow-map.html) | server-entry · agent-chain · agent-client |
| OpenAPI 流式对话 | [链路地图](slice-openapi-chat/lessons/0001-flow-map.html) | server-entry · agent-chain |
| 责任链到 gRPC 分发 | [链路地图](slice-agent-chain-grpc/lessons/0001-flow-map.html) | agent-chain · commons-grpc · agent-client |
| RAG 文档上传摄入 | [链路地图](slice-rag-ingestion/lessons/0001-flow-map.html) | rag · persistence · resource |
| RAG 对话检索注入 | [链路地图](slice-rag-retrieval/lessons/0001-flow-map.html) | rag · agent-chain |
| 短期与长期记忆链路 | [链路地图](slice-memory-flow/lessons/0001-flow-map.html) | memory · persistence |
| 模型配置到运行时调用 | [链路地图](slice-model-runtime/lessons/0001-flow-map.html) | models · agent-client |
| MCP 与 Skill 工具注入 | [链路地图](slice-mcp-skill-tools/lessons/0001-flow-map.html) | skill-mcp · agent-chain · agent-client |
| Client Advisor 流式处理 | [课程 1](slice-client-advisor-stream/lessons/0001-flow-map.html) · [主路径](slice-client-advisor-stream/lessons/0002-main-path.html) · [异常路径](slice-client-advisor-stream/lessons/0003-error-path.html) | agent-client · commons-grpc |
| 存储实例路由 | [链路地图](slice-store-instance-routing/lessons/0001-flow-map.html) | persistence · server-entry |
| 资源上传和访问 | [链路地图](slice-resource-upload-access/lessons/0001-flow-map.html) | resource · persistence |
| OpenAPI Client 示例 | [链路地图](slice-openapi-client-example/lessons/0001-flow-map.html) | agent-client · server-entry |

---

## 📚 学习路线建议

1. **入门**：`00-overview` → `module-starter` → `module-server-entry`
2. **核心链路**：`slice-admin-agent-chat` → `slice-agent-chain-grpc` → `slice-client-advisor-stream`
3. **RAG 专题**：`module-rag` → `slice-rag-ingestion` → `slice-rag-retrieval`
4. **集成开发**：`module-agent-client` → `slice-openapi-client-example`

---

## 🔗 索引

- [项目教学索引](index.md)
- [机器可读进度](_progress.json)
- [人类可读进度](_progress.md)
- [覆盖率扫描](_coverage_scan.md)

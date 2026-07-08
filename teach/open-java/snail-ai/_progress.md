# Snail AI 教学进度

> 最后更新：2026-07-08T09:40:00+08:00

## 总览

- 进度：**36 / 36 goals（100%）**
- 当前轮次：19（含 L3-rag-api 修复轮）
- 教学根目录：`teach/open-java/snail-ai/`
- 源项目：`open-java/snail-ai`

## 按层级统计

| 层级 | 完成 | 总数 | 状态 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ✅ 已完成 |
| L1 模块总览 | 12 | 12 | ✅ 已完成 |
| L2 垂直切片 | 12 | 12 | ✅ 已完成 |
| L3 微观 API | 11 | 11 | ✅ 已完成 |
| L4 深度剖析 | 0 | 0 | 动态发现（本轮无） |

## 当前队列

**队列为空** — 全部 goal 已完成。

## 审查状态

| 结论 | 数量 |
|------|------|
| 通过 | 36 |

`L3-rag-api` 审查 Important 项已于第 19 轮修复（调用示例、测试验证、RagSearch DTO、异常速查、KnowledgeInfoDTO 更正）。

## 最近完成（本轮）

| Goal | 标题 | 主入口 |
|------|------|--------|
| `L3-server-entry-api` | Server Admin/OpenAPI 对外 API | `module-server-entry/reference/server-entry-api.html` |
| `L3-agent-client-api` | Agent Client 与 OpenAPI SDK API | `module-agent-client/reference/agent-client-api.html` |
| `L3-commons-grpc-api` | Commons 与 gRPC 公共类型 API | `module-commons-grpc/reference/commons-grpc-api.html` |
| `L3-persistence-api` | 持久化 PO/Mapper 与存储 API | `module-persistence/reference/persistence-api.html` |
| `L3-rag-api` | RAG DTO/策略/工具 API | `module-rag/reference/rag-api.html` |
| `L3-models-api` | 模型配置与适配器 API | `module-models/reference/models-api.html` |
| `L3-agent-chain-api` | Agent 责任链回调与边缘 Handler API | `module-agent-chain/reference/agent-chain-api.html` |
| `L3-route-strategy-api` | Client 路由策略 API | `module-commons-grpc/reference/route-strategy-api.html` |
| `L3-docs-deploy-api` | 构建与模块 POM 微观说明 | `module-docs-deploy/reference/build-modules-api.html` |
| `L3-resource-api` | 资源模块构建 API | `module-resource/reference/resource-api.html` |
| `L3-skill-mcp-api` | Skill/MCP 模块构建 API | `module-skill-mcp/reference/skill-mcp-api.html` |

## 产出统计

- 25 个 teach 主题目录
- 27 节短课（含 slice-client-advisor-stream 3 节）
- 30 篇参考文档（含 11 篇 L3 API 参考）
- 全主题 `audit_topic.py --all` 通过

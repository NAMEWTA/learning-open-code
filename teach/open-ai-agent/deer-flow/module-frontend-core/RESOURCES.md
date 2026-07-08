# Frontend core 数据层 资源

## 知识

- 本地源码：`open-ai-agent/deer-flow/frontend/src/core/`
  前端业务数据与 API 适配层总目录。适用于建立 core 域划分与出站通道判断。
- 本地源码：`open-ai-agent/deer-flow/frontend/src/core/api/`
  LangGraph SDK 单例与 REST fetch wrapper。适用于理解 CSRF、401 跳转、stream/cancel/joinStream 兼容包装。
- 本地源码：`open-ai-agent/deer-flow/frontend/src/core/auth/`
  服务端鉴权守卫与客户端 AuthProvider。适用于理解 cookie 会话、setup 分流与静态演示模式。
- 本地源码：`open-ai-agent/deer-flow/frontend/src/core/threads/`
  线程列表、流式提交、历史分页、branch、token usage。适用于追踪聊天主链路。
- 本地源码：`open-ai-agent/deer-flow/frontend/src/core/skills/`、`frontend/src/core/mcp/`、`frontend/src/core/uploads/`
  配置类 REST 域的 api + hooks 样板。适用于对照 settings、agents、scheduled-tasks 等同构模块。
- 本地文档：`open-ai-agent/deer-flow/frontend/AGENTS.md`
  前端架构、Data Flow、Thread hooks 与 Key Patterns 说明。
- [TanStack Query React 文档](https://tanstack.com/query/latest/docs/framework/react/overview)
  useQuery/useMutation 缓存模型。适用于理解 core hooks 的 queryKey 与 invalidate 策略。
- [LangGraph JavaScript SDK Reference](https://reference.langchain.com/javascript/langchain-langgraph-sdk)
  Client、threads、runs API。适用于理解 `getAPIClient()` 包装层为何存在。
- [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
  SSR 与客户端边界。适用于理解 `auth/server.ts` 与 `AuthProvider` 的分工。

## 智慧（社区）

- [bytedance/deer-flow GitHub Issues](https://github.com/bytedance/deer-flow/issues)
  适用于检验对前端 API 层、认证、上传、skills/MCP 配置等真实问题的理解。
- [LangChain Forum](https://forum.langchain.com/)
  适用于讨论 LangGraph SDK streaming、thread state、runs 等生态问题。

## 空白

- DeerFlow 没有独立的前端 core 层架构设计文档；本主题主要依赖 `frontend/AGENTS.md` 与源码。
- skills/MCP 的后端语义见 module-skills 与 module-tools-mcp；本课只覆盖前端消费侧契约。

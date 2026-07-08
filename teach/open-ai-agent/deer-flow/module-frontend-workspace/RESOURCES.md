# Frontend workspace 资源

## 知识

- 本地源码：`open-ai-agent/deer-flow/frontend/src/app/workspace/`
  workspace 的 Next.js App Router 页面入口。适用于确认路由、layout 包裹关系和每个功能页的入口。
- 本地源码：`open-ai-agent/deer-flow/frontend/src/components/workspace/`
  workspace 专用 UI 组件族。适用于查聊天框、消息列表、侧栏、artifact、sidecar、workspace changes 等体验如何组合。
- 本地源码：`open-ai-agent/deer-flow/frontend/src/core/api/`、`frontend/src/core/threads/`、`frontend/src/core/tasks/`、`frontend/src/core/scheduled-tasks/`、`frontend/src/core/workspace-changes/`
  前端和 Gateway/LangGraph API 的连接层。适用于追踪数据获取、流式提交、缓存失效和任务状态。
- 本地文档：`open-ai-agent/deer-flow/frontend/README.md`
  前端技术栈和目录说明。适用于建立 Next.js、React Query、LangGraph SDK 的基本背景。
- [Next.js 官方文档：Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)
  App Router 的页面、layout、动态段规则。适用于理解 `src/app/workspace/**/page.tsx` 和 `layout.tsx` 为什么就是路由结构。
- [TanStack Query React 文档](https://tanstack.com/query/latest/docs/framework/react/overview)
  React Query 查询、mutation 和缓存模型。适用于理解 `useQuery`、`useInfiniteQuery`、`useMutation` 在 core hooks 中的职责。
- [LangGraph JavaScript SDK Reference](https://reference.langchain.com/javascript/langchain-langgraph-sdk)
  LangGraph SDK 的 Client、threads、runs 能力参考。适用于理解 `getAPIClient()` 包装 SDK 的原因。
- [LangGraph Streaming API 文档](https://docs.langchain.com/langsmith/streaming)
  LangGraph/LangSmith 部署流式运行说明。适用于理解 DeerFlow 前端为什么围绕 thread、run、stream、joinStream 组织聊天状态。

## 智慧（社区）

- [bytedance/deer-flow GitHub Issues](https://github.com/bytedance/deer-flow/issues)
  适用于检验对 DeerFlow 前端行为的理解，尤其是聊天流、侧栏状态、scheduled tasks、agents feature flag 等真实问题。
- [LangChain Forum](https://forum.langchain.com/)
  适用于讨论 LangGraph SDK、thread 历史、streaming、agent server 等生态问题。
- [Next.js GitHub Discussions](https://github.com/vercel/next.js/discussions)
  适用于核对 App Router、Server/Client Components、路由行为的实践问题。

## 空白

- DeerFlow 当前没有独立的前端 workspace 架构设计文档；本主题主要依赖源码和前端 README。
- scheduled tasks 的前端页面实际依赖 `frontend/src/core/scheduled-tasks/`，而任务单只列出 `frontend/src/core/tasks/`；本课同时记录这两个目录的不同职责。

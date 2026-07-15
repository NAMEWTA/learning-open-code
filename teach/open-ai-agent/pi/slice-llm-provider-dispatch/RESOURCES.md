# 多 Provider LLM 统一调度全链路 资源

## 知识

- [Pi Agent Harness 源码 — packages/ai/src/models.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/models.ts)
  Models / Provider 核心接口定义和 createModels / createProvider 工厂函数。适用于：理解 Models 和 Provider 的类型契约、stream / streamSimple 的调度逻辑。

- [Pi Agent Harness 源码 — packages/ai/src/providers/all.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/providers/all.ts)
  builtinModels() 入口和 35 个 Provider 的注册表。适用于：查看 Provider 的全量列表和注册流程。

- [Pi Agent Harness 源码 — packages/ai/src/auth/resolve.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/auth/resolve.ts)
  resolveProviderAuth 认证解析核心逻辑。适用于：理解 API Key / OAuth / Ambient 三种认证路径的优先级和错误处理。

- [Pi Agent Harness 源码 — packages/ai/src/api/lazy.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/api/lazy.ts)
  lazyStream 和 lazyApi 的懒加载+流包装机制。适用于：理解同步返回流、异步初始化的实现原理。

- [Pi Agent Harness 源码 — packages/ai/src/providers/openai.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/providers/openai.ts)
  OpenAI Provider 作为 Provider 工厂的典型范例，展示 envApiKeyAuth + lazyApi 的组合模式。

- [Pi Agent Harness 源码 — packages/ai/src/providers/anthropic.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/providers/anthropic.ts)
  Anthropic Provider 演示了双认证（envApiKeyAuth + lazyOAuth）的 Provider 写法，是最复杂的认证配置案例。

- [文章：Lazy Loading in TypeScript — Dynamic import() 模式](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
  动态 import() 的基础知识。适用于：理解 lazyApi 中的 `() => import("./openai-completions.ts")` 为什么能实现按需加载。

## 智慧（社区）

- [Pi GitHub Discussions](https://github.com/earendil-works/pi/discussions)
  Pi 项目的官方讨论区，适用于：提问 Provider 适配问题、了解社区自定义 Provider 的最佳实践。

- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)
  本地 LLM 部署与 API 兼容性讨论的活跃社区，适用于：了解如何为本地模型（Ollama/LM Studio 等）编写自定义 Provider。

## 空白

- 缺少面向初学者的 TypeScript async generator / AsyncIterable 深入教程（lazyStream 依赖这些概念）
- 缺少 OAuth 2.0 token refresh 的 Pi 项目特有实现文档（目前仅能从源码推断）
- 缺少 Provider 开发的官方 step-by-step 指南（仅有源码中的 Provider 工厂示例）

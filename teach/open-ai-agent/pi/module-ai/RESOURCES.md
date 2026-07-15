# pi-ai 模块资源

## 知识

- [Pi GitHub 仓库 — packages/ai/](https://github.com/earendil-works/pi/tree/main/packages/ai)
  pi-ai 源码目录，包含 README.md、package.json、src/ 全部源码。适用于：了解包结构、入口文件、构建脚本。

- [package.json — @earendil-works/pi-ai](https://github.com/earendil-works/pi/blob/main/packages/ai/package.json)
  包元数据、exports 子路径定义、bin 命令、dependencies 列表。适用于：确认对外暴露的接口和外部依赖版本。

- [src/index.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/index.ts)
  主入口文件，重导出各子模块的类型和函数。适用于：快速了解 pi-ai 的公共 API 全貌。

- [src/providers/all.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/providers/all.ts)
  所有内置 Provider 的工厂函数集合，`builtinProviders()` 返回完整的 Provider 列表。适用于：理解 Provider 注册机制。

- [src/models.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/models.ts)
  `Provider` 和 `Models` 接口定义。适用于：理解 Provider 如何声明模型、认证和流式调用。

- [src/api/lazy.ts](https://github.com/earendil-works/pi/blob/main/packages/ai/src/api/lazy.ts)
  延迟加载 API 实现的核心工具。适用于：理解为何 pi-ai 可以同时支持 9 种 API 而不造成启动时加载负担。

- [OpenAI Node.js SDK 文档](https://github.com/openai/openai-node)
  pi-ai 的 `openai` 依赖来源。适用于：对比 pi-ai 的抽象层与原生 SDK 的差异。

- [Anthropic SDK 文档](https://docs.anthropic.com/en/api/client-sdks)
  pi-ai 的 `@anthropic-ai/sdk` 依赖来源。

## 智慧（社区）

- [Pi GitHub Issues](https://github.com/earendil-works/pi/issues)
  Pi 项目的 issue 跟踪，可以在其中搜索 pi-ai 相关问题或参与讨论。

- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)
  Reddit 上的本地 LLM 社区，讨论各种 LLM API 调用、Provider 适配等话题。适用于：了解社区对各种 LLM Provider 的实践经验和问题。

## 空白

- pi-ai 目前没有独立的官方文档站点，所有文档在 Pi monorepo 根目录的 README.md 和 AGENTS.md 中。
- 社区中没有 pi-ai 的专门学习资源或教程，学习完全依赖源码阅读。

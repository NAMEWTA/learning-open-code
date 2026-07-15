# Agent Hook 生命周期全链路 资源

## 知识

- [packages/coding-agent/src/core/extensions/types.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/extensions/types.ts) — ExtensionEvent 联合类型（31 种事件）、ExtensionAPI.on() 重载签名、ExtensionHandler 泛型、各事件 Result 类型。适用于：查阅完整的 Hook 事件契约。
- [packages/coding-agent/src/core/extensions/loader.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/extensions/loader.ts) — 扩展模块加载（jiti 引擎）、createExtensionAPI() 实现 api.on() 注册、ExtensionRuntime 创建。适用于：理解 Hook 注册的机制和时序。
- [packages/coding-agent/src/core/extensions/runner.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/extensions/runner.ts) — ExtensionRunner 类、emit() 通用分发、6 种专用 emit 方法（emitContext/emitToolCall/emitToolResult/emitMessageEnd/emitBeforeProviderRequest/emitBeforeAgentStart）、session_before_* 提前取消。适用于：追踪 Hook 事件触发的完整执行流程。
- [packages/coding-agent/docs/extensions.md](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md) — 扩展系统官方文档（103KB），包含 Hook 使用示例和事件分类说明。适用于：了解官方推荐的 Hook 使用模式。
- [packages/coding-agent/examples/extensions/](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions) — 官方扩展示例集（60+ 个示例）。适用于：通过实例学习各类 Hook 的实际用法。

## 智慧（社区）

- [Pi Discord](https://discord.com/invite/3cU7Bz4UPx) — 官方 Discord 社区。适用于：扩展开发问题、Hook 使用经验交流。

## 空白

- 目前未发现 Pi Hook 系统的第三方中文深度分析文章。本课程基于源码分析产出。
- 官方扩展文档（extensions.md）中对 Hook 执行时序的描述较简略，runner.ts 的源码分析是本课程的主要知识来源。

# 工具执行全链路 资源

## 知识

- [packages/coding-agent/src/core/tools/index.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/tools/index.ts) — ToolName 类型定义（7 个工具名）、createTool/createToolDefinition 工厂函数、createAllToolDefinitions 等聚合方法。适用于：理解工具的注册入口和分组策略（coding/readOnly/all）。
- [packages/coding-agent/src/core/tools/tool-definition-wrapper.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/tools/tool-definition-wrapper.ts) — ToolDefinition → AgentTool 的适配层，桥接扩展系统的 ExtensionContext 到 Agent 运行时的 AgentTool 接口。适用于：理解扩展工具与内置工具的统一包装机制。
- [packages/coding-agent/src/core/extensions/wrapper.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/extensions/wrapper.ts) — 扩展注册工具的包装器，wrapRegisteredTool/wrapRegisteredTools 为扩展工具注入 Runner 上下文。适用于：理解扩展工具如何接入 Agent 运行时。
- [packages/coding-agent/src/core/agent-session.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/agent-session.ts) — AgentSession 类：_buildRuntime（L2284-2429）创建工具定义并构建扩展运行时；_refreshToolRegistry（L2338-2429）三层工具注册与激活；_installAgentToolHooks（L419-467）安装 beforeToolCall/afterToolCall 拦截钩子。适用于：理解工具从定义到激活的完整生命周期。
- [packages/coding-agent/src/core/tools/bash.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/tools/bash.ts) — bash 工具：BashOperations 可插拔接口、createLocalBashOperations 本地执行器、streaming output 与截断、超时与 abort 处理。适用于：理解命令执行工具的实现模式。
- [packages/coding-agent/src/core/tools/read.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/tools/read.ts) — read 工具：ReadOperations 可插拔接口、文本/图片双模式读取、offset/limit 分页、truncateHead 输出截断。适用于：理解文件读取工具的实现模式。
- [packages/coding-agent/src/core/tools/write.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/tools/write.ts) — write 工具：WriteOperations 可插拔接口、file-mutation-queue 串行化写操作、增量语法高亮缓存。适用于：理解文件写入工具的实现模式。
- [packages/coding-agent/src/core/tools/edit.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/tools/edit.ts) — edit 工具：EditOperations 可插拔接口、多编辑块精确替换、diff 预览与补丁生成、BOM/行尾规范化。适用于：理解文件编辑工具的实现模式。
- [packages/coding-agent/src/core/tools/file-mutation-queue.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/tools/file-mutation-queue.ts) — 文件变更串行队列，保证同一文件的 write/edit 操作不会并发执行。适用于：理解文件操作的安全保证机制。
- [packages/coding-agent/src/core/tools/truncate.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/tools/truncate.ts) — 输出截断工具：truncateHead/truncateTail/truncateLine 三种策略，支持行数+字节数双重限制。适用于：理解工具输出的安全截断机制。
- [packages/agent/src/agent-loop.ts](https://github.com/earendil-works/pi/blob/main/packages/agent/src/agent-loop.ts) — executeToolCalls / prepareToolCall 工具调用管线，包含参数校验、beforeToolCall/afterToolCall 钩子、异常转为 ToolResultMessage 的安全保证。适用于：理解工具执行的调度层。

## 智慧（社区）

- [Pi Discord](https://discord.com/invite/3cU7Bz4UPx) — 官方 Discord 社区。适用于：自定义工具开发、权限模型设计等高级话题讨论。

## 空白

- 目前未发现关于 Pi 工具系统内部实现的第三方深度分析文章。后续可通过阅读源码产出。
- Anthropic 官方的 tool use 最佳实践文档可作为对比参考，但不是 Pi 特定的。

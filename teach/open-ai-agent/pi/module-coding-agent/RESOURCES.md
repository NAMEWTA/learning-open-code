# pi-coding-agent 模块总览 资源

## 知识

- [packages/coding-agent/package.json](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/package.json) — 包元数据、bin 入口（`pi`）、内部依赖（pi-ai/pi-agent-core/pi-tui）、exports 定义。适用于：了解包的对外接口和依赖关系。
- [packages/coding-agent/src/index.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/index.ts) — 模块主入口，聚合所有公开 API 的 re-export。适用于：了解包的完整公开接口清单。
- [packages/coding-agent/src/cli.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/cli.ts) — CLI 入口文件（`#!/usr/bin/env node`），配置全局 dispatcher 后调用 main()。适用于：追踪 CLI 启动流程的起点。
- [packages/coding-agent/src/cli/args.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/cli/args.ts) — 命令行参数解析，定义所有支持的 flag（provider/model/mode/session/extensions 等）。适用于：了解 CLI 的完整参数清单。
- [packages/coding-agent/src/main.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/main.ts) — 主流程编排，连接参数解析、会话管理、扩展加载、启动模式。适用于：理解 CLI 启动到 Agent 就绪的完整链路。
- [packages/coding-agent/src/rpc-entry.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/rpc-entry.ts) — RPC 服务入口，以 --mode rpc 启动 main()。适用于：了解 Pi 的无头服务器模式。
- [packages/coding-agent/src/core/extensions/types.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/extensions/types.ts) — 扩展系统的类型定义，包含 Extension、ExtensionAPI、Hook 事件等核心类型。适用于：了解扩展系统的契约层。
- [packages/coding-agent/docs/extensions.md](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md) — 扩展系统官方文档（103KB）。适用于：深入理解扩展的注册、Hook、组件和加载机制。
- [packages/coding-agent/docs/sdk.md](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sdk.md) — 编程式 SDK 使用文档。适用于：了解如何以 SDK 方式嵌入 Pi。
- [packages/coding-agent/examples/extensions/](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions) — 官方扩展示例集（60+ 个示例）。适用于：通过实例学习扩展系统的各项能力。
- [Pi 官方网站 (pi.dev)](https://pi.dev) — 项目官网。适用于：了解 Pi 的功能定位与使用方式。

## 智慧（社区）

- [Pi Discord](https://discord.com/invite/3cU7Bz4UPx) — 官方 Discord 社区。适用于：扩展开发、自定义 Provider 等高级话题讨论。

## 空白

- 目前未发现 pi-coding-agent 的第三方中文深度分析文章。后续可通过阅读源码产出。
- 官方扩展文档（extensions.md）内容庞大（103KB），建议后续拆分为多节 slice 课程逐步覆盖。

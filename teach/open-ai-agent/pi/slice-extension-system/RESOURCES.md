# 扩展系统 资源

## 知识

- [Pi 源码 - extensions/types.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/extensions/types.ts) — 扩展系统全部类型定义（55KB），包含 ExtensionAPI、ExtensionContext、所有事件类型与结果类型
- [Pi 源码 - extensions/loader.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/extensions/loader.ts) — 扩展发现与加载实现，含 jiti 运行时加载、缓存机制、三层发现规则
- [Pi 源码 - extensions/runner.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/extensions/runner.ts) — 扩展运行时调度，ExtensionRunner 类含事件分发、上下文创建、生命周期管理
- [Pi 源码 - extensions/wrapper.ts](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/extensions/wrapper.ts) — 扩展工具包装器，将 RegisteredTool 转为 AgentTool
- [Pi 扩展示例目录](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions) — 80+ 个扩展示例文件，覆盖 Hook、工具、Provider、UI 等全部能力
- [Pi 扩展 README](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/examples/extensions/README.md) — 扩展开发官方指南

## 智慧（社区）

- [Pi Discord](https://discord.gg/pi) — Pi 官方社区，可讨论扩展开发、提交 PR
- [Pi GitHub Issues](https://github.com/earendil-works/pi/issues) — 报告扩展相关 bug 或提交功能请求

## 空白

- 扩展系统的性能分析文档（大规模扩展下的加载耗时、内存占用）尚未找到
- 扩展间通信（EventBus）的最佳实践文档缺失，仅能从 `event-bus.ts` 源码推断

# 课程快照：slice-extension-system

## 源项目信息
- **源仓库**：`open-ai-agent/pi`
  - **Git Commit**：`8479bd84743e8889f728acb21a62794102db0529`
  - **短 Commit**：`8479bd8`
  - **分支**：`main`
- **快照时间**：2026-07-15T12:00:00+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/coding-agent/src/core/extensions/types.ts` | 全部类型定义——ExtensionAPI、ExtensionContext、Extension、所有事件类型与结果类型、ToolDefinition | 🔴 核心 |
| `packages/coding-agent/src/core/extensions/loader.ts` | 扩展发现与加载——jiti 编译、virtualModules/aliases、三层发现规则、缓存机制 | 🔴 核心 |
| `packages/coding-agent/src/core/extensions/runner.ts` | 扩展运行时调度——ExtensionRunner 类、事件分发、context 创建、stale 检测 | 🔴 核心 |
| `packages/coding-agent/src/core/extensions/wrapper.ts` | 工具包装器——RegisteredTool → AgentTool 转换、动态工具发现 | 🔴 核心 |
| `packages/coding-agent/src/core/extensions/index.ts` | 扩展模块导出聚合——所有公开 API 的 re-export | 🟡 辅助 |
| `packages/coding-agent/src/core/event-bus.ts` | 扩展间通信事件总线——基于 Node.js EventEmitter | 🟡 辅助 |
| `packages/coding-agent/examples/extensions/hello.ts` | 最小自定义工具示例——ToolDefinition 基础用法 | 🟡 辅助 |
| `packages/coding-agent/examples/extensions/git-checkpoint.ts` | Git 检查点扩展——事件订阅 + exec 的实战模式 | 🟡 辅助 |
| `packages/coding-agent/examples/extensions/todo.ts` | 状态管理扩展示例——session entry 持久化 + 自定义 UI 组件 | 🟡 辅助 |
| `packages/coding-agent/docs/extensions.md` | 扩展系统官方文档——使用指南与 API 参考 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | `lessons/0001-flow-map.html` | 扩展系统加载与执行全链路——六阶段时序图与发现规则 |
| 02 | `lessons/0002-architecture-runtime.html` | 三层架构与共享运行时——Loader/Runner/Wrapper 分离的设计动机与两阶段初始化 |
| 03 | `lessons/0003-event-interception.html` | 事件系统的拦截链设计——7 种分发策略、链式替换、短路取消、错误隔离 |
| 04 | `lessons/0004-module-loading.html` | 扩展模块动态加载机制——jiti、virtualModules vs aliases、缓存策略 |
| 05 | `lessons/0005-tool-pipeline.html` | 工具注册与包装管线——ToolDefinition → RegisteredTool → AgentTool 三阶段转换 |

## 快照摘要
- 课程数：5
- 引用源文件数：10
- 学习记录数：0
- 参考资料数：0
- 资产文件数：0

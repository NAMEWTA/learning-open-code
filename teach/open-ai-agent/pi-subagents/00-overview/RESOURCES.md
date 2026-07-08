# pi-subagents 项目整体架构资源

## 知识

- [本地 README：`open-ai-agent/pi-subagents/README.md`](../../../../open-ai-agent/pi-subagents/README.md)
  项目定位、安装方式、自然语言工作流、前台/后台运行、状态文件、RPC、intercom、配置和运行时文件清单的主来源。
- [本地包清单：`open-ai-agent/pi-subagents/package.json`](../../../../open-ai-agent/pi-subagents/package.json)
  npm 发布元数据、Pi extension 入口、skill/prompt 暴露方式、运行依赖和测试脚本的权威来源。
- [扩展入口：`open-ai-agent/pi-subagents/src/extension/index.ts`](../../../../open-ai-agent/pi-subagents/src/extension/index.ts)
  观察工具注册、wait tool、slash bridge、RPC bridge、async tracker、result watcher、native supervisor channel 和 session 生命周期绑定。
- [执行入口：`open-ai-agent/pi-subagents/src/runs/foreground/subagent-executor.ts`](../../../../open-ai-agent/pi-subagents/src/runs/foreground/subagent-executor.ts)
  单次、并行、链式、管理、status、interrupt、resume、async 分流的核心调度文件。
- [测试目录：`open-ai-agent/pi-subagents/test/unit/` 与 `open-ai-agent/pi-subagents/test/integration/`](../../../../open-ai-agent/pi-subagents/test)
  用于校验导览中的行为边界，尤其是 agent discovery、schema、slash、async、intercom、chain、parallel 和 status。

## 智慧（社区）

- [GitHub 仓库：nicobailon/pi-subagents](https://github.com/nicobailon/pi-subagents)
  适用于核对 issue、release、README 与真实使用反馈；本 L0 课程以本地子模块快照为准。
- [Pi extension 使用者反馈渠道：GitHub Issues](https://github.com/nicobailon/pi-subagents/issues)
  适用于验证后续 L1/L2 主题中的设计取舍是否来自实际用户问题，例如 async 可观测性、模型覆盖、intercom 协调。

## 空白

- 当前未找到独立第三方的深度源码解读文章；后续深入某个模块时应优先补充来自 issue、PR 或 release discussion 的真实设计背景。

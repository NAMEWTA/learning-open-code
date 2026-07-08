# 共享类型、状态与文件基础设施模块资源

## 知识

- [L0 项目整体架构与学习地图](../00-overview/lessons/0001-project-map.html)
  前置课程，说明 `artifacts/status outputs` 为什么是 async 可观测性的基础。
- [L0 总览参考图谱](../00-overview/reference/00-overview.html)
  提供 `src/shared` 与 extension、runs、slash、intercom、TUI 的整体位置关系。
- [`src/shared/types.ts`](../../../../open-ai-agent/pi-subagents/src/shared/types.ts)
  核心契约来源；适用于查 `Details`、`SingleResult`、`AsyncStatus`、事件名、临时目录和 action 列表。
- [`src/shared/artifacts.ts`](../../../../open-ai-agent/pi-subagents/src/shared/artifacts.ts)
  artifacts、project-local `.pi-subagents` 路径和清理策略的主要来源。
- [`src/shared/atomic-json.ts`](../../../../open-ai-agent/pi-subagents/src/shared/atomic-json.ts)
  状态 JSON 原子写入、临时文件重命名和 Windows rename retry 的行为来源。
- [`src/shared/jsonl-writer.ts`](../../../../open-ai-agent/pi-subagents/src/shared/jsonl-writer.ts)
  events JSONL 追加、背压暂停/恢复和文件大小上限的行为来源。
- [`src/shared/settings.ts`](../../../../open-ai-agent/pi-subagents/src/shared/settings.ts)
  chain step 类型、输出/读取/progress 行为、并行输出命名空间和只读任务抑制的来源。
- [`src/shared/fork-context.ts`](../../../../open-ai-agent/pi-subagents/src/shared/fork-context.ts)
  fork session 创建、unsafe thinking block 清理和 thinking override 的来源。
- [`test/unit/artifacts.test.ts`](../../../../open-ai-agent/pi-subagents/test/unit/artifacts.test.ts)、[`test/unit/atomic-json.test.ts`](../../../../open-ai-agent/pi-subagents/test/unit/atomic-json.test.ts)、[`test/unit/jsonl-writer.test.ts`](../../../../open-ai-agent/pi-subagents/test/unit/jsonl-writer.test.ts)、[`test/unit/status-format.test.ts`](../../../../open-ai-agent/pi-subagents/test/unit/status-format.test.ts)
  本主题的核心测试证据，覆盖路径、原子写入、JSONL 写入和状态格式化。

## 智慧（社区）

- [pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues)
  适用于核对真实用户在 async 状态、artifact 路径、后台恢复和模型选择上的使用问题。
- 本地源码测试反馈循环：`node --experimental-strip-types --test test/unit/artifacts.test.ts test/unit/atomic-json.test.ts test/unit/jsonl-writer.test.ts test/unit/status-format.test.ts`
  适用于修改共享基础设施后验证行为边界；本轮已运行该精确命令，结果为 4 个 suite、14 个测试通过。

## 空白

- 本主题未纳入独立的外部架构文章；当前知识依据为源码、测试和 L0 课程。
- Pi runtime 内部 session 格式只在本项目使用处做必要解释；如后续深入 fork/session 机制，需要补充 `@earendil-works/pi-coding-agent` 相关源码或官方说明。

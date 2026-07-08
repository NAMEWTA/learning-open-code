# parallel 与 chain execution 资源

## 知识

- [pi-subagents README](https://github.com/nicobailon/pi-subagents/blob/main/README.md) — 官方对 chain、parallel、background 的用户面说明与示例 prompt
- `open-ai-agent/pi-subagents/src/runs/foreground/chain-execution.ts` — `executeChain` 主循环与 `runParallelChainTasks`
- `open-ai-agent/pi-subagents/src/runs/shared/dynamic-fanout.ts` — expand / materialize / collect 动态扇出
- `open-ai-agent/pi-subagents/src/runs/shared/workflow-graph.ts` — `buildWorkflowGraphSnapshot` 图快照
- `open-ai-agent/pi-subagents/src/shared/settings.ts` — `ChainStep` 类型、`isParallelStep` / `isDynamicParallelStep`、`resolveChainTemplates`
- `open-ai-agent/pi-subagents/test/integration/parallel-execution.test.ts` — `mapConcurrent` 与 top-level parallel 行为
- `open-ai-agent/pi-subagents/test/integration/chain-execution.test.ts` — 顺序链、`{previous}`、parallel step、dynamic fanout、workflowGraph

## 智慧（社区）

- [pi-subagents Issues](https://github.com/nicobailon/pi-subagents/issues) — 链式工作流、并发与 fanout 的实战问题与维护者回复
- [Pi coding agent 生态](https://github.com/earendil-works) — extension 与 subagent 工具链的上下游讨论场

## 空白

- 暂无独立的 chain / fanout 官方设计文档；行为以源码与 integration test 为准
- 中文社区案例较少，复杂 workflow 配置建议对照本主题 `reference/parallel-chain-overview.html` 与测试用例

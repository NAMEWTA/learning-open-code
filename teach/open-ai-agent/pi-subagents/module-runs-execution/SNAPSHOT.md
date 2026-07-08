# 课程快照：module-runs-execution

## 源项目信息
- **源仓库**：`open-ai-agent/pi-subagents`
  - **Git Commit**：`3ccb5645000709fc7856b1a9e3048009f19afaaf`
  - **短 Commit**：`3ccb564`
  - **分支**：`main`
- **快照时间**：2026-07-08T10:09:22+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `agents/chain-serializer.ts` | 课程分析引用 | 🟡 辅助 |
| `background/chain-root-attachment.ts` | 课程分析引用 | 🟡 辅助 |
| `background/completion-batcher.ts` | 课程分析引用 | 🟡 辅助 |
| `background/completion-dedupe.ts` | 课程分析引用 | 🟡 辅助 |
| `background/notify.ts` | 课程分析引用 | 🟡 辅助 |
| `background/parallel-groups.ts` | 课程分析引用 | 🟡 辅助 |
| `extension/fanout-child.ts` | 课程分析引用 | 🟡 辅助 |
| `mcp-cache.json` | 课程分析引用 | 🟡 辅助 |
| `mcp.json` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/agents/*.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/extension/index.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/extension/schemas.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/intercom/*.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/async-execution.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/async-job-tracker.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/async-resume.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/async-status.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/chain-append.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/control-channel.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/fleet-view.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/result-watcher.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/run-id-resolver.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/run-status.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/scheduled-runs.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/stale-run-reconciler.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/subagent-runner.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/top-level-async.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/background/wait.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/foreground/chain-clarify.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/foreground/chain-execution.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/foreground/execution.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/foreground/subagent-executor.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/*.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/chain-outputs.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/model-fallback.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/model-scope.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/parallel-utils.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/subagent-control.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/subagent-prompt-runtime.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/tool-budget.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/turn-budget.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/workflow-graph.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/runs/shared/worktree.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/shared/artifacts.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/shared/types.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/src/slash/*.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/test/integration/async-execution.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/test/integration/chain-execution.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/test/integration/parallel-execution.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi-subagents/test/integration/single-execution.test.ts` | 课程分析引用 | 🟡 辅助 |
| `output.json` | 课程分析引用 | 🟡 辅助 |
| `shared/acceptance.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/completion-guard.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/dynamic-fanout.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/long-running-guard.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/mcp-direct-tool-allowlist.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/nested-events.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/nested-path.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/nested-render.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/pi-args.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/run-history.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/single-output.ts` | 课程分析引用 | 🟡 辅助 |
| `shared/structured-output.ts` | 课程分析引用 | 🟡 辅助 |
| `slash/slash-commands.ts` | 课程分析引用 | 🟡 辅助 |
| `status.json` | 课程分析引用 | 🟡 辅助 |
| `test/integration/result-watcher.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/acceptance.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/chain-root-attachment.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/completion-batcher.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/completion-dedupe.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/completion-guard.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/nested-control.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/nested-events.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/notify.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/pi-args.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/pi-coding-agent-dir.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/single-output.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/subagent-control.test.ts` | 课程分析引用 | 🟡 辅助 |
| `test/unit/subagent-prompt-runtime.test.ts` | 课程分析引用 | 🟡 辅助 |
| `tui/render.ts` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-runs-execution-module-tour | `lessons/0001-runs-execution-module-tour.html` | 0001 runs 执行模块边界导览 |

## 参考资料

- `reference/runs-execution-api.html` — runs execution API 参考（L3）
- `reference/runs-execution-overview.html` — runs execution overview

## 快照摘要
- 课程数：1
- 引用源文件数：81
- 学习记录数：0
- 参考资料数：2
- 资产文件数：0

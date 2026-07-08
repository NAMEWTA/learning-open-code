# 课程快照：slice-context-compaction-flow

## 源项目信息
- **源仓库**：`open-ai-agent/pi`
  - **Git Commit**：`2e4ad6a09423002f58b9a5dc2749f7db7929d0f0`
  - **短 Commit**：`2e4ad6a`
  - **分支**：`main`
- **快照时间**：2026-07-07T16:25:11+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `open-ai-agent/pi/.github/workflows/approve-contributor.yml` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/.github/workflows/build-binaries.yml` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/.github/workflows/ci.yml` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/.github/workflows/issue-analysis.yml` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/.github/workflows/issue-gate.yml` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/.github/workflows/issue-triage-labels.yml` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/.github/workflows/npm-audit.yml` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/.github/workflows/pr-gate.yml` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/.github/workflows/remove-inprogress-on-close.yml` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/src/harness/compaction/branch-summarization.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/src/harness/compaction/compaction.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/src/harness/compaction/utils.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/test/harness/compaction.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/ai/src/auth/context.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/ai/src/utils/overflow.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/ai/test/context-overflow.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/ai/test/overflow.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/docs/compaction.md` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/examples/extensions/custom-compaction.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/examples/sdk/07-context-files.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/compaction/branch-summarization.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/compaction/compaction.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/compaction/index.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/compaction/utils.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/modes/interactive/components/compaction-summary-message.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-auto-compaction-queue.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-compaction.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/compaction-extensions-example.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/compaction-extensions.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/compaction-serialization.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/compaction-summary-reasoning.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/compaction.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/interactive-mode-compaction.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/session-manager/build-context.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/suite/agent-session-compaction.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/suite/regressions/2860-replaced-session-context.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/suite/regressions/5217-compaction-reason.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/suite/regressions/pre-prompt-compaction-no-continue.test.ts` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-flow-map | `lessons/0001-flow-map.html` | 上下文压缩全链路 · 短课 |

## 参考资料

- `reference/context-compaction-flow-flow-map.html` — 上下文压缩全链路 流程速查

## 快照摘要
- 课程数：1
- 引用源文件数：38
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0

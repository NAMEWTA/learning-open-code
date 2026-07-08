# 课程快照：deep-dive-agent-session-arch

## 源项目信息
- **源仓库**：`open-ai-agent/pi`
  - **Git Commit**：`2e4ad6a09423002f58b9a5dc2749f7db7929d0f0`
  - **短 Commit**：`2e4ad6a`
  - **分支**：`main`
- **快照时间**：2026-07-07T16:25:11+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `open-ai-agent/pi/packages/agent/src/harness/session/jsonl-repo.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/src/harness/session/jsonl-storage.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/src/harness/session/memory-repo.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/src/harness/session/memory-storage.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/src/harness/session/repo-utils.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/src/harness/session/session.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/src/harness/session/uuid.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/test/harness/session-test-utils.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/test/harness/session-uuid.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/agent/test/harness/session.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/ai/src/session-resources.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/docs/session-format.md` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/docs/sessions.md` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/examples/extensions/session-name.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/examples/sdk/11-sessions.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/examples/sdk/13-session-runtime.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/cli/session-picker.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/agent-session-runtime.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/agent-session-services.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/agent-session.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/session-cwd.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/session-manager.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/modes/interactive/components/session-selector-search.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/modes/interactive/components/session-selector.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/modes/interactive/model-search.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-auto-compaction-queue.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-branching.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-compaction.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-concurrent.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-dynamic-provider.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-dynamic-tools.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-retry.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-runtime-events.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-stats.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/agent-session-tree-navigation.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/sdk-session-manager.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/session-cwd.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/session-file-invalid.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/session-selector-search.test.ts` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-problem-frame | `lessons/0001-problem-frame.html` | AgentSession 架构深度剖析 · 短课 |

## 参考资料

- `reference/agent-session-arch-notes.html` — AgentSession 架构深度剖析 深度笔记

## 快照摘要
- 课程数：1
- 引用源文件数：39
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0

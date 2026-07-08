# Slash 命令与 prompt workflow 模块资源

## 知识

- `open-ai-agent/pi-subagents/src/slash/slash-commands.ts`
  slash 命令注册、参数解析、`runSlashSubagent`、live card 初始消息、事件请求和最终结果回写的主入口。
- `open-ai-agent/pi-subagents/src/slash/prompt-workflows.ts`
  prompt workflow 的发现目录、frontmatter 解析、参数替换、运行时选项和 `/prompt-workflow`、`/chain-prompts` 注册。
- `open-ai-agent/pi-subagents/src/slash/slash-bridge.ts`
  `subagent:slash:*` 事件桥，负责把 slash 请求交给 executor，并处理 started、update、response、cancel。
- `open-ai-agent/pi-subagents/src/slash/slash-live-state.ts`
  single、parallel、chain 初始结果、进度更新、最终快照、恢复快照的状态模型。
- `open-ai-agent/pi-subagents/src/slash/prompt-template-bridge.ts`
  `prompt-template:subagent:*` 事件桥，服务 prompt template 委派，支持单任务与 tasks 并行 payload。
- `open-ai-agent/pi-subagents/prompts/gather-context-and-clarify.md`
  内置 prompt workflow 示例：先用 subagent 收集上下文，再向用户提问。
- `open-ai-agent/pi-subagents/prompts/parallel-cleanup.md`
  内置 prompt workflow 示例：并行 cleanup review，展示模板如何把 `$@` 作为用户补充范围。
- `open-ai-agent/pi-subagents/prompts/parallel-context-build.md`
  内置 prompt workflow 示例：并行 context-builder 输出 handoff 上下文。
- `open-ai-agent/pi-subagents/prompts/parallel-handoff-plan.md`
  内置 prompt workflow 示例：研究、代码上下文和综合计划的 chain 式 handoff。
- `open-ai-agent/pi-subagents/prompts/parallel-research.md`
  内置 prompt workflow 示例：并行 researcher/scout 调研。
- `open-ai-agent/pi-subagents/prompts/parallel-review.md`
  内置 prompt workflow 示例：并行 reviewer 审查当前工作。
- `open-ai-agent/pi-subagents/prompts/review-loop.md`
  内置 prompt workflow 示例：父会话控制 worker/reviewer 循环。
- `open-ai-agent/pi-subagents/src/extension/index.ts`
  扩展入口证据：注册 slash bridge、prompt template bridge，并调用 `registerSlashCommands`。
- `open-ai-agent/pi-subagents/test/unit/prompt-workflows.test.ts`
  验证 prompt 发现优先级、`/prompt-workflow` 参数转换和 `/chain-prompts` 链式参数。
- `open-ai-agent/pi-subagents/test/unit/prompt-template-bridge.test.ts`
  验证 prompt template bridge 的成功、取消、无上下文、tasks 并行结果和缺失结果边界。
- `open-ai-agent/pi-subagents/test/unit/slash-bridge.test.ts`
  验证 slash bridge 优先使用请求携带的 ctx，避免旧 UI context 污染执行。
- `open-ai-agent/pi-subagents/test/integration/slash-live-state.test.ts`
  验证进度流入可渲染快照、长 chain placeholder 和最终快照恢复。
- `open-ai-agent/pi-subagents/test/integration/slash-commands.test.ts`
  验证 `/run`、`/parallel` 等命令的消息投递、参数转发、最终快照和 session 持久化。

## 智慧（社区）

- 本仓库的测试与 review 回路
  适用于检验对 slash workflow 的理解：修改命令解析或模板桥接前，先用相关 unit/integration 测试证明行为边界没有漂移。

## 空白

- 暂未引入外部社区资源；本主题是项目内部源码链路，可信知识优先来自源码、内置 prompt 模板与本仓库测试。

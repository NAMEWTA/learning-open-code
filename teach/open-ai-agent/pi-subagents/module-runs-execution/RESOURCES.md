# 前台、后台与链式运行核心模块资源

## 知识

- `open-ai-agent/pi-subagents/src/runs/foreground/subagent-executor.ts`
  runs 模块的核心调度器。适用于判断 management action、single、parallel、chain 与 async 分流。
- `open-ai-agent/pi-subagents/src/runs/foreground/execution.ts`
  前台 single child Pi 执行器。适用于理解 spawn、JSONL 解析、progress、artifact、timeout、预算与 acceptance 如何汇总到 `SingleResult`。
- `open-ai-agent/pi-subagents/src/runs/foreground/chain-execution.ts`
  前台 chain/parallel group 执行器。适用于理解 `{previous}`、命名输出、dynamic fanout 与 workflow graph。
- `open-ai-agent/pi-subagents/src/runs/background/async-execution.ts`
  async single/chain 的启动层。适用于理解 detached runner config、`jiti`、async dir、started event 与启动提示。
- `open-ai-agent/pi-subagents/src/runs/background/subagent-runner.ts`
  后台 runner 主体。适用于理解 `status.json`、`events.jsonl`、output log、result JSON 的写入时机。
- `open-ai-agent/pi-subagents/src/runs/background/async-job-tracker.ts`
  session 内后台 job map 与 widget 恢复。适用于理解 active jobs 如何恢复和刷新。
- `open-ai-agent/pi-subagents/src/runs/background/run-status.ts`
  status/fleet/transcript 格式化入口。适用于理解 `subagent({ action: "status" })` 对外返回。
- `open-ai-agent/pi-subagents/src/runs/background/wait.ts`
  `wait` 工具实现。适用于理解非交互运行中为何不能靠 sleep/poll 等后台完成。
- `open-ai-agent/pi-subagents/src/runs/background/chain-root-attachment.ts`
  chain step 附着已有 async root 的等待与 result 归一化。适用于理解 `importAsyncRoot` 不重新 spawn 时的轮询与 `ImportedAsyncRootResult`。
- `open-ai-agent/pi-subagents/src/runs/background/completion-batcher.ts`
  后台成功 completion 的智能批处理与 straggler 窗口。适用于理解 sibling job 分组通知与 `completionBatch` 配置。
- `open-ai-agent/pi-subagents/src/runs/background/completion-dedupe.ts`
  completion 事件去重键与 TTL 记忆。适用于理解 notify 与 result-watcher 如何避免重复投递。
- `open-ai-agent/pi-subagents/src/runs/background/notify.ts`
  `SUBAGENT_ASYNC_COMPLETE_EVENT` → Pi `subagent-notify` 消息。适用于理解 extension 注册的后台完成 UI 通知。
- `open-ai-agent/pi-subagents/src/runs/background/parallel-groups.ts`
  async chain 扁平 step 与逻辑 step 索引映射。适用于理解 parallel group 在 status/fleet/TUI 中的步号标注。
- `open-ai-agent/pi-subagents/src/runs/shared/acceptance.ts`
  Acceptance Contract 推断、校验、prompt 注入、report 解析与 `evaluateAcceptance`。适用于理解验收失败如何影响 exit 与 ledger。
- `open-ai-agent/pi-subagents/src/runs/shared/completion-guard.ts`
  实现类任务零变更完成守卫。适用于理解 `expectsImplementationMutation` 与 model fallback 触发条件。
- `open-ai-agent/pi-subagents/src/runs/shared/long-running-guard.ts`
  `active_long_running` 阈值与 mutating tool 失败升级。适用于理解 control 通知与 needs_attention 升级。
- `open-ai-agent/pi-subagents/src/runs/shared/mcp-direct-tool-allowlist.ts`
  `mcpDirectTools` → 子 Pi builtin tool 名解析。适用于理解 MCP 直连工具如何进入 `pi-args`。
- `open-ai-agent/pi-subagents/src/runs/shared/nested-events.ts`
  嵌套 subagent 事件总线、registry 投影与 control-request 协议。适用于理解 status 中的 nested 树数据来源。
- `open-ai-agent/pi-subagents/src/runs/shared/nested-path.ts`
  嵌套路径 env 编解码与消毒。适用于理解子 run 如何继承父 `NestedPathEntry[]`。
- `open-ai-agent/pi-subagents/src/runs/shared/nested-render.ts`
  `NestedRunSummary` → status/fleet 文本行。适用于理解 `formatNestedRunStatusLines` 与 aggregate 摘要。
- `open-ai-agent/pi-subagents/src/runs/shared/run-history.ts`
  本地 `run-history.jsonl` 记录与按 agent 加载。适用于理解 foreground/chain 完成后的历史落盘。
- `open-ai-agent/pi-subagents/src/runs/shared/single-output.ts`
  单 agent 输出文件契约（注入路径、快照、file-only）。适用于理解 `output` frontmatter 与 `SavedOutputReference`。
- `open-ai-agent/pi-subagents/src/runs/shared/structured-output.ts`
  `outputSchema` 临时 schema 文件、env 传递与 TypeBox 校验。适用于理解 structured_output 终态约束。
- `open-ai-agent/pi-subagents/src/runs/shared/*.ts`（其余）
  model scope、workflow graph、worktree、prompt runtime、budget、control 等共享运行工具。适用于 L2/L3 深挖时按需索引。
- `open-ai-agent/pi-subagents/test/unit/acceptance.test.ts`
  acceptance 输入校验、`evaluateAcceptance` 与 ledger 行为的单元测试佐证。
- `open-ai-agent/pi-subagents/test/unit/chain-root-attachment.test.ts`
  `waitForImportedAsyncRoot` 轮询与终态归一化的单元测试佐证。
- `open-ai-agent/pi-subagents/test/unit/completion-batcher.test.ts`
  debounce、maxWait、straggler 分组行为的单元测试佐证。
- `open-ai-agent/pi-subagents/test/unit/completion-dedupe.test.ts`
  `buildCompletionKey` 与 TTL 去重的单元测试佐证。
- `open-ai-agent/pi-subagents/test/unit/completion-guard.test.ts`
  task/agent 变更意图分类与 guard 触发的单元测试佐证。
- `open-ai-agent/pi-subagents/test/unit/notify.test.ts`
  `registerSubagentNotify`、分组/单条格式化与会话过滤的单元测试佐证。
- `open-ai-agent/pi-subagents/test/unit/nested-events.test.ts`
  nested route、registry 投影与事件写入的单元测试佐证。
- `open-ai-agent/pi-subagents/test/unit/single-output.test.ts`
  输出路径解析、快照与 `file-only` 模式的单元测试佐证。
- `open-ai-agent/pi-subagents/test/integration/single-execution.test.ts`
  前台 single 与 executor 基础行为的集成测试佐证。
- `open-ai-agent/pi-subagents/test/integration/parallel-execution.test.ts`
  top-level parallel、concurrency、output 和 timeout 行为的集成测试佐证。
- `open-ai-agent/pi-subagents/test/integration/chain-execution.test.ts`
  sequential chain、parallel step、named output、dynamic fanout 与 workflow graph 的集成测试佐证。
- `open-ai-agent/pi-subagents/test/integration/async-execution.test.ts`
  async runner、status、result file、timeout、control event 与后台输出的集成测试佐证。

## 智慧（社区）

- 本地 integration tests：`npm run test:integration -- single-execution parallel-execution chain-execution async-execution`
  适用于把阅读结论转化为可运行断言，尤其是分流、artifact、状态文件和后台事件。
- 本仓库已生成的 L0 导览：`teach/open-ai-agent/pi-subagents/00-overview/lessons/0001-project-map.html`
  适用于回看 runs 模块在 Pi extension 注册、agent discovery、intercom、slash/RPC 之间的位置。

## 空白

目前未收录外部社区讨论链接；本次 L1 以源码和本地测试为主要可信来源。若后续要研究真实用户工作流或故障案例，需要补充 upstream issue、PR 或 release discussion。

# async lifecycle、status 与 wait 全链路资源

## 知识

- 本地源码：`open-ai-agent/pi-subagents/src/runs/background/async-execution.ts`
  讲解 detached runner 如何写 config、spawn `subagent-runner.ts`、创建 `asyncDir` 并发出 `SUBAGENT_ASYNC_STARTED_EVENT`。适用于理解 async 启动与“禁止 sleep-poll”提示的来源。
- 本地源码：`open-ai-agent/pi-subagents/src/runs/background/async-job-tracker.ts`
  讲解 session 内 `asyncJobs` map、轮询 `status.json`、转发 `events.jsonl` 控制事件、恢复 active jobs 与 widget 刷新。适用于理解父进程内存态如何跟上磁盘状态。
- 本地源码：`open-ai-agent/pi-subagents/src/runs/background/run-status.ts`
  讲解 `subagent({ action: "status" })` 如何 reconcile、格式化 fleet/transcript/exact status，并在 result 文件存在时回退读取。适用于一次性巡检与排障。
- 本地源码：`open-ai-agent/pi-subagents/src/runs/background/wait.ts`
  讲解 `wait()` 如何阻塞当前 turn、事件唤醒与轮询兜底、`all`/`id` 语义，以及 `needs_attention` 提前返回。适用于 skill 与非交互式单 turn 场景。
- 本地源码：`open-ai-agent/pi-subagents/src/runs/background/result-watcher.ts`
  讲解 `RESULTS_DIR` 下 result JSON 如何被 watch、去重、触发 `SUBAGENT_ASYNC_COMPLETE_EVENT` 与 intercom delivery。适用于理解完成通知的最后一跳。
- 本地接线：`open-ai-agent/pi-subagents/src/extension/index.ts`
  注册 `wait` tool、挂载 job tracker 与 result watcher、订阅 started/complete 事件。适用于把五段链路放回 extension 启动上下文。
- 本地测试：`open-ai-agent/pi-subagents/test/integration/async-execution.test.ts`
  验证 async spawn、status 读写、launch message、timeout、live output、result 文件与 events 上限等行为。
- 本地测试：`open-ai-agent/pi-subagents/test/integration/async-job-tracker.test.ts`
  验证 started/complete 处理、control event 转发、active job 恢复与清理计时器。
- 本地测试：`open-ai-agent/pi-subagents/test/integration/async-status.test.ts`
  验证 `listAsyncRuns` 与 status 格式化边界。
- 上游 L1 参考：`teach/open-ai-agent/pi-subagents/module-runs-execution/reference/runs-execution-overview.html`
  runs 三层边界与入口清单；本切片是其 async lifecycle 深化。

## 智慧（社区）

- [nicobailon/pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues)
  上游问题讨论入口。适用于把 status/wait/async 行为差异对照到真实 bug 或回归报告。
- 本仓库 teach-goal 评审会话
  适用于把本切片与后续“控制与恢复”L2 串联验证。

## 空白

- 未找到 pi-subagents 官方独立文档专门描述 `wait` 与 status 语义差异；当前课程以源码注释、`extension/tool-description.ts` 与集成测试为可信来源。

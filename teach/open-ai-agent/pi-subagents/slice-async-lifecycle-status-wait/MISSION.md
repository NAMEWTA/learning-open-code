# 使命：async lifecycle、status 与 wait 全链路

## 为什么
学习者已经知道 runs 模块会把 `async: true` 分流到后台，但还不清楚 detached run 启动之后，状态如何落盘、父会话如何观测、何时该 `status`、何时该 `wait`，以及完成通知怎样回到当前 turn。掌握这条 L2 垂直切片后，可以独立排查“后台任务还在跑却看不到结果”“不该 sleep-poll 却一直在轮询”“skill 里 async 子任务跑完但父 agent 没收到完成”这类问题。

## 成功的样子
- 能口述 async run 从 `executeAsyncSingle` 到 `SUBAGENT_ASYNC_COMPLETE_EVENT` 的五段链路，并指出每段对应源码文件。
- 能区分 `status`（一次性快照）、`wait`（阻塞当前 turn）和 completion notification（交互式下一 turn 唤醒）三种观测方式及适用场景。
- 能说出 `status.json`、`events.jsonl`、`RESULTS_DIR/*.json` 三类产物各自服务哪一层。
- 遇到 `needs_attention` 或 timeout 时，知道应先读 `run-status.ts` 还是 `wait.ts`，而不是盲目 sleep-poll。

## 约束条件
- 课程按 15 分钟短课合约拆分；长表、状态机和文件索引放入 `reference/`。
- 只覆盖本切片列出的 background 文件与相关测试，不展开 `subagent-runner.ts` 逐步执行细节或 control/resume 控制面。
- 产出写入 `teach/open-ai-agent/pi-subagents/slice-async-lifecycle-status-wait/`。

## 不在范围内
- 不逐行讲解 `subagent-runner.ts` 内部 step 循环、worktree、acceptance 与 nested fanout。
- 不覆盖 `interrupt` / `resume` / `steer` / `append-step` 控制协议（留给控制面 L2）。
- 不展开 TUI widget 渲染实现（`module-tui-rendering`）与 intercom grouped result 细节（`module-intercom`）。

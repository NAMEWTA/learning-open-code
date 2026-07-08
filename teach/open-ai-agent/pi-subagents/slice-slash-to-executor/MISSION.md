# 使命：Slash 命令到 executor 桥接全链路

## 为什么
在 pi-subagents 里，用户通过 `/run`、`/chain`、`/parallel` 等 slash 命令触发子 agent，但命令解析、事件桥接、live card 与真正 spawn child Pi 的 executor 分属不同文件。调试「slash 发了但没跑」「进度卡死」「bridge 没响应」时，必须能从前台输入一路指到 `executor.execute` 的分流点。

## 成功的样子
- 能按顺序说出 `/run` 从命令 handler 到 `runSinglePath` 的八跳链路
- 能区分 `slash-bridge`（`subagent:slash:*`）与 `prompt-template-bridge`（`prompt-template:subagent:*`）两条入口，并说明它们如何汇合到同一 `executor.execute`
- 能解释 `requestSlashRun` 为何依赖 bridge 同步 emit `started`，以及无 bridge 时的快速失败
- 能读懂 `slash-commands.test.ts` 对 params 转发与 live snapshot 的关键断言

## 约束条件
- 以 foreground slash 路径为主，不展开 prompt-workflow 模板发现细节（见 `module-slash-workflows`）
- 单节课 15 分钟内完成，长表与事件清单查 reference 速查页

## 不在范围内
- child Pi spawn 与 JSONL 解析（见 `slice-single-foreground-run`）
- chain / parallel 编排语义（见 `slice-parallel-chain-execution`）
- async 后台 runner 生命周期（见 `slice-async-lifecycle-status-wait`）

# 使命：远端操作下载、转换、应用与冲突边界全链路

## 为什么
学习者需要能诊断 Super Productivity 同步中“远端 operation 已下载，但本地状态为何变了、没变、被过滤、触发 LWW，或进入 full-state 冲突门”的问题。掌握这条链路后，可以从日志或源码快速定位是下载游标、SYNC_IMPORT 边界、vector clock 冲突、NgRx replay，还是本地 op-log 写入状态出了问题。

## 成功的样子
- 能说清远端 ops 下载后如何过滤重复、schema migration、SYNC_IMPORT clean-slate 过滤，以及何时推进 `lastServerSeq`。
- 能区分普通 remote ops、`SYNC_IMPORT`、`BACKUP_IMPORT`、`REPAIR` 和 force download，不把它们混成一条 apply 路径。
- 能追到 `applyRemoteOperations()` 如何先写 `remote/pending`，再批量 replay，最后标记 `applied` 并合并 vector clock。
- 能判断何时走 `SyncImportConflictGateService`、何时走 LWW、何时直接 full-state import，以及哪些路径会写本地 store/op-log。

## 约束条件
- 本主题是 L2 垂直切片，只讲远端操作下载后的处理、转换、应用与冲突边界。
- 源项目目录只读；课程内容只写入 `teach/open-productivity/super-productivity/slice-remote-op-apply-flow/`。
- 不修改项目级 `index.md`、`_progress.json`、`_progress.md` 或其他主题目录。

## 不在范围内
- 不展开 SuperSync 服务端 SQL、鉴权、quota 或 WebSocket 细节。
- 不逐行讲每个 feature reducer 的业务语义。
- 不把本地 action 捕获与上传完整链路重复讲一遍；相关背景链接到 `slice-op-log-sync-flow`。

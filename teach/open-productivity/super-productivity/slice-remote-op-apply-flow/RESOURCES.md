# 远端操作下载、转换、应用与冲突边界全链路资源

## 知识

- [src/app/op-log/sync/operation-log-download.service.ts](../../../../open-productivity/super-productivity/src/app/op-log/sync/operation-log-download.service.ts)
  远端下载入口。适用于核对分页下载、gap reset、重复过滤、解密、snapshotState 和 `latestServerSeq` 返回边界。
- [src/app/op-log/sync/operation-log-sync.service.ts](../../../../open-productivity/super-productivity/src/app/op-log/sync/operation-log-sync.service.ts)
  下载后的主编排。适用于确认 fresh-client gate、file snapshot hydration、incoming full-state conflict gate、`processRemoteOps()` 调用和游标推进。
- [src/app/op-log/sync/remote-ops-processing.service.ts](../../../../open-productivity/super-productivity/src/app/op-log/sync/remote-ops-processing.service.ts)
  本主题核心入口。适用于理解 schema migration、SYNC_IMPORT 过滤、full-state 分支、vector clock 冲突检测、direct apply 和 Checkpoint D。
- [src/app/op-log/sync/sync-import-filter.service.ts](../../../../open-productivity/super-productivity/src/app/op-log/sync/sync-import-filter.service.ts)
  clean-slate 过滤。适用于判断普通 ops 是否被最新 full-state import 失效。
- [src/app/op-log/sync/sync-import-conflict-gate.service.ts](../../../../open-productivity/super-productivity/src/app/op-log/sync/sync-import-conflict-gate.service.ts)
  incoming full-state 门。适用于判断 `SYNC_IMPORT` / `BACKUP_IMPORT` / `REPAIR` 到达前是否应提示用户选择本地或远端。
- [src/app/op-log/sync/conflict-resolution.service.ts](../../../../open-productivity/super-productivity/src/app/op-log/sync/conflict-resolution.service.ts)
  LWW 冲突解决。适用于理解远端胜出如何 apply、本地胜出如何生成新的 local update op。
- [src/app/op-log/apply/operation-applier.service.ts](../../../../open-productivity/super-productivity/src/app/op-log/apply/operation-applier.service.ts)
  NgRx replay 入口。适用于确认批量 dispatch、archive side effects、deferred local actions 边界。
- [src/app/op-log/apply/operation-converter.util.ts](../../../../open-productivity/super-productivity/src/app/op-log/apply/operation-converter.util.ts)
  operation 到 action 的转换。适用于确认 full-state payload、LWW payload id 修正和 `meta.isRemote`。
- [src/app/op-log/persistence/operation-log-store.service.ts](../../../../open-productivity/super-productivity/src/app/op-log/persistence/operation-log-store.service.ts)
  本地 op-log 持久化。适用于确认 `appendBatchSkipDuplicates()`、`markApplied()`、`markFailed()`、`clearFullStateOpsExcept()` 和 `mergeRemoteOpClocks()`。
- [packages/sync-core/src/remote-apply.ts](../../../../open-productivity/super-productivity/packages/sync-core/src/remote-apply.ts)
  框架无关 remote apply 协调器。适用于确认 crash-safety 写入顺序。
- [packages/sync-core/src/sync-import-filter.ts](../../../../open-productivity/super-productivity/packages/sync-core/src/sync-import-filter.ts)
  full-state clean-slate 的 vector clock 分类。适用于核对 `GREATER_THAN`、`EQUAL`、`CONCURRENT`、`LESS_THAN` 的保留/过滤规则。
- [packages/sync-core/src/conflict-resolution.ts](../../../../open-productivity/super-productivity/packages/sync-core/src/conflict-resolution.ts)
  LWW 分区与 DELETE/UPDATE 转换的通用逻辑。适用于理解 App service 之前的纯算法。
- [src/app/root-store/meta/task-shared-meta-reducers/lww-update.meta-reducer.ts](../../../../open-productivity/super-productivity/src/app/root-store/meta/task-shared-meta-reducers/lww-update.meta-reducer.ts)
  LWW Update 在 NgRx 根 meta-reducer 中的落地。适用于确认 winning entity 如何替换或重建。
- [src/app/op-log/apply/bulk-hydration.meta-reducer.ts](../../../../open-productivity/super-productivity/src/app/op-log/apply/bulk-hydration.meta-reducer.ts)
  批量 replay meta-reducer。适用于确认批量 action 如何逐 op 转换并进入 reducer 链。
- [docs/sync-and-op-log/operation-log-architecture.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/operation-log-architecture.md)
  项目内 operation log 架构说明。适用于补齐本主题与 L1 `module-op-log-sync` 的关系。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/johannesjo/super-productivity/issues)
  适用于把课程中的冲突、导入、加密、Dropbox/WebDAV 重复同步等判断点对照真实缺陷。
- 项目内 sync regression specs
  重点看 `src/app/op-log/sync/remote-ops-processing.service.spec.ts`、`operation-log-sync.service.spec.ts`、`sync-import-filter.service.spec.ts`、`sync-import-conflict-gate.service.spec.ts`。适用于验证边界条件是否曾经回归。

## 空白

- 本轮未检索外部博客或论坛文章；该主题以项目源码、项目内文档和测试为准。

# 本地操作捕获、持久化与同步上传下载全链路资源

## 知识

- [docs/sync-and-op-log/operation-log-architecture.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/operation-log-architecture.md)
  项目内 operation log 架构说明。适用于理解 action capture、operation、vector clock、远端 replay 的整体意图。
- [docs/sync-and-op-log/diagrams/01-local-persistence.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/diagrams/01-local-persistence.md)
  本地持久化图。适用于核对 `SUP_OPS`、operation 写入和 state cache 的关系。
- [docs/sync-and-op-log/diagrams/02-server-sync.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/diagrams/02-server-sync.md)
  服务端同步图。适用于理解 SuperSync upload/download、server sequence 和 piggyback。
- [docs/sync-and-op-log/diagrams/04-file-based-sync.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/diagrams/04-file-based-sync.md)
  文件型 provider 同步图。适用于理解远端同步文件、snapshot 与 recent ops。
- [docs/sync-and-op-log/supersync-encryption-architecture.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/supersync-encryption-architecture.md)
  SuperSync 加密架构说明。适用于理解 E2EE、password/key、encrypted payload 的边界。
- [src/app/op-log/capture/](../../../../open-productivity/super-productivity/src/app/op-log/capture/)
  本地 action 捕获源码入口。适用于追踪 NgRx action 如何变成 operation。
- [src/app/op-log/persistence/](../../../../open-productivity/super-productivity/src/app/op-log/persistence/)
  `SUP_OPS` 持久化源码入口。适用于追踪 ops、state cache、vector clock、client id 和 compact format。
- [src/app/op-log/sync/](../../../../open-productivity/super-productivity/src/app/op-log/sync/)
  op-log sync 编排、upload、download、remote apply、冲突和校验入口。
- [src/app/op-log/sync-providers/](../../../../open-productivity/super-productivity/src/app/op-log/sync-providers/)
  App 侧 provider factory、wrapper、file-based adapter 和 SuperSync wiring。
- [packages/sync-core/src/](../../../../open-productivity/super-productivity/packages/sync-core/src/)
  框架无关的 vector clock、upload/download planning、encryption、compression、remote apply 算法。
- [packages/sync-providers/src/provider-types.ts](../../../../open-productivity/super-productivity/packages/sync-providers/src/provider-types.ts)
  provider 合同。适用于确认 `OperationSyncCapable`、`superSyncOps`、`fileSnapshotOps` 的边界。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/johannesjo/super-productivity/issues)
  适用于把课程中的故障排查线索对照真实同步缺陷、平台差异和回归案例。
- [Super Productivity GitHub Discussions](https://github.com/johannesjo/super-productivity/discussions)
  适用于了解用户如何描述同步、加密、WebDAV、Dropbox、Android 后台同步等实际问题。
- 项目内 regression specs
  例如 `src/app/op-log/capture/operation-log-effect-stream-survival.regression.spec.ts`、`src/app/op-log/sync/operation-log-lock-reentry.regression.spec.ts`。适用于确认曾经出错的边界条件。

## 空白

- 本轮未检索外部博客或论坛文章；该切片以项目源码、项目内文档和测试为准。

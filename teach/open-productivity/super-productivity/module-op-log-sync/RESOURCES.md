# Operation Log、本地持久化与同步架构资源

## 知识

- [docs/sync-and-op-log/README.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/README.md)
  op-log 与 sync 文档入口。适用于确认统一 operation log、各专题文档和场景目录。
- [docs/sync-and-op-log/operation-log-architecture.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/operation-log-architecture.md)
  本地持久化、文件型同步、SuperSync、验证修复和实现状态的权威架构说明。适用于建立 L1 模块边界。
- [docs/sync-and-op-log/package-boundaries.md](../../../../open-productivity/super-productivity/docs/sync-and-op-log/package-boundaries.md)
  说明 `@sp/sync-core`、`@sp/sync-providers`、`src/app`、`shared-schema` 和服务端依赖方向。适用于判断代码应放在哪一层。
- [src/app/op-log/](../../../../open-productivity/super-productivity/src/app/op-log/)
  app 侧 capture、apply、persistence、sync、provider wiring 与 validation。适用于从 NgRx action 追到持久化和同步。
- [src/app/imex/sync/](../../../../open-productivity/super-productivity/src/app/imex/sync/)
  用户同步配置、触发、错误对话框和全局 sync wrapper。适用于理解 UI 如何进入 op-log sync。
- [packages/sync-core/src/index.ts](../../../../open-productivity/super-productivity/packages/sync-core/src/index.ts)
  框架无关同步核心 public exports。适用于查找 vector clock、upload/download planning、replay、conflict helper 和 port 类型。
- [packages/sync-providers/src/provider-types.ts](../../../../open-productivity/super-productivity/packages/sync-providers/src/provider-types.ts)
  provider 契约、文件型 provider、operation sync provider mode 和 `OperationSyncCapable`。适用于理解 provider 边界。
- [packages/super-sync-server/README.md](../../../../open-productivity/super-productivity/packages/super-sync-server/README.md)
  SuperSync 服务端架构、Docker 部署、API 入口和 PostgreSQL append-only log 说明。适用于服务端线索阅读。

## 智慧（社区）

- [super-productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)
  适用于验证同步 bug、数据丢失风险和 provider 行为是否已有上游讨论。
- [super-productivity GitHub Pull Requests](https://github.com/super-productivity/super-productivity/pulls)
  适用于观察同步边界变更、迁移策略和测试补充的真实评审上下文。

## 空白

- 本课未检索外部分布式系统论文或通用同步框架资料；当前目标是读懂本仓库实现边界。后续进入 vector clock、CRDT 取舍或 E2EE 同步设计时，应补充外部权威资料。

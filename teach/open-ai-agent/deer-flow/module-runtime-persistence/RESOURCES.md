# Runtime 与 persistence 资源

## 知识

- [`teach/open-ai-agent/deer-flow/00-overview/reference/00-overview.html`](../00-overview/reference/00-overview.html)
  L0 总览已把 DeerFlow 定位为 Gateway embedded runtime + LangGraph harness，本主题沿用其中的 runtime/persistence 边界。
- [`backend/app/gateway/deps.py`](../../../../open-ai-agent/deer-flow/backend/app/gateway/deps.py)
  Gateway lifespan 的真实装配点：创建 stream bridge、SQLAlchemy engine、checkpointer、store、run repository、event store 和 `RunManager`。
- [`backend/app/gateway/services.py`](../../../../open-ai-agent/deer-flow/backend/app/gateway/services.py)
  `start_run()` 展示 HTTP run 请求如何创建 `RunRecord`、构建配置并启动后台 `run_agent()`。
- [`backend/packages/harness/deerflow/runtime/runs/worker.py`](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/runs/worker.py)
  run 执行主线：状态切换、LangGraph streaming、journal、goal continuation、checkpoint rollback、workspace changes 和最终清理。
- [`backend/packages/harness/deerflow/runtime/runs/manager.py`](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/runs/manager.py)
  `RunManager` 的 in-memory registry、线程索引、并发策略、持久化重试与 orphaned run recovery。
- [`backend/packages/harness/deerflow/runtime/journal.py`](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/journal.py)
  `RunJournal` 如何把 LangChain callback 标准化为 run events，并汇总 token/message 便利字段。
- [`backend/packages/harness/deerflow/runtime/events/store/base.py`](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/runtime/events/store/base.py)
  `RunEventStore` 的抽象契约：message、trace、run events 的统一查询接口。
- [`backend/packages/harness/deerflow/persistence/`](../../../../open-ai-agent/deer-flow/backend/packages/harness/deerflow/persistence/)
  SQLAlchemy ORM、repository、engine lifecycle、bootstrap 和 Alembic migration 的实际实现。
- [`backend/tests/test_run_manager.py`](../../../../open-ai-agent/deer-flow/backend/tests/test_run_manager.py)
  `RunManager` 并发策略、store fallback、线程索引和持久化失败行为的主要测试证据。
- [`backend/tests/test_run_journal.py`](../../../../open-ai-agent/deer-flow/backend/tests/test_run_journal.py)
  `RunJournal` 的事件捕获和 token 汇总行为证据。
- [`backend/tests/test_persistence_bootstrap.py`](../../../../open-ai-agent/deer-flow/backend/tests/test_persistence_bootstrap.py)
  empty、legacy、versioned 三种数据库 bootstrap 分支的行为证据。
- [`backend/tests/test_stream_bridge.py`](../../../../open-ai-agent/deer-flow/backend/tests/test_stream_bridge.py)
  memory/redis stream bridge 的 replay、heartbeat、Last-Event-ID 与配置行为证据。
- [`backend/tests/test_run_worker_rollback.py`](../../../../open-ai-agent/deer-flow/backend/tests/test_run_worker_rollback.py)
  worker rollback、pre-run checkpoint 和异常路径恢复的行为证据。

## 智慧（社区）

- 本轮不引入外部社区。该主题目标是源码考古和本仓库教学产物生成，最可靠的反馈来自运行 DeerFlow 后端测试、复现 Gateway run 请求、审阅 runtime/persistence 源码。

## 空白

- 未收录 LangGraph 官方文档链接；本课先以当前 deer-flow 源码为准，避免把上游文档版本差异混入 L1 模块总览。
- 未覆盖生产数据库调优资料；后续若生成部署专题，可补充 Postgres pool、Redis Streams 和 SQLite WAL 的运维资源。

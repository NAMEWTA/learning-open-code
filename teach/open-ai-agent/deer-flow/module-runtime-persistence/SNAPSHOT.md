# 课程快照：module-runtime-persistence

## 源项目信息
- **源仓库**：`open-ai-agent/deer-flow`
  - **Git Commit**：`eb5eb9c5743997ac60cbd8d902e49a44f94120ff`
  - **短 Commit**：`eb5eb9c`
  - **分支**：`main`
- **快照时间**：2026-07-08T09:49:30+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `backend/app/gateway/deps.py` | 课程分析引用 | 🟡 辅助 |
| `backend/app/gateway/routers/thread_runs.py` | 课程分析引用 | 🟡 辅助 |
| `backend/app/gateway/services.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/config/checkpointer_config.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/config/database_config.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/config/run_events_config.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/config/stream_bridge_config.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/base.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/bootstrap.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/engine.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/migrations/versions/0001_baseline.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/migrations/versions/0002_runs_token_usage.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/migrations/versions/0003_scheduled_tasks.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/models/run_event.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/run/model.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/run/sql.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/thread_meta/model.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/persistence/thread_meta/sql.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/checkpointer/async_provider.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/checkpointer/provider.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/events/store/base.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/events/store/db.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/events/store/jsonl.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/events/store/memory.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/goal.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/journal.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/runs/manager.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/runs/schemas.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/runs/store/base.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/runs/store/memory.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/runs/worker.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/serialization.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/store/async_provider.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/store/provider.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/stream_bridge/async_provider.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/stream_bridge/base.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/stream_bridge/memory.py` | 课程分析引用 | 🟡 辅助 |
| `backend/packages/harness/deerflow/runtime/stream_bridge/redis.py` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-runtime-persistence-module-tour | `lessons/0001-runtime-persistence-module-tour.html` | Runtime 与 persistence：一次 run 会落到哪些边界 |

## 参考资料

- `reference/runtime-persistence-api.html` — Runtime 与 persistence 公共 API
- `reference/runtime-persistence-overview.html` — Runtime 与 persistence 模块参考

## 快照摘要
- 课程数：1
- 引用源文件数：38
- 学习记录数：0
- 参考资料数：2
- 资产文件数：0

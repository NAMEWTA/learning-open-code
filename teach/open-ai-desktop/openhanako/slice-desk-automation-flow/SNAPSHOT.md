# 课程快照：slice-desk-automation-flow

## 源项目信息
- **源仓库**：`open-ai-desktop/openhanako`
  - **Git Commit**：`acb1b2b860d0d877a9ba57b9022347643e892b1c`
  - **短 Commit**：`acb1b2b`
  - **分支**：`main`
- **快照时间**：2026-07-07T14:30:00+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `lib/desk/activity-store.ts` | 活动存储全链路分析 — ActivityStore 类、原子写入、崩溃恢复 | 🔴 核心 |
| `lib/desk/agent-run-automation.ts` | Agent 执行器构造 — 3 种 prompt 模板、executor 序列化 | 🔴 核心 |
| `lib/desk/automation-executors.ts` | 执行器提取薄层 — 从 job 字段推导 executor | 🟡 辅助 |
| `lib/desk/automation-normalizer.ts` | 数据标准化 — v1/v2 → v3 schema、trigger/executor 分离 | 🔴 核心 |
| `lib/desk/cron-scheduler.ts` | Cron 调度器 — 60s 轮询、Promise.race 超时、防重入锁 | 🔴 核心 |
| `lib/desk/cron-store.ts` | Cron 持久化 — CRUD、JSONL 历史、退避算法、cron 表达式解析 | 🔴 核心 |
| `lib/desk/desk-manager.ts` | Desk 目录管理 — 确保 cron-jobs.json + cron-runs/ 目录结构 | 🟡 辅助 |
| `core/studio-cron-service.ts` | Studio 级服务 — 多 Agent cron 统一管理、旧版迁移 | 🔴 核心 |
| `lib/file-ref/resource-io.ts` | 文件资源 I/O — PathRef / SessionFileRef 解析、跨 root 复制 | 🟡 辅助 |
| `lib/desk/heartbeat.ts` | 心跳活动参考（背景知识） | 🟡 辅助 |
| `lib/desk/permissions.ts` | Desk 权限定义参考 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| desk-automation-flow | `lessons/desk-automation-flow.html` | 书桌文件拖拽与定时任务全链路 · L2 垂直切片 · HanaAgent |

## 快照摘要
- 课程数：1
- 引用源文件数：11
- 学习记录数：0
- 参考资料数：0
- 资产文件数：0

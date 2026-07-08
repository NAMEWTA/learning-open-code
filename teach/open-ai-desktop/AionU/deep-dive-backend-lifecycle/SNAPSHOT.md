# 课程快照：deep-dive-backend-lifecycle

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T20:12:22+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/index.ts` | 桌面启动顺序、单实例、WebUI/resetpass 分支证据 | 🔴 核心 |
| `packages/desktop/src/process/services/database/drivers/BetterSqlite3Driver.ts` | 课程分析引用 | 🟡 辅助 |
| `packages/desktop/src/process/services/database/runLegacyDatabaseMigrations.ts` | 课程分析引用 | 🟡 辅助 |
| `packages/desktop/src/process/services/database/schema.ts` | 课程分析引用 | 🟡 辅助 |
| `packages/desktop/src/process/startup/backendStartup.ts` | 课程分析引用 | 🟡 辅助 |
| `packages/desktop/src/process/utils/webuiConfig.ts` | 设置页 WebUI 复用现有 backend port 的关键证据 | 🔴 核心 |
| `packages/web-host/src/backend-launcher.test.ts` | 课程分析引用 | 🟡 辅助 |
| `packages/web-host/src/backend-launcher.ts` | BackendLifecycleManager owner、启动参数、健康检查与停止清理主证据 | 🔴 核心 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-problem-frame | `lessons/0001-problem-frame.html` | Backend lifecycle 为什么必须单点管理 |

## 参考资料

- `reference/backend-lifecycle-notes.html` — Backend lifecycle 与 SQLite 竞争规避速查

## 快照摘要
- 课程数：1
- 引用源文件数：8
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0

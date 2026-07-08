# 课程快照：Backend 启动失败恢复全链路

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
- **短 Commit**：`0ea13fd01`
- **分支**：`main`
- **快照时间**：2026-07-07T19:27:40+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/index.ts` | main 启动失败状态、同步 IPC、数据库恢复 handler、默认桌面失败后继续建窗 | 🔴 核心 |
| `packages/desktop/src/process/startup/backendStartupFailure.ts` | backend 启动失败分类优先级和 reason 生成 | 🔴 核心 |
| `packages/desktop/src/process/startup/recoverCorruptedDatabase.ts` | 可恢复数据库损坏确认后的 stop、restart、mark ready、reload 顺序 | 🔴 核心 |
| `packages/desktop/src/preload/main.ts` | failure 注入 renderer 与恢复 IPC 暴露 | 🔴 核心 |
| `packages/desktop/src/renderer/main.tsx` | failure dialog 与正常 App 根渲染分流 | 🔴 核心 |
| `packages/desktop/src/renderer/components/layout/InstallationIntegrityDialog.tsx` | 安装完整性、数据迁移、本地数据修复和可恢复数据库损坏弹窗动作 | 🔴 核心 |
| `packages/desktop/src/common/types/platform/electron.ts` | `BackendStartupFailureInfo` 和 preload API 类型 | 🟡 辅助 |
| `tests/unit/bootstrap/backendStartupFailure.test.ts` | 分类器、架构检查和 modal action 单元证据 | 🔴 核心 |
| `tests/unit/bootstrap/recoverCorruptedDatabase.test.ts` | 数据库恢复动作守卫、成功顺序和失败边界证据 | 🟡 辅助 |
| `tests/unit/bootstrap/recoverCorruptedDatabasePreload.test.ts` | preload 恢复 IPC 暴露证据 | 🟡 辅助 |
| `tests/e2e/specs/installation-integrity.e2e.ts` | 安装完整性弹窗和诊断上报 E2E 证据 | 🔴 核心 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | lessons/0001-flow-map.html | Backend 启动失败从 main 分类到 renderer 弹窗与数据库恢复的短课 |

## 已生成参考文档

| 编号 | 参考文件 | 描述 |
|------|---------|------|
| 01 | reference/backend-recovery-flow-map.html | 失败分类、分层路径、时序图、恢复边界和测试证据速查 |

## 快照摘要
- 课程数：1
- 参考文档数：1
- 引用源文件数：11
- 学习记录数：0

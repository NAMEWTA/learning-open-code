# 课程快照：slice-desktop-startup

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T19:01:09+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/index.ts` | Electron entry、模式分支、backend 启动、窗口创建、renderer 装载 | 核心 |
| `packages/desktop/src/process/index.ts` | process 初始化汇合点、storage/bridge/i18n 前置 | 核心 |
| `packages/desktop/src/process/utils/initBridge.ts` | bridge 注册副作用入口 | 辅助 |
| `packages/desktop/src/process/bridge/index.ts` | main process bridge 聚合注册 | 辅助 |
| `packages/desktop/src/process/backend/index.ts` | backend 二进制解析导出口 | 辅助 |
| `packages/desktop/src/process/startup/backendStartup.ts` | backend 启动成功、失败、取消语义 | 核心 |
| `packages/desktop/src/preload/main.ts` | backend port、语言、失败状态注入 renderer | 核心 |
| `packages/desktop/src/common/config/configService.ts` | renderer 配置初始化请求的 backend port 使用 | 辅助 |
| `packages/desktop/src/renderer/services/bootstrapRenderer.ts` | renderer 配置启动闸门 | 辅助 |
| `packages/desktop/src/renderer/hooks/context/AuthContext.tsx` | 桌面运行时认证 ready 逻辑 | 辅助 |
| `packages/desktop/src/renderer/main.tsx` | React bootstrap、provider 栈、失败弹窗、root render | 核心 |
| `packages/desktop/src/renderer/components/layout/Router.tsx` | Router 首屏路由和认证守卫 | 核心 |
| `tests/e2e/specs/app-launch.e2e.ts` | 启动烟雾测试证据 | 核心 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-flow-map | `lessons/0001-flow-map.html` | 桌面启动全链路地图 |
| 0002-main-process-window | `lessons/0002-main-process-window.html` | main/process 到窗口装载主路径 |
| 0003-renderer-first-screen-and-boundary | `lessons/0003-renderer-first-screen-and-boundary.html` | renderer/Router 首屏与失败边界 |

## 参考资料

- `reference/desktop-startup-flow-map.html` — 桌面启动到首屏全链路参考图谱

## 快照摘要
- 课程数：3
- 引用源文件数：13
- 学习记录数：0
- 参考资料数：1
- 资产文件数：1

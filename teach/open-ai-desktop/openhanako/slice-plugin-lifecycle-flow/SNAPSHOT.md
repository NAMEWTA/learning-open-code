# 课程快照：slice-plugin-lifecycle-flow

## 源项目信息
- **源仓库**：`open-ai-desktop/openhanako`
  - **Git Commit**：`acb1b2b860d0d877a9ba57b9022347643e892b1c`
  - **短 Commit**：`acb1b2b`
  - **分支**：`main`
- **快照时间**：2026-07-07T13:21:58+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `core/plugin-manager.ts` | 插件管理器核心：scan/loadAll/installPlugin/enablePlugin/disablePlugin/unloadPlugin/removePlugin/setFullAccess/getDiagnostics | 🔴 核心 |
| `core/plugin-context.ts` | 插件上下文注入：createPluginContext/createPluginBusProxy/createPluginNetwork/createPluginResources | 🔴 核心 |
| `core/plugin-config.ts` | 插件配置管理：createPluginConfigStore/normalizePluginConfigSchema/validatePluginConfigPatch/redactConfigValues | 🔴 核心 |
| `core/plugin-dev-service.ts` | 插件开发服务：installFromSource/reloadPlugin/enablePlugin/disablePlugin/resetPlugin/uninstallPlugin/invokeTool/runScenario | 🟡 辅助 |
| `core/plugin-route-request-context.ts` | 路由请求级能力鉴权上下文 | 🟡 辅助 |
| `server/routes/plugins.ts` | 插件 REST API 路由：安装/卸载/启用/禁用/marketplace/配置/代理 | 🔴 核心 |
| `hub/event-bus.ts` | EventBus：发布订阅 + 请求响应 + 能力目录 | 🟡 辅助 |
| `packages/plugin-runtime/src/index.ts` | 插件 SDK 类型定义 + definePlugin/defineTool 助手 | 🟡 辅助 |
| `lib/plugin-format-guard.ts` | OpenClaw 格式检测 | 🟡 辅助 |
| `lib/plugin-versioning.ts` | Semver 比较与兼容性检查 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| plugin-lifecycle-flow | `lessons/plugin-lifecycle-flow.html` | 插件安装与加载全链路 · L2 垂直切片 · HanaAgent · 含 Mermaid 时序图、8 层切片详解、5 要素分析、3 条异常路径 |

## 快照摘要
- 课程数：1
- 引用源文件数：10
- 学习记录数：0
- 参考资料数：0
- 资产文件数：0

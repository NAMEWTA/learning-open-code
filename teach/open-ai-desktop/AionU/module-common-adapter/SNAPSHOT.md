# 课程快照：module-common-adapter

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T17:24:53+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `open-ai-desktop/AionU/packages/desktop/src/common/index.ts` | `ipcBridge` 对 renderer 的导出入口 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/constant.ts` | 统一 adapter channel 常量 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/main.ts` | main 侧统一桥接入口与窗口广播 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/httpBridge.ts` | HTTP 请求、错误封装与 WebSocket 工厂 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts` | 全量能力域清单与传输映射 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/registry.ts` | WebSocket broadcaster 与 bridge emitter 注册表 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/apiModelMapper.ts` | conversation/model 映射与请求体修正 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/searchMapper.ts` | 消息搜索结果映射 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/teamMapper.ts` | team 数据与状态枚举映射 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/fileSnapshotMapper.ts` | snapshot compare 字段修正 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/workspaceMapper.ts` | workspace 路径与目录树映射 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/api/ClientFactory.ts` | 公共 API client 工厂与协议归一化 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/types/provider/providerApi.ts` | provider 相关 HTTP wire contract | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/types/team/teamTypes.ts` | team 前端共享契约 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/types/agent/assistantTypes.ts` | assistants 返回结构契约 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/common/types/platform/fileSnapshot.ts` | snapshot 前端目标类型 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/preload/main.ts` | preload 注入 `electronAPI` 与启动快照 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/process/bridge/index.ts` | main 侧 provider 注册聚合入口 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/process/bridge/windowControlsBridge.ts` | IPC 能力示例：窗口控制 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/process/bridge/themeBridge.ts` | IPC 能力示例：theme 缓存与广播 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/process/bridge/webuiBridge.ts` | 混合能力示例：WebUI 生命周期走 IPC | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/process/bridge/systemSettingsBridge.ts` | 混合能力示例：部分设置留在 Electron main | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/helpers/httpBridge.ts` | 从测试侧验证 renderer 已迁到 HTTP 调用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-common-adapter-module-tour | `lessons/0001-common-adapter-module-tour.html` | Common adapter 与 API 映射短课 |

## 参考资料

- `reference/common-adapter-overview.html` — AionU Common Adapter 参考总览

## 快照摘要
- 课程数：1
- 引用源文件数：23
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0

# 课程快照：外部平台消息桥接全链路

## 源项目信息
- **源仓库**：`open-ai-desktop/openhanako`
  - **Git Commit**：`acb1b2b860d0d877a9ba57b9022347643e892b1c`
  - **短 Commit**：`acb1b2b`
  - **分支**：`main`
- **快照时间**：2026-07-07T15:00:00+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `core/bridge-session-manager.ts` | Bridge 会话管理器：外部消息执行、会话 match、Prompt 构建、响应捕获 | 🔴 核心 |
| `lib/bridge/bridge-manager.ts` | 桥接管理器：消息去重聚合、斜杠命令拦截、附件下载、流式投递 | 🔴 核心 |
| `lib/bridge/dingtalk-adapter.ts` | 钉钉适配器：Stream 连接、消息规范化、Markdown 分片发送 | 🔴 核心 |
| `hub/index.ts` | Hub 消息路由中枢：四条规则路由匹配 | 🟡 辅助 |
| `hub/channel-router.ts` | 频道路由器：Agent Phone 模型与频道工具 | 🟡 辅助 |
| `hub/event-bus.ts` | 事件总线：发布订阅 + request/handle 模式 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| bridge-message-flow | `lessons/bridge-message-flow.html` | 外部平台消息桥接全链路 · L2 垂直切片 · 10 层穿透 + Mermaid 时序图 + 5 异常路径 |

## 快照摘要
- 课程数：1
- 引用源文件数：6
- 学习记录数：0
- 参考资料数：0

# 课程快照：slice-agent-conversation-flow

## 源项目信息
- **源仓库**：`open-ai-desktop/openhanako`
  - **Git Commit**：`acb1b2b860d0d877a9ba57b9022347643e892b1c`
  - **短 Commit**：`acb1b2b`
  - **分支**：`main`
- **快照时间**：2026-07-07T13:21:58+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `server/routes/chat.ts` | WS 消息路由、事件广播（第2层 + 第8层核心入口） | 核心 |
| `hub/index.ts` | Hub 消息调度中枢、路由表（第3层） | 核心 |
| `core/engine.ts` | HanaEngine Thin Facade、Manager 组装（第4层） | 核心 |
| `core/agent.ts` | Agent 初始化、System Prompt 拼装、工具注册（第5层） | 核心 |
| `core/session-coordinator.ts` | Session 生命周期、promptSession、executeIsolated（第6层） | 核心 |
| `core/llm-client.ts` | callText 非流式 LLM 调用、多 Provider 协议适配（第7层） | 核心 |
| `core/desktop-session-submit.ts` | 桌面 session 防重入提交（第4层入口） | 核心 |
| `desktop/src/react/components/chat/ChatArea.tsx` | React 聊天面板 LRU 渲染（第1层） | 核心 |
| `desktop/src/react/components/chat/ChatMessageSurface.tsx` | 消息列表渲染、流式增量更新（第1层） | 辅助 |
| `desktop/src/react/components/chat/AssistantMessage.tsx` | AI 消息渲染、Markdown 解析（第1层） | 辅助 |
| `desktop/src/react/components/chat/UserMessage.tsx` | 用户消息气泡（第1层） | 辅助 |
| `core/compaction-utils.ts` | 硬截断降级算法（异常路径2） | 辅助 |
| `core/session-compactor.ts` | 缓存保留压缩（异常路径2） | 辅助 |
| `core/events.ts` | ThinkTagParser、MoodParser、CardParser 流式解析器（第8层） | 辅助 |
| `server/ws-protocol.ts` | WS 消息格式定义（第2层） | 辅助 |
| `server/session-stream-store.ts` | Ring buffer 事件存储、resume 续传（第8层） | 辅助 |
| `server/ws-scope.ts` | WS 客户端权限校验（第2层） | 辅助 |
| `lib/llm/provider-client.ts` | Provider 认证 header、URL 构造（第7层） | 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| agent-conversation-flow | `lessons/agent-conversation-flow.html` | Agent 对话全链路：用户输入→WS→Hub→Engine→Agent→SessionCoord→PiSDK→LLM→EventBus→WS→React |

## 快照摘要
- 课程数：1
- 引用源文件数：18
- 学习记录数：0
- 参考资料数：0
- 资产文件数：0

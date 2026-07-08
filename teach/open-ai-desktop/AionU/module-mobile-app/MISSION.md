# 使命：移动端应用工程

## 为什么
用户需要把 AionU 的 `mobile/` 工程讲清楚，建立“移动端如何远程连上桌面/后端 Cowork 能力”的整体心智模型。完成这一层后，后续继续深挖会话流、文件浏览、鉴权恢复或移动端 UI 时，能先知道入口、状态边界和通信链路各落在哪一层。

## 成功的样子
- 能从 `app/index.tsx` 和 `app/connect.tsx` 说明移动端首次连接、鉴权成功、进入聊天页的完整跳转链路。
- 能指出 `ConnectionContext`、`WebSocketContext`、`ConversationContext`、`ChatContext` 分别持有什么状态、解决什么问题。
- 能把 `bridge.ts`、`websocket.ts`、`api.ts` 和 `__tests__/` 的关系讲成“协议层、传输层、REST 补充层、回归证据”四段。

## 约束条件
- 本 goal 只产出 L1 模块总览，不展开到单组件逐行细讲。
- lesson 必须是 15 分钟内可完成的短课，完整清单和长表格放进 reference。
- 只覆盖 `mobile/` 真实源码工程，不改动源项目实现。

## 不在范围内
- 不讲桌面端 `packages/desktop` 的完整 renderer 细节，只在需要时作为回链背景提及。
- 不展开 Expo 原生打包、EAS 发布和 UI 视觉设计细节。

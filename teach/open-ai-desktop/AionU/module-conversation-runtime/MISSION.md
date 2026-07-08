# 使命：Conversation / Agent 运行时 UI

## 为什么
本主题服务于 AionU renderer 主线中的会话工作区学习：用户已经知道 renderer shell 如何启动，下一步需要建立“真正聊天时页面怎样跑起来”的心智模型。只有先看懂 conversation runtime 如何把页面入口、消息流、workspace、preview 和 ACP / aionrs 平台接在一起，后续深入单个 hook、消息协议或文件预览时才不会迷路。

## 成功的样子
- 能从 `packages/desktop/src/renderer/pages/conversation/index.tsx` 说清会话页如何加载会话、处理不存在会话并在切换时清空 preview。
- 能从 `ChatConversation.tsx` 与 `ChatLayout/index.tsx` 解释统一壳层和平台实现的分工，知道 ACP 与 aionrs 在哪里分叉、又在哪些 UI 组件上复用。
- 能指出 runtime gate、消息列表、workspace、preview 和 sendbox 之间的连接点，并据此决定下一步该读平台流、预览系统还是文件工作区。

## 约束条件
- 本轮只做 L1 模块总览，短课必须控制在 15 分钟内完成，聚焦“conversation runtime 如何组织起来”，不写成长篇页面百科。
- 所有改动仅写入 `teach/open-ai-desktop/AionU/module-conversation-runtime/`，不修改源项目与其他教学主题。
- 参考文档负责清单化索引，lesson 只保留完成学习目标所需的最短路径。

## 不在范围内
- 不逐条考古 `useAcpMessage`、`useAionrsMessage` 的流式协议细节。
- 不展开 Preview 编辑器、Workspace 文件操作或 Message 各子组件的全部实现。
- 不覆盖 team 页面、cron 页面和设置页面，只在必要处点到它们复用 conversation runtime 的接口。

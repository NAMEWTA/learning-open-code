# Conversation / Agent 运行时 UI 资源

## 知识

- [AionU conversation 页面入口](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/index.tsx) — 先看路由落点如何加载会话、处理删除后回退、切换会话时关闭 preview。
- [AionU 会话运行时总装](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/components/ChatConversation.tsx) — 观察平台分流、模型选择器、workspace 开关与 `ChatLayout` 组装。
- [AionU 会话布局壳层](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/components/ChatLayout/index.tsx) — 理解消息区、preview 面板、workspace 面板如何在同一个壳层里稳定共存。
- [AionU ACP 平台实现](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/platforms/acp/AcpChat.tsx) — 查看 ACP 会话怎样接入 `MessageList`、`AcpSendBox` 与上下文 provider。
- [AionU aionrs 平台实现](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/platforms/aionrs/AionrsChat.tsx) — 对照 ACP，看 aionrs 在本地图片预览、模型选择和发送逻辑上的差异。
- [AionU 运行时视图 hook](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/runtime/useConversationRuntimeView.ts) — 这是“能不能继续发送 / 当前是否正在跑”的统一闸门。
- [AionU 运行时状态仓库](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/runtime/conversationRuntimeViewStore.ts) — 用于理解 hydration、本地发送闸门、stop 确认与 turn completion 的状态转换。
- [AionU preview 上下文](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/Preview/context/PreviewContext.tsx) — 说明预览标签页、sendbox 注入和本地持久化如何被 conversation runtime 消费。
- [AionU workspace 面板](../../../../open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/Workspace/index.tsx) — 说明文件树、改动列表、粘贴/拖入与 preview 打开点如何挂到会话 UI。
- [AionU 消息协议定义](../../../../open-ai-desktop/AionU/packages/desktop/src/common/chat/chatLib.ts) — 理解消息类型、工具调用、tips/plan/thinking 等渲染输入。
- [AionU slash command 合并规则](../../../../open-ai-desktop/AionU/packages/desktop/src/common/chat/slash/mergeSlashCommands.ts) — 解释内建命令、ACP 命令和技能模板怎样汇总到发送框。
- [AionU 导航拦截器](../../../../open-ai-desktop/AionU/packages/desktop/src/common/chat/navigation/NavigationInterceptor.ts) — 说明 agent 浏览器导航结果怎样被拦截到 preview 面板。
- [AionU aionrs 基础流 E2E](../../../../open-ai-desktop/AionU/tests/e2e/features/conversations/aionrs/basic-flow.e2e.ts) — 用产品级测试验证会话创建、workspace 关联与消息收发。
- [AionU ACP 发送失败 E2E](../../../../open-ai-desktop/AionU/tests/e2e/features/conversations/acp/send-error-surfacing.e2e.ts) — 用失败路径说明 conversation runtime 不只是 happy path UI。
- [AionU conversation runtime 单测](../../../../open-ai-desktop/AionU/tests/unit/conversation/runtime/) — 集中验证 runtime gate、命令队列和 hydration 逻辑。
- [React 条件渲染参考](https://react.dev/learn/conditional-rendering) — 对照理解 `ChatConversation` 如何按 conversation type 选择平台实现与 header 组件。
- [React `useSyncExternalStore` 参考](https://react.dev/reference/react/useSyncExternalStore) — 对照 `useConversationRuntimeView` 如何从独立 store 向 React 暴露稳定快照。

## 智慧（社区）

- [AionUi GitHub Discussions](https://github.com/iOfficeAI/AionUi/discussions) — 适合验证你对 ACP / aionrs 会话形态、workspace 交互与运行时产品决策的理解。
- [AionUi GitHub Issues](https://github.com/iOfficeAI/AionUi/issues) — 适合搜索 conversation、preview、workspace、sendbox 相关缺陷，反推哪些路径是维护重点。

## 空白

- 上游暂时没有专门解释 conversation runtime 分层的设计文档，很多结构需要从源码和测试反推。
- ACP 与 aionrs 的平台协议文档分散在不同目录，尚缺一份统一的运行时状态机说明；后续课程可补到更细的 L2 主题。

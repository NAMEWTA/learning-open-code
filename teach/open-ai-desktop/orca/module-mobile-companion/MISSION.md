# 使命：移动端 Companion 模块

## 为什么
用户要完整学习 Orca，需要理解 mobile app 如何作为桌面 runtime 的远程 companion：它不复制桌面能力，而是通过 pairing、持久化 host、共享 WebSocket RPC、工作区列表和 session 路由来控制桌面上的 agent 与终端。这个主题补齐 L1 最后一块，为后续移动端配对与会话恢复 L2 链路做准备。

## 成功的样子
- 能说明移动端从 Expo Router 根布局到首页 host 列表的启动路径。
- 能追踪 pairing URL 如何进入 confirm screen，如何验证桌面 runtime，再如何保存 host profile 与 device token。
- 能解释 `RpcClient` 的 E2EE handshake、请求/订阅、断线重连和 stream replay 是移动端所有功能的底座。
- 能指出 worktree list、resume card、session screen、terminal/browser/file 面板分别依赖哪些 RPC。

## 约束条件
- 短课只覆盖移动端 companion 的主干，不展开每个 session 面板、PR review、文件预览和 terminal WebView 的全部实现。
- 所有结论以 Orca 仓库内移动端源码和测试为准。
- L1 主题必须通过快照、审计和独立审查后才能标记完成。

## 不在范围内
- 不分析桌面 runtime RPC server 的内部 pairing token、device registry 和 WebSocket server 实现；那属于 main runtime 与 L2 mobile pairing flow。
- 不逐行讲解 React Native 样式、图标、动画和具体表单控件。

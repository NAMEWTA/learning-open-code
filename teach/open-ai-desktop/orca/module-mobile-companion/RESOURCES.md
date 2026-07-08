# 移动端 Companion 模块资源

## 知识

- [mobile/README.md](../../../../open-ai-desktop/orca/mobile/README.md)  
  移动端本地开发、pairing、mock server、协议兼容和目录结构说明。
- [mobile/app/_layout.tsx](../../../../open-ai-desktop/orca/mobile/app/_layout.tsx)  
  Expo Router 根布局，安装 `RpcClientProvider`、deep link、通知跳转、splash 和 navigation stack。
- [mobile/app/index.tsx](../../../../open-ai-desktop/orca/mobile/app/index.tsx)  
  首页 host 列表、resume card、account usage、task entry、host actions 和多 host 状态聚合。
- [mobile/app/pair.tsx](../../../../open-ai-desktop/orca/mobile/app/pair.tsx)  
  `orca://pair` 路由的跳转页，将 code 参数或 initial URL 统一转到 confirm screen。
- [mobile/app/pair-scan.tsx](../../../../open-ai-desktop/orca/mobile/app/pair-scan.tsx)  
  QR 扫码入口，负责从摄像头扫描 desktop pairing code；细节留到 L2 mobile pairing flow。
- [mobile/app/pair-confirm.tsx](../../../../open-ai-desktop/orca/mobile/app/pair-confirm.tsx)  
  pairing 确认页，连接桌面、请求 `status.get`、保存 host profile，并展示 pairing log。
- [mobile/src/transport/pairing.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pairing.ts)  
  解析 `orca://pair` URL、裸 base64 code 和 desktop QR payload。
- [mobile/src/transport/host-store.ts](../../../../open-ai-desktop/orca/mobile/src/transport/host-store.ts)  
  host metadata 与 device token 的持久化边界；token 在 native 上走 Expo SecureStore。
- [mobile/src/transport/client-context.tsx](../../../../open-ai-desktop/orca/mobile/src/transport/client-context.tsx)  
  每 host 一个共享 `RpcClient` 的 React provider，处理 acquire/release、force reconnect 和 foreground recovery。
- [mobile/src/transport/rpc-client.ts](../../../../open-ai-desktop/orca/mobile/src/transport/rpc-client.ts)  
  移动端 WebSocket RPC client，负责 E2EE handshake、请求/订阅、重连、stream replay、terminal/browser 二进制帧。
- [mobile/app/h/[hostId]/index.tsx](../../../../open-ai-desktop/orca/mobile/app/h/[hostId]/index.tsx)  
  Host detail/worktree list 页面，读取 `worktree.ps`、`repo.list`、`ui.get`，并发送 worktree 操作。
- [mobile/app/h/[hostId]/session/[worktreeId].tsx](../../../../open-ai-desktop/orca/mobile/app/h/[hostId]/session/[worktreeId].tsx)  
  Worktree session 页面，订阅 terminal/session tabs，驱动 terminal、browser、file、markdown、source-control 等面板。
- [mobile/src/worktree/resume-worktree.ts](../../../../open-ai-desktop/orca/mobile/src/worktree/resume-worktree.ts)  
  首页 Resume card 的 worktree 选择策略：优先桌面 active worktree，再按最近输出兜底。
- [mobile/src/transport/rpc-client.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/rpc-client.test.ts)  
  验证连接超时、stale socket、stream unsubscribe、reconnect replay 等 RPC client 行为。
- [mobile/src/transport/pairing.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pairing.test.ts)  
  验证 pairing URL/code 的解析兼容性。
- [mobile/src/transport/pair-confirm-state.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pair-confirm-state.test.ts)  
  验证 confirm route 对 code 和错误状态的解析。
- [mobile/src/transport/pairing-connection-attempt.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pairing-connection-attempt.test.ts)  
  验证 pairing 阶段的整体超时与 dispose 行为。
- [mobile/src/worktree/resume-worktree.test.ts](../../../../open-ai-desktop/orca/mobile/src/worktree/resume-worktree.test.ts)  
  验证 Resume card 优先桌面 active worktree，再 fallback 到最近输出。
- [mobile/src/transport/rpc-client-live-recovery.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/rpc-client-live-recovery.test.ts)  
  opt-in 实网/真实计时恢复 harness，覆盖 foreground probe 和 parked retry loop recovery。

## 智慧（社区）

- [Expo Router 文档](https://docs.expo.dev/router/introduction/)  
  用于理解 `mobile/app/` 的文件式路由、dynamic route 和 Stack 布局。
- [Expo SecureStore 文档](https://docs.expo.dev/versions/latest/sdk/securestore/)  
  用于理解移动端为何把 pairing token 放到设备级安全存储。

## 空白

- 本主题不展开 `TerminalWebView`、PR review、browser screencast 和文件编辑面板的所有细节；它们适合在 L2/L3 中按链路或 API 单独拆。

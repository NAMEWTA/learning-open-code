# 移动端配对与会话恢复全链路资源

## 知识

- [src/renderer/src/components/settings/MobilePane.tsx](../../../../open-ai-desktop/orca/src/renderer/src/components/settings/MobilePane.tsx)  
  桌面设置页移动端配对入口，生成 QR、选择网络地址、轮询 paired devices。
- [src/renderer/src/components/settings/MobileNetworkInterfaceSection.tsx](../../../../open-ai-desktop/orca/src/renderer/src/components/settings/MobileNetworkInterfaceSection.tsx)  
  网络接口选择 UI，解释 LAN/Tailscale 地址选择对二维码 endpoint 的影响。
- [src/renderer/src/components/settings/MobilePairingQrSection.tsx](../../../../open-ai-desktop/orca/src/renderer/src/components/settings/MobilePairingQrSection.tsx)  
  QR 与 paste pairing code 展示，说明二维码和复制码共享同一个 pairing URL。
- [src/main/ipc/mobile.ts](../../../../open-ai-desktop/orca/src/main/ipc/mobile.ts)  
  main IPC handler，生成 mobile scope QR、runtime scope pairing URL、列 paired devices、撤销设备。
- [src/main/runtime/runtime-rpc.ts](../../../../open-ai-desktop/orca/src/main/runtime/runtime-rpc.ts)  
  runtime pairing offer、WebSocket/E2EE channel、device token 验证、mobile allowlist 和 `status.get` scope 注入。
- [src/main/runtime/device-registry.ts](../../../../open-ai-desktop/orca/src/main/runtime/device-registry.ts)  
  每台设备的 token registry，支持 pending token 合并、显式 rotate、lastSeen、scope 和 revocation。
- [src/main/runtime/e2ee-keypair.ts](../../../../open-ai-desktop/orca/src/main/runtime/e2ee-keypair.ts)  
  桌面端持久 E2EE keypair，public key 进入 pairing offer，secret key 只留在 runtime userData。
- [src/main/runtime/mobile-pairing-files.ts](../../../../open-ai-desktop/orca/src/main/runtime/mobile-pairing-files.ts)  
  mobile pairing 凭据文件名与迁移单元，保证 registry 和 E2EE keypair 不分裂。
- [src/main/runtime/rpc/e2ee-channel.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/e2ee-channel.ts)  
  桌面 WebSocket 的 E2EE 握手状态机，控制 `e2ee_hello`、`e2ee_auth`、认证后消息转发。
- [src/main/runtime/rpc/ws-transport.ts](../../../../open-ai-desktop/orca/src/main/runtime/rpc/ws-transport.ts)  
  WebSocket transport，负责连接上限、pre-auth timeout、heartbeat、clientId close cleanup。
- [src/shared/pairing.ts](../../../../open-ai-desktop/orca/src/shared/pairing.ts)  
  桌面/shared pairing URL 编解码 contract，定义 `orca://pair?code=...` 和 optional scope。
- [src/shared/runtime-types.ts](../../../../open-ai-desktop/orca/src/shared/runtime-types.ts)  
  `DeviceScope` 和 `RuntimeStatus.deviceScope` 类型来源。
- [mobile/README.md](../../../../open-ai-desktop/orca/mobile/README.md)  
  移动端开发和网络要求说明；其中 QR payload 的 TLS fingerprint 描述已过期，payload 以 `src/shared/pairing.ts` 为准。
- [mobile/app/_layout.tsx](../../../../open-ai-desktop/orca/mobile/app/_layout.tsx)  
  Expo 根布局，安装 `RpcClientProvider`，处理 cold/warm deep link 到 `/pair-confirm`。
- [mobile/app/pair.tsx](../../../../open-ai-desktop/orca/mobile/app/pair.tsx)  
  `orca://pair` route redirect，读取 URL/code 并跳转到确认页。
- [mobile/app/pair-scan.tsx](../../../../open-ai-desktop/orca/mobile/app/pair-scan.tsx)  
  QR scan 和 paste flow，扫码后直接连接、`status.get` 验证并保存 host。
- [mobile/app/pair-confirm.tsx](../../../../open-ai-desktop/orca/mobile/app/pair-confirm.tsx)  
  deep link 确认页，解析 code、连接桌面、验证状态、保存 host。
- [mobile/src/transport/pairing.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pairing.ts)  
  mobile 侧 pairing parser，兼容 QR URL、query/hash code、裸 base64 payload。
- [mobile/src/transport/pair-confirm-state.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pair-confirm-state.ts)  
  confirm route state 解析，区分 missing、invalid 和 ready。
- [mobile/src/transport/pairing-connection-attempt.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pairing-connection-attempt.ts)  
  pairing 专用 25 秒总超时和临时 client cleanup。
- [mobile/src/transport/types.ts](../../../../open-ai-desktop/orca/mobile/src/transport/types.ts)  
  mobile `PairingOffer`、`HostProfile`、`StoredHostProfile` 和 connection state 类型。
- [mobile/src/transport/host-store.ts](../../../../open-ai-desktop/orca/mobile/src/transport/host-store.ts)  
  host metadata + device token 持久化；native token 进入 SecureStore，web fallback 才用 AsyncStorage。
- [mobile/src/transport/e2ee.ts](../../../../open-ai-desktop/orca/mobile/src/transport/e2ee.ts)  
  mobile E2EE primitive，使用 tweetnacl、ExpoCrypto、base64 text frame 和 binary frame。
- [mobile/src/transport/rpc-client.ts](../../../../open-ai-desktop/orca/mobile/src/transport/rpc-client.ts)  
  mobile WebSocket RPC client，E2EE 握手、request、stream replay、binary frame、foreground recovery。
- [mobile/src/transport/client-context.tsx](../../../../open-ai-desktop/orca/mobile/src/transport/client-context.tsx)  
  每 host 共享一个 `RpcClient`，负责 acquire/release、forceReconnect、foreground/network nudge。
- [mobile/src/transport/connection-revival-triggers.ts](../../../../open-ai-desktop/orca/mobile/src/transport/connection-revival-triggers.ts)  
  AppState active 与网络变化触发恢复探测。
- [mobile/app/index.tsx](../../../../open-ai-desktop/orca/mobile/app/index.tsx)  
  mobile home，加载 hosts、prime clients、聚合 worktree/account 状态、显示 Resume 卡片。
- [mobile/app/h/[hostId]/index.tsx](../../../../open-ai-desktop/orca/mobile/app/h/[hostId]/index.tsx)  
  host detail，复用 host client 读取 `worktree.ps`，进入 worktree session。
- [mobile/src/worktree/resume-worktree.ts](../../../../open-ai-desktop/orca/mobile/src/worktree/resume-worktree.ts)  
  单个 host 内的 Resume 选择策略：优先 desktop active，再按 lastOutputAt 回退；跨 host 排序在 `mobile/app/index.tsx`。
- [mobile/src/transport/pairing.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pairing.test.ts)  
  pairing parser 测试，覆盖 query/hash、lookalike route、裸 base64。
- [mobile/src/transport/pair-confirm-state.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pair-confirm-state.test.ts)  
  confirm route 状态测试，覆盖 valid URL、missing code、invalid code。
- [mobile/src/transport/pairing-connection-attempt.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/pairing-connection-attempt.test.ts)  
  pairing 总超时和 dispose cleanup 测试。
- [mobile/src/transport/rpc-client.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/rpc-client.test.ts)  
  mobile RPC client 测试，覆盖 foreground recovery、auth retry、request timeout、stream replay。
- [mobile/src/transport/rpc-client-live-recovery.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/rpc-client-live-recovery.test.ts)  
  opt-in real WebSocket/E2EE 恢复复现 harness。
- [mobile/src/transport/connection-revival-triggers.test.ts](../../../../open-ai-desktop/orca/mobile/src/transport/connection-revival-triggers.test.ts)  
  App foreground 和网络恢复触发 nudge 的测试。
- [mobile/src/worktree/resume-worktree.test.ts](../../../../open-ai-desktop/orca/mobile/src/worktree/resume-worktree.test.ts)  
  Resume 选择策略测试。
- [src/main/ipc/mobile.test.ts](../../../../open-ai-desktop/orca/src/main/ipc/mobile.test.ts)  
  mobile IPC 测试，覆盖 tailnet address 优先、mobile/runtime scope、paired device filtering。
- [src/main/runtime/runtime-rpc.test.ts](../../../../open-ai-desktop/orca/src/main/runtime/runtime-rpc.test.ts)  
  runtime pairing、E2EE auth、revocation、mobile allowlist、`status.get` scope 注入等测试。
- [src/main/runtime/mobile-rpc-allowlist.test.ts](../../../../open-ai-desktop/orca/src/main/runtime/mobile-rpc-allowlist.test.ts)  
  静态扫描 mobile app 使用的 RPC，确保 allowlist 和 runtime method manifest 不漂移。
- [src/main/runtime/mobile-pairing-userdata-path.test.ts](../../../../open-ai-desktop/orca/src/main/runtime/mobile-pairing-userdata-path.test.ts)  
  pairing registry 与 E2EE keypair userData 路径稳定性和迁移测试。

## 智慧（社区）

- 本主题暂不依赖外部社区资料。关键理解来自 Orca 自己的桌面 runtime、Electron IPC、Expo mobile 和测试。

## 空白

- Expo SecureStore 的平台差异、iCloud/Keystore 恢复边界可在移动安全主题里补。
- TLS/wss、证书固定与 overlay network 安全模型没有在本主题展开。
- App Store 版本滞后、protocol compatibility hard-block 可在移动协议兼容主题里补。

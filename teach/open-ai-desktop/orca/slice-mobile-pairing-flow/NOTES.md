# 移动端配对与会话恢复全链路笔记

## 核心判断

- 桌面 Settings 的 QR 不是单纯地址；它是 `orca://pair?code=...`，shared payload 里有 endpoint、deviceToken、publicKeyB64 和 optional scope。
- `src/main/ipc/mobile.ts` 只负责把 renderer 请求转成 runtime pairing offer；真正发 token 和 public key 的边界在 `OrcaRuntimeRpcServer.createPairingOffer()`。
- `DeviceRegistry` 把每台设备变成独立 token，并记录 scope；mobile scope 会经过 runtime 的 mobile RPC allowlist。
- QR 生成会合并未扫描的 pending token；显式 regenerate 才 rotate pending token。
- `lastSeenAt === 0` 的 mobile device 只是已生成二维码，还没有真正配对；桌面 paired devices 列表会过滤它。
- 手机端 QR scan、deep link、paste code 都先解析成 mobile 本地 `PairingOffer`；该 schema 当前不暴露 `scope`，解析成功也不等于配对成功。
- 手机端配对的可信验证点是临时 `RpcClient` 成功完成 E2EE auth 后调用 `status.get`。
- `pair-scan.tsx` 和 `pair-confirm.tsx` 都使用 25 秒总超时；超时会 dispose 临时 client，避免后台继续连。
- 保存 host 是第二阶段：`saveHost()` 成功后才进入 `/h/:hostId`；连接成功但保存失败会显示独立错误。
- native mobile 的 deviceToken 不保存在 AsyncStorage host metadata，而是 SecureStore；AsyncStorage 只保存 endpoint/publicKey/name/lastConnected。
- App 启动后 `RpcClientProvider` 按 host 共享连接；屏幕只 acquire/release，不为每个页面新建 WebSocket。
- 已保存 host 的恢复不是重新扫码，而是 `loadHosts()` 合并 SecureStore token 后重建 `connect(endpoint, token, publicKey)`。
- `rpc-client.ts` 的 foreground/network recovery 是会话恢复关键：connected 时发 `status.get` probe，reconnecting 时重置 backoff。
- 首页 Resume 卡片依赖已连接 host 的 worktree snapshot；先优先本机 last visited，再按 host `lastConnected` 跨 host 遍历，每个 host 内才回退到 desktop active 或 lastOutputAt。
- runtime 的 `status.get` 会注入 authenticated device scope，旧 pairing/saved clients 也能知道自己是 mobile 还是 runtime。

## 容易误解

- 复制 pairing code 和扫描 QR 是同一份 `pairingUrl`，不是两种凭据。
- mobile pairing URL 带 bearer token；它必须当成敏感材料处理，不能写进日志或学习记录样例。
- `scope` 在桌面/shared pairing payload 中存在，但 mobile 本地不依赖它；runtime 仍以 deviceToken registry、allowlist 和 `status.get.deviceScope` 为准。
- `ws://0.0.0.0:6768` 不是手机可连地址；renderer/main 会选择 LAN 或 tailnet IP 写进 QR endpoint。
- `status.get` 成功说明 token 和 E2EE 通道可用，不保证后续业务 RPC 都允许；mobile scope 仍会过 allowlist。
- host 详情/会话页看到 reconnect，不代表 pairing 丢失；只有 auth retry 耗尽才进入 `auth-failed` 并提示 re-pair。

## 后续可深挖

- mobile terminal/browser streaming 的 binary frame 和订阅 replay。
- paired device revocation 后 server 如何 terminate active WebSocket 并清理 runtime presence state。
- protocol compatibility 如何让 mobile/desktop 版本滞后时硬阻断。
- Tailscale/ZeroTier 和 public `ws://` endpoint 的安全提示与诊断。

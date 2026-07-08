# 使命：移动端配对与会话恢复全链路

## 为什么

用户要系统学习 Orca，需要能把桌面端生成二维码、手机扫码、WebSocket/E2EE 握手、设备令牌保存和后续会话恢复串成一条可验证链路。这个 L2 主题把 renderer 设置页、main IPC、runtime pairing registry、Expo pairing screens、mobile RPC client 和首页 Resume 入口连起来。

## 成功的样子

- 能解释桌面二维码里真正携带的四类信息：endpoint、deviceToken、publicKeyB64 和 scope。
- 能从 Settings 里的 Generate QR Code 追到 `src/main/ipc/mobile.ts`、`OrcaRuntimeRpcServer.createPairingOffer()` 和 `DeviceRegistry`。
- 能说明手机端 QR、deep link、paste code 三个入口如何收敛到 `PairingOffer` 和 `status.get` 验证。
- 能区分配对成功、连接验证成功、host profile 本地保存成功这三个阶段。
- 能解释设备令牌为什么保存在 SecureStore，而不是直接放在 AsyncStorage host metadata 里。
- 能说明已配对 host 之后如何通过共享 `RpcClientProvider`、foreground probe 和 Resume 卡片恢复会话。

## 约束条件

- 短课控制在 15 分钟内，只建立主路径和关键安全边界。
- 参考页可以展开桌面/mobile 双侧文件与测试护栏，但所有结论必须能回到 Orca 当前源码。
- 本主题是 L2 跨模块切片，建立在主进程 Runtime、主进程 IPC、共享协议和移动端 Companion 的 L1 主题之上。

## 不在范围内

- 不深入 terminal/browser/file 等移动端业务面板的完整实现。
- 不讲 Expo 构建、App Store 发布、native notification 权限和 mobile UI 视觉细节。
- 不覆盖 web/runtime scope 的远程 Orca Server 客户端完整链路；这里只在对比 scope 时点到为止。

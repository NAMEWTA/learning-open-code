# 教学笔记：插件系统、插件 API 与运行时加载

- 本轮角色是 teach-goal 的 L1 内容 worker，只写 `teach/open-productivity/super-productivity/module-plugin-system/**`。
- 关键表述必须对齐 Angular L1：`PLUGIN_INITIALIZER_PROVIDER` 只是 `PLUGIN_INITIALIZER` token 接线点，不是当前插件运行时初始化链。
- 桌面 OAuth 与 Node 执行必须明确归入 Electron 主进程能力；renderer 只能通过 `window.ea`、`PluginOAuthBridgeService`、`PluginBridgeService` 等受控桥进入。
- 后续 L2 线索：Node execution grant/consent 安全模型、OAuth PKCE loopback 链路、issue provider 插件到 two-way sync adapter、iframe 插件消息桥、上传插件 zip/cache 生命周期。

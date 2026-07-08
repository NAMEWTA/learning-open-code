# 便签

- 本主题是 L2 垂直切片，主入口固定为 `lessons/0001-flow-map.html`，完整参考固定为 `reference/desktop-startup-flow-map.html`。
- 链路超过 4 个关键阶段，已拆为 3 节短课：全链路地图、main/process 到窗口装载、renderer/Router 到首屏与边界。
- 关键边界：桌面模式下 backend 启动失败不会立刻退出；失败状态会经 main IPC、preload 和 renderer failure dialog 进入首屏路径。
- 审计前需要先运行 snapshot 生成或手工保持 `SNAPSHOT.md` 摘要与实际课程、参考、资产数量一致。

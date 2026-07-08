# 使命：REST/WS adapter 替代传统 IPC 的设计

## 为什么
用户需要维护 AionU 的 renderer-backend contract，在不破坏现有 renderer 调用面的前提下判断某个能力应继续走 Electron IPC，还是迁到 aioncore REST/WS。掌握本主题后，用户可以把 `ipcBridge` 这个历史名字和真实传输层拆开看，减少改接口、补测试和排查事件回流时的误判。

## 成功的样子
- 能解释为什么 AionU 保留 `ipcBridge.*.invoke/on` 形状，却把大量业务能力改成 HTTP 和 WebSocket。
- 能读懂 `httpBridge.ts` 的 provider-like invoke、错误封装、响应解包和 WS emitter 机制。
- 能为新增或修复 adapter 能力选择 REST、WS、IPC、mapper、E2E helper 的正确组合。

## 约束条件
- 本轮是 L4 深度剖析，不重复 L1 的完整接口清单。
- 每节短课控制在 15 分钟内，只保留少量关键源码证据。
- 只写入 `teach/open-ai-desktop/AionU/deep-dive-adapter-rest-ws/`，不修改源项目。

## 不在范围内
- 不系统讲解 aioncore 后端路由实现。
- 不重写 `common/adapter/ipcBridge.ts` 的所有 API 表。
- 不覆盖 Electron preload、WebUI、conversation、team、cron、skills 的完整垂直切片。

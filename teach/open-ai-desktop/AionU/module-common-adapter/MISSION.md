# 使命：Common adapter 与 API 映射

## 为什么
需要把 AionU 的 renderer 和 main/backend 边界读清楚，才能判断一个业务能力为什么会落到 `ipcBridge`、什么时候应该继续走 Electron IPC、什么时候已经被改写成 REST + WebSocket。学完这个主题，后续新增桌面能力、排查桥接故障或继续做模块级教学时，都能更快定位正确落点。

## 成功的样子
- 能从 `ipcBridge.*` 的某个接口名，判断它最终是走 `ipcRenderer.invoke`、HTTP `/api/*`，还是 WebSocket 事件。
- 能说清 `preload/main.ts`、`common/adapter/main.ts`、`httpBridge.ts`、`process/bridge/*` 在同一条调用链里的分工。
- 能用一个具体例子解释 mapper 为什么存在，以及它在“前端类型 ↔ 后端 wire contract”之间修正了什么。

## 约束条件
- 本轮只做 L1 模块总览，不展开某个单独业务域的全部细节。
- lesson 保持 15 分钟短课，接口全表和 mapper 清单下沉到 `reference/`。
- 只基于当前仓库源码、现有教学文档和官方文档建立结论，不修改源项目。

## 不在范围内
- 不讲 renderer 页面本身的 React 组织方式；相关内容回看 `module-renderer-core`。
- 不逐个深入 `process/bridge/*` 的 provider 实现细节；这里只选代表链路。
- 不覆盖 AionU backend Rust 端的内部实现，只讨论前端公共适配层如何对接它。

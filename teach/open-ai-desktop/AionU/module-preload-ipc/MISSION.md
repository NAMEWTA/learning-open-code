# 使命：Preload 与 IPC 安全边界

## 为什么
用户需要在阅读 AionU 的 Electron 桌面端时，快速判断 renderer 到 main 的能力边界，避免把“前端能做什么”和“主进程必须代做什么”混在一起。掌握这个模块后，用户可以更稳地追踪安全相关改动、定位 IPC 故障，并评估新增桥接接口是否越权。

## 成功的样子
- 能解释 `preload/main.ts` 为什么只暴露受控的 `electronAPI`、同步状态和托盘事件，而不直接开放 Electron/Node 原语。
- 能从 `common/adapter/main.ts` 说清 renderer `emit`、main `provider`、窗口广播三段式链路。
- 能区分主窗口 preload 与 pet 多窗口 preload 的职责差异，并指出它们各自依赖的主进程处理器。

## 约束条件
- 本轮只做 L1 模块总览，课程必须是 15 分钟内可完成的短课。
- lesson 聚焦“preload 如何限制 renderer 能力边界”，完整 channel 清单下沉到 reference。
- 讲解以仓库源码和测试为主，不扩写 Electron 通用安全百科。

## 不在范围内
- 不展开 renderer 侧 React 业务页面如何消费每个接口。
- 不深入 backend HTTP/WS adapter 的完整 REST 设计。
- 不覆盖桌面 pet 的动画逻辑与窗口布局细节。

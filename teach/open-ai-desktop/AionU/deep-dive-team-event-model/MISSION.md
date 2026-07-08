# 使命：Team Mode 事件模型

## 为什么
维护 AionU Team Mode 的开发者需要能判断一次 Team run 的 UI 状态到底来自 REST ack、WebSocket 事件、结构变更 reconcile，还是 slot 级 gate。掌握这个模型后，排查“某个成员输入框被误锁”“run 已结束但按钮仍忙”“新增成员后状态串扰”等问题时，可以直接定位到状态合成边界。

## 成功的样子
- 能解释 `ITeamRunAck` 如何被转成 run event，并为什么不能只等 WebSocket。
- 能区分团队级 run、成员 child turn、slot work 三层状态。
- 能判断哪些结构事件必须触发 `getRunState` reconcile。
- 能指出现有 E2E 对 send/run event 全链路覆盖不足的位置。

## 约束条件
- 本主题只写入 `teach/open-ai-desktop/AionU/deep-dive-team-event-model/`。
- 每节 lesson 控制在 15 分钟内，源码片段少而精，详细表格放入 reference。
- 以真实源码、既有课程和测试文件为证据，不伪造事件或测试覆盖。

## 不在范围内
- 不重画 Team 创建和运行 flow map。
- 不讲 aioncore 内部 Team 调度算法。
- 不修改 AionU 源码或补测试实现。

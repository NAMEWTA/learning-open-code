# 教学笔记：Team Mode 事件模型

## 注意事项

- 本主题聚焦 renderer 侧 Team run event model；后端如何产生 `team.run*` 与 `team.childTurn*` 事件仍属于后续缺口。
- E2E 证据必须和源码证明分开表述，不能把 UI 发送测试夸大成 ack/reducer 合并顺序测试。

# 使命：Team 创建并运行全链路

## 为什么
这次切片要帮助学习者从一个可见的产品动作出发，追清 AionU Team Mode 如何创建团队、生成成员 slot、复用会话运行时，并把 Team run 的状态事件回流到页面。掌握这条链路后，学习者可以判断 Team 功能问题到底落在 UI 状态、common adapter、backend contract、运行态事件还是 E2E 预期上。

## 成功的样子
- 能从创建 Team 的真实入口代码说清请求 payload 怎样形成，并指出创建后页面如何进入 `/team/:id`。
- 能按层次解释 Team 页面、成员 slot、conversation runtime、common adapter/HTTP 与 WebSocket 事件各自负责什么。
- 能用 E2E 证据验证“创建团队”和“添加成员”两条关键路径，并识别至少一个边界失败路径。

## 约束条件
- 源项目 `open-ai-desktop/AionU/` 只读。
- 本主题只写入 `teach/open-ai-desktop/AionU/slice-team-run/`。
- 短课控制在 15 分钟内完成，详细清单分流到 `reference/team-run-flow-map.html`。

## 不在范围内
- 不讲 aioncore 内部 Team 调度算法实现。
- 不重写 `module-team-mode`、`module-common-adapter` 或 `module-conversation-runtime` 的 L1 总览。
- 不修改项目级索引、进度台账或源项目代码。

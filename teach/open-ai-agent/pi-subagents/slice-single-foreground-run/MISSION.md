# 使命：单次前台 subagent run 全链路

## 为什么
学习者已完成 L0 项目地图与 L1 的 extension-runtime、agent-system、runs-execution 模块导览，现在需要把「一次 `{ agent, task }` 调用」从 Pi tool 入口追到 child Pi 进程退出、父会话拿到 `SingleResult` 的完整路径串起来。没有这个垂直切片，读 executor 源码时容易把注册层、门卫层、spawn 层和 JSONL 解析层混在一起。

## 成功的样子
- 能按顺序说出 6–8 个关键跳点：tool 注册 → executor 门卫 → `runSinglePath` → `runSync` → `getPiSpawnCommand` → child stdout → `SingleResult` → tool result。
- 能判断一次调用为何走前台 single 而不是 async、parallel 或 chain。
- 能指出 `test/integration/single-execution.test.ts` 验证了哪些链路环节。
- 遇到细节（model fallback、acceptance、control event）知道该去参考页还是后续短课。

## 约束条件
- 本节只覆盖单次前台 run；不展开 parallel、chain、async。
- lesson 控制在 15 分钟内，正文 800–1200 字；长表与索引放 reference。
- 源码路径以 `open-ai-agent/pi-subagents/src/` 为准。

## 不在范围内
- 后台 async runner 生命周期与 wait/status。
- chain 的 `{previous}` 与 parallel 限流。
- intercom detach、nested fanout 的完整协议。

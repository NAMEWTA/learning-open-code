# 使命：Native supervisor 与 intercom 协调全链路

## 为什么
学习者已经通过 L1 intercom 模块知道 bridge、supervisor channel、result intercom 三条通道各自负责什么，但还不清楚一次前台 subagent run 如何把三者串起来：启动前如何注入协调工具、运行中如何通过文件通道请求父会话决策、完成后如何把 grouped payload 送回父会话并压缩普通 tool result。掌握这条 L2 垂直切片后，可以独立排查「子 agent 没有 contact_supervisor」「need_decision 发出但父端看不到 pending」「run 完成却只有简短 receipt 没有完整输出」等问题。

## 成功的样子
- 能口述从 `resolveIntercomBridge` 到 `maybeBuildForegroundIntercomReceipt` 的五段链路，并指出每段对应源码文件。
- 能区分 bridge 注入、supervisor 文件通道、result event delivery 三种协调时机与承载位置。
- 能说出 `contact_supervisor` 三种 reason 的等待语义，以及父端 `subagent_supervisor` reply 如何写回 reply 文件。
- 遇到 delivery 未确认或 bridge inactive 时，知道会回退 legacy foreground output 而非误以为丢结果。

## 约束条件
- 课程按 15 分钟短课合约拆分；长表、消息类型与测试索引放入 `reference/`。
- 聚焦 foreground 主路径与列出的 intercom 源文件；async result-watcher 仅作交叉引用，不展开 async 生命周期细节。
- 产出写入 `teach/open-ai-agent/pi-subagents/slice-native-supervisor-intercom/`。

## 不在范围内
- 不逐行讲解 `extension/fanout-child.ts` 嵌套 follow-up 与 live resume 控制面。
- 不展开 TUI 如何渲染 supervisor request 消息（`module-tui-rendering`）。
- 不覆盖 async watcher 完整 delivery 链路（留给 `slice-async-result-intercom-delivery` 候选主题）。

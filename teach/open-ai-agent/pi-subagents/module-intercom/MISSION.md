# 使命：父子进程 intercom 与 supervisor 协调模块

## 为什么
学习者需要能判断 pi-subagents 中父进程、子进程和结果回传之间的协调责任，避免把“问 supervisor”“给子进程注入工具”“完成后回传结果”混成同一条通道。掌握这个边界后，后续排查子 agent 卡住、结果丢失、异步 resume 失败或 intercom 配置失效时，可以快速定位到正确模块。

## 成功的样子
- 能画出 `intercom-bridge`、`native-supervisor-channel`、`result-intercom` 三者的职责边界。
- 能解释 `contact_supervisor` 什么时候阻塞等待回复，什么时候只排队进度更新。
- 能根据结果是否成功经由 intercom 送达，判断 foreground/async 路径应该看哪个调用方和测试。
- 能识别后续 L2 切片：阻塞问答、异步结果回传、resume/live follow-up、嵌套子 agent 控制。

## 约束条件
- 本主题是 L1 模块总览，短课只聚焦职责边界；接口细节、长矩阵和测试证据放入参考页。
- 源码引用限定在 intercom 三个核心文件，调用方和测试只作佐证。
- 不修改源码、项目索引或 teach-goal 进度文件。

## 不在范围内
- 不讲完整 subagent 执行器、异步 job tracker、fanout 执行模型的所有分支。
- 不讲外部 pi-intercom 扩展实现，只讲 pi-subagents 自带 native supervisor channel 与 fallback 行为。
- 不覆盖 UI widget、slash bridge、prompt template bridge 等相邻扩展功能。

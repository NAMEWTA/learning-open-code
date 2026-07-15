# 使命：定时任务全链路追踪

## 为什么
理解 Hermes Agent 如何将用户的一句自然语言定时指令（如"每天早上 9 点告诉我天气"）转化为一条跨越七个阶段的、防崩溃、防注入、多平台投递的可靠自动化流水线。掌握这条链路后，能够定位 cron 任务"静默失败"或"重复触发"等生产问题。

## 成功的样子
- 能画出从 `create_job` 到 `_deliver_result` 的完整调用时序图
- 能解释 lifecycle_guard 在创建时和 prompt injection 扫描在运行时各阻止了什么攻击
- 能说明双线程池（parallel + sequential）的分区策略及其对 workdir 作业的隔离意义

## 约束条件
- 基于 L1-cron 模块导览和 L1-gateway 消息网关的前置知识
- 短课格式：800-1200 中文字，≤4 章节，≤3 代码片段

## 不在范围内
- croniter 库的底层实现细节
- 各消息平台适配器的协议级实现
- 外部 scheduler provider（Chronos）的集成细节

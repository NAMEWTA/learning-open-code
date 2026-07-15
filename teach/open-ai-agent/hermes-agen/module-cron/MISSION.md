# 使命：定时任务调度 — croniter 集成、自然语言定时、多平台投递

## 为什么
理解 Hermes Agent 的 cron 调度引擎如何以自然语言描述定时任务并自动投递到 Telegram/Discord/Slack/企业微信等 19+ 个平台，从而能设计自己的 Agent 自动化工作流，让 AI agent 定时执行代码审查、日报生成、邮件监控等无需人工触发的任务。

## 成功的样子
- 能读懂 cron/ 目录中 10 个 Python 文件的职责分工与调度链路
- 能解释 tick() → get_due_jobs() → run_job() → deliver 的完整执行流程
- 能说出 croniter 如何将 "every 30m" 等自然语言描述转换为标准 cron 表达式
- 能说明定时任务如何自动路由到不同聊天平台的 home channel / origin / 显式 target
- 能识别 lifecycle_guard.py 和 prompt injection 扫描等安全防护机制的设计意图

## 约束条件
- 15 分钟内完成本节短课，聚焦架构理解，不涉及运行调试
- 中文教学，代码标识符保留原文

## 不在范围内
- 手动运行 gateway daemon 或安装 systemd/launchd 服务（运维层面）
- 编写新的 blueprint 或自定义 scheduler provider 插件
- 修改 cron 源码进行二次开发

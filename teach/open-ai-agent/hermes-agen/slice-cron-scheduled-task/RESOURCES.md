# 定时任务全链路 资源

## 知识

- [cron/scheduler.py](../../../open-ai-agent/hermes-agen/cron/scheduler.py) — tick() 入口、run_job 执行体、_build_job_prompt 拼装、_deliver_result 投递，全链路核心调度文件（3637 行）
- [cron/jobs.py](../../../open-ai-agent/hermes-agen/cron/jobs.py) — Job CRUD、parse_schedule 自然语言解析、croniter 集成、get_due_jobs 到期判定、claim_dispatch 去重（2033 行）
- [cron/lifecycle_guard.py](../../../open-ai-agent/hermes-agen/cron/lifecycle_guard.py) — 四分支正则阻断 gateway 自杀命令，#30719 SIGTERM-respawn 循环防护（141 行）
- [cron/scheduler_provider.py](../../../open-ai-agent/hermes-agen/cron/scheduler_provider.py) — CronScheduler ABC、InProcessCronScheduler 60s 守护线程、per-profile 隔离
- [gateway/delivery.py](../../../open-ai-agent/hermes-agen/gateway/delivery.py) — DeliveryRouter 多平台路由、live-adapter → standalone 四级回退、dead-target 自愈

## 智慧（社区）

- [Hermes Agent GitHub Issues](https://github.com/NPC-Dao/hermes-agent/issues) — 搜索 cron、scheduler、lifecycle_guard 标签查看真实生产问题讨论
- [croniter 文档](https://pypi.org/project/croniter/) — cron 表达式解析库的官方文档

## 空白

- 外部 scheduler provider（Chronos / NAS）的 Phase 4 实现尚未开源，目前仅有接口定义
- 投递层对 Matrix E2EE 房间的加密路径仅在使用 live adapter 时生效，standalone 路径不支持 E2EE

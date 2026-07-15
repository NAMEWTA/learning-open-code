# 定时任务调度 资源

## 知识

- [croniter PyPI 页面](https://pypi.org/project/croniter/)
  croniter 库官方文档，支持标准 cron 表达式与自然语言 "every 30m" 描述。适用于：理解 cron/ 目录中 `HAS_CRONITER` 条件导入和 `get_due_jobs()` 中的时间计算逻辑。

- [Hermes Agent cron 模块源码 — cron/jobs.py (2033 行)](../../open-ai-agent/hermes-agen/cron/jobs.py)
  作业存储、CRUD 操作、文件锁、job 字段校验。适用于：理解 job 生命周期管理与 per-profile 隔离设计。

- [Hermes Agent cron 模块源码 — cron/scheduler.py (3637 行)](../../open-ai-agent/hermes-agen/cron/scheduler.py)
  tick() 调度循环、run_job() agent 生成、platform delivery、prompt injection 扫描。适用于：理解完整的"定时触发 → agent 执行 → 平台投递"链路。

- [Hermes Agent cron 模块源码 — cron/scheduler_provider.py (194 行)](../../open-ai-agent/hermes-agen/cron/scheduler_provider.py)
  CronScheduler 抽象基类与 InProcessCronScheduler 实现。适用于：理解 scheduler provider 接口设计（Axis B 触发器抽象）。

- [Hermes Agent cron 模块源码 — cron/blueprint_catalog.py (713 行)](../../open-ai-agent/hermes-agen/cron/blueprint_catalog.py)
  参数化自动化蓝图，表单渲染 → slash command → cron job 创建。适用于：理解 BlueprintSlot 类型系统和 WEEKDAY_PRESETS 等预设。

- [Hermes Agent cron 模块源码 — cron/suggestions.py (260 行)](../../open-ai-agent/hermes-agen/cron/suggestions.py)
  建议式 cron job 注册，consent-first 设计，dedup_key 防重复推送。适用于：理解 catalog/blueprint/usage/integration 四种建议来源。

- [Hermes Agent cron 模块源码 — cron/lifecycle_guard.py (141 行)](../../open-ai-agent/hermes-agen/cron/lifecycle_guard.py)
  网关生命周期命令阻断，防止 agent 自毁循环。适用于：理解 _GATEWAY_LIFECYCLE_PATTERN 正则如何匹配 4 种命令分支。

- [Hermes Agent AGENTS.md](../../open-ai-agent/hermes-agen/AGENTS.md)
  Hermes 项目整体 AI 协作指南，包含 cron 模块的独立任务会话设计理念。

## 智慧（社区）

- [Hermes Agent Discord](https://discord.gg/hermes-agent)
  Hermes 官方 Discord 社区，discord 频道中有 cron-job 使用经验分享和自动化场景探讨。

- [Hermes Agent GitHub Issues](https://github.com/hermes-agent/hermes-agent/issues)
  搜索标签 `cron` 或 `scheduler`，可查看 cron 模块的实际故障报告和设计讨论。

## 空白

- croniter 库的内部实现原理（本课程聚焦于集成使用，不深入 croniter 算法细节）
- 外部 scheduler provider（如 Chronos NAS 调度）目前尚未集成，plugin 接口已预留但无实践案例
- Windows 平台上的 cron 行为差异（代码中 fcntl/msvcrt 有分支，但无实际测试报告）

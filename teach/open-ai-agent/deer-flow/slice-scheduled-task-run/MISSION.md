# 使命：scheduled task 创建与执行

## 为什么
我想在 deer-flow 里用定时任务让 lead agent 按 cron 或一次性计划自动跑 prompt，而不是每次手动点聊天。需要看清从前端创建任务到后台调度器真正触发 run 的完整链路，才能排查「任务建了但不跑」「跑了但线程不对」这类问题。

## 成功的样子
- 能在源码里按顺序指出：前端表单 → Gateway API → 持久化 → 调度轮询 → `launch_run` → 普通 run 生命周期
- 能解释 `context_mode`、`next_run_at`、lease 认领、`task_run` 记录各自扮演什么角色
- 能判断一次执行是 `scheduled` 触发还是手动 `trigger`，以及 run 完成后任务状态如何回写

## 约束条件
- 以 L2 垂直切片为主：一条主链路，不展开 pause/resume、i18n recipe 等旁支
- 课程控制在 15 分钟内，细节查参考页

## 不在范围内
- 调度器配置项逐项调参（`config.yaml` → `scheduler.*`）
- 前端 E2E 测试与 cron 表达式编辑器实现细节
- 自定义 agent 作为 `assistant_id` 的高级用法

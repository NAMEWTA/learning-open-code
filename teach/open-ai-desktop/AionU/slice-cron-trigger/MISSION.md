# 使命：Cron 任务创建与触发全链路

## 为什么

用户需要能从 AionU 的定时任务页面或 AI 对话创建入口，追踪一个 Cron 任务如何被创建、编辑、启停、立即执行，并最终反馈到会话状态与任务列表。掌握这条链路后，维护者可以定位“任务创建后列表不刷新”“立即执行没有跳到会话”“AI 修改任务变成新建任务”等问题。

## 成功的样子

- 能从 `ScheduledTasksPage`、`CreateTaskDialog`、`TaskDetailPage` 读出任务创建、编辑、启停和 run-now 的真实调用点。
- 能说明 renderer cron 页面、hook、common adapter、HTTP/WS 事件、会话侧 `localCronCommands` 和状态刷新之间的层级边界。
- 能用 Mermaid 时序图复述手动创建和立即触发的主路径。
- 能指出至少一个边界路径：手动任务不显示启停、run-now 防重入、缺失 timezone 修复、AI 更新保持 job id。
- 能用 E2E 与 unit 测试说明这些行为有哪些证据，哪些后端 scheduler 细节本切片未覆盖。

## 约束条件

- 源项目 `open-ai-desktop/AionU/` 只读。
- 本主题只写入 `teach/open-ai-desktop/AionU/slice-cron-trigger/`。
- 不修改项目级 `index.md`、`00-index.md`、`_progress.json`、`_progress.md`。
- L2 以 renderer + common adapter 的垂直切片为主，后端 scheduler 内部调度循环不在本轮深挖。

## 不在范围内

- 重写 Cron 后端调度器、数据库迁移或 API。
- 覆盖所有 skill suggest、通知、系统休眠与 cron skill 保存功能。
- 用目录或通配符代替具体源文件建立快照。

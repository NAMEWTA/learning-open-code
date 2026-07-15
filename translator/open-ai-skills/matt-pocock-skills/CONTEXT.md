# Matt Pocock Skills

一组由 Claude Code 加载的 agent skill（斜杠命令和行为）。技能按分类组织，由 `/setup-matt-pocock-skills` 生成的按仓库配置来消费。

## 术语

**Issue tracker（问题追踪器）**：
托管仓库 issues 的工具——GitHub Issues、Linear、本地 `.scratch/` markdown 约定或类似工具。`to-tickets`、`to-spec`、`triage` 和 `qa` 等技能从中读取和写入。
*避免使用*：backlog manager、backlog backend、issue host

**Issue（问题）**：
**Issue tracker** 中单个被追踪的工作单元——bug、任务、spec 或由 `to-tickets` 生成的切片。
*避免使用*：ticket（仅在引用称其为 ticket 的外部系统时使用）

**Triage role（分类角色）**：
在分类过程中应用于 **Issue** 的规范状态机标签（如 `needs-triage`、`ready-for-afk`）。每个角色通过 `docs/agents/triage-labels.md` 映射到 **Issue tracker** 中的真实标签字符串。

## 关系

- 一个 **Issue tracker** 包含多个 **Issue**
- 一个 **Issue** 一次携带一个 **Triage role**

## 已标记的歧义

- "backlog" 之前被用于同时表示*托管 issues 的工具*和其中的*工作体*——已解决：工具是 **Issue tracker**；"backlog" 不再作为领域术语使用。
- "backlog backend" / "backlog manager"——已解决：合并为 **Issue tracker**。

---
name: setup-matt-pocock-skills
description: "为本仓库配置工程化技能 —— 设置 issue tracker、triage 标签词汇表以及领域文档布局。在首次使用其他工程化技能之前运行一次。"
disable-model-invocation: true
---

# 配置 Matt Pocock 技能

搭建工程化技能所依赖的每仓库配置：

- **Issue tracker** —— issue 的存放位置（默认使用 GitHub；也支持本地 markdown）
- **Triage 标签** —— 五个标准 triage 角色使用的字符串
- **领域文档** —— `CONTEXT.md` 和 ADR 的存放位置，以及读取它们的消费方规则

这是一个提示驱动的技能，不是确定性脚本。先探索，展示发现结果，与用户确认，然后写入。

## 流程

### 1. 探索

查看当前仓库以了解其初始状态。读取已有内容；不要假设：

- `git remote -v` 和 `.git/config` —— 这是 GitHub 仓库吗？是哪一个？
- 仓库根目录下的 `AGENTS.md` 和 `CLAUDE.md` —— 是否存在？其中是否已有 `## Agent skills` 章节？
- 仓库根目录下的 `CONTEXT.md` 和 `CONTEXT-MAP.md`
- `docs/adr/` 和所有 `src/*/docs/adr/` 目录
- `docs/agents/` —— 此技能之前的输出是否已存在？
- `.scratch/` —— 表示本地 markdown issue tracker 约定已在使用中的标志
- `triage` 技能是否已安装？（此技能旁边的 `triage` 技能文件夹，或你的可用技能中有 `triage`。）这决定 B 节是否执行。
- Monorepo 信号 —— 是否有 `pnpm-workspace.yaml`、`package.json` 中的 `workspaces` 字段，或带有独立 `src/` 的非空 `packages/*`。这些只出现在真正的大型多包仓库中；它们的缺失意味着单上下文，而几乎每个仓库都是单上下文。

### 2. 展示发现结果并询问

总结已存在的和缺失的内容。然后按顺序处理各节 —— 一节，一个回答，再进入下一节。

每节先用推荐答案开场，让用户一个字就能接受。只有在选择真正产生分支时才给一行解释；当探索已经确定了答案时，整节跳过（`triage` 未安装时跳过 B 节，没有 monorepo 时跳过 C 节）。

**A 节 —— Issue tracker。**

> 解释："Issue tracker" 是本仓库 issue 的存放位置。`to-tickets`、`triage`、`to-spec` 等技能会从中读取和写入 —— 它们需要知道是调用 `gh issue create`、在 `.scratch/` 下写入 markdown 文件，还是遵循你描述的其他工作流。请选择你实际跟踪本仓库工作的地方。

默认倾向：这些技能是为 GitHub 设计的。如果 `git remote` 指向 GitHub，则建议使用 GitHub。如果 `git remote` 指向 GitLab（`gitlab.com` 或自托管主机），则建议使用 GitLab。否则（或用户偏好其他方式），提供：

- **GitHub** —— issue 存放在仓库的 GitHub Issues 中（使用 `gh` CLI）
- **GitLab** —— issue 存放在仓库的 GitLab Issues 中（使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI）
- **本地 markdown** —— issue 以文件形式存放在本仓库的 `.scratch/<feature>/` 下（适合个人项目或无远程仓库的场景）
- **其他**（Jira、Linear 等）—— 请用户用一段话描述工作流；技能将记录为自由文本

将选择记录到 `docs/agents/issue-tracker.md`。GitHub 和 GitLab 模板带有一个"PR 作为请求渠道"标志，默认**关闭** —— 保持关闭且不要主动提起；希望外部 PR 进入 triage 队列的用户之后可以在文件中自行翻转该标志。

**B 节 —— Triage 标签词汇表。** 如果 `triage` 技能未安装（探索已告诉你），整节跳过 —— 未安装的技能不需要标签。

如果已安装，只问一个问题：

> 你想保留默认的 triage 标签吗？（推荐：**是**）

默认值是五个标准角色，每个标签字符串等于其名称：`needs-triage`、`needs-info`、`ready-for-agent`、`ready-for-human`、`wontfix`。回答**是**就直接写入。只有当用户回答否 —— 通常是因为他们的 tracker 已使用其他名称（例如用 `bug:triage` 表示 `needs-triage`）—— 才收集覆盖项，让 `triage` 应用现有标签而不是创建重复标签。

**C 节 —— 领域文档。** 默认**单上下文** —— 仓库根目录下一个 `CONTEXT.md` + `docs/adr/`。这几乎适用于所有仓库；直接写入，无需询问。

只有当探索发现 monorepo 信号时，才提供**多上下文** —— 根目录下 `CONTEXT-MAP.md` 指向各上下文的 `CONTEXT.md` 文件。然后确认他们想要哪种布局。

### 3. 确认并编辑

向用户展示以下内容的草稿：

- 要添加到 `CLAUDE.md` / `AGENTS.md`（根据第 4 步的选择规则决定编辑哪个文件）的 `## Agent skills` 块
- `docs/agents/issue-tracker.md`、`docs/agents/domain.md` 的内容，以及 `docs/agents/triage-labels.md`（仅当 `triage` 已安装时）

让他们在写入之前编辑。

### 4. 写入

**选择要编辑的文件：**

- 如果 `CLAUDE.md` 存在，编辑它。
- 否则如果 `AGENTS.md` 存在，编辑它。
- 如果两者都不存在，询问用户要创建哪一个 —— 不要替他们选择。

当 `CLAUDE.md` 已存在时绝不创建 `AGENTS.md`（反之亦然）—— 始终编辑已存在的那个。

如果所选文件中已有 `## Agent skills` 块，原地更新其内容，而不是追加重复块。不要覆盖用户对周围章节的编辑。

该块的内容：

```markdown
## Agent skills

### Issue tracker

[关于 issue 跟踪位置的一句话总结]。参见 `docs/agents/issue-tracker.md`。

### Triage labels

[关于标签词汇表的一句话总结]。参见 `docs/agents/triage-labels.md`。

### Domain docs

[关于布局的一句话总结 —— "单上下文"或"多上下文"]。参见 `docs/agents/domain.md`。
```

仅当 `triage` 已安装且 B 节执行时，才包含 `### Triage labels` 子块并写入 `docs/agents/triage-labels.md`。未安装时两者都省略。

然后使用此技能文件夹中的种子模板作为起点，写入文档文件：

- [issue-tracker-github.md](./issue-tracker-github.md) —— GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) —— GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md) —— 本地 markdown issue tracker
- [triage-labels.md](./triage-labels.md) —— 标签映射（仅当 `triage` 已安装时）
- [domain.md](./domain.md) —— 领域文档消费方规则 + 布局

对于"其他"issue tracker，根据用户的描述从头编写 `docs/agents/issue-tracker.md`。

### 5. 完成

告诉用户配置已完成，以及哪些工程化技能现在将读取这些文件。提醒他们之后可以直接编辑 `docs/agents/*.md` —— 只有在需要切换 issue tracker 或从头重新配置时才需要重新运行此技能。

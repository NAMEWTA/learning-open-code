---
name: setup-matt-pocock-skills
description: 为本仓库配置工程技能——设置其 issue 追踪器、分类标签词汇和领域文档布局。在其他工程技能首次使用前运行一次。
disable-model-invocation: true
---

# 设置 Matt Pocock 的技能

搭建工程技能所依赖的每个仓库配置：

- **Issue 追踪器**——issue 存放的位置（默认为 GitHub；本地 markdown 也开箱支持）
- **分类标签**——用于五个规范分类角色的字符串
- **领域文档**——`CONTEXT.md` 和 ADR 存放的位置，以及读取它们的消费规则

这是一个提示词驱动的技能，而非确定性脚本。探索、展示发现、与用户确认、然后写入。

## 流程

### 1. 探索

查看当前仓库以了解其起始状态。阅读任何存在的内容；不要假设：

- `git remote -v` 和 `.git/config`——这是一个 GitHub 仓库吗？哪个？
- 仓库根目录的 `AGENTS.md` 和 `CLAUDE.md`——任一是否存在？其中是否已有 `## Agent skills` 部分？
- 仓库根目录的 `CONTEXT.md` 和 `CONTEXT-MAP.md`
- `docs/adr/` 和任何 `src/*/docs/adr/` 目录
- `docs/agents/`——此技能的先前输出是否已存在？
- `.scratch/`——本地 markdown issue 追踪器约定是否已在使用的标志

### 2. 展示发现并询问

总结存在什么和缺少什么。然后**逐一**引导用户完成三个决策——呈现一个部分，获取用户答案，然后移到下一个。不要一次性倾倒全部三个。

假设用户不知道这些术语是什么意思。每个部分以简短说明开始（它是什么、为什么这些技能需要它、如果选择不同会改变什么）。然后展示选择和默认值。

**A 部分——Issue 追踪器。**

> 说明："Issue 追踪器"是此仓库 issue 存放的位置。像 `to-issues`、`triage`、`to-prd` 和 `qa` 这样的技能从中读取和写入——它们需要知道是调用 `gh issue create`、在 `.scratch/` 下写入 markdown 文件还是遵循你描述的其他工作流。选择你实际跟踪此仓库工作的地方。

默认姿态：这些技能是为 GitHub 设计的。如果 `git remote` 指向 GitHub，提议它。如果 `git remote` 指向 GitLab（`gitlab.com` 或自托管主机），提议 GitLab。否则（或如果用户偏好），提供：

- **GitHub**——issue 存放在仓库的 GitHub Issues（使用 `gh` CLI）
- **GitLab**——issue 存放在仓库的 GitLab Issues（使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI）
- **本地 markdown**——issue 作为文件存放在此仓库的 `.scratch/<feature>/` 下（适合个人项目或无远程的仓库）
- **其他**（Jira、Linear 等）——请用户用一段话描述工作流；技能将将其记录为自由格式散文

如果——且仅当——用户选择了 **GitHub** 或 **GitLab**，追问一个问题：

> 说明：开源仓库通常以 Pull Request 而非仅 issue 的形式接收功能请求——PR 是附带代码的 issue。如果你启用此功能，`/triage` 将*外部* PR 拉入同一队列，并使用与 issue 相同的标签和状态进行处理（协作者进行中的 PR 不受影响）。如果 PR 不是你的请求面，保持关闭。

- **PR 作为请求面**——是 / 否（默认：否）。将答案记录在 `docs/agents/issue-tracker.md` 中。对于本地 markdown 和其他追踪器，跳过此问题——没有 PR。

**B 部分——分类标签词汇。**

> 说明：当 `triage` 技能处理传入的 issue 时，它将其移过一个状态机——需要评估、等待报告者、可供 AFK 代理领取、可供人工处理、或不修复。为此，它需要应用与你*实际配置*的字符串匹配的标签（或 issue 追踪器中的等效项）。如果你的仓库已使用不同的标签名（例如 `bug:triage` 而非 `needs-triage`），在此映射它们，以便技能应用正确的标签而非创建重复标签。

五个规范角色：

- `needs-triage`——维护者需要评估
- `needs-info`——等待报告者
- `ready-for-agent`——完全明确，AFK 就绪（代理无需人工上下文即可领取）
- `ready-for-human`——需要人工实现
- `wontfix`——不采取行动

默认：每个角色的字符串等于其名称。询问用户是否要覆盖任何。如果其 issue 追踪器没有现有标签，默认值即可。

**C 部分——领域文档。**

> 说明：某些技能（`improve-codebase-architecture`、`diagnosing-bugs`、`tdd`）读取 `CONTEXT.md` 文件以学习项目的领域语言，以及 `docs/adr/` 获取过去的架构决策。它们需要知道仓库是有一个全局上下文还是有多个（例如带有独立前端/后端上下文的 monorepo），以便在正确的位置查找。

确认布局：

- **单上下文**——仓库根目录下一个 `CONTEXT.md` + `docs/adr/`。大多数仓库如此。
- **多上下文**——根目录下的 `CONTEXT-MAP.md` 指向每个上下文的 `CONTEXT.md` 文件（通常是 monorepo）。

### 3. 确认并编辑

向用户展示草稿：

- 要添加到正在编辑的 `CLAUDE.md` / `AGENTS.md`（参见步骤 4 的选择规则）的 `## Agent skills` 块
- `docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md` 的内容

在写入前让他们编辑。

### 4. 写入

**选择要编辑的文件：**

- 如果 `CLAUDE.md` 存在，编辑它。
- 否则如果 `AGENTS.md` 存在，编辑它。
- 如果两者都不存在，询问用户创建哪个——不要替他们选择。

当 `CLAUDE.md` 已存在时，绝不要创建 `AGENTS.md`（反之亦然）——始终编辑已存在的那个。

如果所选文件中已存在 `## Agent skills` 块，原地更新其内容而非追加重复。不要覆盖用户对周围部分的编辑。

块内容：

```markdown
## Agent skills

### Issue tracker

[一行摘要，issue 跟踪位置，以及外部 PR 是否作为分类面]。参见 `docs/agents/issue-tracker.md`。

### Triage labels

[一行摘要，标签词汇]。参见 `docs/agents/triage-labels.md`。

### Domain docs

[一行摘要，布局——"单上下文"或"多上下文"]。参见 `docs/agents/domain.md`。
```

然后使用此技能文件夹中的种子模板作为起点，编写三个文档文件：

- [issue-tracker-github.md](./issue-tracker-github.md)——GitHub issue 追踪器
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md)——GitLab issue 追踪器
- [issue-tracker-local.md](./issue-tracker-local.md)——本地 markdown issue 追踪器
- [triage-labels.md](./triage-labels.md)——标签映射
- [domain.md](./domain.md)——领域文档消费规则 + 布局

对于"其他" issue 追踪器，使用用户的描述从头编写 `docs/agents/issue-tracker.md`。

### 5. 完成

告诉用户设置已完成，以及哪些工程技能现在将从这些文件中读取。提及他们之后可以直接编辑 `docs/agents/*.md`——重新运行此技能仅在需要切换 issue 追踪器或从头重启时才需要。

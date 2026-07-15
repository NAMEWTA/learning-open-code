快速开始：

```bash
npx skills add mattpocock/skills --skill=setup-matt-pocock-skills
```

```bash
npx skills update setup-matt-pocock-skills
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills)

## 功能说明

`setup-matt-pocock-skills` 教会一个仓库这些工程 skill 应该如何在其中运作 —— issue 在哪里、triage 的标签叫什么、领域文档放在哪里 —— 并将这些答案记录为其他 skill 会读取的**配置**。

它写入配置，不会硬编码行为。工程链条假定 `docs/agents/` 下存在三个文件；本 skill 是一次性的初始化引导，从你的实际仓库（`git remote`、现有标签、现有 `CONTEXT.md`）中发现信息，并与你确认而非猜测，然后生成这些文件。它是 prompt 驱动的 —— 探索、展示发现、确认、然后写入 —— 而不是确定性的脚手架。

## 何时使用

通过输入 `/setup-matt-pocock-skills` 来调用 —— Agent 不会自行触发它。

**每个仓库执行一次，在任何其他工程 skill 首次使用之前**。如果 [triage](https://aihero.dev/skills-triage)、[to-spec](https://aihero.dev/skills-to-spec) 或 [to-tickets](https://aihero.dev/skills-to-tickets) 开始猜测你的 issue 在哪里，或者应用了不存在的标签，说明它们尚未在此完成设置。仅当你需要切换 issue 追踪器或重新开始时，才重新运行它 —— 日常微调直接编辑 `docs/agents/*.md` 即可。

## 三个决策

它会引导你逐个完成三个选择，每个都有平实语言的解释（假定你尚不了解这些术语）：

- **Issue 追踪器** —— 工作在哪里被追踪，这样 `triage`/`to-spec`/`to-tickets` 就知道应该调用 `gh`、`glab`、在 `.scratch/` 下写 markdown，还是按照你描述的工作流来操作。可选：GitHub、GitLab、本地 markdown 或其他。
- **Triage 标签** —— 五个规范角色背后的字符串（`needs-triage`、`needs-info`、`ready-for-agent`、`ready-for-human`、`wontfix`），映射到你已经配置好的标签，这样 `triage` 会使用真实的标签而不是创建重复的。
- **领域文档** —— 仓库是使用一个 `CONTEXT.md` 还是多上下文映射，这样需要读取领域语言的 skill 就知道去哪里找。

输出是三个文件 —— `docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md` —— 以及一个 `## Agent skills` 块，指向仓库已有的 `CLAUDE.md` 或 `AGENTS.md` 中的这些文件。这些文件是工具链其余部分所依存的共享基础。

## 有效的标志

- `docs/agents/` 下生成了三个文件，且 `CLAUDE.md` 或 `AGENTS.md` 中出现了 `## Agent skills` 部分。
- 它建议的追踪器匹配你真实的 `git remote`，且标签匹配你仓库中已经存在的字符串。
- 此后，`triage` 和 `to-tickets` 会在正确的地方以正确的标签操作，而不再询问或猜测。

## 在系统中的位置

`setup-matt-pocock-skills` 是**一次性运行**的设置 —— 整个工程 skill 集合的基石，不是需要重复执行的步骤。它的邻居是那些读取它写入内容的 skill：[triage](https://aihero.dev/skills-triage)，因为它应用了在这里配置的标签词汇，以及 [to-spec](https://aihero.dev/skills-to-spec) / [to-tickets](https://aihero.dev/skills-to-tickets)，因为它们将内容发布到在这里配置的 issue 追踪器中。先运行它；下游的一切都假定它已经运行过了。当你拿不准哪个 skill 或流程合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。

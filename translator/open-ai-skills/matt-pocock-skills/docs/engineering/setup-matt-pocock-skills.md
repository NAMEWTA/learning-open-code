## 功能说明

`setup-matt-pocock-skills` 回答关于一个仓库的三个问题——issue 住在哪里、triage 标签叫什么、领域文档放在哪里——并把答案记录为 `docs/agents/` 下的 markdown 文件。

这些文件是仓库之间唯一不同的东西。skill 本身处处相同；它们在运行时读取 `docs/agents/issue-tracker.md`，然后照做。这就是整套不绑死 GitHub 的原因，也是没有任何 skill 文件需要编辑来指向别处的原因。用"把 skills 链接到自定义 issue 追踪器"来调用它，凡是你能编程连接的东西都行，对 skills 零改动。

它是提示驱动的 skill，不是确定性脚本。它读你的 `git remote`、你现有的 `CLAUDE.md`、你现有的 `CONTEXT.md`，提出它发现的东西，写入任何东西之前等你确认。

## 何时使用

输入 `/setup-matt-pocock-skills` 来调用它——[Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 不会自行调用。它被刻意标记为不可调用，所以其他 skill 也不能替你触发它。

每个仓库跑一次，在第一个其他工程 skill 使用之前。如果 [triage](https://aihero.dev/skills-triage)、[to-spec](https://aihero.dev/skills-to-spec)、[to-tickets](https://aihero.dev/skills-to-tickets) 或 [wayfinder](https://aihero.dev/skills-wayfinder) 开始猜你的 issue 去哪，或应用你的追踪器没有的标签，说明它们在这里还没被设置。一个项目已经进行到一半的仓库完全可以跑它；skill 读取已存在的内容，之前的工作不会浪费。

## 前置条件

它写入你运行它的仓库：

| 它写 | 位置 |
| --- | --- |
| `issue-tracker.md` | `docs/agents/` |
| `domain.md` | `docs/agents/` |
| `triage-labels.md` | `docs/agents/`，仅当安装了 `triage` skill |
| 一个 `## Agent skills` 块 | 已经存在的 `CLAUDE.md` / `AGENTS.md` 中那个 |

全部是已提交的 markdown。没有用户级或全局模式：配置住在仓库里，所以每个仓库都有自己的副本。

## 三个决策

它给每一节都先带推荐答案，跳过已经被现有内容解决掉的探索。大多数运行是两次确认就完事。

| 决策 | 它提议什么 | 它什么时候真的问 |
| --- | --- | --- |
| **Issue 追踪器** | 与你 `git remote` 匹配的那个 | 总是——这是唯一一个真正的选择 |
| **Triage 标签** | 保留五个规范名字（`needs-triage`、`needs-info`、`ready-for-agent`、`ready-for-human`、`wontfix`） | 仅当安装了 `triage` skill |
| **领域文档** | 单上下文：根目录一个 `CONTEXT.md` 加 `docs/adr/` | 仅当它发现 monorepo 信号，然后它提供多上下文 `CONTEXT-MAP.md` |

追踪器选项：

| 选项 | issue 住在哪里 | 需要 |
| --- | --- | --- |
| **GitHub** | 仓库的 GitHub Issues | `gh` CLI |
| **GitLab** | 仓库的 GitLab Issues | `glab` CLI |
| **本地 markdown** | 本仓库 `.scratch/<feature>/` 下的文件 | 什么都不需要——完全没有 remote |
| **Other** | 你说哪里就哪里 | 你写一段描述工作流的话 |

前三个作为模板随 skill 发布，开箱即用。本地 markdown 是一等公民选项，不是回退：没有 remote 的个人项目完全受支持。一条告诫值得重复：如果你用 GitHub，就别用本地 markdown。它们是替代关系，不是分层关系。

"Other" 也不是空壳。它是 Jira、Linear、Azure DevOps 和 Beads 都有效的原因：你描述工作流，skill 把你的散文记进 `docs/agents/issue-tracker.md`，下游 skills 跟着散文走。社区已经做过了——一个基于 [MCP](https://www.aihero.dev/ai-coding-dictionary/mcp) 的 Jira 变体、一个形状像 `gh` 的 Gitea CLI、一个手搭的本地仪表盘。

## 常见问题

**我必须用 GitHub 吗？**

不用。GitHub、GitLab 和 `.scratch/` 下的本地 markdown 都作为现成模板发布，其他一切走 "other" 路径。这是记录中被重复最多的问题，大致是这些话：*"hard locked to github"*、*"can I use GitLab / Jira"*、*"what about Azure DevOps"*。每次的回答都是：追踪器是一个设置答案，不是 skill 属性。

**更新 skills 之后需要重跑吗？**

v1.1 之后被直接问到，Matt 说需要。skill 自己的收尾信息更软——它告诉你重跑只在换追踪器或从头开始时才需要。两种说法都站得住，差距存在的原因是真的：种子模板在版本之间会变，所以旧版本写出的 `docs/agents/issue-tracker.md` 相对现在读它的 skills 可能过期。如果某个下游 skill 开始做出文档描述不同的行为，重跑就是便宜的修复。

**它写进了 `CLAUDE.md`，但我在用 Codex。**

已知缺口，仍然开放。文件选择规则是"存在 `CLAUDE.md` 就编辑它，否则 `AGENTS.md`"——它检查哪个文件存在，不检查哪个 [工具链](https://www.aihero.dev/ai-coding-dictionary/harness) 在跑。一个从 Claude Code 时代留下 `CLAUDE.md` 的仓库，会在 Codex 从不读的地方拿到它的 `## Agent skills` 块。两个变通办法在流传：手动把块移到 `AGENTS.md`，或者让 `AGENTS.md` 成为规范、`CLAUDE.md` 只放一行指向它的指针。如果两个文件都不存在，skill 会问你要建哪个，而不是自己选——这让那些期待它直接决定的人困惑。

**它没创建我的 triage 标签。**

它不创建。`docs/agents/triage-labels.md` 是一份*映射*——它告诉 `/triage` 你追踪器里的哪些字符串对应五个规范角色。它不跑 `gh label create`。在一个全新的 GitHub 仓库上，标签确实还不存在，这被当成 bug 报过不止一次。两个后续：

- 如果你的追踪器已经用了规范名字，映射就是一张恒等表，没有要配置的东西。那是预期的常见情况，不是缺失步骤。
- [wayfinder](https://aihero.dev/skills-wayfinder) 的 `wayfinder:map` 和 `wayfinder:<type>` 标签也不在这里创建，而 `gh issue create --label <missing>` 会直接失败，而不是顺手创建标签。在 GitHub 仓库上第一次跑 wayfinder 之前手动创建它们。

**我能在这里配置其他 skill 的行为吗——[质询](https://www.aihero.dev/ai-coding-dictionary/grilling) 节奏、问题格式、语气？**

不能。它配置三件事：追踪器、标签、文档布局。有人直接请求过把它变成按用户偏好的大本营，而长期答案是 skills 保持有主见：*"Config is death."* 偏好属于你的 `CLAUDE.md`，作为平白指令，每个 skill 本来就会读。

**我能把配置放在 `~/.claude` 而不是提交到每个仓库吗？**

今天不行。有一个来自跨很多仓库使用这些 skills 的人的开放请求，要求正是这个，但用户级模式不存在。每个仓库自带自己的 `docs/agents/`。

**有一个配置其他 skill 的 skill，不奇怪吗？**

一项长期抱怨说奇怪，原话是：*"having a skill to set up the other skill does not feel right to me——那意味着 LLM 在配置自己的 skills。"*这个取舍是真的，也被承认：设置步骤的替代方案是把追踪器指令复制进每个碰 issue 的 skill。输出是可检查、可编辑的 markdown，这是缓解——你能读它写的每个文件、手动改，日常微调正是那样，而不是再跑一次。

## 有效的标志

- `docs/agents/issue-tracker.md` 和 `docs/agents/domain.md` 存在，装了 `triage` 的话还有 `triage-labels.md`。
- 你的工具链真正读取的指令文件里出现 `## Agent skills` 节，带一行指向每个文件的摘要。
- 它提议的追踪器匹配你真正用的 remote，标签字符串匹配你的追踪器里真实存在的标签。
- 之后，`/to-tickets` 发布时不再问 issue 住哪，`/triage` 应用标签而不是发明标签。
- skill 文件本身没有任何变化。如果设置编辑了某个 `SKILL.md`，就有东西出错了。

## 在系统中的位置

`setup-matt-pocock-skills` 是工程流程的**运行一次**的设置，是其他一切当作前提的东西，而非链条中的一步。它的邻居是它的读者：[triage](https://aihero.dev/skills-triage)——应用这里写下的标签词汇；[to-spec](https://aihero.dev/skills-to-spec) 和 [to-tickets](https://aihero.dev/skills-to-tickets)——发布进这里点名的追踪器；以及 [wayfinder](https://aihero.dev/skills-wayfinder)——读同一追踪器文件的"Wayfinding operations"节，才知道地图和子 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) 怎么存。它记录的领域文档布局，正是 [domain-modeling](https://aihero.dev/skills-domain-modeling) 之后填的——它惰性创建 `CONTEXT.md` 和 ADR，在某个术语或决策真正定稿时，所以设置后仓库为空是预期的状态。接下来够哪个 skill，[ask-matt](https://aihero.dev/skills-ask-matt) 为整套路由。

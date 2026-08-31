## 功能说明

`code-review` 审查 `HEAD` 与某个你指定的固定点——一次提交、一个分支、一个标签、`main`、`HEAD~5`——之间的 diff，沿两个轴进行。**规范轴**（Standards）检查代码是否遵循本仓库的书写方式；**规格轴**（Spec）检查代码是否实现了源 issue 或 [规格](https://www.aihero.dev/ai-coding-dictionary/spec) 所要求的内容。每个轴在自己的 [子代理](https://www.aihero.dev/ai-coding-dictionary/subagent) 中运行，互不看到对方的推理。

两个轴的结果从不合并、从不重新排序。报告以*每个轴*的最严重问题收尾，拒绝跨轴选出单一赢家——因为一个变更可能通过一个轴而挂掉另一个轴：遵循了所有约定却实现了错误东西的代码，通过规范轴而挂掉规格轴；完全按 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) 要求做了、却破坏了仓库约定的代码则相反。混合式结论会让通过的轴掩盖挂掉的轴。

## 何时使用

输入 `/code-review`，或者当你要求审查一个分支、一个 PR、进行中的工作或任何"自 X 以来"的内容时，Agent 会自动调用它。

| 你的情况 | 使用 |
| --- | --- |
| 存在一个 diff，你想知道它是否既构建正确*又*是正确的东西 | `code-review` |
| 你想在 diff 里猎 bug——空指针路径、竞态、差一错误 | Claude Code 自带的审查，不是这个（见下方的同名冲突） |
| 什么都还没写，你想让它先写测试 | [tdd](https://aihero.dev/skills-tdd) |
| 整个规格需要从零构建，含审查 | [implement](https://aihero.dev/skills-implement)，它自己会调用本 skill |
| 整个代码库都漂移了，不是一个 diff | [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) |
| 有东西坏了，你不知道为什么 | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

你必须提供固定点。如果不提供，skill 会向你询问而不是猜；然后它会先确认 ref 能解析、diff 非空，才启动任何东西——这样打错的分支名会当着你的面失败，而不是在两个子代理内部失败。

## 前置条件

规范轴什么都不需要。它读取仓库文档化的内容（`CODING_STANDARDS.md`、`CONTRIBUTING.md` 之类），仓库没有文档时则回退到内置基线。

规格轴需要一份存在的、可找到的规格。它按以下顺序查找：

1. 提交信息中的 issue 引用（`#123`、`Closes #45`、GitLab 的 `!67`），通过 `docs/agents/issue-tracker.md` 获取。
2. 你作为参数传入的路径。
3. `docs/`、`specs/` 或 `.scratch/` 下与分支名或功能名匹配的规格文件。
4. 直接问你。

第 1 步依赖 `docs/agents/issue-tracker.md`，它由 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 写入。没有它时，只要给它一个路径，规格轴照样工作。完全找不到规格时，规格子代理会被跳过，报告写明"无可用规格"，而不是凭空捏造需求。

## 两个轴

| | 规范轴 | 规格轴 |
| --- | --- | --- |
| 问题 | 构建是否正确？ | 是否构建了正确的东西？ |
| 读取 | 仓库文档化的标准，加上坏味道基线 | 源 issue 或规格 |
| 报告 | 有据可查的违规（可能很严格），以及坏味道（永远属于判断） | 缺失或部分实现的需求、范围蔓延、实现错误的需求 |
| 每条发现引用 | 标准文件和规则，或具名的坏味道加对应代码块 | 规格中的对应行 |

一个不认识你标准的通用审查 skill，正是这套设计要避免的东西——它会把你代码库中*有意为之*的东西标出来，却漏掉你代码库真正依赖的不变量。所以仓库自己的文档才是规范轴上的 [一手来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)，**仓库永远优先**。

**坏味道基线**是它之下的地板：来自《重构》（_Refactoring_）第 3 章的十二个 Fowler 代码坏味道——Mysterious Name（令人迷惑的名字）、Duplicated Code（重复代码）、Feature Envy（依恋情结）、Data Clumps（数据泥团）、Primitive Obsession（基本类型偏执）、Repeated Switches（重复的 switch）、Shotgun Surgery（霰弹式修改）、Divergent Change（发散式变化）、Speculative Generality（夸夸其谈的未来性）、Message Chains（过度耦合的消息链）、Middle Man（中间人）、Refused Bequest（被拒绝的遗赠）。每个都是一条带标签的启发式规则（"可能是 Feature Envy"），绝不是硬性违规；每条都以*它是什么* → *怎么修*的形式表述，所以一条发现会带着行动方案而来，而不是一句抱怨。你的 linter 已经强制检查的内容，两个轴都会跳过。

## 常见问题

**它和 Claude Code 自带的 `/code-review` 撞名了。我该怎么办？**

这是本 skill 被报告最多的问题，而且没有修复。Claude Code 自带自己的 `/code-review`，功能不同——它在 diff 里猎 bug，而这个检查规格符合度和仓库标准。安装本库意味着两者必有一个胜出，谁胜出取决于你的安装方式。通过插件市场安装时，所有东西都带 `mattpocock-skills:` 前缀别名，内置的以不带限定符的名字就难够到了；通过普通 skills 安装时，本地文件胜出，本 skill 会遮蔽内置的。一个干净的解法是彻底移除 Claude Code 的内置 skills：能省下大量 [上下文](https://www.aihero.dev/ai-coding-dictionary/context)，冲突也不再要紧。遮蔽这件事本身算得上 Claude Code [工具链](https://www.aihero.dev/ai-coding-dictionary/harness) 的一个 bug——skill 作者理应有权给 skill 取任意名字——所以另一个解法是给本地副本改名。编辑 frontmatter 或重命名目录会被 `npx skills update` 撤销；用户报告的可持久做法是把 skill fork 成一个新名字，并把 `code-review` 从受管集合中移除，记下 fork 时的提交以便日后手动重新同步。

**它的子代理不停地再次调用 `/code-review`，又生出更多代理。**

已知未修复的 bug，多人在不止一个工具链上复现过。规范轴和规格轴的提示词没有禁止委派，所以子代理可能重新发现这个 skill 并再次分叉——有一份报告跑出了 50 多个代理。人们在 fork 上应用的修复是往两份子代理简报末尾各加一行："不要调用 `/code-review` 或再启动其他代理——直接执行本次审查。"也有人倾向于在工具链层面处理，让每个 skill 都继承这道护栏。两者都还没进入发布的 skill。如果你无人值守地运行它，留意一下代理数量。

**我该在写出代码的同一场 [会话](https://www.aihero.dev/ai-coding-dictionary/session) 里运行它吗？**

最好开一场新会话。正如一位读者所说："同样的上下文审查自己，那不是审查，是带斜杠命令的确认偏误。"创作会话里的审查 Agent 持有塑造了这段代码的全部假设，而独立审查者恰恰不该有这些上下文。这也是人们要求 [implement](https://aihero.dev/skills-implement) 不带内置审查步骤的原因——它会在刚写完 diff 的那场会话内部运行审查。自己从一场干净会话里调用 `/code-review`，才是诚实的版本。

**每个 ticket 之后审查，还是最后一次性审查？**

两种都行，skill 不替你决定。按 ticket 审查能让每个 diff 足够小，规格轴可以对照一份清晰的规格检查，这也是 `implement` 采用的模式。攒到分支末尾批量审查，能抓住各 ticket 之间的相互作用——逐 ticket 审查会各漏一爪。拿不准的话，按 ticket 审查，再对着分支点跑一次最终检查。

**我能信任这些发现吗？**

不检查不行。子代理的输出是假设，不是证据——有一个团队报告说，十几个破坏性变更都被基于散文的审查放行了。skill 会逐字或轻度清理地汇总两份报告，而不是逐条对照文件复核每个断言，所以一条发现可能引用了错误的位置或夸大了影响。对每条发现，先读它的引用再行动。每条发现都必须带引用——一条标准规则、一个坏味道加对应代码块、或一行规格——这正是这套东西尚且可核查的原因。

**为什么我每次运行它都会发现新问题？**

因为修复会制造新的表面，也因为规范轴的判断那一半在两次运行之间并不确定。一位读者直白地描述了这种循环："/code-review 和 /improve-code-architecture 每次都总能发现新东西。我实施修复，重跑这些 skill，然后又一轮。"没有收敛保证。把通过当成一份线索清单，只处理那些背后有明确规则引用的，然后收手——不要循环跑到它干净为止，因为它不会干净。

**它审查我未提交的工作吗？**

不。它 diff `<fixed-point>...HEAD`，三点式，从合并基点算起，排除暂存区和工作树中的改动。如果 `implement` 没有做过中间提交，即将提交的工作对审查是不可见的。先提交，再审查，然后 amend 或补一个 fixup。

## 有效的标志

- 在启动任何子代理之前，它拒绝在坏的 ref 或空 diff 上开始。
- 报告以 `## Standards` 和 `## Spec` 两个独立区块抵达，而不是一份合并清单。
- 每条规范轴发现都点明仓库某个文件中的一条规则或十二个坏味道之一，并引用对应代码块；每条规格轴发现都引用规格中的一行。
- 结尾总结给出每个轴的最严重问题，并拒绝选出整体赢家。
- 没有可用规格时，规格区块直接说明，而不是列出它从代码推断出来的需求。

## 在系统中的位置

`code-review` 是构建链尾部的审查步骤——`grill-with-docs → to-spec → to-tickets → implement → code-review`——也可以单独用在任何你指向的分支或 PR 上。

- [implement](https://aihero.dev/skills-implement) 是它最近的邻居：implement 驱动构建，并在提交前把本 skill 作为自己的收尾审查。
- [to-spec](https://aihero.dev/skills-to-spec) 和 [to-tickets](https://aihero.dev/skills-to-tickets) 产出规格轴对照检查的文档；一份含糊的规格会让那个轴也变得含糊。
- [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 是它全代码库层面的对应物——本 skill 永远只看一个 diff。

拿不准情况该用哪个 skill 时，[ask-matt](https://aihero.dev/skills-ask-matt) 会跨整个集合为你路由。

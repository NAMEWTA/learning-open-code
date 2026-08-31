## 功能说明

`triage` 处理你项目追踪器上的 issues，通过一个小型 **triage 角色**状态机——一个类别角色和一个状态角色——流转每一个，最后留下要么一份 Agent 就绪的简报、一个给报告者的具体问题、或一个带记录理由的已关闭 issue。

它只服务于**不是你创建**的 issues。原始 bug 报告、进来的功能请求、一封不请自来的外部 pull request——从外部落进追踪器的工作，无论报告者把它留成什么形状。[to-tickets](https://aihero.dev/skills-to-tickets) 产出的 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) 按构造就已经是 Agent 就绪的，对它们跑 `triage` 至多算浪费。规则是平的：`/triage` 只处理进来的 issues，不处理你自己创建的。

第二件把它和手工打标签区分开的事：它推荐并等待。它带着推理告诉你它的类别和状态判断，加上它在代码库里发现了什么，在你指示之前什么都不应用。

## 何时使用

输入 `/triage` 然后用平白语言描述你想要什么——[Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 不会自行调用。"Show me anything that needs my attention"、"let's look at #42"、"move #42 to ready-for-agent"。

| 你拥有什么 | 去哪里 |
| --- | --- |
| 一个装满他人原始报告的追踪器 | `/triage` |
| 你自己的一个粗略想法，什么都没写下 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| 一场定案的对话要变成 [规格](https://www.aihero.dev/ai-coding-dictionary/spec) | [to-spec](https://aihero.dev/skills-to-spec) |
| 一份要拆成 Agent 就绪 tickets 的规格 | [to-tickets](https://aihero.dev/skills-to-tickets) |
| 一个已确认的 bug，需要根因而非标签 | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

## 前置条件

`triage` 读写你的 issue 追踪器，所以 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 必须先配置好那个追踪器和它的标签词汇。下面的角色名是**规范名**；你追踪器里的标签字符串可能不同，映射就是 setup 提供的东西。如果你的追踪器恰好已经精确使用规范名，就没有要映射的，也没有要设置的。

追踪器配置还决定外部 pull request 是否算作请求表面，以及谁算外部。那个开关默认关闭，不再是设置问题——想要 PR 进范围，就在 `docs/agents/issue-tracker.md` 里翻它。

## 状态机

每个被 triage 的条目最后恰好携带一个类别角色和一个状态角色。两个类别：`bug`（有东西坏了）和 `enhancement`（新功能或改进）。五个状态：

| 状态 | 含义 |
| --- | --- |
| `needs-triage` | 你需要评估它。未打标签的 issue 通常先落在这里。 |
| `needs-info` | 等报告者。他们回复时回到 `needs-triage`。 |
| `ready-for-agent` | 完全规格化，附 Agent 简报。一个 [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) Agent 可以接手。 |
| `ready-for-human` | 同样的简报，加上为什么这不能委托——判断、外部访问、手工测试。 |
| `wontfix` | 已关闭，理由已记录。 |

这就是全部词汇，而"恰好一个状态角色"的不变量是让查询保持简单的关键。它也是这个 [skill](https://www.aihero.dev/ai-coding-dictionary/skill) 被要求最多的区域：用户要求过第六个状态给已规格化但被另一个 issue 阻塞的工作、给被未来触发条件门控的 `deferred` 工作，以及一个终态 `implemented`。这些都没发布。见下方的问题。

`wontfix` 分三种，区别很重要，因为只有一种会写入知识库：

| 你关闭它的原因 | 发生什么 |
| --- | --- |
| 已实现 | 一条评论指向它已经存在的地方。不写入 `.out-of-scope/`——它是已建成的功能，不是被拒的，归档到那里会毒化去重检查。 |
| 被拒的 bug | 礼貌的解释，然后关闭。 |
| 被拒的功能请求 | `.out-of-scope/` 里一个文件，从关闭评论链接，然后关闭。 |

`.out-of-scope/` 每个被拒**概念**一个 markdown 文件，而不是每个 issue 一个，写成一短篇设计文档而非数据库行：被拒的是什么、为什么、以及每个问过它的 issue。`triage` 在评估任何东西之前读整个目录，按概念而非关键词匹配——"夜间主题"匹配 `dark-mode.md`。命中时它浮出旧决策，问你是否仍然这样想，而不是从头重新辩论请求。

## 先验证，再写简报

在任何 [质询](https://www.aihero.dev/ai-coding-dictionary/grilling) 之前，`triage` 检查说法是否成立。对 bug，它按报告者的步骤复现它。对 PR，它 checkout 分支并跑相关测试。然后它报告三件事中哪件发生了：确认，带代码路径；无法复现；或细节不足以尝试——后者本身就是最强有力的 `needs-info` 信号。

同一遍里它还会对代码库跑两项检查——**冗余检查**（这是否已实现？按领域概念搜索，而非按报告者的措辞）和**过往拒绝检查**（`.out-of-scope/` 是否已经说过不？）。两者都便宜，命中时都产出 `wontfix`。

这一切存在是为了让一件工件变好：**Agent 简报**，issue 移入 `ready-for-agent` 时发布的带结构评论。一旦发布，简报就是契约，原始报告只是上下文。简报为**持久**而写，而非精确，因为一个 issue 可以在 `ready-for-agent` 里坐几周，而代码在它底下移动。所以它们点名类型、签名和行为契约，绝不写文件路径或行号。一次确认的复现产出的简报比猜测强得多。

## PR 就是附带代码的 issue

在追踪器把外部 pull request 当作请求表面的地方，它们走同一台机器——同样的类别、同样的状态、同样的流转。状态只是对着 diff 读：`ready-for-agent` 意味着简报已附、Agent 该对代码采取下一步，`ready-for-human` 意味着可以让人合并了。PR 上的简报描述对现有 diff 还剩下什么要做，而不是如何从零构建那东西。

发现只暴露*外部* PR，因为协作者进行中的分支不是 triage 工作。那个过滤只是发现层面的——显式点名一个 PR，无论谁写的它都会被 triage。一个粗糙边缘：GitHub 模板的外部 PR 列表命令向 `gh pr list` 要一个 `gh` 不暴露的 `authorAssociation` 字段，所以那条命令照写就整个失败（[#468](https://github.com/mattpocock/skills/issues/468)）。

## 常见问题

**我跑了 `/to-spec` 和 `/to-tickets`，现在那些 tickets 坐在那里没被 triage。我要对它们跑 `/triage` 吗？**
不用。它们已经 Agent 就绪——`to-tickets` 在发布时就应用 `ready-for-agent` 标签，正是为了让 AFK runner 不需要再跑一遍就能拾起它们。撞上这个问题的用户跑了规格流程，看到输出上的 `needs-triage`，然后发现自己的 AFK runner 忽略一切。`triage` 是外部到达的工作的入口；规格流程是你发起的工作的车道。它们在 `ready-for-agent` 相遇，不在那之前。

**现在有 `to-spec` → `to-tickets` → `implement` 流程了，`triage` 还有用吗？**
只有在你有人境工作的时候。`triage` 比那条主线更早，做的是不同的活：它是别人提交的报告的车道。如果你追踪器里的一切都出自你自己的规划，你很少会打开它。如果你维护任何公开的东西，或你的团队朝你报 bug，它是前门。主要用途是接收外部贡献者 issues 的开源仓库。

**Agent 想应用 `ready-for-agent`，而 `gh` 说标签不存在。**
已知开放 bug（[#616](https://github.com/mattpocock/skills/issues/616)）。`setup-matt-pocock-skills` 把标签词汇写进 `docs/agents/triage-labels.md`，但不在你的追踪器里创建标签。用 `gh label create` 或追踪器 UI 自己创建一次那五个状态标签和两个类别标签，就好了。issue 里链接了一个未合并的社区修复分支。

**五个状态不够——blocked、deferred 或 implemented 呢？**
这是本 skill 被归档最多的缺口，三种形状。一个完全规格化但等另一个 issue 关闭的 issue（[#139](https://github.com/mattpocock/skills/issues/139)）——报告者的抱怨是 `ready-for-agent` 在那里"技术上成立"但误导，所以 Agent 拾起它撞墙。被触发条件门控、意图明确但尚不可执行的未来工作（[#297](https://github.com/mattpocock/skills/issues/297)）。以及一个"已实现，等待验证"的终态，没有它 AFK runner 会把已完成的 tickets 重新排队。Matt 同意 blocked 案例是真的，对名字（`blocked` 对 `paused`）还没决定。什么都没发布。人们用的变通办法是类别旁边加一个仓库本地额外标签，让规范状态位被诚实的东西占据，代价是 skill 不知道它。一个社区衍生品走得更远，加了 `needs-slicing`、`tracking` 和 effort 标签——那有效，但那是他们的，不是 skill 的。

**这和 `/diagnosing-bugs` 有什么不同？**
这里的验证步骤刻意很浅——足以回答"这是真的吗，大致住在哪里"，而不是找根因。当一个 bug 几分钟内按报告者步骤复现不了，诚实的动作是 `needs-info`，或者如果你想现在就追它，用 [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs)。两个 skill 的文本目前都不提对方；有位用户发现了那条接缝，它仍然开着。

**我能把它指向整个积压并让它跑吗？**
你可以问，但留意它读什么。"显示需要关注的内容"那一遍是便宜的列表，为*选择*而设——你挑一个，然后它对你挑的那个收集完整 [上下文](https://www.aihero.dev/ai-coding-dictionary/context)。一次对着二十个 issues 跑，Agent 可能悄悄回退到用那个便宜列表当证据基础，它返回 issue 正文但不返回评论。一位用户恰好撞上：三个 issues 已经带着"已修复，建议关闭"的评论，三个却都拿到崭新的 Agent 简报。如果你想要批量过一遍，明说必须逐 issue 读评论。

**它能用 Linear 或 GitHub Issues 之外的任何东西吗？**
能——追踪器是配置，不是硬编码假设，人们用它跑 Linear（经 `linear` CLI）、GitLab 和 `.scratch/` 下的纯 markdown 文件。一个常见的拆分是 Linear 管 issues 和规划，GitHub 管代码和 PR：说"issue tracker"的 skills 映射到 Linear，说"PR"的 skills 映射到 GitHub。本地 markdown 追踪器上有一个开放模板 bug：生成的文件可能把验收标准带两遍，一遍在顶层、一遍在 Agent 简报里（[#200](https://github.com/mattpocock/skills/issues/200)）。

## 有效的标志

- 它碰过的每个条目最后恰好一个类别角色、一个状态角色——从不少，也从不同时两个状态冲突。
- 它给你一个带推理的推荐然后停下，而不是重新打标签继续走。
- bug 被复现，或 PR 被 checkout 并运行，然后才到达 `ready-for-agent`。
- 它写的简报点名类型和行为，不含文件路径、不含行号。
- 六个月前被拒的请求回来了，它说出来并引述旧理由，而不是新鲜 triage 一遍。
- 它发的每条评论以 `> *This was generated by AI during triage.*` 开头。

## 在系统中的位置

`triage` 是一条**入口通道**，不是主链中的一步。主流程从你有的想法出发——grill、spec、tickets、implement、review——而 `triage` 是"送上门的工作"的平行车道。它在同一个地方汇合：一个带着简报、贴着 `ready-for-agent` 标签的 issue，[implement](https://aihero.dev/skills-implement) 拾起它，和拾起 [to-tickets](https://aihero.dev/skills-to-tickets) 的 ticket 完全一样。当一个请求在能写简报之前需要打磨，`triage` 把 [grilling](https://aihero.dev/skills-grilling) 和 [domain-modeling](https://aihero.dev/skills-domain-modeling) 一起跑，一次一轮问题，让决策在做出时落进 `CONTEXT.md` 和 ADR。拿不准自己身处哪条车道时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。

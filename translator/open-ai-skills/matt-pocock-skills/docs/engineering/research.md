## 功能说明

`research` 通过阅读掌握答案的源头资料来回答问题，然后在仓库里留下一份带引用的 Markdown 文件。它只基于 **[一手来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)** 工作——官方文档、源代码、规范、第一方 API——并把每条说法追溯到拥有它的来源，所以在 API 自己的文档可达时，它不会复述某篇博客对那个 API 的转述。

它不在对话里回答你。输出是一个文件，写在仓库本来就放这类笔记的地方，每条说法都带链接。这才是重点：一份你可以回应、交给另一个 Agent、或扔掉的文档，而不是一场 [会话](https://www.aihero.dev/ai-coding-dictionary/session) 结束就消失的答案。

## 何时使用

输入 `/research`，或当任务变成阅读体力活时 [Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 会自动调用它。

当下一步是从工作目录之外*查明某事*——第三方 API 怎么表现、规范到底说了什么、某个版本说法是否成立——而且你不想让自己的主线因为去做阅读而停顿时使用它。你需要什么决定用哪个 skill：

| 你需要 | 使用 |
| --- | --- |
| 一个决策在等待的外部事实 | `research` |
| 一个*和你一起*、通过访谈做出的决策 | [grilling](https://aihero.dev/skills-grilling) |
| 一个持久的架构决策，写进 `CONTEXT.md` 和 ADR | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| 查明某个做法在你的代码库里是否可行 | [prototype](https://aihero.dev/skills-prototype) |
| 一个大得装不进单次会话的计划 | [wayfinder](https://aihero.dev/skills-wayfinder) |

`research` 与 `grill-with-docs` 的分界线是**带回来的东西的保质期**。Research 产出短命资产——这个库的鉴权机制截至本周是如何运作的。ADR 记录一个你要留住的决策。如果你产出的是决策而非事实，你在 [质询](https://www.aihero.dev/ai-coding-dictionary/grilling)，不是在 research。

## 委托出去的体力活

标志性动作是阅读以**后台 Agent** 的方式运行。你继续工作；它跑出去，把每条说法追溯到一手来源，写一个 Markdown 文件，然后回报。Research 是你委托的体力活，不是外包的思考——你拿到一份可以对着质询、规划或设计的文档，拍板仍由你来。

委托没有护栏，后台 Agent 还能再生出它自己的后台 Agent。这是本 skill 有据可查的最粗糙边缘。

文件落在哪里由仓库决定，不由 skill 决定：它匹配现有的笔记约定，没有约定就选一个合理的地方并告诉你。每次运行写一个文件。

## 常见问题

**它又生了一个 research Agent——这是预期吗？**

不是。这是一个开放 bug，[issue #530](https://github.com/mattpocock/skills/issues/530)。skill 让调用者启动一个后台 Agent，但没有限制 Agent 类型，所以它启动的是持有 `Agent` 工具的 `general-purpose` 类型 Agent，带着同样的指令——然后又触发一遍。一位报告者测得单次 research 任务在三个重叠运行中花了约 45 万 [token](https://www.aihero.dev/ai-coding-dictionary/token)，重复的那个半小时后完成，完全在视野之外。它在 Claude Code 之外也能复现；同样的嵌套在 Codex 里用 GPT-5.6-sol 确认过。没有已发布的修复。用户给自己装的副本打过补丁，加一行告诉已经是 [子代理](https://www.aihero.dev/ai-coding-dictionary/subagent) 的 Agent 自己做这个活，这有帮助，但只是指令层面，不是结构层面。调用之后盯一下你的后台任务列表，停掉重复的那个。

相反方向的失败也存在：如果你自己的全局指令禁止 Agent 再委派工作，后台 Agent 会礼貌地拒绝任务，skill 就悄悄地什么都不做。

**文件应该住哪——而且我该提交它吗？**

skill 把文件放在仓库本来就放笔记的地方，除此之外没有意见。社区共识相当明确：ADR 留住，research 文件不留。最尖锐的说法来自一条恰好讨论这个问题的 Discord 讨论串："ADR 留。其他一切完成后归档或删除。否则它变成工作的渣滓，如果你已经偏离了规格/研究，还会毒化未来的仓库读取。"一份 research 文件记录的是它写下的那天为真的东西，所以过期的比没有更糟。总体而言这些工件不太属于 git，也没有规范的家——人们改用 Obsidian、独立的知识仓库或 issue 追踪器。

**什么算"高信任"一手来源，谁来决定？**

[模型](https://www.aihero.dev/ai-coding-dictionary/model) 决定。skill 点名合格的来源*种类*——官方文档、源代码、规范、第一方 API——没有白名单、没有领域闸门、没有验证环节。这是 skill 最初被提议时最响亮的反对意见，而且从未得到公开回答："五个 research 子代理指向垃圾，只是更快地给你五个自信的错误答案。你怎么把关什么算高信任来源？"你实际拥有的缓解是每条说法上的引用。跟着其中两三条走。如果它们落在一件事的转述上而不是那件事本身，这次运行就败在了它唯一的职责上。

**之后的会话会复用早先运行找到的东西吗？**

不会。没有东西自动加载过去的 research 文件；它是一份坐在仓库里的文档，直到某个人或某个 skill 指向它。这一点很早就被提出，作为对这个设计最强的挑战——"价值在于 Markdown 成为 Agent 之后重新读取的上下文，而不在抓取本身。一份写完即死的文件只是花哨的搜索"——而发布的 skill 没有解决它。实践中，文件靠被刻意喂进下一步来赚取存在价值：把它附到规格上、引述进质询会话、让 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) 指向它。

**为什么不直接让 Agent 去读文档？**

你可以，而一段恰好这么说的两行提示正是本 skill 取代的做法。skill 比提示多买两样东西：它在后台运行，让你的会话保持 [上下文](https://www.aihero.dev/ai-coding-dictionary/context) 干净；一手来源约束和带引用文件输出每次都按同样方式出来，而不是取决于你碰巧怎么措辞。对一个 [工具链](https://www.aihero.dev/ai-coding-dictionary/harness) 自己的深度研究模式，区别在工件和来源纪律，不在搜索。如果一个小问题两行提示就够，用两行提示。

**它什么时候停止阅读？**

skill 里没有停止标准，这表现为两个看起来相反、实则是同一缺口的两份抱怨：跑得太深的 Agent，以及大而全地覆盖主题却漏掉唯一要紧的那个具体细节的 Agent。一位从业者说成"深度研究 skill 有时候有点太深。而让 Agent 去做研究通常导致漏掉关键细节"。范围控制在你。一个狭窄、可回答的问题——一个 API、一个行为、一个版本说法——回来的东西远比"研究 X"好。

**`/wayfinder` 创建了 research tickets——我自己解决它们吗？**

不用，它现在替你开火。在 v1.1 之后未发布的改动里，制图会话为每个 research ticket 启动一个 `/research` 子代理，并行烧完它们，把发现捕获在一次性 `research/<name>` 分支上，ticket 上留 [上下文指针](https://www.aihero.dev/ai-coding-dictionary/context-pointer)。Research tickets 是 wayfinder"一会话一 ticket"规则的唯一例外，因为它们是 [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) 的——没有东西等你。这些分支有两个已知的绊脚点：子代理曾被看到从一条从没打算合并的分支开 draft PR（[issue #576](https://github.com/mattpocock/skills/issues/576)）；以及之后删除分支会弄坏 tickets 持有的上下文指针。

## 有效的标志

- 你自己的会话继续往前走。如果你坐着看它读，委托就没发生。
- 后台恰好出现一个新任务。第二个名字几乎一样的，就是嵌套 bug。
- 出现一个新的 Markdown 文件，在仓库本来就用来放笔记的文件夹里，Agent 告诉你路径。
- 文件里每条说法都带链接，随机跟两条会落在官方文档、规范或真正的源文件上——而不是某人写的转述。
- 你单凭文件就能做出那个被卡住的决策，不必自己再回到源头。

## 在系统中的位置

一个随时可取的独立工具，喂养思考类 skill，而不坐在构建链里。它的文件是要带*进*流程的东西：[grilling](https://aihero.dev/skills-grilling) 和 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 在事实已经摆上桌时问出更尖锐的问题，[to-spec](https://aihero.dev/skills-to-spec) 可以对着它综合。[wayfinder](https://aihero.dev/skills-wayfinder) 是唯一直接调用它的 skill，用 `/research` 子代理解决它地图上的每个 research ticket。完整地图见 [ask-matt](https://aihero.dev/skills-ask-matt)。

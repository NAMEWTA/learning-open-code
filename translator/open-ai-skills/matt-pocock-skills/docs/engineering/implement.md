## 功能说明

`implement` 构建已经定案的工作。你把它指向一个 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket)、一份 [规格](https://www.aihero.dev/ai-coding-dictionary/spec)、或你刚在对话里达成的计划，它写代码、在接缝处驱动 [tdd](https://aihero.dev/skills-tdd)、边写边类型检查、结尾跑 [code-review](https://aihero.dev/skills-code-review)，然后提交到当前分支。

它从不重新打开计划。没有访谈、没有澄清轮、没有提出不同方案的环节。上游已经定案的一切就是输入，skill 的全部工作就是把它变成一次提交。这正是它区别于对全新 [Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 说"把这件事建出来"的地方——后者会一边构建一边愉快地重新设计这份工作。

## 何时使用

输入 `/implement` 来调用它——Agent 不会自行调用。它出厂就带 `disable-model-invocation: true`，所以其他 skill 也不能调用它。无论 [ask-matt](https://aihero.dev/skills-ask-matt) 还是 [to-tickets](https://aihero.dev/skills-to-tickets) 说"然后按 ticket `/implement`"，那都是给你的指令，不是 Agent 会主动做的事。

工作目前住在哪里，决定这是不是正确的 skill：

| 工作现在是…… | 使用 |
| --- | --- |
| 追踪器上的一个 ticket | `/implement #42`，一个 [会话](https://www.aihero.dev/ai-coding-dictionary/session) 一个 ticket，ticket 之间 [清掉](https://www.aihero.dev/ai-coding-dictionary/clearing) 上下文 |
| 一份规格，尚未拆分，而构建横跨多次会话 | 先 [to-tickets](https://aihero.dev/skills-to-tickets)，再按 ticket `/implement` |
| 一份规格，而且构建很小 | 直接对着规格 `/implement` |
| 只在你刚进行的那场对话里，而且仍然很小 | 就在那里 `/implement`，同一个窗口 |
| 还没写在任何地方 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs)，没有代码库则用 [grill-me](https://aihero.dev/skills-grill-me) |
| 一个你想先测后写的具体行为，没有规格 | 直接用 [tdd](https://aihero.dev/skills-tdd) |
| 已经建好，你想检查它 | 直接用 [code-review](https://aihero.dev/skills-code-review) |

同会话的情况值得点名，因为 skill 自己的第一行没覆盖它。`SKILL.md` 写的是"规格或 tickets"，这会促使 [模型](https://www.aihero.dev/ai-coding-dictionary/model) 去找一个并不存在的文件。如果计划只在对话里，调用时说出来。

## 前置条件

`implement` 提交到你当前所在的分支。它不创建分支，也不问。开始之前先确认你就在想要工作的分支上。

如果 tickets 来自 [to-tickets](https://aihero.dev/skills-to-tickets)，它们所在追踪器由 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 配置。`code-review` 读同一份配置，在收尾时找到源规格。

## 一次运行做什么

一次运行是五个节拍，按顺序：

1. 读 ticket 或规格，找出接缝。
2. 在预先约定的接缝处驱动 [tdd](https://aihero.dev/skills-tdd)，一次一个红绿切片。
3. 频繁类型检查，过程中运行单个测试文件。
4. 结尾跑一次完整测试套件。
5. 跑 [code-review](https://aihero.dev/skills-code-review)，然后提交到当前分支。

一次运行覆盖一个 ticket。[to-tickets](https://aihero.dev/skills-to-tickets) 产出的 tickets 是曳光弹式垂直切片，大小恰好塞进一个全新的 [上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window)，所以预期的节奏是：清上下文、实现一个 ticket、提交、再清。每个 ticket 自包含，这正是让上一个 ticket 的上下文可以丢弃的原因。

## 预先约定的接缝

skill 运行所依赖的理念是**接缝**：你观察行为的公共边界，不必伸进内部。测试住在接缝处。在写任何代码之前约定的接缝上工作，是测试保持持久的原因——底下的实现可以重写而测试不动。

"预先约定"这个词干着真正的活，它也是 skill 最脆弱的关节。`implement` 内部没有任何东西去约定接缝。`tdd` 是提问的那个 skill，它拒绝在未确认的接缝上写测试。所以实践中，约定要么发生在上游的规格里，要么发生在运行的第一轮交流中。如果哪里都没发生，前置条件永远不触发，运行就悄悄变成"把代码写了"。在规格里点名接缝，正是阻止这种情况的东西。

## 常见问题

**它完成了，但我的 ticket 还开着，验收标准还没勾。**

对，而且这是预期。`implement` 没有完成步骤。它在提交处结束，从不触碰工作项——在 GitHub Issues 和本地 Markdown 追踪器上都确认过——所以这不是追踪器集成问题。它也不处理 `code-review` 产出的发现，不勾源 issue 上的 `- [ ]` 框。自己关 ticket、自己对账标准。这在依赖链上咬人最狠，因为 `to-tickets` 把前沿定义为所有阻塞项都已关闭的 tickets。如果什么都不关，就永远没有东西可见地解除阻塞。

**我能一次指向我所有 tickets，或并行跑几个吗？**

不能。一次调用，一个 ticket。跨 ticket 队列批量派发和 [子代理](https://www.aihero.dev/ai-coding-dictionary/subagent) 扇出都被反复请求过，两者都不存在。在一个 checkout 里并排跑多个 `/implement` 会话比不支持更糟：一份现场报告描述了某个会话里的 `git commit --amend` 落在另一场会话的提交上、一个 stash 从 `refs/stash` 消失、提交落在错误分支上——全都发生在同一个下午、跨三个 issue。这些会话共享一个工作目录、一个索引、一个 HEAD。Git worktree 是社区的变通办法，但注意 `refs/stash` 也跨 worktree 共享，所以光有 worktree 修不了 stash 那个案例。今天想要并行，你自己组装。

**它能开一个 pull request 而不是提交吗？**

没有内置。它直接提交到当前分支，几个人觉得这太心急：代码在他们有机会验证能用之前就落地了。没有配置开关，没有 PR 模式。人们在调用时覆盖它（"提交到一个分支并开一个 PR"），或编辑本地副本的 skill。

**`code-review` 说它看不到我的改动。**

`code-review` 审查 `git diff <fixed-point>...HEAD`，那排除了暂存区和工作树改动。`implement` 在提交之前跑它，所以除非已经存在中间提交，那个 diff 里没有东西可审。多人报告过这个，两边都未修复。先提交，再对着你分支出去的那个点审查。

另外，有些人刻意完全不想要运行内的审查，因为审查自己刚写的代码的 Agent 偏向自己的方案。在一个全新会话里对着固定点跑 [code-review](https://aihero.dev/skills-code-review) 是合法的替代，也正因此 skill 把两个轴放在两个独立子代理里。

**一个 ticket 烧了 15 万 token。我用错了吗？**

多半是 ticket 太大，而不是 skill 用错了。一次运行包含代码库探索、每个接缝的红绿循环、完整套件和一次审查，所以一个像样的 ticket 超过 10 万 [token](https://www.aihero.dev/ai-coding-dictionary/token) 是正常的，不是出事的信号。杠杆在上游：在 [to-tickets](https://aihero.dev/skills-to-tickets) 里把 tickets 切到合适大小，让每个正好塞进一个全新窗口。如果单个 ticket 一直爆掉，拆它，而不是提高 [effort](https://www.aihero.dev/ai-coding-dictionary/effort) 级别。

**新会话里的 `/implement #2` 做了完全不相关的事。**

`#2` 按 Agent 能看到的任意编号列表解析，在新会话里那可能是 todo 文件、清单或别的工作列表，而不是配置好的追踪器。解析是自信式而非失败关闭式的，所以错误要到开始之后才明显。传完整引用——issue URL 或 `owner/repo#2`——并要它在开始前把标题复述回来确认。

## 有效的标志

- 会话以读 ticket 或规格、复述将要构建什么开头，而不是问你要构建什么。
- 你能在轨迹里看到一次真实的 `/tdd` 调用，而不只是 diff 里出现测试。
- 运行期间类型检查和单个测试文件反复运行，完整套件在接近结尾时跑一次。
- 运行到达你当前分支上的一次提交，不需要你催它继续。
- diff 是一个 ticket 量的改动：贯穿每一层的垂直切片，而不是几个 ticket 扫成一团。

## 在系统中的位置

`implement` 是主链的构建步骤，倒数第二个：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

它的邻居是 [to-tickets](https://aihero.dev/skills-to-tickets)——产出它消费的 tickets，并声明决定其顺序的阻塞边；[tdd](https://aihero.dev/skills-tdd)——它在每个接缝内部驱动它；以及 [code-review](https://aihero.dev/skills-code-review)——它在提交前跑它。它位于规划类 skill 的下游并信任它们。它不重新验证交给它的东西的形状，所以一张结构糟糕的地图或一个水平分层的 ticket 会被照原样建出来。

这份信任正是 [wayfinder](https://aihero.dev/skills-wayfinder) 在 [to-spec](https://aihero.dev/skills-to-spec) 处汇入链条、而不是把它的地图直接循环进 `implement` 的原因。只有当工作结果确实很小时，才从地图直奔 `implement`。

不确定自己身处哪条流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 是覆盖整个集合的路由器。
